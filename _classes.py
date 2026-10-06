import pygame as pg
import _variables as v

from room_init import init_room
from window_init import init_window

# Sprites
class Background:
    def __init__(self, image: str):
        self.image = v.img[image]
        self.rect = self.image.get_rect(center=(400,400))
        self.scale = 1
    
    def update(self):
        v.screen.blit(self.image, self.rect)

class Image:
    def __init__(self, image: str, pos: tuple=(0,0)):
        self.image = v.img[image]
        self.rect = self.image.get_rect(center=pos)
        self.scale = 1

    def update(self):
        v.screen.blit(self.image, self.rect)

class Mask:
    def __init__(self):
        self.surf = pg.Surface((800,800))
        self.surf.fill((0,0,0))
        self.alpha = 225
        self.scale = 1
    
    def update(self):
        self.surf.set_alpha(self.alpha)
        v.screen.blit(self.surf, (0,0))

        if v.lights: self.stage = 0
        else: self.stage = 1

        if self.stage == 0:
            self.alpha -= 20
            if self.alpha < 0: self.alpha = 0
        
        elif self.stage == 1:
            self.alpha += 25
            if self.alpha > 225: self.alpha = 225

class Fader(pg.sprite.Sprite):
    def __init__(self, floor: int, room: int):
        super().__init__()
        self.surf = pg.Surface((800,800))
        self.surf.fill((0,0,0))
        
        self.floor = floor
        self.room = room
        self.stage = 0
        self.alpha = 0
        v.sfx['whoosh'].play()
    
    def update(self):
        self.surf.set_alpha(self.alpha)
        v.screen.blit(self.surf, (0,0))

        v.interact = False
        if self.stage == 0:
            self.alpha += 10
            if self.alpha > 255:
                init_room(self.floor, self.room)
                self.stage = 1
                self.alpha = 255

        elif self.stage == 1:
            self.alpha -= 10
            if self.alpha < 0:
                v.interact = True
                self.kill()

class Hitbox:
    def __init__(self, width: int, height: int, center: tuple=(0,0)):
        self.width = width
        self.height = height
        self.surf = pg.Surface((width,height))
        self.surf.fill((255,100,100))
        self.surf.set_alpha(200)
        self.rect = pg.Rect(0, 0, width, height)
        self.rect.center = center
        self.clicked = 0
        self.scale = 1

    def update(self):
        #v.screen.blit(self.surf, self.rect) # Hitbox Vision
        for event in v.events:
            if event.type == pg.MOUSEBUTTONDOWN and v.interact and v.display == None:
                if self.clicked == 0 and self.rect.collidepoint(v.mouse_pos):
                    self.clicked = 1
            elif event.type == pg.MOUSEBUTTONUP and v.interact and v.display == None:
                if self.clicked == 1 and self.rect.collidepoint(v.mouse_pos):
                    return True
                self.clicked = 0
        return False

class Hoverbox:
    def __init__(self, width: int, height: int, center: tuple=(0,0)):
        self.width = width
        self.height = height
        self.surf = pg.Surface((width,height))
        self.surf.fill((100,100,255))
        self.surf.set_alpha(200)
        self.rect = pg.Rect(0, 0, width, height)
        self.rect.center = center
        self.clicked = 0
        self.scale = 1

    def update(self):
        #v.screen.blit(self.surf, self.rect) # Hitbox Vision
        for event in v.events:
            if event.type == pg.MOUSEBUTTONUP and self.rect.collidepoint(v.mouse_pos): return True
        return False

class Arrow:
    def __init__(self, center: tuple=(0,0), angle: int=360):
        self.image = v.img['arrow']
        self.image = pg.transform.rotozoom(self.image, angle, 1)
        self.center = center
        self.rect = self.image.get_rect(center = self.center)
        self.clicked = 0
        self.scale = 1

    def update(self):
        v.screen.blit(self.image, self.rect)
        for event in v.events:
            if event.type == pg.MOUSEBUTTONDOWN and v.interact and v.display == None:
                if self.clicked == 0 and self.rect.collidepoint(v.mouse_pos):
                    self.clicked = 1
            elif event.type == pg.MOUSEBUTTONUP and v.interact:
                if self.clicked == 1 and self.rect.collidepoint(v.mouse_pos):
                    return True
                self.clicked = 0
        return False

class InvArrow:
    def __init__(self, type='left'):
        self.type = type
        if self.type == 'left':
            self.image = v.img['inventory_left']
            self.rect = self.image.get_rect(center = (100,750))
        elif self.type == 'right':
            self.image = v.img['inventory_right']
            self.rect = self.image.get_rect(center = (700,750))
        self.clicked = 0
    
    def update(self):
        v.screen.blit(self.image, self.rect)
        if len(v.inventory) > 5:
            for event in v.events:
                if event.type == pg.MOUSEBUTTONDOWN and v.interact and v.display == None:
                    if self.clicked == 0 and self.rect.collidepoint(v.mouse_pos):
                        self.clicked = 1
                elif event.type == pg.MOUSEBUTTONUP and v.interact and v.display == None:
                    if self.clicked == 1 and self.rect.collidepoint(v.mouse_pos):
                        return True
                    self.clicked = 0
                return False

class Button:
    def __init__(self, image: str, center: tuple=(0,0)):
        super().__init__()
        self.image = v.img[image]
        self.center = center
        self.rect = self.image.get_rect(center = self.center)
        self.clicked = 0
        self.scale = 1

    def update(self):
        v.screen.blit(self.image, self.rect)
        for event in v.events:
            if event.type == pg.MOUSEBUTTONDOWN and v.interact and v.display == None:
                if self.clicked == 0 and self.rect.collidepoint(v.mouse_pos):
                    self.clicked = 1
            elif event.type == pg.MOUSEBUTTONUP and v.interact and v.display == None:
                if self.clicked == 1 and self.rect.collidepoint(v.mouse_pos):
                    return True
                self.clicked = 0
        return False

class Switch:
    def __init__(self):
        self.frames = [v.img['breaker_off'], v.img['breaker_on']]
        self.index = 0
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect(center = (400,313))
        self.clicked = 0
    
    def update(self):
        self.image = self.frames[self.index]
        v.screen.blit(self.image, self.rect)
        for event in v.events:
            if event.type == pg.MOUSEBUTTONDOWN and v.interact and v.display == None:
                if self.clicked == 0 and self.rect.collidepoint(v.mouse_pos):
                    self.clicked = 1
            elif event.type == pg.MOUSEBUTTONUP and v.interact and v.display == None:
                if self.clicked == 1 and self.rect.collidepoint(v.mouse_pos):
                    if not v.lights:
                        self.index = 1
                        v.lights = True
                        v.sfx['electricity'].play()
                        v.sfx['tv_static'].play()
                    else:
                        self.index = 0
                        v.lights = False
                    v.sfx['flip_switch'].play()
                self.clicked = 0
        return None

class TV:
    def __init__(self):
        self.frames = [v.img['ad2'], v.img['ad3'], v.img['ad4'], v.img['ad1']]
        self.audio = [v.sound['ad2'], v.sound['ad3'], v.sound['ad4'], v.sound['ad1']]
        self.index = 0
        self.index2 = 0
        self.image = self.frames[0]
        self.rect = self.image.get_rect(center = (365,400))
    
    def update(self):
        self.index += 0.2/60
        if int(self.index) >= len(self.frames):
            self.index = 0
            self.index2 = 0
        if self.index > self.index2:
            self.index2 += 1
            self.audio[self.index2 - 1].play()
            return True
        self.image = self.frames[int(self.index)]
        v.screen.blit(self.image, self.rect)
        return False

class Flicker:
    def __init__(self):
        self.pattern = [
            1,1,1,0,1,0,1,1,1,
            0,0,0,
            1,0,1,
            0,0,0,
            1,1,1,0,1,
            0,0,0,
            1,1,1,0,1,0,1,
            0,0,0,0,0,0,0
        ]
        self.index = -4/60
        self.index2 = -1
        self.image = v.img['dark_filter']
        self.rect = self.image.get_rect(center = (400,400))
    
    def update(self):
        self.index += 4/60
        if self.index >= len(self.pattern):
            self.index = 0
            self.index2 = -1
        if self.pattern[int(self.index)] == 0:
            v.screen.blit(self.image, self.rect)
            return True
        else:
            if int(self.index) > self.index2:
                v.sfx['electric_buzz'].play()
                self.index2 += 1
        return False

class UsedItem(pg.sprite.Sprite):
    def __init__(self, reg_path: str, inv_path: str, show_path: str):
        super().__init__()
        self.reg_img = v.img[reg_path]
        self.reg_rect = self.reg_img.get_rect(topleft = (0,0))
        self.inv_img = v.img[inv_path]
        self.inv_rect = self.inv_img.get_rect(topleft = (0,0))
        self.show_img = v.img[show_path]
        self.show_rect = self.show_img.get_rect(topleft = (0,0))
        self.clicked = 0
        self.status = ''
    
    def update(self, center: tuple=(0,0)):
        if self in v.inventory and self.status == 'stored':
            self.inv_rect.center = center
            v.screen.blit(self.inv_img, self.inv_rect)

            for event in v.events:
                if event.type == pg.MOUSEBUTTONDOWN and v.interact and v.display == None:
                    if self.clicked == 0 and self.inv_rect.collidepoint(v.mouse_pos):
                        self.clicked = 1
                elif event.type == pg.MOUSEBUTTONUP and v.interact and v.display == None:
                    if self.clicked == 1 and self.inv_rect.collidepoint(v.mouse_pos):
                        self.status = 'shown'
                    self.clicked = 0
        
        elif self in v.inventory and self.status == 'shown':
            self.show_rect.center = (400,400)
            v.screen.blit(self.show_img, self.show_rect)

            v.interact = False
            v.display = self

            for event in v.events:
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.clicked == 0 and not self.show_rect.collidepoint(v.mouse_pos):
                        self.clicked = 1
                elif event.type == pg.MOUSEBUTTONUP:
                    if self.clicked == 1 and not self.show_rect.collidepoint(v.mouse_pos):
                        self.status = 'stored'
                        v.interact = True
                        v.display = None
                    self.clicked = 0
        
        else:
            self.reg_rect.center = center
            v.screen.blit(self.reg_img, self.reg_rect)

            for event in v.events:
                if event.type == pg.MOUSEBUTTONDOWN and v.interact and v.display == None:
                    if self.clicked == 0 and self.reg_rect.collidepoint(v.mouse_pos):
                        self.clicked = 1
                elif event.type == pg.MOUSEBUTTONUP and v.interact and v.display == None:
                    if self.clicked == 1 and self.reg_rect.collidepoint(v.mouse_pos):
                        self.status = 'stored'
                        return True
                    self.clicked = 0
            return False

class PlacedItem(pg.sprite.Sprite):
    def __init__(self, reg_path: str, inv_path: str):
        super().__init__()
        self.reg_img = v.img[reg_path]
        self.reg_rect = self.reg_img.get_rect(topleft = (0,0))
        self.inv_img = v.img[inv_path]
        self.inv_rect = self.inv_img.get_rect(topleft = (0,0))
        self.clicked = 0
        self.status = ''
    
    def update(self, center: tuple=(0,0)):
        if self in v.inventory:
            if self.status == 'stored':
                self.inv_rect.center = center
                v.screen.blit(self.inv_img, self.inv_rect)

                if v.mouse_pressed[0] and self.inv_rect.collidepoint(v.mouse_pos) and v.interact and v.display == None:
                    self.status = 'dragged'
                    v.display = self

            elif self.status == 'dragged':
                self.reg_rect.center = v.mouse_pos
                if v.mouse_pressed[0]:
                    v.screen.blit(self.reg_img, self.reg_rect)
                else:
                    self.status = 'stored'
                    v.display = None
            
        else:
            self.reg_rect.center = center
            v.screen.blit(self.reg_img, self.reg_rect)

            for event in v.events:
                if event.type == pg.MOUSEBUTTONDOWN and v.interact and v.display == None:
                    if self.clicked == 0 and self.reg_rect.collidepoint(v.mouse_pos):
                        self.clicked = 1
                elif event.type == pg.MOUSEBUTTONUP and v.interact and v.display == None:
                    if self.clicked == 1 and self.reg_rect.collidepoint(v.mouse_pos):
                        self.status = 'stored'
                        return True
                    self.clicked = 0
            return False

class DraggedItem(pg.sprite.Sprite):
    def __init__(self, reg_path: str, inv_path: str):
        super().__init__()
        self.reg_img = v.img[reg_path]
        self.reg_rect = self.reg_img.get_rect(topleft = (0,0))
        self.inv_img = v.img[inv_path]
        self.inv_rect = self.inv_img.get_rect(topleft = (0,0))
        self.clicked = 0
        self.status = ''
    
    def update(self, center: tuple=(0,0)):
        if self in v.inventory:
            if self.status == 'stored':
                self.inv_rect.center = center
                v.screen.blit(self.inv_img, self.inv_rect)

                if v.mouse_pressed[0] and self.inv_rect.collidepoint(v.mouse_pos) and v.interact and v.display == None:
                    self.status = 'dragged'
                    v.display = self

            elif self.status == 'dragged':
                self.reg_rect.center = v.mouse_pos
                if v.mouse_pressed[0]:
                    v.screen.blit(self.reg_img, self.reg_rect)
                else:
                    self.status = 'stored'
                    v.display = None
            
        else:
            self.reg_rect.center = center
            v.screen.blit(self.reg_img, self.reg_rect)

            for event in v.events:
                if event.type == pg.MOUSEBUTTONDOWN and v.interact and v.display == None:
                    if self.clicked == 0 and self.reg_rect.collidepoint(v.mouse_pos):
                        self.clicked = 1
                elif event.type == pg.MOUSEBUTTONUP and v.interact and v.display == None:
                    if self.clicked == 1 and self.reg_rect.collidepoint(v.mouse_pos):
                        self.status = 'stored'
                        return True
                    self.clicked = 0
            return False

class PlaceUseItem(pg.sprite.Sprite):
    def __init__(self, place_path: str, inv_path: str, show_path: str, drag_path: str, insert_path: str):
        super().__init__()
        self.place_img = v.img[place_path]
        self.insert_img = v.img[insert_path]
        self.reg_rect = self.place_img.get_rect(topleft = (0,0))
        self.inv_img = v.img[inv_path]
        self.inv_rect = self.inv_img.get_rect(topleft = (0,0))
        self.show_img = v.img[show_path]
        self.show_rect = self.show_img.get_rect(topleft = (0,0))
        self.drag_img = v.img[drag_path]
        self.drag_rect = self.drag_img.get_rect(topleft = (0,0))
        self.clicked = 0
        self.status = 'placed'
    
    def update(self, center: tuple=(0,0)):
        if self in v.inventory:
            if self.status == 'stored':
                self.inv_rect.center = center
                v.screen.blit(self.inv_img, self.inv_rect)

                for event in v.events:
                    if event.type == pg.MOUSEBUTTONDOWN and v.interact and v.display == None:
                        if self.clicked == 0 and self.inv_rect.collidepoint(v.mouse_pos):
                            self.clicked = 1
                    elif event.type == pg.MOUSEBUTTONUP and v.interact and v.display == None:
                        if self.clicked == 1 and self.inv_rect.collidepoint(v.mouse_pos):
                            self.status = 'shown'
                        self.clicked = 0
                    elif event.type == pg.MOUSEMOTION:
                        if self.clicked == 1:
                            self.status = 'dragged'
                            v.display = self

        
            elif self.status == 'shown':
                self.show_rect.center = (400,400)
                v.screen.blit(self.show_img, self.show_rect)
                v.interact = False
                v.display = self

                for event in v.events:
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if self.clicked == 0 and not self.show_rect.collidepoint(v.mouse_pos):
                            self.clicked = 1
                    elif event.type == pg.MOUSEBUTTONUP:
                        if self.clicked == 1 and not self.show_rect.collidepoint(v.mouse_pos):
                            self.status = 'stored'
                            v.interact = True
                            v.display = None
                        self.clicked = 0
            
            elif self.status == 'dragged':
                self.drag_rect.center = v.mouse_pos
                if v.mouse_pressed[0]:
                    v.screen.blit(self.drag_img, self.drag_rect)
                else:
                    self.status = 'stored'
                    self.clicked = 0
                    v.display = None
            
        else:
            if self.status == 'placed':
                self.reg_rect = self.place_img.get_rect(center = center)
                v.screen.blit(self.place_img, self.reg_rect)
            elif self.status == 'inserted':
                self.reg_rect = self.insert_img.get_rect(center = center)
                v.screen.blit(self.insert_img, self.reg_rect)

            for event in v.events:
                if event.type == pg.MOUSEBUTTONDOWN and v.interact and v.display == None:
                    if self.clicked == 0 and self.reg_rect.collidepoint(v.mouse_pos):
                        self.clicked = 1
                elif event.type == pg.MOUSEBUTTONUP and v.interact and v.display == None:
                    if self.clicked == 1 and self.reg_rect.collidepoint(v.mouse_pos):
                        self.status = 'stored'
                        return True
                    self.clicked = 0
            return False

class Slowtype(pg.sprite.Sprite):
    def __init__(self, screen, text: str, lps: int, linger: int, font_path: str, size: int, color: tuple=(0,0,0), pos: tuple=(0,0), maxwidth: int=700):
        super().__init__()
        self.screen = screen
        self.text = text
        self.font_path = font_path
        self.size = size
        self.color = color
        self.pos = pos
        self.maxwidth = maxwidth

        self.index = -lps/60
        self.index2 = -1
        self.string = ''
        self.lps = lps
        self.linger = linger
        self.triggered = False
    
    def update(self):
        self.index += self.lps/60
        if int(self.index) > self.index2 and self.index2 < len(self.text) - 1:
            self.index2 += 1
            self.string += (self.text[self.index2])
            v.sfx['text_blip'].play()
        if self.index > len(self.text) - 1:
            self.index = len(self.text) - 1
            self.index2 = len(self.text) - 1
            self.linger -= 1/60
        if self.linger > 0:
            v.newline_text(self.screen, self.string, self.font_path, self.size, self.color, self.pos, self.maxwidth)
        else:
            self.kill()
            if not self.triggered:
                self.triggered = True
                return True
        return False

class wFader(pg.sprite.Sprite):
    def __init__(self, window: pg.Surface, fadeout: int, fadein: int):
        super().__init__()
        self.surf = pg.Surface((800,800))
        self.surf.fill((0,0,0))
        
        self.window = window
        self.fadeout = fadeout
        self.fadein = fadein
        self.stage = 0
        self.alpha = 0
    
    def update(self):
        self.surf.set_alpha(self.alpha)
        v.screen.blit(self.surf, (0,0))

        v.interact = False
        if self.stage == 0:
            self.alpha += self.fadeout
            if self.alpha > 255:
                init_window(self.window)
                self.stage = 1
                self.alpha = 255

        elif self.stage == 1:
            self.alpha -= self.fadein
            if self.alpha < 0:
                v.interact = True
                self.kill()

class Credits(pg.sprite.Sprite):
    def __init__(self, title: str, name: str, font: pg.font.Font):
        super().__init__()
        self.text1 = title
        self.text2 = name
        self.font = font
        self.size1 = 75
        self.size2 = 50
        self.color1 = (100,0,0)
        self.color2 = (150,100,100)
        self.x = 400
        self.y = 900
    
    def update(self):
        self.y -= 2
        v.display_text(v.screen, self.text1, self.font, self.size1, self.color1, 'middle', (self.x, self.y))
        v.display_text(v.screen, self.text2, self.font, self.size2, self.color2, 'middle', (self.x, self.y + 75))
        if self.y < -100:
            v.num_credits -= 1
            self.kill()

class LeaderboardColumn(pg.sprite.Sprite):
    def __init__(self, header: str, list: list, font: pg.font.Font, centerx: int):
        super().__init__()
        self.text1 = header
        self.text2 = list
        self.font = font
        self.size1 = 30
        self.size2 = 20
        self.color1 = (100,0,0)
        self.color2 = (150,100,100)
        self.x = centerx
        self.y = 25
    
    def update(self):
        v.display_text(v.screen, self.text1, self.font, self.size1, self.color1, 'middle', (self.x, self.y))
        for i in range(len(self.text2)):
            v.display_text(v.screen, self.text2[i], self.font, self.size2, self.color2, 'middle', (self.x, self.y + 10 + 30*(i+1)))
