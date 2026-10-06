import pygame as pg
import os

from math import ceil

# Functions ----- #
def load_images(path_to_directory: str, exclude: list=[]):
    images = {}
    for dirpath, dirnames, filenames in os.walk(path_to_directory):
        dirnames[:] = [d for d in dirnames if d not in exclude] #https://stackoverflow.com/questions/19859840/excluding-directories-in-os-walk
        for name in filenames:
            if name.endswith('.png'):
                key = name[:-4]
                png = pg.image.load(os.path.join(dirpath, name)).convert_alpha()
                png = pg.transform.rotozoom(png, 0, 800/1920)
                images[key] = png
                print(os.path.join(dirpath, name))
    return images

def load_sounds(path_to_directory: str, exclude: list=[]):
    sound = {}
    for dirpath, dirnames, filenames in os.walk(path_to_directory):
        dirnames[:] = [d for d in dirnames if d not in exclude] #https://stackoverflow.com/questions/19859840/excluding-directories-in-os-walk
        for name in filenames:
            if name.endswith('.mp3'):
                key = name[:-4]
                mp3 = pg.mixer.Sound(os.path.join(dirpath, name))
                sound[key] = mp3
                print(os.path.join(dirpath, name))
    return sound

def display_text(surface: pg.Surface, text: str, font_path: str, size: int, color: tuple=(0,0,0), position='middle', start: tuple=(0,0)):
    font = pg.font.Font(font_path, size)
    message = font.render(text, 1, color)
    if position == 'left': message_rect = message.get_rect(midleft = start)
    elif position == 'middle': message_rect = message.get_rect(center = start)
    elif position == 'right': message_rect = message.get_rect(midright = start)
    
    surface.blit(message, message_rect)

def newline_text(surface: pg.Surface, text: str, font_path: str, size: int, color: pg.Color, pos: tuple=(200,100), max_width=500): #https://stackoverflow.com/questions/42014195/rendering-text-with-multiple-lines-in-pygame
    font = pg.font.Font(font_path, size)
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 1, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

def render_inventory():
    global screen, inventory, inv_index, events, interact, display
    box = img['inventory_box']

    box1 = box.get_rect(center = (200,750))
    screen.blit(box, box1)
    box2 = box.get_rect(center = (300,750))
    screen.blit(box, box2)
    box3 = box.get_rect(center = (400,750))
    screen.blit(box, box3)
    box4 = box.get_rect(center = (500,750))
    screen.blit(box, box4)
    box5 = box.get_rect(center = (600,750))
    screen.blit(box, box5)

    if inv_index > 0:
        inv_left.image = img['inventory_left']
        inv_left.rect = inv_left.image.get_rect(center = (100,750))
    else:
        inv_left.image = img['inventory_left2']
        inv_left.rect = inv_left.image.get_rect(center = (100,750))
    if inv_left.update() and inv_index > 0 and interact and display == None: inv_index -= 1

    if inv_index < len(inventory) - 5:
        inv_right.image = img['inventory_right']
        inv_right.rect = inv_left.image.get_rect(center = (700,750))
    else:
        inv_right.image = img['inventory_right2']
        inv_right.rect = inv_left.image.get_rect(center = (700,750))
    if inv_right.update() and inv_index < len(inventory) - 5 and interact and display == None:
        inv_index += 1

    for i in range(5):
        try: inventory[i+inv_index].update((200 + 100*i,750))
        except: pass

def update_hints():
    global time, hints
    global puzzle1, puzzle2, puzzle3, puzzle4, puzzle5, puzzle6, puzzle7, puzzle8, puzzle9, puzzle10
    global hints_puzzle1, hints_puzzle2, hints_puzzle3, hints_puzzle4, hints_puzzle5, hints_puzzle6, hints_puzzle7, hints_puzzle8, hints_puzzle9, hints_puzzle10
    
    if hints is not None: old_hints = hints[0]
    if puzzle1 is not True: hints[0] = 0
    elif puzzle2 is not True: hints[0] = 1
    elif puzzle3 is not True: hints[0] = 2
    elif puzzle4 is not True: hints[0] = 3
    elif puzzle5 is not True: hints[0] = 4
    elif puzzle6 is not True: hints[0] = 5
    elif puzzle7 is not True: hints[0] = 6
    elif puzzle8 is not True: hints[0] = 7
    elif puzzle9 is not True: hints[0] = 8
    elif puzzle10 is not True: hints[0] = 9
    else: hints = None
    
    if hints is not None:
        if old_hints != hints[0]: hints[1] = 0
        else: hints[1] += 1

        if hints[1] > 3: hints[1] = 3
        else:
            time -= (1 + hints[1]) * 30

            if hints[0] == 0: hints_puzzle1 += 1
            elif hints[0] == 1: hints_puzzle2 += 1
            elif hints[0] == 2: hints_puzzle3 += 1
            elif hints[0] == 3: hints_puzzle4 += 1
            elif hints[0] == 4: hints_puzzle5 += 1
            elif hints[0] == 5: hints_puzzle6 += 1
            elif hints[0] == 6: hints_puzzle7 += 1
            elif hints[0] == 7: hints_puzzle8 += 1
            elif hints[0] == 8: hints_puzzle9 += 1
            elif hints[0] == 9: hints_puzzle10 += 1

def update_puzzle1(input):
    code = [4,3,3,7]

    global puzzle1, puzzle1_text, sfx
    puzzle1_text = ''
    if puzzle1 is not True:
        if type(input) == type(0):
            sfx['digital_beep'].play()
            if len(puzzle1) < 10: puzzle1.append(input)
            for num in puzzle1: puzzle1_text += str(num)
        
        elif input == 'enter':
            if puzzle1 == code:
                puzzle1 = True
                sfx['digital_valid'].play()
            else:
                puzzle1 = []
                sfx['digital_invalid'].play()

        elif input == 'clear':
            puzzle1 = []
            sfx['digital_beeep'].play()

def update_puzzle2():
    code = [3,2,4,1]

    global skillet, saucepan, pot, kettle, stove_placed, puzzle2, sfx
    if puzzle2 is not True:
        puzzle2 = []
        for sprite in stove_placed:
            if sprite == skillet: puzzle2.append(1)
            elif sprite == saucepan: puzzle2.append(2)
            elif sprite == pot: puzzle2.append(3)
            elif sprite == kettle: puzzle2.append(4)
            else: puzzle2.append(0)
        
        if puzzle2 == code:
            puzzle2 = True
            sfx['digital_beeep'].play()
        else: sfx['digital_beep'].play()

def update_puzzle3(input):
    code = [2,4,3]

    global puzzle3, puzzle3_text, sfx
    puzzle3_text = ''
    if puzzle3 is not True:
        if type(input) == type(0):
            if len(puzzle3) < 5:
                puzzle3.append(input)
            sfx['microwave_beep'].play()
            for num in puzzle3:
                puzzle3_text += str(num)
        
        elif input == 'enter':
            if puzzle3 == code:
                puzzle3 = True
                sfx['microwave_valid'].play()
                sfx['microwave_open'].play()
            else:
                puzzle3 = []
                sfx['microwave_invalid'].play()

        elif input == 'clear':
            puzzle3 = []
            sfx['microwave_beeep'].play()

def update_puzzle4(input):
    code = ['K','I','N','D']

    global puzzle4, puzzle4_text, p4_bpressed, p4_bindex, p4_btime, sfx
    puzzle4_text = ''
    if puzzle4 is not True:
        if type(input) == type(0):
            sfx['digital_beep'].play()
            if input >= 1 and input <= 9:
                options = [
                    ['A','B','C',1],
                    ['D','E','F',2],
                    ['G','H','I',3],
                    ['J','K','L',4],
                    ['M','N','O',5],
                    ['P','Q','R',6],
                    ['S','T','U',7],
                    ['V','W','X',8],
                    ['Y','Z',9],
                ]
                if p4_bpressed == input and p4_btime > 0:
                    puzzle4[-1] = (options[input-1][p4_bindex])
                    p4_bindex += 1
                    if p4_bindex >= len(options[input-1]): p4_bindex = 0
                else:
                    if len(puzzle4) < 8:
                        puzzle4.append(options[input-1][0])
                        p4_bpressed = input
                        p4_bindex = 1
                p4_btime = 1.5

            elif input == 0:
                puzzle4.append(0)
                p4_bpressed = 0
                p4_bindex = 0
            
            for char in puzzle4: puzzle4_text += str(char)
        
        elif input == 'enter':
            if puzzle4 == code:
                puzzle4 = True
                sfx['digital_valid'].play()
            else:
                puzzle4 = []
                sfx['digital_invalid'].play()

        elif input == 'clear':
            puzzle4 = []
            sfx['digital_beeep'].play()

def update_puzzle5(input):
    array = [
            ['A','W','V','G','F'], #G
            ['B','H','O','P','L'], #O
            ['C','N','R','J','U'], #N
            ['D','S','M','T','E']  #E
        ]
    
    global puzzle5, p5_index1, p5_index2, p5_index3, p5_index4, sfx
    puzzle5 = ['','','','']
    if input == 1:
        p5_index1 += 1
        if p5_index1 >= len(array[0]): p5_index1 = 0
    elif input == 2:
        p5_index2 += 1
        if p5_index2 >= len(array[1]): p5_index2 = 0
    elif input == 3:
        p5_index3 += 1
        if p5_index3 >= len(array[2]): p5_index3 = 0
    elif input == 4:
        p5_index4 += 1
        if p5_index4 >= len(array[3]): p5_index4 = 0
    sfx['combination_click'].play()

    puzzle5[0] = array[0][p5_index1]
    puzzle5[1] = array[1][p5_index2]
    puzzle5[2] = array[2][p5_index3]
    puzzle5[3] = array[3][p5_index4]

def update_puzzle6(input):
    code = [[5],[2,5],[6]]
    code2 = [[5],[2,5],[0,6]]
    code3 = [[0,5],[2,5],[6]]
    code4 = [[0,5],[2,5],[0,6]]

    global puzzle6, p6_index, p6_pressed, p6_text1, p6_text2, p6_text3, sfx
    if puzzle6 is not True:
        p6_text1 = ''
        p6_text2 = ''
        p6_text3 = ''
        if type(input) == type(0):
            sfx['digital_beep'].play()
            if len(puzzle6[p6_index]) < 2: puzzle6[p6_index].append(input)
            p6_pressed = 1
            
        elif input == 'enter':
            if p6_index < 2:
                if len(puzzle6[p6_index]) > 0:
                    p6_index += 1
                sfx['button_click'].play()
            else:
                if puzzle6 == code or puzzle6 == code2 or puzzle6 == code3 or puzzle6 == code4:
                    puzzle6 = True
                    sfx['digital_valid'].play()
                else:
                    puzzle6 = [[],[],[]]
                    p6_index = 0
                    sfx['digital_invalid'].play()
            p6_pressed = 1

        elif input == 'clear':
            if p6_index >= 0 and p6_index < 3:
                if p6_pressed == 1:
                    p6_pressed = 0
                else: p6_index -= 1
                if p6_index < 0: p6_index = 0
                puzzle6[p6_index] = []
            sfx['digital_beep'].play()
        
        if puzzle6 is not True:
            for num in puzzle6[0]: p6_text1 += str(num)
            for num in puzzle6[1]: p6_text2 += str(num)
            for num in puzzle6[2]: p6_text3 += str(num)
        else:
            p6_text1 = 'UN'
            p6_text2 = 'LO'
            p6_text3 = 'CK'

def update_puzzle9(input):
    array = [
            [0,1,2,3,4,5,6,7,8,9], #0
            [0,1,2,3,4,5,6,7,8,9], #6
            [0,1,2,3,4,5,6,7,8,9], #2
            [0,1,2,3,4,5,6,7,8,9]  #9
        ]
    
    global puzzle9, p9_index1, p9_index2, p9_index3, p9_index4, sfx
    puzzle9 = ['','','','']
    if input == 1:
        p9_index1 += 1
        if p9_index1 >= len(array[0]): p9_index1 = 0
    elif input == 2:
        p9_index2 += 1
        if p9_index2 >= len(array[1]): p9_index2 = 0
    elif input == 3:
        p9_index3 += 1
        if p9_index3 >= len(array[2]): p9_index3 = 0
    elif input == 4:
        p9_index4 += 1
        if p9_index4 >= len(array[3]): p9_index4 = 0
    sfx['combination_click'].play()

    puzzle9[0] = str(array[0][p9_index1])
    puzzle9[1] = str(array[1][p9_index2])
    puzzle9[2] = str(array[2][p9_index3])
    puzzle9[3] = str(array[3][p9_index4])

def update_time(counting=True):
    global time, display_time, puzzle_time, time_puzzle1, time_puzzle2, time_puzzle3, time_puzzle4, time_puzzle5, time_puzzle6, time_puzzle7, time_puzzle8, time_puzzle9, time_puzzle10, puzzle_list
    if counting:
        time -= 1/60
        puzzle_time += 1/60
        puzzle_list2 = [puzzle1, puzzle2, puzzle3, puzzle4, puzzle5, puzzle6, puzzle7, puzzle8, puzzle9, puzzle10]

        if puzzle_list != puzzle_list2:
            for i in range(len(puzzle_list)):
                if puzzle_list[i] != puzzle_list2[i] and puzzle_list2[i] is True:
                    if i == 0: time_puzzle1 = puzzle_time
                    elif i == 1: time_puzzle2 = puzzle_time
                    elif i == 2: time_puzzle3 = puzzle_time
                    elif i == 3: time_puzzle4 = puzzle_time
                    elif i == 4: time_puzzle5 = puzzle_time
                    elif i == 5: time_puzzle6 = puzzle_time
                    elif i == 6: time_puzzle7 = puzzle_time
                    elif i == 7: time_puzzle8 = puzzle_time
                    elif i == 8: time_puzzle9 = puzzle_time
                    elif i == 9: time_puzzle10 = puzzle_time
                    puzzle_time = 0
    
    if time <= 0: display = '0:00:00'
    else:
        time_seconds = ceil(time)
        hours = int(time_seconds/3600)
        minutes = int((time_seconds - hours*3600) / 60)
        seconds = int(time_seconds - hours*3600 - minutes*60)
        display = str(hours) + ':'
        if minutes < 10: display += '0' + str(minutes) + ':'
        else: display += str(minutes) + ':'
        if seconds < 10: display += '0' + str(seconds)
        else: display += str(seconds)
        display_time = display

    display_text(screen, display_time, 'fonts/fofbb_reg.ttf', 50, (0,0,0), 'left', (25,50))
    puzzle_list = [puzzle1, puzzle2, puzzle3, puzzle4, puzzle5, puzzle6, puzzle7, puzzle8, puzzle9, puzzle10]

def update_username(input):
    global username_submit, username_list, username, b_pressed, b_index, b_time, sfx
    username = ''
    if username_submit is not True:
        if type(input) == type(0):
            sfx['digital_beep'].play()
            if input >= 0 and input <= 9:
                options = [
                    ['A','B','C',1],
                    ['D','E','F',2],
                    ['G','H','I',3],
                    ['J','K','L',4],
                    ['M','N','O',5],
                    ['P','Q','R',6],
                    ['S','T','U',7],
                    ['V','W','X',8],
                    ['Y','Z',9],
                    ['_',0]
                ]
                if b_pressed == input and b_time > 0:
                    username_list[-1] = (options[input-1][b_index])
                    b_index += 1
                    if b_index >= len(options[input-1]): b_index = 0
                else:
                    if len(username_list) < 8:
                        username_list.append(options[input-1][0])
                        b_pressed = input
                        b_index = 1
                b_time = 1.5
            
            for char in username_list: username += str(char)
        
        elif input == 'enter':
            for char in username_list: username += str(char)
            if len(username_list) >= 3:
                username_submit = True
                sfx['digital_valid'].play()
            else:
                sfx['digital_invalid'].play()

        elif input == 'clear':
            username_list = []
            sfx['digital_beeep'].play()

def reset_game():
    global time_show, time, puzzle_time, puzzle_list
    # Game Interface ----- #
    time_show = False
    time = 0
    puzzle_time = 0
    puzzle_list = []

    global time_puzzle1, time_puzzle2, time_puzzle3, time_puzzle4, time_puzzle5, time_puzzle6, time_puzzle7, time_puzzle8, time_puzzle9, time_puzzle10
    time_puzzle1 = 0
    time_puzzle2 = 0
    time_puzzle3 = 0
    time_puzzle4 = 0
    time_puzzle5 = 0
    time_puzzle6 = 0
    time_puzzle7 = 0
    time_puzzle8 = 0
    time_puzzle9 = 0
    time_puzzle10 = 0

    global floor, room, enlarge, display
    floor = 0
    room = str
    enlarge = str
    display = None

    global pause, play, pause_screen, dialogue_count
    pause = None
    play = None
    pause_screen = None
    dialogue_count = 0

    global inventory, inv_index, inv_left, inv_right, interact
    inventory = []
    inv_index = 0
    inv_left = None
    inv_right = None
    interact = False

    global hints, hint_button, hint_active
    hints = []
    hint_button = None
    hint_active = False

    global hints_puzzle1, hints_puzzle2, hints_puzzle3, hints_puzzle4, hints_puzzle5, hints_puzzle6, hints_puzzle7, hints_puzzle8, hints_puzzle9, hints_puzzle10
    hints_puzzle1 = 0
    hints_puzzle2 = 0
    hints_puzzle3 = 0
    hints_puzzle4 = 0
    hints_puzzle5 = 0
    hints_puzzle6 = 0
    hints_puzzle7 = 0
    hints_puzzle8 = 0
    hints_puzzle9 = 0
    hints_puzzle10 = 0

    global lights, mask, fader, vtext
    # Game Elements ----- #
    lights = False
    mask = None
    vtext = None

    global a_up, a_up2, a_upleft, a_left, a_left2, a_down, a_downright, a_right
    # Arrows/Buttons ----- #
    a_up = None
    a_up2 = None
    a_upleft = None
    a_left = None
    a_left2 = None
    a_down = None
    a_downright = None
    a_right = None

    global close_button
    close_button = None

    # Floors ----- #
    global cabinet1, b1, b2, b3, b4, b5, b6, b7, b8, b9, b0, b_enter, b_clear, puzzle1, puzzle1_text, cookbook
    ### Floor 1
    ## Kitchen
    cabinet1 = None
    # Cabinet 1
    b1 = None
    b2 = None
    b3 = None
    b4 = None
    b5 = None
    b6 = None
    b7 = None
    b8 = None
    b9 = None
    b0 = None
    b_enter = None
    b_clear = None
    puzzle1 = []
    puzzle1_text = ''
    cookbook = None

    global microwave, microwave_sprites, key, puzzle3, puzzle3_text
    microwave = None
    # Microwave
    b1 = None
    b2 = None
    b3 = None
    b4 = None
    b5 = None
    b6 = None
    b7 = None
    b8 = None
    b9 = None
    b0 = None
    b_enter = None
    b_clear = None
    microwave_sprites = []
    key = None
    puzzle3 = []
    puzzle3_text = ''

    global cabinet2
    cabinet2 = None
    # Cabinet 2

    global sink
    sink = None
    # Sink

    global cabinet3, cabinet3_sprites, skillet, saucepan, pot, kettle
    cabinet3 = None
    # Cabinet 3
    cabinet3_sprites = [None, None, None, None]
    skillet = None
    saucepan = None
    pot = None
    kettle = None

    global stove, burner1, burner2, burner3, burner4, stove_enter, stove_valid, stove_placed, puzzle2
    stove = None
    # Stove
    burner1 = None
    burner2 = None
    burner3 = None
    burner4 = None
    stove_enter = None
    stove_valid = []
    stove_placed = [None, None, None, None]
    puzzle2 = [None, None, None, None]

    global oven, oven_sprites, oven_paper
    oven = None
    # Oven
    oven_sprites = []
    oven_paper = None

    global breaker, breaker_switch
    ## Entrance/Laundry
    breaker = None
    # Breaker
    breaker_switch = None

    ## Living
    global bookshelf, bookshelf_level, shelf1_valid, bookshelf_slot1, shelf2_valid, bookshelf_slot2, shelf3_valid, bookshelf_slot3, puzzle10
    bookshelf = None
    # Bookshelf
    bookshelf_level = 0
    shelf1_valid = []
    bookshelf_slot1 = None
    shelf2_valid = []
    bookshelf_slot2 = None
    shelf3_valid = []
    bookshelf_slot3 = None
    puzzle10 = [None, None, None]

    global posters
    posters = None
    # Posters

    global tv, tv_screen, tv_adcount
    tv = None
    # TV
    tv_screen = None
    tv_adcount = 0

    global study_door, can_escape, desk, desk_view, desk_paper, newspaper, doctor_letter
    ## Study
    study_door = None
    can_escape = 0
    desk = None
    # Desk
    desk_view = 0
    desk_paper = 1
    newspaper = None
    doctor_letter = None

    ### Floor 2
    global hallway_placed, room1_door, room1_lock
    ## Hallway
    hallway_placed = []

    global room0_door
    # Bathroom Door
    room0_door = None

    global room0_open
    ## Bathroom
    room0_open = False

    room1_door = None
    # Bedroom 1 Door
    room1_lock = None

    global room1_open, morse_code, binary_code, flicker
    room1_open = False
    ## Bedroom 1
    morse_code = None
    binary_code = None
    flicker = None

    global room2_door, p4_bpressed, p4_btime, p4_bindex, puzzle4, puzzle4_text
    room2_door = None
    # Bedroom 2 Door
    b1 = None
    b2 = None
    b3 = None
    b4 = None
    b5 = None
    b6 = None
    b7 = None
    b8 = None
    b9 = None
    b0 = None
    b_enter = None
    b_clear = None
    p4_bpressed = 0
    p4_btime = 0
    p4_bindex = 0
    puzzle4 = []
    puzzle4_text = ''

    global computer, room3_door, p5_index1, p5_index2, p5_index3, p5_index4, puzzle5
    ## Bedroom 2
    computer = None

    room3_door = None
    # Bedroom 3 Door
    p5_index1 = 0
    p5_index2 = 0
    p5_index3 = 0
    p5_index4 = 0
    puzzle5 = []

    global bedroom3_sprites, ladder, hallway_place, hallway_valid, hallway_sprites, attic_hatch
    ## Bedroom 3
    bedroom3_sprites = []
    ladder = None

    hallway_place = None
    hallway_valid = []
    hallway_sprites = []
    attic_hatch = None
    global p6_index, p6_pressed, puzzle6, p6_text1, p6_text2, p6_text3
    # Attic Hatch
    b1 = None
    b2 = None
    b3 = None
    b4 = None
    b5 = None
    b6 = None
    b7 = None
    b8 = None
    b9 = None
    b0 = None
    b_enter = None
    b_clear = None
    p6_index = 0
    p6_pressed = 0
    puzzle6 = [[],[],[]]
    p6_text1 = ''
    p6_text2 = ''
    p6_text3 = ''

    global box1, box1_cut, puzzle7, box1_sprites, hit_list, family_history
    ### Floor 3
    ## Attic
    box1 = None
    ## Box 1
    box1_cut = None
    puzzle7 = False
    box1_sprites = []
    hit_list = None
    family_history = None

    global table, table_sprites, mom_diary, pigpen_code
    table = None
    ## Table
    table_sprites = []
    mom_diary = None
    pigpen_code = None

    global box2, box2_cut, puzzle8, laura_diary_locked, diary_view, p9_index1, p9_index2, p9_index3, p9_index4, puzzle9, box2_sprites, laura_diary
    box2 = None
    ## Box 2
    box2_cut = None
    puzzle8 = False
    laura_diary_locked = None
    diary_view = 0
    p9_index1 = 0
    p9_index2 = 0
    p9_index3 = 0
    p9_index4 = 0
    puzzle9 = []
    box2_sprites = []
    laura_diary = None

    global rug, box_cutter
    rug = None
    ## Rug
    box_cutter = None

def init_ending():
    global text
    # Escaped
    text = None

    global keypad, username, username_submit, username_list, b_pressed, b_index, b_time
    # Username
    keypad = None
    username = ''
    username_submit = False
    username_list = []
    b_pressed = 0
    b_index = 0
    b_time = 0

    # Credits 1

    global num_credits, credits_delay, credits_list, credits_group
    # Credits 2
    num_credits = 0
    credits_delay = 0
    credits_list = []
    credits_group = pg.sprite.Group()

    global survey, circle, select, submit
    # Survey
    survey = None
    circle = None
    select = 0
    submit = None

    global survey1, survey2, survey3, survey4, survey5, survey6
    survey1 = None
    survey2 = None
    survey3 = None
    survey4 = None
    survey5 = None
    survey6 = None

# Floor 1:
## Kitchen
### Cabinet 1/Open
    #PUZZLE 1: 4337

    #Cookbook
### Microwave/Open
    #PUZZLE 3: 243

    # Key
### Sink
### Cabinet 2
    # Pots and pans
### Stove
    #PUZZLE 2: [POT, SAUCEPAN ; KETTLE, PAN]
### Oven/Open

    # Paper scrap


## Entrance
### Breaker
    #Toggle lights

## Living Room
### Bookshelf/To Study
    #Shelf 1
    #Shelf 2
    #Shelf 3

    ## Study
    ### Desk
        #Newspaper 1
        #Newspaper 2
        #Doctor Letter
    #Exit

### Posters
### TV

# Floor 2:
## Hallway
    #Place Ladder
## Bedroom 1/Open
# Keyhole
    #Morse Code Paper
    #Binary Code Paper
## Bedroom 2/Open | PUZZLE 4: "KIND"
### Computer
## Bedroom 3/Open | PUZZLE 5: "GONE"
    # Ladder
# Floor 3:
## Attic/Open | PUZZLE 6: [5, 25, 6]
### Box 1
    # Family History Book/PUZZLE 8: Laura
### Table
    # Mom Diary/PUZZLE 7: "UNDER THE RUG"
### Box 2
    # Girl Diary/PUZZLE 9: 0629
### Rug Corner
    # Box Cutter

# Resolution ----- #
screen = pg.Surface
icon = pg.Surface
font = pg.font.Font
info = pg.display.Info
clock = pg.time.Clock

# Variables ----- #
img = {str : pg.Surface}
sfx = {str : pg.mixer.Sound}
sound = {str : pg.mixer.Sound}
intro_music = pg.mixer.Sound
events = [pg.event.Event]
mouse_pos = (int, int)
mouse_pressed = (bool, bool, bool)

dialogue = [
    [0, "The front door won't open anymore! Am I trapped in here? There must be a way out! But it's too dark to see anything..."], #0
    [0, "The lights are on now. I think I heard a static sound coming from the living room."], #1
    [0, "This is the sound I heard before. Could this ad be important?"], #2
    [0, "These ads seem to be repeating in a specific order. This has to mean something!"], #3
    [0, "Why would a kitchen cabinet need to have a lock?"], #4
    [0, "Who replaced ingredients with poisons? I can see why this is locked up now."], #5
    [0, "Why do I need this? This is no time to cook!"], #6
    [0, "Probably an excerpt from a book. Torn and in the oven, though? Someone must really dislike art around here."], #7
    [0, "These paintings look interesting. They probably don't mean anything, though..."], #8
    [0, "The paper seemed to point here. I'd better take a good look."], #9
    [0, "This microwave won't open for some reason. Does it need a code or something?"], #10
    [0, "There was a key in this microwave- err, safe? Was someone else locked in here?"], #11
    [0, "I could find some answers in the attic, but I can't reach it."], #12
    [0, "I heard the lock click! Did the door unlock? I should back up a little bit."], #13
    [0, "This must be a boys' bedroom. What's happening with the lights?"], #14
    [0, "Looks like someone had moved in and brought a computer, but it's still here now."], #15
    [0, "A girl's bedroom, with a totally-not-ominous passcode. A ladder for whatever reason..."], #16
    [0, "The attic is locked as well? There must be something important hidden up there."], #17
    [0, "Sounds normal for a family. There is something strange about this house, though, so it could mean something else."], #18
    [0, "This box is taped shut! I need something to cut it open with."], #19
    [0, "Very interesting… How come the recent birth dates don't have a year? Was it a printing mistake?"], #20
    [0, "The mystery leads to this little book. Of course it's locked."], #21
    [0, "I think this child had some issues. Did she kill her brother? Did she kill her entire family?"], #22
    [0, "These shelves appear to be missing a few books. Maybe I can find some around here."], #23
    [0, "Woah, a secret passage in the bookshelf! What secrets lie inside?"], #24
    [0, "Someone must've gone through great lengths to conceal whatever's in this room."], #25
    [0, "She killed her youngest brother, and now the middle brother is dead? That can't be a coincidence."], #26
    [0, "Her father was killed by her as well! How did this even happen?"], #27
    [0, "The mother left a page from her diary... looks like she had a secret exit from this place, but it was too late."], #28
    [0, "This was the cause of the family's death. A deadly disease that caused the daughter to kill everyone in her family and eventually die. I hope it wasn't contagious."], #29
    [0, "At last, the exit! It wasn't locked. I understand everything now, but now I have to get out of here!"] #30
]

question_list = [
    ['The lights should be on... I heard a static sound, but I forgot where it came from.', #1
     "I'm looking at the ads, but I don't see anything other than lots of numbers.",
     'The big numbers are in order, but what about the gray numbers?'],
    ['I found the cabinet! What do I do with this cookbook?', #2
     "Okay, there's an oven and a stove. What else?",
     'How do I place these pots and pans?'],
    ['There was a piece of paper in the oven, kinda random.', #3
     'I found some posters in the living room. What do they mean?',
     "There are flowers in a vase, heart-shaped balloons, and flowers on a cactus, along with a word."],
    ['The key opened up a bedroom! What a mess... so many papers!', #4
     'The lights seem to be broken... but I turned the power on downstairs!',
     "But I can't decipher morse code, it's too difficult! What does it say?"],
    ["There's nothing in this room except for a bed, a computer, and a plant.", #5
     'The keyboard is missing some keys, but what letters are they?',
     'There are some keys missing... but which keys?'],
    ['This room has nothing useful except for a ladder. Strange.', #6
     'Something about the vanity mirror in this room reminds me of the first room.',
     'This is a code, I know it! ...Which code is it again?'],
    ["There are two boxes, but I can't open them.", #7
     'Okay, there is a diary with a bunch of symbols and a paper with a bunch of letters and symbols.',
     'It takes too long to decode this message, can you help me?'],
    ['A box cutter! I can use that on the first box. What could be inside?', #8
     'Another book. "Family History", huh... but a hit list!? Why?',
     'The way they worded this list makes it so hard to find the right people, although that was probably the point.'],
    ["That's all in the first box, so let's see what's inside the second box.", #9
     "Laura's diary this time! I wonder what she had to say about her mom.",
     'Her password could be anything. How would I guess it?'],
    ["This is interesting and all, but I still can't get out of the house.", #10
     "Yeah, I read the books. Caroline's diary led to the family history, which led to Laura's diary. Isn't that it?",
     'The stuff Laura wrote in her diary is a little disturbing. Why would I want to read it again?']
]
hint_list = [
    ["That sound came from the TV. I'm pretty sure there was something in particular that sounded like that.", #1
     'The ads follow a pattern, right? And the pattern seems to be related to the big numbers on the screen.',
     'The lighter digit in each phone number is the number you enter. All of the ads are numbered, which shows the order of the code. And since the cabinet ad made that sound, the code must be for the cabinet lock.'],
    ["You cook with a cookbook, obviously! But there are other things you'll need as well...", #2
     "Check all the cabinets. There shold be some pots and pans in one of them.",
     'The pots and pans go on the stove. The positions are shown in the pictures of the cookbook.'],
    ['The paper in the oven said something about art, right? Is there anything around that is related to art?', #3
     'The paper also mentioned something about details. Each picture has details that are important.',
     'Each picture seems to have a certain number of features. Those numbers may be the solution to the code. But the last one says "backwards." So the code is backward as well.'],
    ['There are piles of paper on the floor. Some of those papers could be important later on.', #4
     'The flickering light looks and souds like morse code. One of the papers on the floor is a morse code key.',
     "The morse code is a four-letter word repeating over and over again. The letters are K, I, N, and D."],
    ["Nothing works except for the keyboard. You'd think that a computer has a lot of information, but maybe it's the lack of information that matters.", #5
     "The standard keyboard layout is right in front of you, just look down.",
     'The missing keys are "E", "O", "G", and "N". Need I say more?'],
    ["You'll probably want to place the ladder in order to access the attic hatch.", #6
     "The vanity mirror has the same problem as the light in the first room: it's missing lights! But this time, it's not morse code.",
     'The lights look like binary code this time. And there was a binary code paper in the first room! To decode binary, add the values of the corresponding lights on each side to get three numbers.'],
    ["Both boxes are taped shut, but there's something on the table. That might be more helpful.", #7
     'This looks like a pigpen cipher, a common cipher that codes all twenty-six letters of the alphabet. The symbols in the diary re the same.',
     'The first two words are "UNDER" and "THE." An item you may need is probably under something in the attic.'],
    ["There's a book, but if you looked closely, there was also a piece of paper underneath it.", #8
     "A hit list? We're assuming some people need to be crossed off the family tree. It wouldn't make sense to cross out people who already died, though.",
     'First person? Charles. Second person? Billy. Third person? Alex. Fourth person? Caroline. So who does that leave?'],
    ["This box is taped shut as well. You'll probably need the box cutter you used for the first box.", #9
     '...And the diary is locked. Surely Laura would use a secure code and not one that anybody could guess, right?',
     'It has to be her birthday shown in the family history book, June 29. Six twenty-nine... hmm. What about "zero six" instead?'],
    ["Great. You've been through the entire house, and there's still no exit? Well, at least you have a few important items, like cipher keys, an actual key, some books... some books...", #10
     "Everything in the house did something, but the books had almost no use! Why not have papers instead? Well, you read Caroline's diary, the family history book, and Laura's diary. On second thought, you may want to read that one again.",
     'Laura wrote something important in her diary: "hidden in plain sight." Where could books go to be hidden in plain sight? Blending in with other books... in the bookshelf!']
]

bg = None
window = str
text = None

phone = None
black = None
black_rect = None
window_delay = int

lb_h1 = str
lb_c1 = str
lb_h2 = str
lb_c2 = str
lb_h3 = str
lb_c3 = str
leaderboard1 = None
leaderboard2 = None
leaderboard3 = None

door_closed = None
phone_dead = None
text1 = None
text2 = None
text3 = None
text4 = None
text5 = None
text6 = None
t1 = bool
t2 = bool
t3 = bool
t4 = bool
t5 = bool
t6 = bool

start = None
quit = None
fader = None

fading = bool
playing = bool
paused = bool
escaped = bool