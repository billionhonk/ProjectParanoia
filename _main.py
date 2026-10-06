import pygame as pg

from pygame import quit
from sys import exit


### GAME INFO ###

# 1 hour time limit
# 3 floors * 3 puzzles each = 9 puzzles total
# + 1 cumulative puzzle = 10 in all
# 3 hints/puzzle * 9 puzzles = 27 hints total
# 1st hint: -:30, 2nd hint: -1:00, 3rd hint: -1:30
# time stops once you leave, not once you enter the study


# Initialize ----- #
pg.init()

import _variables as v

# Resolution ----- #
v.screen = pg.display.set_mode((800,800))
pg.display.set_caption('Project Paranoia')

v.icon = pg.image.load('images/menu/team_logo.png').convert_alpha()
pg.display.set_icon(v.icon)

v.info = pg.display.Info()
v.clock = pg.time.Clock()

# Variables ----- #
v.mouse_pos = pg.mouse.get_pos()
v.mouse_pressed = pg.mouse.get_pressed()
v.img = v.load_images('images/menu')
v.sfx = v.load_sounds('music/sfx/menu')
v.sound = v.load_sounds('music/bg/menu')

# Functions ---- #
def init_game():
    # Clear Windows #
    v.window = ''

    # Dialogue #
    for line in v.dialogue: line[0] = 0
        
    # Interface #
    v.time = 3600

    v.floor = 1
    v.room = 'entrance'
    v.enlarge = ''
    v.display = None
    v.paused = False

    v.inventory = []
    v.inv_left = c.InvArrow('left')
    v.inv_right = c.InvArrow('right')
    v.interact = True
    v.hint_button = c.Button('lightbulb', (250,50))
    v.hints = [0,-1]
    v.pause = c.Button('pause', (750,50))
    v.play = c.Button('play', (750,50))
    v.pause_screen = c.Background('paused')

    v.puzzle5 = ['A','B','C','D']
    v.puzzle9 = ['0','0','0','0']
    
    # Background #
    v.sound['bg_game'].play(loops = -1, fade_ms = 500)
    v.lights = False
    v.mask = c.Mask()
    v.breaker_switch = c.Switch()
    v.tv_screen = c.TV()
    v.flicker = c.Flicker()

    # Items #
    v.cookbook = c.UsedItem('cookbook_side', 'inv_cookbook', 'cookbook_open')
    v.skillet = c.PlacedItem('skillet', 'inv_skillet')
    v.saucepan = c.PlacedItem('saucepan', 'inv_saucepan')
    v.pot = c.PlacedItem('pot', 'inv_pot')
    v.kettle = c.PlacedItem('kettle', 'inv_kettle')
    v.oven_paper = c.UsedItem('ovenpaper_place', 'inv_ovenpaper', 'ovenpaper')
    v.key = c.DraggedItem('key', 'inv_key')
    v.morse_code = c.UsedItem('morse_key', 'inv_morse', 'morse_code')
    v.binary_code = c.UsedItem('binary_key', 'inv_binary', 'binary_code')
    v.ladder = c.PlacedItem('ladder', 'inv_ladder')
    v.box_cutter = c.DraggedItem('boxcutter', 'inv_boxcutter')
    v.hit_list = c.UsedItem('hitlist_place', 'inv_hitlist', 'hitlist')
    v.family_history = c.PlaceUseItem('famhist', 'inv_famhist', 'famhist_open', 'famhist', 'spine_hist')
    v.mom_diary = c.PlaceUseItem('momdiary_place', 'inv_momdiary', 'momdiary_open', 'momdiary', 'spine_mom')
    v.pigpen_code = c.UsedItem('pigpen_key', 'inv_pigpen', 'pigpen_code')
    v.laura_diary = c.PlaceUseItem('lauradiary', 'inv_lauradiary', 'lauradiary_open', 'lauradiary', 'spine_laura')

    # Item Lists #
    v.microwave_sprites.append(v.key)
    v.cabinet3_sprites[0] = v.pot
    v.cabinet3_sprites[1] = v.saucepan
    v.cabinet3_sprites[2] = v.skillet
    v.cabinet3_sprites[3] = v.kettle
    v.stove_valid = [v.skillet, v.saucepan, v.pot, v.kettle]
    v.oven_sprites.append(v.oven_paper)
    v.bedroom3_sprites.append(v.ladder)
    v.hallway_valid = [v.ladder]
    v.box1_sprites.append(v.hit_list)
    v.box1_sprites.append(v.family_history)
    v.table_sprites.append(v.mom_diary)
    v.table_sprites.append(v.pigpen_code)
    v.box2_sprites.append(v.laura_diary)
    v.shelf1_valid.append(v.family_history)
    v.shelf2_valid.append(v.mom_diary)
    v.shelf3_valid.append(v.laura_diary)
    
    v.playing = True
    init_room(v.floor, v.room)

def init_starting():
    v.leaderboard1 = None
    v.leaderboard2 = None
    v.leaderboard3 = None
    
    init_window('title')
    v.fading = False

    v.playing = False
    v.interact = True

    v.img.update(v.load_images('images', ['menu']))
    v.sfx.update(v.load_sounds('music/sfx', ['menu']))
    v.sound.update(v.load_sounds('music/bg', ['menu']))

# Game ----- #
import _classes as c

from room_init import init_room
from room_render import render_room
from window_init import init_window
from window_render import render_window

v.reset_game()
v.init_ending()
init_starting()

# Skip title and intro
#init_game()
#v.sound['bg_intro'].stop()

while True:
    # Events
    v.events = pg.event.get()
    for event in v.events:
        if event.type == pg.QUIT:
            quit(), exit()

    # Main
    v.mouse_pos = pg.mouse.get_pos()
    v.mouse_pressed = pg.mouse.get_pressed()

    if v.playing:

        if v.window != '':
            init_game()
            v.window = ''
            v.sound['bg_intro'].fadeout(3000)
        
        if v.paused:
            v.bg.update()
            v.update_time(False)
            v.pause_screen.update()

            if v.play.update():
                v.paused = False
                v.sfx['button_click'].play()
                pg.mixer.unpause()

        else:
            if v.enlarge == '':
                if v.pause.update():
                    v.paused = True
                    pg.mixer.pause()
                    v.sfx['button_click'].play()

            if v.hint_active:
                v.bg.update()

                if v.text.update():
                    if v.dialogue_count == 0:
                        if v.hints[1] < 3:
                            v.text = c.Slowtype(v.screen, v.hint_list[v.hints[0]][v.hints[1]], 30, 3, 'fonts/open-sans-bold.ttf', 25, (255,0,0), (50,600), 700)
                        else:
                            v.text = c.Slowtype(v.screen, "Sorry, that's the best I can come up with.", 30, 1.5, 'fonts/open-sans-bold.ttf', 30, (255,0,0), (50,600), 700)
                        v.dialogue_count = 1
                        
                    elif v.dialogue_count == 1:
                        init_room(v.floor, v.room)
                        v.hint_active = False
                        v.dialogue_count = 0
                
                v.update_time(False)

            else:
                render_room()
                v.render_inventory()
                
                if v.text is not None: v.text.update()
                if v.hint_button.update():
                    v.sfx['hint'].play()

                    v.update_hints()
                    if v.hints is not None:
                        v.bg = c.Background('guide')
                        if v.hints[1] < 3:
                            v.text = c.Slowtype(v.screen, v.question_list[v.hints[0]][v.hints[1]], 30, 3, 'fonts/open-sans-bold.ttf', 25, (100,100,255), (50,650), 700)
                        else:
                            v.text = c.Slowtype(v.screen, "I still need more help...", 30, 1.5, 'fonts/open-sans-bold.ttf', 30, (100,100,255), (50,650), 700)
                        v.dialogue_count = 0
                        v.hint_active = True

                    else:
                        v.text = c.Slowtype(v.screen, 'The exit is open! What are you waiting for? GO!', 30, 1.5, 'fonts/open-sans-bold.ttf', 25, (255,0,0), (75,100), 700)
                        
                v.update_time(True)

            if v.time <= 0:
                v.playing = False
                v.time_show = True
                v.escaped = False
                v.init_ending()
                v.sfx['scary_swoosh'].play()
                v.fader = c.wFader('arrested', 1, 3)
            
            if v.enlarge == '': v.pause.update()
            v.mask.update()
            if v.fader is not None: v.fader.update()

    else:
        render_window()
        if v.time_show is True: v.update_time(False)
        if v.fader is not None: v.fader.update()

    pg.display.update()
    v.clock.tick(60)