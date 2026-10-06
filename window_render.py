import _variables as v
import _classes as c
import leaderboard as l
import feedback as f


def render_window():
    v.bg.update()

    if v.window == 'title':
        v.leaderboard1.update()
        v.leaderboard2.update()
        v.leaderboard3.update()
        if v.start.update():
            v.sfx['button_click'].play()
            if not v.fading:
                v.fader = c.wFader('intro1', 2, 5)
                v.fading = True
        if v.quit.update():
            v.sfx['button_click'].play()
            if not v.fading:
                v.fader = c.wFader('quit', 2, 0)
                if v.intro_music is None: v.sound['bg_intro'].fadeout(2000)
                else: v.intro_music.fadeout(2000)
                v.fading = True

    elif v.window == 'intro1':
        v.window_delay -= 1/60
        if v.window_delay <= 0:
            if not v.fading:
                v.fader = c.wFader('intro2', 5, 5)
                v.fading = True

    elif v.window == 'intro2':
        v.window_delay -= 1/60
        if v.window_delay <= 0:
            if not v.fading:
                v.fader = c.wFader('intro3', 5, 5)
                v.fading = True
    
    elif v.window == 'intro3':
        v.window_delay -= 1/60
        if v.window_delay <= 0:
            if not v.fading:
                v.fader = c.wFader('intro4', 5, 5)
                v.sound['bg_intro'].fadeout(5000)
                v.fading = True

    elif v.window == 'intro4':
        v.screen.blit(v.black, v.black_rect)

        v.window_delay -= 1/60
        v.phone.update()

        if v.window_delay <= 24 and v.window_delay > 4:
            v.phone = c.Background('phone_blank')
        elif v.window_delay <= 4:
            v.phone = c.Background('phone_low')
            if v.phone_dead is not True:
                v.sfx['battery_low'].play()
                v.phone_dead = True

        if v.window_delay <= 8:
            if v.door_closed is not True:
                v.sfx['close_door'].play()
                v.door_closed = True
        
        if v.window_delay <= 24 and v.window_delay > 10:
            v.text1.update()
            if v.t1 is not True:
                v.sfx['text_message'].play()
                v.t1 = True
            
        if v.window_delay <= 21 and v.window_delay > 10:
            v.text2.update()
            if v.t2 is not True:
                v.sfx['text_message'].play()
                v.t2 = True
        if v.window_delay <= 18 and v.window_delay > 10:
            v.text3.update()
            if v.t3 is not True:
                v.sfx['text_message'].play()
                v.t3 = True
        if v.window_delay <= 15 and v.window_delay > 10:
            v.text4.update()
            if v.t4 is not True:
                v.sfx['text_message'].play()
                v.t4 = True
        if v.window_delay <= 10 and v.window_delay > 4:
            v.text5.update()
            if v.t5 is not True:
                v.sfx['text_message'].play()
                v.t5 = True
        if v.window_delay <= 6 and v.window_delay > 4:
            v.text6.update()
            if v.t6 is not True:
                v.sfx['text_message'].play()
                v.t6 = True

        if v.window_delay <= 0:
            if not v.fading:
                v.sfx['scary_swoosh'].play()
                v.fader = c.Fader(1, 'entrance')
                v.fading = True

    if v.window == 'escaped':

        if v.text != None:
            if v.text.update():
                if v.dialogue_count == 1:
                    v.text = c.Slowtype(v.screen, 'You made me go in the first place!', 30, 3, 'fonts/open-sans-bold.ttf', 30, (100,100,255), (50,100), 700)
                    v.dialogue_count = 2
                elif v.dialogue_count == 2:
                    v.text = c.Slowtype(v.screen, "Sorry! I didn't mean to let you go in alone... Let's never do something like this ever again.", 30, 3, 'fonts/open-sans-bold.ttf', 30, (255,0,0), (50,50), 700)
                    v.dialogue_count = 3
                elif v.dialogue_count == 3:
                    v.text = c.Slowtype(v.screen, "I'm fine with that. But if we do anything even remotely dangerous, you're going first this time.", 30, 3, 'fonts/open-sans-bold.ttf', 30, (100,100,255), (50,100), 700)
                    v.dialogue_count = 4
                elif v.dialogue_count == 4:
                    v.sound['bg_game'].fadeout(1000)
                    v.fader = c.wFader('username', 2, 5)

    elif v.window == 'arrested':
        v.window_delay -= 1/60
        if v.window_delay <= 0 and v.dialogue_count == 0:
            v.text = c.Slowtype(v.screen, "Police! Police! We know you're in there! Open up!", 30, 3, 'fonts/open-sans-bold.ttf', 30, (255,0,255), (50,100), 700)
            v.dialogue_count = 1
        if v.text != None:
            if v.text.update():
                if v.dialogue_count == 1:
                    v.text = c.Slowtype(v.screen, "I can't even open the door!", 30, 2, 'fonts/open-sans-bold.ttf', 30, (100,100,255), (50,50), 700)
                    v.dialogue_count = 2
                elif v.dialogue_count == 2:
                    v.text = c.Slowtype(v.screen, "Don't make things harder for yourself. You're under arrest for breaking and entering. Both of you, come out with your hands up!", 30, 3, 'fonts/open-sans-bold.ttf', 30, (255,0,255), (50,100), 700)
                    v.dialogue_count = 3
                elif v.dialogue_count == 3:
                    v.text = c.Slowtype(v.screen, "What?! But we called the police in the first place! I'm trapped inside!", 30, 2, 'fonts/open-sans-bold.ttf', 30, (100,100,255), (50,50), 700)
                    v.dialogue_count = 4
                elif v.dialogue_count == 4:
                    v.text = c.Slowtype(v.screen, "We'll get to the bottom of this. This property is protected by the Screamville police, and nobody is allowed to enter. But considering the circumstances, you two may receive a lighter sentence.", 25, 4, 'fonts/open-sans-bold.ttf', 30, (255,0,255), (50,100), 700)
                    v.dialogue_count = 5
                elif v.dialogue_count == 5:
                    v.text = c.Slowtype(v.screen, "Well, this is one way to escape. Not great, but at least I won't be here for much longer. I didn't even find out what happened in the house. Guess I'm a criminal now...", 30, 3, 'fonts/open-sans-bold.ttf', 30, (100,100,255), (50,50), 700)
                    v.dialogue_count = 6
                elif v.dialogue_count == 6:
                    v.sound['bg_game'].fadeout(1000)
                    v.fader = c.wFader('username', 2, 5)

    elif v.window == 'username':
        v.keypad.update()
        if v.escaped is True:
            v.display_text(v.screen, 'You Escaped!', 'fonts/fofbb_reg.ttf', 100, (255,100,100), 'middle', (400,75))
            v.display_text(v.screen, f'Remaining Time: {v.display_time}', 'fonts/open-sans-bold.ttf', 50, (0,0,0), 'middle', (400,690))
        else:
            v.display_text(v.screen, 'Game Over!', 'fonts/fofbb_reg.ttf', 100, (255,100,100), 'middle', (400,75))
        v.display_text(v.screen, 'What is your name?', 'fonts/fofbb_reg.ttf', 50, (255,255,255), 'middle', (400,160))
        v.b_time -= 1/60
        if v.b_time < 0: v.b_time = 0
        if v.b1.update(): v.update_username(1)
        if v.b2.update(): v.update_username(2)
        if v.b3.update(): v.update_username(3)
        if v.b4.update(): v.update_username(4)
        if v.b5.update(): v.update_username(5)
        if v.b6.update(): v.update_username(6)
        if v.b7.update(): v.update_username(7)
        if v.b8.update(): v.update_username(8)
        if v.b9.update(): v.update_username(9)
        if v.b_clear.update(): v.update_username('clear')
        if v.b0.update(): v.update_username(0)
        if v.b_enter.update(): v.update_username('enter')
        v.display_text(v.screen, v.username, 'fonts/digital-7.ttf', 30, (0,200,0), 'left', (322,249))
        if v.username_submit is True:
            if not v.fading:
                if v.escaped is True: v.fader = c.wFader('credits1', 2, 3)
                else: v.fader = c.wFader('survey1', 1, 3)
                v.fading = True
                l.update_data()
    
    elif v.window == 'credits1':
        v.window_delay -= 1/60
        if v.window_delay < 0:
            if not v.fading:
                v.fader = c.wFader('credits2', 3, 3)
                v.fading = True
    
    elif v.window == 'credits2':
        if len(v.credits_list) > 0:
            v.credits_delay -= 1/60
            if v.credits_delay <= 0:
                v.credits_group.add(v.credits_list[0])
                v.credits_list.remove(v.credits_list[0])
                v.credits_delay = 2
        v.credits_group.update()
        if v.num_credits <= 0: v.window_delay -= 1/60
        if v.window_delay < 0:
            if not v.fading:
                v.fader = c.wFader('survey1', 1, 3)
                v.fading = True

    elif v.window == 'survey1':
        v.display_text(v.screen, 'Take Our Survey!', 'fonts/fofbb_reg.ttf', 75, (0,200,0), 'middle', (400,125))
        v.survey.update()
        if v.b1.update():
            v.sfx['button_click'].play()
            v.circle = c.Image('survey_fill', v.b1.rect.center)
            v.select = 1
        if v.b2.update():
            v.sfx['button_click'].play()
            v.circle = c.Image('survey_fill', v.b2.rect.center)
            v.select = 2
        if v.b3.update():
            v.sfx['button_click'].play()
            v.circle = c.Image('survey_fill', v.b3.rect.center)
            v.select = 3
        if v.b4.update():
            v.sfx['button_click'].play()
            v.circle = c.Image('survey_fill', v.b4.rect.center)
            v.select = 4
        if v.b5.update():
            v.sfx['button_click'].play()
            v.circle = c.Image('survey_fill', v.b5.rect.center)
            v.select = 5
        if v.circle != None:
            v.circle.update()
        if v.submit.update():
            v.sfx['button_click'].play()
            if v.select != 0 and not v.fading:
                v.survey1 = v.select
                v.fader = c.wFader('survey2', 5, 4)
    
    elif v.window == 'survey2':
        v.display_text(v.screen, 'Take Our Survey!', 'fonts/fofbb_reg.ttf', 75, (0,200,0), 'middle', (400,125))
        v.survey.update()
        if v.b1.update():
            v.sfx['button_click'].play()
            v.circle = c.Image('survey_fill', v.b1.rect.center)
            v.select = 1
        if v.b2.update():
            v.sfx['button_click'].play()
            v.circle = c.Image('survey_fill', v.b2.rect.center)
            v.select = 2
        if v.b3.update():
            v.sfx['button_click'].play()
            v.circle = c.Image('survey_fill', v.b3.rect.center)
            v.select = 3
        if v.b4.update():
            v.sfx['button_click'].play()
            v.circle = c.Image('survey_fill', v.b4.rect.center)
            v.select = 4
        if v.b5.update():
            v.sfx['button_click'].play()
            v.circle = c.Image('survey_fill', v.b5.rect.center)
            v.select = 5
        if v.circle != None:
            v.circle.update()
        if v.submit.update():
            v.sfx['button_click'].play()
            if v.select != 0 and not v.fading:
                v.survey2 = v.select
                v.fader = c.wFader('survey3', 5, 4)

    elif v.window == 'survey3':
        v.display_text(v.screen, 'Take Our Survey!', 'fonts/fofbb_reg.ttf', 75, (0,200,0), 'middle', (400,125))
        v.survey.update()
        if v.b1.update():
            v.sfx['button_click'].play()
            v.circle = c.Image('survey_fill', v.b1.rect.center)
            v.select = 1
        if v.b2.update():
            v.sfx['button_click'].play()
            v.circle = c.Image('survey_fill', v.b2.rect.center)
            v.select = 2
        if v.b3.update():
            v.sfx['button_click'].play()
            v.circle = c.Image('survey_fill', v.b3.rect.center)
            v.select = 3
        if v.b4.update():
            v.sfx['button_click'].play()
            v.circle = c.Image('survey_fill', v.b4.rect.center)
            v.select = 4
        if v.b5.update():
            v.sfx['button_click'].play()
            v.circle = c.Image('survey_fill', v.b5.rect.center)
            v.select = 5
        if v.circle != None:
            v.circle.update()
        if v.submit.update():
            v.sfx['button_click'].play()
            if v.select != 0 and not v.fading:
                v.survey3 = v.select
                v.fader = c.wFader('survey4', 5, 4)

    elif v.window == 'survey4':
        v.display_text(v.screen, 'Take Our Survey!', 'fonts/fofbb_reg.ttf', 75, (0,200,0), 'middle', (400,125))
        v.survey.update()
        if v.b1.update():
            v.sfx['button_click'].play()
            v.circle = c.Image('survey_fill', v.b1.rect.center)
            v.select = 1
        if v.b2.update():
            v.sfx['button_click'].play()
            v.circle = c.Image('survey_fill', v.b2.rect.center)
            v.select = 2
        if v.b3.update():
            v.sfx['button_click'].play()
            v.circle = c.Image('survey_fill', v.b3.rect.center)
            v.select = 3
        if v.b4.update():
            v.sfx['button_click'].play()
            v.circle = c.Image('survey_fill', v.b4.rect.center)
            v.select = 4
        if v.b5.update():
            v.sfx['button_click'].play()
            v.circle = c.Image('survey_fill', v.b5.rect.center)
            v.select = 5
        if v.circle != None:
            v.circle.update()
        if v.submit.update():
            v.sfx['button_click'].play()
            if v.select != 0 and not v.fading:
                v.survey4 = v.select
                v.fader = c.wFader('survey5', 5, 4)

    elif v.window == 'survey5':
        v.display_text(v.screen, 'Take Our Survey!', 'fonts/fofbb_reg.ttf', 75, (0,200,0), 'middle', (400,125))
        v.survey.update()
        if v.b1.update():
            v.sfx['button_click'].play()
            v.circle = c.Image('survey_fill', v.b1.rect.center)
            v.select = 1
        if v.b2.update():
            v.sfx['button_click'].play()
            v.circle = c.Image('survey_fill', v.b2.rect.center)
            v.select = 2
        if v.b3.update():
            v.sfx['button_click'].play()
            v.circle = c.Image('survey_fill', v.b3.rect.center)
            v.select = 3
        if v.b4.update():
            v.sfx['button_click'].play()
            v.circle = c.Image('survey_fill', v.b4.rect.center)
            v.select = 4
        if v.b5.update():
            v.sfx['button_click'].play()
            v.circle = c.Image('survey_fill', v.b5.rect.center)
            v.select = 5
        if v.circle != None:
            v.circle.update()
        if v.submit.update():
            if v.select != 0 and not v.fading:
                v.survey5 = v.select
                v.fader = c.wFader('survey6', 5, 4)
            v.sfx['button_click'].play()

    elif v.window == 'survey6':
        v.display_text(v.screen, 'Take Our Survey!', 'fonts/fofbb_reg.ttf', 75, (0,200,0), 'middle', (400,125))
        v.survey.update()
        if v.b1.update():
            v.sfx['button_click'].play()
            v.circle = c.Image('survey_fill', v.b1.rect.center)
            v.select = 1
        if v.b2.update():
            v.sfx['button_click'].play()
            v.circle = c.Image('survey_fill', v.b2.rect.center)
            v.select = 2
        if v.b3.update():
            v.sfx['button_click'].play()
            v.circle = c.Image('survey_fill', v.b3.rect.center)
            v.select = 3
        if v.b4.update():
            v.sfx['button_click'].play()
            v.circle = c.Image('survey_fill', v.b4.rect.center)
            v.select = 4
        if v.b5.update():
            v.sfx['button_click'].play()
            v.circle = c.Image('survey_fill', v.b5.rect.center)
            v.select = 5
        if v.circle != None:
            v.circle.update()
        if v.submit.update():
            v.sfx['button_click'].play()
            if v.select != 0 and not v.fading:
                v.survey6 = v.select
                v.fader = c.wFader('title', 1, 3)
                f.update_data()
                v.sound['bg_intro'].fadeout(3000)
                v.fading = True