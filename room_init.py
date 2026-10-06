import _variables as v
import _classes as c


def init_room(tofloor=0, toroom=''):
    v.playing = True
    v.floor = tofloor
    v.room = toroom
    
    if v.enlarge != '': v.sfx['button_click'].play()

    if v.floor == 1:

        if v.room == 'kitchen':

            if v.enlarge == 'cabinet1':
                if v.puzzle1 == True:
                    v.bg = c.Background('cabinet_open')
                else:
                    v.bg = c.Background('cabinet_closed')

                    v.b1 = c.Hitbox(15, 15, (441,419))
                    v.b2 = c.Hitbox(15, 15, (464,419))
                    v.b3 = c.Hitbox(15, 15, (489,419))
                    v.b4 = c.Hitbox(15, 15, (513,419))
                    v.b5 = c.Hitbox(15, 15, (536,419))
                    v.b6 = c.Hitbox(15, 15, (441,442))
                    v.b7 = c.Hitbox(15, 15, (464,442))
                    v.b8 = c.Hitbox(15, 15, (489,442))
                    v.b9 = c.Hitbox(15, 15, (513,442))
                    v.b0 = c.Hitbox(15, 15, (536,442))
                    v.b_enter = c.Hitbox(15, 15, (560,419))
                    v.b_clear = c.Hitbox(15, 15, (560,442))

                v.close_button = c.Button('x_out', (750,50))

            elif v.enlarge == 'microwave': 
                
                if v.puzzle3 == True:
                    v.bg = c.Background('microwave_open')
                else:
                    v.bg = c.Background('microwave_closed')

                    v.puzzle3 = []
                    v.b1 = c.Hitbox(25, 25, (535,377))
                    v.b2 = c.Hitbox(25, 25, (570,377))
                    v.b3 = c.Hitbox(25, 25, (605,377))
                    v.b4 = c.Hitbox(25, 25, (535,410))
                    v.b5 = c.Hitbox(25, 25, (570,410))
                    v.b6 = c.Hitbox(25, 25, (605,410))
                    v.b7 = c.Hitbox(25, 25, (535,443))
                    v.b8 = c.Hitbox(25, 25, (570,443))
                    v.b9 = c.Hitbox(25, 25, (605,443))
                    v.b0 = c.Hitbox(25, 25, (570,475))
                    v.b_enter = c.Hitbox(25, 25, (605,475))
                    v.b_clear = c.Hitbox(25, 25, (535,475))

                v.close_button = c.Button('x_out', (750,50))

            elif v.enlarge == 'cabinet2':
                v.bg = c.Background('microwave_cab')

                v.close_button = c.Button('x_out', (750,50))

            elif v.enlarge == 'sink':
                v.bg = c.Background('sink')

                v.close_button = c.Button('x_out', (750,50))

            elif v.enlarge == 'cabinet3':
                v.bg = c.Background('sinkcab_open')

                v.close_button = c.Button('x_out', (750,50))

            elif v.enlarge == 'stove':
                v.bg = c.Background('stove_top')

                v.burner1 = c.Hoverbox(150, 90, (270,310))
                v.burner2 = c.Hoverbox(150, 90, (530,310))
                v.burner3 = c.Hoverbox(200, 100, (225,430))
                v.burner4 = c.Hoverbox(200, 100, (575,430))
                v.stove_enter = c.Hitbox(55, 25, (637,232))

                v.close_button = c.Button('x_out', (750,50))

            elif v.enlarge == 'oven':
                if v.puzzle2 != True:
                    v.bg = c.Background('oven_closed')
                else:
                    v.bg = c.Background('oven_open')

                v.close_button = c.Button('x_out', (750,50))

            else:
                v.bg = c.Background('kitchen')

                v.cabinet1 = c.Hitbox(200, 130, (232,228))
                v.microwave = c.Hitbox(150, 90, (225,350))
                v.cabinet2 = c.Hitbox(205, 140, (233,473))
                v.sink = c.Hitbox(200, 75, (462,360))
                v.cabinet3 = c.Hitbox(200, 140, (455,473))
                v.stove = c.Hitbox(90, 70, (670,370))
                v.oven = c.Hitbox(180, 115, (710,490))

                if v.lights: v.a_upleft = c.Arrow((50,400), 135)
                v.a_right = c.Arrow((750,400), 0)

        if v.room == 'entrance':

            if v.enlarge == 'breaker':
                v.bg = c.Background('breaker_box')

                v.close_button = c.Button('x_out', (750,50))
            else:
                v.bg = c.Background('entrance')

                v.breaker = c.Hitbox(30, 50, (400,368))

                v.a_left = c.Arrow((50,400), 180)
                v.a_right = c.Arrow((750,400), 0)

        elif v.room == 'living':

            if v.enlarge == 'bookshelf':
                if v.bookshelf_level == 1:
                    v.bg = c.Background('bookshelf_top')

                    v.bookshelf_slot1 = c.Hoverbox(90, 375, (488,398))

                    v.a_down = c.Arrow((400,650), -90)

                elif v.bookshelf_level == 2:
                    v.bg = c.Background('bookshelf_middle')

                    v.bookshelf_slot2 = c.Hoverbox(90, 375, (313,398))
                    
                    v.a_up = c.Arrow((400,50), 90)
                    v.a_down = c.Arrow((400,650), -90)

                elif v.bookshelf_level == 3:
                    v.bg = c.Background('bookshelf_bottom')

                    v.bookshelf_slot3 = c.Hoverbox(90, 375, (488,399))

                    v.a_up = c.Arrow((400,50), 90)

                v.close_button = c.Button('x_out', (750,50))
            
            elif v.enlarge == 'posters':
                v.bg = c.Background('wall_art')
                
                v.close_button = c.Button('x_out', (750,50))

            elif v.enlarge == 'tv':
                v.bg = c.Background('tv_close')
                
                v.close_button = c.Button('x_out', (750,50))

            else:
                if v.puzzle10 != True:
                    v.bg = c.Background('living_room')
                    v.bookshelf = c.Hitbox(180, 300, (90,395))
                else:
                    v.bg = c.Background('living_study')
                    v.a_right = c.Arrow((80,400), 180)
                v.bookshelf_level = 1
                v.posters = c.Hitbox(240, 115, (400,375))
                v.tv = c.Hitbox(100, 60, (400,465))

                v.a_down = c.Arrow((400,650), -90)

        elif v.room == 'study':

            if v.enlarge == 'desk':

                if v.desk_view == 1:

                    if v.desk_paper == 1:
                        v.bg = c.Background('desk_news2')

                        v.a_right = c.Arrow((750,400), 0)

                    elif v.desk_paper == 2:
                        v.bg = c.Background('desk_news1')

                        v.a_left = c.Arrow((50,400), 180)
                        v.a_right = c.Arrow((750,400), 0)

                    elif v.desk_paper == 3:
                        v.bg = c.Background('desk_mom')

                        v.a_left = c.Arrow((50,400), 180)
                    
                    elif v.desk_paper == 4:
                        v.bg = c.Background('desk_doctor')

                else:
                    v.bg = c.Background('desk')

                    v.desk_paper = 0
                    v.newspaper = c.Hitbox(195, 150, (400,390))
                    v.doctor_letter = c.Hitbox(120, 95, (592,410))

                v.close_button = c.Button('x_out', (750,50))

            else:
                if v.can_escape != True:
                    v.bg = c.Background('study_closed')

                    v.study_door = c.Hitbox(110, 205, (168,298))
                else:
                    v.bg = c.Background('study_open')

                    v.a_up = c.Arrow((165,400), 90)
                v.desk = c.Hitbox(260, 170, (580,400))

                v.a_down = c.Arrow((400,650), -90)

    elif v.floor == 2:

        if v.room == 'hallway':
            
            if v.enlarge == 'door1':
                v.bg = c.Background('boy_lock')

                v.room1_lock = c.Hoverbox(90, 50, (500,420))

                v.close_button = c.Button('x_out', (750,50))

            elif v.enlarge == 'door2':
                v.bg = c.Background('parent_lock')

                v.b1 = c.Hitbox(50, 35, (345,315))
                v.b2 = c.Hitbox(50, 35, (400,315))
                v.b3 = c.Hitbox(50, 35, (455,315))
                v.b4 = c.Hitbox(50, 33, (345,352))
                v.b5 = c.Hitbox(50, 33, (400,352))
                v.b6 = c.Hitbox(50, 33, (455,352))
                v.b7 = c.Hitbox(50, 35, (345,391))
                v.b8 = c.Hitbox(50, 35, (400,391))
                v.b9 = c.Hitbox(50, 35, (455,391))
                v.b_clear = c.Hitbox(50, 35, (345,430))
                v.b0 = c.Hitbox(50, 35, (400,430))
                v.b_enter = c.Hitbox(50, 35, (455,430))

                v.close_button = c.Button('x_out', (750,50))

            elif v.enlarge == 'door3':
                v.bg = c.Background('girl_lock')

                v.b1 = c.Hitbox(50, 125, (291,400))
                v.b2 = c.Hitbox(50, 125, (366,400))
                v.b3 = c.Hitbox(50, 125, (439,400))
                v.b4 = c.Hitbox(50, 125, (511,400))

                v.close_button = c.Button('x_out', (750,50))

            elif v.enlarge == 'hatch':
                v.bg = c.Background('attic_lock')

                v.b1 = c.Hitbox(65, 53, (331,339))
                v.b2 = c.Hitbox(65, 53, (400,339))
                v.b3 = c.Hitbox(65, 53, (469,339))
                v.b4 = c.Hitbox(66, 57, (331,397))
                v.b5 = c.Hitbox(65, 57, (400,397))
                v.b6 = c.Hitbox(66, 57, (469,397))
                v.b7 = c.Hitbox(65, 48, (331,453))
                v.b8 = c.Hitbox(65, 48, (400,453))
                v.b9 = c.Hitbox(65, 48, (469,453))
                v.b_clear = c.Hitbox(65, 55, (331,506))
                v.b0 = c.Hitbox(65, 55, (400,506))
                v.b_enter = c.Hitbox(65, 55, (469,506))

                v.close_button = c.Button('x_out', (750,50))

            else:
                v.bg = c.Background('hallway')

                if v.room0_open == False: v.room0_door = c.Hitbox(110, 550, (55,450))
                else: v.a_left = c.Arrow((115,675), 180)

                if v.room1_open == False: v.room1_door = c.Hitbox(50, 260, (240,450))
                else: v.a_left2 = c.Arrow((275,550), 180)

                if not v.ladder in v.hallway_placed:
                    if v.puzzle4 != True: v.room2_door = c.Hitbox(100, 140, (400,440))
                    else: v.a_up = c.Arrow((400,525), 90)

                if v.puzzle5 != True: v.room3_door = c.Hitbox(50, 260, (555,450))
                else: v.a_right = c.Arrow((525,550), 0)

                if v.ladder in v.hallway_placed:
                    if v.puzzle6 != True: v.attic_hatch = c.Hitbox(135, 110, (400,175))
                    else: v.a_up2 = c.Arrow((400,225), 90)
                v.hallway_place = c.Hoverbox(100, 100, (400,380))

                v.a_downright = c.Arrow((750,550), -45)

        elif v.room == 'bathroom':
            v.bg = c.Background('bathroom')

            v.room0_open = True

            v.a_down = c.Arrow((400,650), -90)

        elif v.room == 'bedroom1':
            v.bg = c.Background('boy_room')

            v.a_down = c.Arrow((400,650), -90)

        elif v.room == 'bedroom2':

            if v.enlarge == 'computer':
                v.bg = c.Background('keyboard')

                v.close_button = c.Button('x_out', (750,50))
            else:
                v.bg = c.Background('parent_room')

                v.computer = c.Hitbox(200, 150, (400,385))

                v.a_down = c.Arrow((400,650), -90)

        elif v.room == 'bedroom3':
            v.bg = c.Background('girl_room')

            v.a_down = c.Arrow((400,650), -90)

    elif v.floor == 3:

        if v.room == 'attic':
            if v.enlarge == 'box1':
                if v.puzzle7 != True:
                    v.bg = c.Background('taped_box')

                    v.box1_cut = c.Hoverbox(300, 300, (400,400))
                else: v.bg = c.Background('fambox_open')

                v.close_button = c.Button('x_out', (750,50))

            elif v.enlarge == 'table':
                v.bg = c.Background('table')

                v.close_button = c.Button('x_out', (750,50))

            elif v.enlarge == 'box2':
                if v.puzzle8 != True:
                    v.bg = c.Background('taped_box')

                    v.box2_cut = c.Hoverbox(300, 300, (400,400))
                else:
                    if v.puzzle9 != True:
                        if v.diary_view == 1:
                            v.bg = c.Background('lauradiary_lockclose')

                            v.b1 = c.Hitbox(70, 35, (558, 360))
                            v.b2 = c.Hitbox(70, 35, (558, 405))
                            v.b3 = c.Hitbox(70, 35, (558, 450))
                            v.b4 = c.Hitbox(70, 35, (558, 495))
                        else:
                            v.bg = c.Background('laurabox_open')
                            v.laura_diary_locked = c.Button('lauradiary_lock', (400,400))
                    else:
                        v.bg = c.Background('laurabox_open')

                v.close_button = c.Button('x_out', (750,50))

            elif v.enlarge == 'rug':
                v.bg = c.Background('under_rug')

                v.close_button = c.Button('x_out', (750,50))

            else:
                v.bg = c.Background('attic')

                v.box1 = c.Hitbox(100, 85, (220,480))
                v.table = c.Hitbox(170, 225, (400,400))
                v.box2 = c.Hitbox(100, 85, (585,465))
                v.rug = c.Hitbox(100, 60, (750,540))

                v.a_down = c.Arrow((400,620), -90)
