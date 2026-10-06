import _variables as v
import _classes as c

from room_init import init_room


def update_dialogue(num: int):
    if v.dialogue[num][0] == 0:
        v.text = c.Slowtype(v.screen, v.dialogue[num][1], 30, 2.5, 'fonts/open-sans-bold.ttf', 25, (0,0,0), (50,100), 700)
        v.dialogue[num][0] = 1

def render_room():
    
    v.bg.update()

    if v.display is v.cookbook:
        update_dialogue(5)
    for item in [v.pot, v.skillet, v.kettle, v.saucepan]:
        if item in v.inventory:
            update_dialogue(6)
            break
    if v.display is v.oven_paper:
        update_dialogue(7)
    if v.key in v.inventory:
        update_dialogue(11)
    if v.display is v.mom_diary:
        update_dialogue(18)
    if v.display is v.family_history:
        update_dialogue(20)
    if v.display is v.laura_diary:
        update_dialogue(22)
    
    if v.floor == 1:

        if v.room == 'kitchen':

            if v.enlarge == 'cabinet1':
                update_dialogue(4)
                if v.puzzle1 is True:
                    if not v.cookbook in v.inventory:
                        if v.cookbook.update((280,325)):
                            v.inventory.append(v.cookbook)
                            v.sfx['item_pickup'].play()

                else:
                    v.display_text(v.screen, v.puzzle1_text, 'fonts/digital-7.ttf', 20, (0,200,0), 'left', (430,390))
                    if v.b1.update():
                        v.update_puzzle1(1)
                    if v.b2.update():
                        v.update_puzzle1(2)
                    if v.b3.update():
                        v.update_puzzle1(3)
                    if v.b4.update():
                        v.update_puzzle1(4)
                    if v.b5.update():
                        v.update_puzzle1(5)
                    if v.b6.update():
                        v.update_puzzle1(6)
                    if v.b7.update():
                        v.update_puzzle1(7)
                    if v.b8.update():
                        v.update_puzzle1(8)
                    if v.b9.update():
                        v.update_puzzle1(9)
                    if v.b0.update():
                        v.update_puzzle1(0)
                    if v.b_enter.update():
                        v.update_puzzle1('enter')
                        init_room(v.floor, v.room)
                    if v.b_clear.update():
                        v.update_puzzle1('clear')
                
                if v.close_button.update():
                    v.enlarge = ''
                    init_room(v.floor, v.room)
                    v.sfx['button_click'].play()

            elif v.enlarge == 'microwave':
                update_dialogue(10)
                
                if v.puzzle3 is True:
                    v.display_text(v.screen, 'OPEN', 'fonts/digital-7.ttf', 30, (0,255,0), 'right', (615,310))
                    if not v.key in v.inventory:
                        if v.key.update((310,475)):
                            v.inventory.append(v.key)
                            v.sfx['item_pickup'].play()
                else:
                    v.display_text(v.screen, v.puzzle3_text, 'fonts/digital-7.ttf', 30, (0,255,0), 'right', (615,310))
                    if v.b1.update(): v.update_puzzle3(1)
                    if v.b2.update(): v.update_puzzle3(2)
                    if v.b3.update(): v.update_puzzle3(3)
                    if v.b4.update(): v.update_puzzle3(4)
                    if v.b5.update(): v.update_puzzle3(5)
                    if v.b6.update(): v.update_puzzle3(6)
                    if v.b7.update(): v.update_puzzle3(7)
                    if v.b8.update(): v.update_puzzle3(8)
                    if v.b9.update(): v.update_puzzle3(9)
                    if v.b0.update(): v.update_puzzle3(0)
                    if v.b_enter.update():
                        v.update_puzzle3('enter')
                        init_room(v.floor, v.room)
                    if v.b_clear.update(): v.update_puzzle3('clear')
                
                if v.close_button.update():
                    v.enlarge = ''
                    init_room(v.floor, v.room)
                    v.sfx['button_click'].play()

            elif v.enlarge == 'cabinet2':
                if v.close_button.update():
                    v.enlarge = ''
                    init_room(v.floor, v.room)
                    v.sfx['button_click'].play()

            elif v.enlarge == 'sink':
                if v.close_button.update():
                    v.enlarge = ''
                    init_room(v.floor, v.room)
                    v.sfx['button_click'].play()

            elif v.enlarge == 'cabinet3':
                try:
                    if v.cabinet3_sprites[0].update((275,325)):
                        v.inventory.append(v.cabinet3_sprites[0])
                        v.sfx['item_pickup'].play()
                        v.cabinet3_sprites[0] = None
                except: pass
                try:
                    if v.cabinet3_sprites[1].update((505,335)):
                        v.inventory.append(v.cabinet3_sprites[1])
                        v.sfx['item_pickup'].play()
                        v.cabinet3_sprites[1] = None
                except: pass
                try:
                    if v.cabinet3_sprites[2].update((300,525)):
                        v.inventory.append(v.cabinet3_sprites[2])
                        v.sfx['item_pickup'].play()
                        v.cabinet3_sprites[2] = None
                except: pass
                try:
                    if v.cabinet3_sprites[3].update((515,505)):
                        v.inventory.append(v.cabinet3_sprites[3])
                        v.sfx['item_pickup'].play()
                        v.cabinet3_sprites[3] = None
                except: pass

                if v.close_button.update():
                        v.enlarge = ''
                        init_room(v.floor, v.room)
                        v.sfx['button_click'].play()

            elif v.enlarge == 'stove':
                try: 
                    if v.stove_placed[0].update(v.burner1.rect.center):
                        v.inventory.append(v.stove_placed[0])
                        v.sfx['item_pickup'].play()
                        v.stove_placed[0] = None
                except: pass
                try:
                    if v.stove_placed[1].update(v.burner2.rect.center):
                        v.inventory.append(v.stove_placed[1])
                        v.sfx['item_pickup'].play()
                        v.stove_placed[1] = None
                except: pass
                try: 
                    if v.stove_placed[2].update(v.burner3.rect.center):
                        v.inventory.append(v.stove_placed[2])
                        v.sfx['item_pickup'].play()
                        v.stove_placed[2] = None
                except: pass
                try: 
                    if v.stove_placed[3].update(v.burner4.rect.center):
                        v.inventory.append(v.stove_placed[3])
                        v.sfx['item_pickup'].play()
                        v.stove_placed[3] = None
                except: pass
                
                if v.burner1.update() and v.display in v.stove_valid:
                    if v.stove_placed[0] is None:
                        index = v.stove_valid.index(v.display)
                        v.stove_placed[0] = v.stove_valid[index]
                        v.inventory.remove(v.stove_valid[index])
                        v.sfx['place_pot'].play()
                        v.interact = True
                        v.display = None
                if v.burner2.update() and v.display in v.stove_valid:
                    if v.stove_placed[1] is None:
                        index = v.stove_valid.index(v.display)
                        v.stove_placed[1] = v.stove_valid[index]
                        v.inventory.remove(v.stove_valid[index])
                        v.sfx['place_pot'].play()
                        v.interact = True
                        v.display = None
                if v.burner3.update() and v.display in v.stove_valid:
                    if v.stove_placed[2] is None:
                        index = v.stove_valid.index(v.display)
                        v.stove_placed[2] = v.stove_valid[index]
                        v.inventory.remove(v.stove_valid[index])
                        v.sfx['place_pot'].play()
                        v.interact = True
                        v.display = None
                if v.burner4.update() and v.display in v.stove_valid:
                    if v.stove_placed[3] is None:
                        index = v.stove_valid.index(v.display)
                        v.stove_placed[3] = v.stove_valid[index]
                        v.inventory.remove(v.stove_valid[index])
                        v.sfx['place_pot'].play()
                        v.interact = True
                        v.display = None
                if v.puzzle2 is not True:
                    if v.stove_enter.update(): v.update_puzzle2()
                else:
                    v.display_text(v.screen, 'Door', 'fonts/digital-7.ttf', 40, (0,200,0), 'left', (453,230))
                
                if v.close_button.update():
                    v.enlarge = ''
                    init_room(v.floor, v.room)
                    v.sfx['button_click'].play()
            
            elif v.enlarge == 'oven':
                if v.puzzle2 is True and not v.oven_paper in v.inventory:
                    if v.oven_paper.update((400,400)):
                        v.inventory.append(v.oven_paper)
                        v.sfx['item_pickup'].play()
                
                if v.close_button.update():
                    v.enlarge = ''
                    init_room(v.floor, v.room)
                    v.sfx['button_click'].play()

            else:
                if v.cabinet1.update() and v.lights:
                    v.enlarge = 'cabinet1'
                    init_room(v.floor, v.room)
                if v.microwave.update() and v.lights:
                    v.enlarge = 'microwave'
                    init_room(v.floor, v.room)
                if v.cabinet2.update() and v.lights:
                    v.enlarge = 'cabinet2'
                    init_room(v.floor, v.room)
                if v.sink.update() and v.lights:
                    v.enlarge = 'sink'
                    init_room(v.floor, v.room)
                if v.cabinet3.update() and v.lights:
                    v.enlarge = 'cabinet3'
                    init_room(v.floor, v.room)
                if v.stove.update() and v.lights:
                    v.enlarge = 'stove'
                    init_room(v.floor, v.room)
                if v.oven.update() and v.lights:
                    v.enlarge = 'oven'
                    init_room(v.floor, v.room)
                if v.lights:
                    if v.a_upleft.update():
                        v.fader = c.Fader(2, 'hallway')
                        v.sfx['walk_stairs'].play()
                
                if v.a_right.update():
                    v.fader = c.Fader(1, 'entrance')

        elif v.room == 'entrance':
            update_dialogue(0)

            if v.enlarge == 'breaker':
                v.breaker_switch.update()
                if v.lights:
                    update_dialogue(1)
                
                if v.close_button.update():
                    v.enlarge = ''
                    init_room(v.floor, v.room)
                    v.sfx['button_click'].play()

            else:
                if v.breaker.update():
                    v.enlarge = 'breaker'
                    init_room(v.floor, v.room)
                
                if v.a_left.update():
                    v.fader = c.Fader(1, 'kitchen')
                if v.a_right.update():
                    v.fader = c.Fader(1, 'living')
            

        elif v.room == 'living':

            if v.enlarge == 'bookshelf':
                update_dialogue(23)
                if v.bookshelf_level == 1:
                    try:
                        if v.puzzle10[0].update(v.bookshelf_slot1.rect.center):
                            v.inventory.append(v.puzzle10[0])
                            v.sfx['item_pickup'].play()
                            v.puzzle10[0] = None
                    except: pass

                    if v.bookshelf_slot1.update() and v.display in v.shelf1_valid:
                        index = v.shelf1_valid.index(v.display)
                        v.puzzle10[0] = v.shelf1_valid[index]
                        v.puzzle10[0].status = 'inserted'
                        v.inventory.remove(v.shelf1_valid[index])
                        v.sfx['book_place'].play()
                        v.interact = True
                        v.display = None

                    if v.a_down.update():
                        v.bookshelf_level = 2
                        init_room(v.floor, v.room)

                elif v.bookshelf_level == 2:
                    try:
                        if v.puzzle10[1].update(v.bookshelf_slot2.rect.center):
                            v.inventory.append(v.puzzle10[1])
                            v.sfx['item_pickup'].play()
                            v.puzzle10[1] = None
                    except: pass

                    if v.bookshelf_slot2.update() and v.display in v.shelf2_valid:
                        index = v.shelf2_valid.index(v.display)
                        v.puzzle10[1] = v.shelf2_valid[index]
                        v.puzzle10[1].status = 'inserted'
                        v.inventory.remove(v.shelf2_valid[index])
                        v.sfx['book_place'].play()
                        v.interact = True
                        v.display = None

                    if v.a_up.update():
                        v.bookshelf_level = 1
                        init_room(v.floor, v.room)
                    if v.a_down.update():
                        v.bookshelf_level = 3
                        init_room(v.floor, v.room)
                        
                elif v.bookshelf_level == 3:
                    try:
                        if v.puzzle10[2].update(v.bookshelf_slot3.rect.center):
                            v.inventory.append(v.puzzle10[2])
                            v.sfx['item_pickup'].play()
                            v.puzzle10[2] = None
                    except: pass

                    if v.bookshelf_slot3.update() and v.display in v.shelf3_valid:
                        index = v.shelf3_valid.index(v.display)
                        v.puzzle10[2] = v.shelf3_valid[index]
                        v.puzzle10[2].status = 'inserted'
                        v.inventory.remove(v.shelf3_valid[index])
                        v.sfx['book_place'].play()
                        v.interact = True
                        v.display = None

                    if v.a_up.update():
                        v.bookshelf_level = 2
                        init_room(v.floor, v.room)

                if v.close_button.update():
                    if v.puzzle10[0] == v.shelf1_valid[0] and v.puzzle10[1] == v.shelf2_valid[0] and v.puzzle10[2] == v.shelf3_valid[0]:
                        v.puzzle10 = True
                    v.enlarge = ''
                    init_room(v.floor, v.room)
                    v.sfx['button_click'].play()
                    v.sfx['shine_fade'].play()

            elif v.enlarge == 'posters':
                if v.oven_paper in v.inventory:
                    update_dialogue(9)
                else:
                    update_dialogue(8)
                
                if v.close_button.update():
                    v.enlarge = ''
                    init_room(v.floor, v.room)
                    v.sfx['button_click'].play()

            elif v.enlarge == 'tv':
                if v.tv_screen.update():
                    v.tv_adcount += 1
                if v.tv_adcount >= 4:
                    update_dialogue(2)
                if v.tv_adcount >= 9:
                    update_dialogue(3)
                
                if v.close_button.update():
                    v.enlarge = ''
                    init_room(v.floor, v.room)
                    v.sfx['button_click'].play()

            else:
                if v.puzzle10 is not True:
                    if v.bookshelf.update() and v.lights:
                        v.enlarge = 'bookshelf'
                        init_room(v.floor, v.room)
                else:
                    update_dialogue(24)
                    
                    if v.lights:
                        if v.a_right.update():
                            v.fader = c.Fader(1, 'study')
                if v.tv.update() and v.lights:
                    v.enlarge = 'tv'
                    init_room(v.floor, v.room)
                if v.posters.update() and v.lights:
                    v.enlarge = 'posters'
                    init_room(v.floor, v.room)
                
                if v.a_down.update():
                    v.fader = c.Fader(1, 'entrance')

        elif v.room == 'study':
            
            if v.enlarge == 'desk':
                
                if v.desk_view == 1:
                
                    if v.desk_paper == 1:
                        update_dialogue(26)
                        if v.a_right.update():
                            v.desk_paper = 2
                            init_room(v.floor, v.room)
                            v.sfx['turn_page'].play()

                        if v.close_button.update():
                            v.desk_view = 0
                            init_room(v.floor, v.room)
                            v.sfx['button_click'].play()

                    elif v.desk_paper == 2:
                        update_dialogue(27)
                        if v.a_left.update():
                            v.desk_paper = 1
                            init_room(v.floor, v.room)
                            v.sfx['turn_page'].play()
                        if v.a_right.update():
                            v.desk_paper = 3
                            init_room(v.floor, v.room)
                            v.sfx['turn_page'].play()

                        if v.close_button.update():
                            v.desk_view = 0
                            init_room(v.floor, v.room)
                            v.sfx['button_click'].play()

                    elif v.desk_paper == 3:
                        update_dialogue(28)
                        if v.a_left.update():
                            v.desk_paper = 2
                            init_room(v.floor, v.room)
                            v.sfx['turn_page'].play()
                        
                        if v.close_button.update():
                            v.desk_view = 0
                            init_room(v.floor, v.room)
                            v.sfx['button_click'].play()

                    elif v.desk_paper == 4:
                        update_dialogue(29)

                        if v.close_button.update():
                            v.desk_view = 0
                            init_room(v.floor, v.room)
                            v.sfx['button_click'].play()
                
                else:
                    if v.newspaper.update():
                        v.desk_view = 1
                        v.desk_paper = 1
                        init_room(v.floor, v.room)
                        v.sfx['turn_page'].play()
                    if v.doctor_letter.update():
                        v.desk_view = 1
                        v.desk_paper = 4
                        init_room(v.floor, v.room)
                        v.sfx['turn_page'].play()

                    if v.close_button.update():
                        v.enlarge = ''
                        init_room(v.floor, v.room)
                        v.sfx['button_click'].play()

            else:
                if v.can_escape is not True:
                    update_dialogue(25)
                    if v.study_door.update():
                        v.can_escape = True
                        init_room(v.floor, v.room)
                        v.sfx['open_door'].play()
                else:
                    update_dialogue(30)

                    if v.a_up.update():
                        v.playing = False
                        v.window = 'escaped'
                        v.time_show = True
                        v.escaped = True
                        v.sound['bg_game'].fadeout(3000)
                        v.sfx['scary_swoosh'].play()
                        v.init_ending()
                        v.fader = c.wFader('escaped', 1, 3)
                if v.desk.update():
                    v.enlarge = 'desk'
                    init_room(v.floor, v.room)
                    v.sfx['button_click'].play()

                if v.a_down.update():
                    v.fader = c.Fader(1, 'living')

    elif v.floor == 2:

        if v.room == 'hallway':

            if v.enlarge == 'door1':
                if v.room1_lock.update() and v.display is v.key:
                    v.room1_open = True
                    v.sfx['use_key'].play()
                    update_dialogue(13)

                if v.close_button.update():
                    v.enlarge = ''
                    init_room(v.floor, v.room)
                    v.sfx['button_click'].play()
                    if v.room1_open is True: v.sfx['open_door'].play()

            elif v.enlarge == 'door2':
                v.p4_btime -= 1/60
                if v.p4_btime < 0: v.p4_btime = 0
                if v.b1.update(): v.update_puzzle4(1)
                if v.b2.update(): v.update_puzzle4(2)
                if v.b3.update(): v.update_puzzle4(3)
                if v.b4.update(): v.update_puzzle4(4)
                if v.b5.update(): v.update_puzzle4(5)
                if v.b6.update(): v.update_puzzle4(6)
                if v.b7.update(): v.update_puzzle4(7)
                if v.b8.update(): v.update_puzzle4(8)
                if v.b9.update(): v.update_puzzle4(9)
                if v.b_clear.update(): v.update_puzzle4('clear')
                if v.b0.update(): v.update_puzzle4(0)
                if v.b_enter.update(): v.update_puzzle4('enter')
                if v.puzzle4 is not True:
                    v.display_text(v.screen, v.puzzle4_text, 'fonts/digital-7.ttf', 30, (0,200,0), 'left', (325,256))
                else:
                    v.display_text(v.screen, '- OPEN -', 'fonts/digital-7.ttf', 30, (0,200,0), 'left', (325,256))
                
                if v.close_button.update():
                    v.enlarge = ''
                    init_room(v.floor, v.room)
                    v.sfx['button_click'].play()
                    if v.puzzle4 is True: v.sfx['open_door'].play()

            elif v.enlarge == 'door3':
                v.display_text(v.screen, v.puzzle5[0], 'fonts/open-sans-bold.ttf', 50, (0,0,0), 'middle', (291,400))
                v.display_text(v.screen, v.puzzle5[1], 'fonts/open-sans-bold.ttf', 50, (0,0,0), 'middle', (366,400))
                v.display_text(v.screen, v.puzzle5[2], 'fonts/open-sans-bold.ttf', 50, (0,0,0), 'middle', (439,400))
                v.display_text(v.screen, v.puzzle5[3], 'fonts/open-sans-bold.ttf', 50, (0,0,0), 'middle', (511,400))
                
                if v.b1.update(): v.update_puzzle5(1)
                if v.b2.update(): v.update_puzzle5(2)
                if v.b3.update(): v.update_puzzle5(3)
                if v.b4.update(): v.update_puzzle5(4)

                if v.close_button.update():
                    if v.puzzle5[0] == 'G' and v.puzzle5[1] == 'O' and v.puzzle5[2] == 'N' and v.puzzle5[3] == 'E':
                        v.puzzle5 = True
                        v.sfx['unlock'].play()
                        v.sfx['open_door'].play()
                    v.enlarge = ''
                    init_room(v.floor, v.room)

            elif v.enlarge == 'hatch':
                update_dialogue(17)
                v.display_text(v.screen, v.p6_text1, 'fonts/digital-7.ttf', 60, (0,0,0), 'middle', (328,268))
                v.display_text(v.screen, v.p6_text2, 'fonts/digital-7.ttf', 60, (0,0,0), 'middle', (398,268))
                v.display_text(v.screen, v.p6_text3, 'fonts/digital-7.ttf', 60, (0,0,0), 'middle', (468,268))
                if v.b1.update(): v.update_puzzle6(1)
                if v.b2.update(): v.update_puzzle6(2)
                if v.b3.update(): v.update_puzzle6(3)
                if v.b4.update(): v.update_puzzle6(4)
                if v.b5.update(): v.update_puzzle6(5)
                if v.b6.update(): v.update_puzzle6(6)
                if v.b7.update(): v.update_puzzle6(7)
                if v.b8.update(): v.update_puzzle6(8)
                if v.b9.update(): v.update_puzzle6(9)
                if v.b_clear.update(): v.update_puzzle6('clear')
                if v.b0.update(): v.update_puzzle6(0)
                if v.b_enter.update(): v.update_puzzle6('enter')

                if v.close_button.update():
                    v.enlarge = ''
                    init_room(v.floor, v.room)
                    v.sfx['button_click'].play()
                    if v.puzzle6 is True: v.sfx['open_door'].play()

            else:
                update_dialogue(12)

                if v.room0_open == False:
                    if v.room0_door.update():
                        v.fader = c.Fader(2, 'bathroom')
                else:
                    if v.a_left.update():
                        v.fader = c.Fader(2, 'bathroom')

                if v.room1_open == False:
                    if v.room1_door.update():
                        v.enlarge = 'door1'
                        init_room(v.floor, v.room)
                else:
                    if v.a_left2.update():
                        v.fader = c.Fader(2, 'bedroom1')

                if not v.ladder in v.hallway_placed:
                    if v.puzzle4 is not True:
                        if v.room2_door.update():
                            v.enlarge = 'door2'
                            init_room(v.floor, v.room)
                    else:
                        if v.a_up.update():
                            v.fader = c.Fader(2, 'bedroom2')

                if v.puzzle5 is not True:
                    if v.room3_door.update():
                        v.enlarge = 'door3'
                        init_room(v.floor, v.room)
                else:
                    if v.a_right.update():
                        v.fader = c.Fader(2, 'bedroom3')

                ladder_attic = 0
                if v.ladder in v.hallway_placed:
                    if v.puzzle6 is not True:
                        if v.attic_hatch.update():
                            v.enlarge = 'hatch'
                            init_room(v.floor, v.room)
                            ladder_attic = 1
                    else:
                        if v.a_up2.update():
                            v.fader = c.Fader(3, 'attic')
                            ladder_attic = 1
                            v.sfx['walk_stairs'].play()

                try: 
                    if v.hallway_placed[0].update(v.hallway_place.rect.center) and ladder_attic == 0:
                        v.inventory.append(v.hallway_placed[0])
                        v.sfx['item_pickup'].play()
                        v.hallway_placed.remove(v.hallway_placed[0])
                        init_room(v.floor, v.room)
                except: pass

                if v.hallway_place.update() and v.display in v.hallway_valid:
                    v.hallway_placed.append(v.hallway_valid[0])
                    v.inventory.remove(v.hallway_valid[0])
                    v.sfx['place_ladder'].play()
                    v.interact = True
                    v.display = None
                    init_room(v.floor, v.room)
                
                if v.a_downright.update():
                    v.fader = c.Fader(1, 'kitchen')
                    v.sfx['walk_stairs'].play()

        elif v.room == 'bathroom':
            if v.a_down.update():
                v.fader = c.Fader(2, 'hallway')

        elif v.room == 'bedroom1':
            update_dialogue(14)
            if not v.morse_code in v.inventory:
                if v.morse_code.update((300,500)):
                    v.inventory.append(v.morse_code)
                    v.sfx['item_pickup'].play()
            if not v.binary_code in v.inventory:
                if v.binary_code.update((500,500)):
                    v.inventory.append(v.binary_code)
                    v.sfx['item_pickup'].play()
            
            if v.a_down.update():
                v.fader = c.Fader(2, 'hallway')
                
            v.flicker.update()

        elif v.room == 'bedroom2':
            update_dialogue(15)
            if v.enlarge == 'computer':
                if v.close_button.update():
                    v.enlarge = ''
                    init_room(v.floor, v.room)
                    v.sfx['button_click'].play()
            else:
                update_dialogue(8)
                if v.computer.update():
                    v.enlarge = 'computer'
                    init_room(v.floor, v.room)
                if v.a_down.update():
                    v.fader = c.Fader(2, 'hallway')

        elif v.room == 'bedroom3':
            update_dialogue(16)
            if v.ladder in v.bedroom3_sprites:
                if v.ladder.update((725,400)):
                    v.inventory.append(v.ladder)
                    v.sfx['item_pickup'].play()
                    v.bedroom3_sprites.remove(v.ladder)
            if v.a_down.update():
                v.fader = c.Fader(2, 'hallway')

    elif v.floor == 3:

        if v.room == 'attic':
            if v.enlarge == 'box1':
                update_dialogue(19)
                if v.puzzle7 is not True:
                    if v.box1_cut.update() and v.display is v.box_cutter:
                        v.puzzle7 = True
                        init_room(v.floor, v.room)
                        v.sfx['open_box'].play()
                else:
                    if v.hit_list in v.box1_sprites:
                        if v.hit_list.update((400,400)):
                            v.inventory.append(v.hit_list)
                            v.sfx['item_pickup'].play()
                            v.box1_sprites.remove(v.hit_list)
                    if v.family_history in v.box1_sprites:
                        if v.family_history.update((400,400)):
                            v.inventory.append(v.family_history)
                            v.sfx['item_pickup'].play()
                            v.box1_sprites.remove(v.family_history)
                if v.close_button.update():
                    v.enlarge = ''
                    init_room(v.floor, v.room)
                    v.sfx['button_click'].play()

            elif v.enlarge == 'table':
                if v.mom_diary in v.table_sprites:
                    if v.mom_diary.update((400,400)):
                        v.inventory.append(v.mom_diary)
                        v.sfx['item_pickup'].play()
                        v.table_sprites.remove(v.mom_diary)
                if v.pigpen_code in v.table_sprites:
                    if v.pigpen_code.update((500,400)):
                        v.inventory.append(v.pigpen_code)
                        v.sfx['item_pickup'].play()
                        v.table_sprites.remove(v.pigpen_code)
                if v.close_button.update():
                    v.enlarge = ''
                    init_room(v.floor, v.room)
                    v.sfx['button_click'].play()

            elif v.enlarge == 'box2':
                update_dialogue(19)
                if v.puzzle8 is not True:
                    if v.box2_cut.update() and v.display is v.box_cutter:
                        v.puzzle8 = True
                        init_room(v.floor, v.room)
                        v.sfx['open_box'].play()
                else:
                    if v.puzzle9 is not True:
                        if v.diary_view == 1:
                            update_dialogue(21)
                            v.display_text(v.screen, v.puzzle9[0], 'fonts/open-sans-bold.ttf', 30, (0,0,0), 'middle', (558,360))
                            v.display_text(v.screen, v.puzzle9[1], 'fonts/open-sans-bold.ttf', 30, (0,0,0), 'middle', (558,405))
                            v.display_text(v.screen, v.puzzle9[2], 'fonts/open-sans-bold.ttf', 30, (0,0,0), 'middle', (558,450))
                            v.display_text(v.screen, v.puzzle9[3], 'fonts/open-sans-bold.ttf', 30, (0,0,0), 'middle', (558,495))
                            
                            if v.b1.update(): v.update_puzzle9(1)
                            if v.b2.update(): v.update_puzzle9(2)
                            if v.b3.update(): v.update_puzzle9(3)
                            if v.b4.update(): v.update_puzzle9(4)

                            if v.close_button.update():
                                if v.puzzle9[0] == '0' and v.puzzle9[1] == '6' and v.puzzle9[2] == '2' and v.puzzle9[3] == '9':
                                    v.puzzle9 = True
                                    v.sfx['unlock'].play()
                                v.enlarge = 'box2'
                                v.diary_view = 0
                                init_room(v.floor, v.room)

                        else:
                            if v.laura_diary_locked.update():
                                v.diary_view = 1
                                init_room(v.floor, v.room)
                    else:
                        if v.laura_diary in v.box2_sprites:
                            if v.laura_diary.update((400,400)):
                                v.inventory.append(v.laura_diary)
                                v.sfx['item_pickup'].play()
                                v.box2_sprites.remove(v.laura_diary)

                if v.close_button.update():
                    v.enlarge = ''
                    init_room(v.floor, v.room)
                    v.sfx['button_click'].play()

            elif v.enlarge == 'rug':
                if not v.box_cutter in v.inventory:
                    if v.box_cutter.update((550,425)):
                        v.inventory.append(v.box_cutter)
                        v.sfx['item_pickup'].play()
                if v.close_button.update():
                    v.enlarge = ''
                    init_room(v.floor, v.room)
                    v.sfx['button_click'].play()

            else:
                if v.box1.update():
                    v.enlarge = 'box1'
                    init_room(v.floor, v.room)
                if v.table.update():
                    v.enlarge = 'table'
                    init_room(v.floor, v.room)
                if v.box2.update():
                    v.enlarge = 'box2'
                    init_room(v.floor, v.room)
                if v.rug.update():
                    v.enlarge = 'rug'
                    init_room(v.floor, v.room)
                if v.a_down.update():
                    v.enlarge = ''
                    v.fader = c.Fader(2, 'hallway')
