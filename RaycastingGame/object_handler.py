from sprite_object import *


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.anim_sprite_path = 'resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite
        
        #sprite map
        add_sprite(SpriteObject(game))
        add_sprite(AnimatedSprite(game))
        add_sprite(AnimatedSprite(game, pos=(1.5, 1.5)))
        add_sprite(AnimatedSprite(game, pos=(1.5, 7.5)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 6.5)))
        add_sprite(AnimatedSprite(game, pos=(2.5, 3.5)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 4.5)))
        add_sprite(AnimatedSprite(game, pos=(10.5, 6.5), path=self.anim_sprite_path + 'red_light/0.png'))
        add_sprite(AnimatedSprite(game, pos=(15.5, 2.5), path=self.anim_sprite_path + 'red_light/0.png'))
        add_sprite(AnimatedSprite(game, pos=(2.5, 8.5), path=self.anim_sprite_path + 'red_light/0.png'))
        add_sprite(AnimatedSprite(game, pos=(13.5, 0.5), path=self.anim_sprite_path + 'red_light/0.png'))
        
        
    def update(self):
        [sprite.update() for sprite in self.sprite_list]
        
    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)