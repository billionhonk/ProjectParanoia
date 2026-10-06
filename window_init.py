import pygame as pg
import _variables as v
import _classes as c
import leaderboard as l

from pygame import quit
from sys import exit


def init_window(towindow=''):
    v.fading = False
    v.window = towindow

    if v.window == 'quit': quit(), exit()

    elif v.window == 'title':
        v.lb_h1, v.lb_c1, v.lb_h2, v.lb_c2, v.lb_h3, v.lb_c3 = l.leaderboard_text()
        v.leaderboard1 = c.LeaderboardColumn(v.lb_h1, v.lb_c1, 'fonts/open-sans-bold.ttf', 200)
        v.leaderboard2 = c.LeaderboardColumn(v.lb_h2, v.lb_c2, 'fonts/open-sans-bold.ttf', 400)
        v.leaderboard3 = c.LeaderboardColumn(v.lb_h3, v.lb_c3, 'fonts/open-sans-bold.ttf', 600)
        v.bg = c.Background('intro2')

        v.start = c.Button('start', (400,600))
        v.quit = c.Button('quit', (400,700))
        v.sound['bg_intro'].play(loops = -1)
    
    elif v.window == 'intro1':
        v.bg = c.Background('house_ext')
        v.window_delay = 4
    
    elif v.window == 'intro2':
        v.bg = c.Background('house_close')
        v.window_delay = 4
    
    elif v.window == 'intro3':
        v.bg = c.Background('house_open')
        v.sfx['open_door'].play()
        v.window_delay = 5
    
    elif v.window == 'intro4':
        v.black = pg.surface.Surface((800,800))
        v.black_rect = v.black.get_rect(center = (400,400))
        v.phone = c.Background('phone_blank')
        v.door_closed = False
        v.phone_dead = False
        v.text1 = c.Image('text1_1', (430,325))
        v.t1 = False
        v.text2 = c.Image('text1_2', (370,375))
        v.t2 = False
        v.text3 = c.Image('text1_3', (435,425))
        v.t3 = False
        v.text4 = c.Image('text1_4', (365,475))
        v.t4 = False
        v.text5 = c.Image('text2_1', (430,325))
        v.t5 = False
        v.text6 = c.Image('text2_2', (430,375))
        v.t6 = False
        v.window_delay = 24

    elif v.window == 'escaped':
        v.bg = c.Background('escaped2')

        v.time_show = False
        v.text = c.Slowtype(v.screen, 'You made it out alive!', 30, 3, 'fonts/open-sans-bold.ttf', 30, (255,0,0), (50,50), 700)
        v.dialogue_count = 1

    elif v.window == 'arrested':
        v.bg = c.Background('lost')
        v.sfx['police_siren'].play()

        v.time_show = False
        v.window_delay = 3
        v.dialogue_count = 0

    elif v.window == 'username':
        v.bg = c.Background('escaped')
        v.sound['bg_intro'].play(loops = -1)

        v.keypad = c.Background('keypad')
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

        v.username_submit = False
    
    elif v.window == 'credits1':
        v.bg = c.Background('intro2')
        v.window_delay = 6
    
    elif v.window == 'credits2':
        v.bg = c.Background('outro2')
        v.credits_list = [
            c.Credits('Project Manager', 'Brianna (Scarlet) Ramirez', 'fonts/fofbb_reg.ttf'),
            c.Credits('Plot Designer', 'Rita Ma', 'fonts/fofbb_reg.ttf'),
            c.Credits('Puzzle Master', 'Jaiden Nwabuzor', 'fonts/fofbb_reg.ttf'),
            c.Credits('Media Manager', 'Mina Ree', 'fonts/fofbb_reg.ttf'),
            c.Credits('Chief Coder', 'William Hoang', 'fonts/fofbb_reg.ttf'),
            c.Credits('Interface Manager', 'Thomas Kim', 'fonts/fofbb_reg.ttf'),
            c.Credits('Data Analyst', 'Jerusha Samuel', 'fonts/fofbb_reg.ttf'),
            c.Credits('Support Manager', 'Veannie Aplaca', 'fonts/fofbb_reg.ttf'),
            c.Credits('The User - You!', 'Thank you for playing!', 'fonts/fofbb_reg.ttf')]
        v.num_credits = len(v.credits_list)
        v.credits_delay = 2
        v.window_delay = 3
    
    elif v.window == 'survey1':
        v.bg = c.Background('house_ext')
        v.survey = c.Background('survey_q1')
        v.b1 = c.Hitbox(30, 30, (267,410))
        v.b2 = c.Hitbox(30, 30, (335,410))
        v.b3 = c.Hitbox(30, 30, (400,410))
        v.b4 = c.Hitbox(30, 30, (468,410))
        v.b5 = c.Hitbox(30, 30, (535,410))
        v.circle = None
        v.survey1 = 0
        v.select = 0
        v.submit = c.Button('survey_submit', (400,700))
    
    elif v.window == 'survey2':
        v.bg = c.Background('house_ext')
        v.survey = c.Background('survey_q2')
        v.b1 = c.Hitbox(30, 30, (267,410))
        v.b2 = c.Hitbox(30, 30, (335,410))
        v.b3 = c.Hitbox(30, 30, (400,410))
        v.b4 = c.Hitbox(30, 30, (468,410))
        v.b5 = c.Hitbox(30, 30, (535,410))
        v.circle = None
        v.survey2 = 0
        v.select = 0
        v.submit = c.Button('survey_submit', (400,700))

    elif v.window == 'survey3':
        v.bg = c.Background('house_ext')
        v.survey = c.Background('survey_q3')
        v.b1 = c.Hitbox(30, 30, (267,410))
        v.b2 = c.Hitbox(30, 30, (335,410))
        v.b3 = c.Hitbox(30, 30, (400,410))
        v.b4 = c.Hitbox(30, 30, (468,410))
        v.b5 = c.Hitbox(30, 30, (535,410))
        v.circle = None
        v.survey3 = 0
        v.select = 0
        v.submit = c.Button('survey_submit', (400,700))

    elif v.window == 'survey4':
        v.bg = c.Background('house_ext')
        v.survey = c.Background('survey_q4')
        v.b1 = c.Hitbox(30, 30, (267,410))
        v.b2 = c.Hitbox(30, 30, (335,410))
        v.b3 = c.Hitbox(30, 30, (400,410))
        v.b4 = c.Hitbox(30, 30, (468,410))
        v.b5 = c.Hitbox(30, 30, (535,410))
        v.circle = None
        v.survey4 = 0
        v.select = 0
        v.submit = c.Button('survey_submit', (400,700))

    elif v.window == 'survey5':
        v.bg = c.Background('house_ext')
        v.survey = c.Background('survey_q5')
        v.b1 = c.Hitbox(30, 30, (267,410))
        v.b2 = c.Hitbox(30, 30, (335,410))
        v.b3 = c.Hitbox(30, 30, (400,410))
        v.b4 = c.Hitbox(30, 30, (468,410))
        v.b5 = c.Hitbox(30, 30, (535,410))
        v.circle = None
        v.survey5 = 0
        v.select = 0
        v.submit = c.Button('survey_submit', (400,700))

    elif v.window == 'survey6':
        v.bg = c.Background('house_ext')
        v.survey = c.Background('survey_q6')
        v.b1 = c.Hitbox(30, 30, (267,410))
        v.b2 = c.Hitbox(30, 30, (335,410))
        v.b3 = c.Hitbox(30, 30, (400,410))
        v.b4 = c.Hitbox(30, 30, (468,410))
        v.b5 = c.Hitbox(30, 30, (535,410))
        v.circle = None
        v.survey6 = 0
        v.select = 0
        v.submit = c.Button('survey_submit', (400,700))