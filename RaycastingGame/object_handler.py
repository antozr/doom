from sprite_object import *
from npc import *
from random import choices, randrange

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resources/sprites/npc/'
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.anim_sprite_path = 'resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}
        
        # spawn npc
        self.enemies = 20  # npc count
        self.npc_types = [SoldierNPC, CacoDemonNPC, CyberDemonNPC]
        self.weights = [70, 20, 10]
        self.restricted_area = {(i, j) for i in range(10) for j in range(10)}
        self.spawn_npc()

        # sprite map
        add_sprite(SpriteObject(game))
        add_sprite(AnimatedSprite(game))
        add_sprite(AnimatedSprite(game, pos=(1.5, 1.5)))
        add_sprite(AnimatedSprite(game, pos=(1.5, 7.5)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 6.5)))
        add_sprite(AnimatedSprite(game, pos=(2.5, 3.5)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 4.5)))
        add_sprite(AnimatedSprite(game, pos=(10.5, 6.5),
                   path=self.anim_sprite_path + 'red_light/0.png'))
        add_sprite(AnimatedSprite(game, pos=(15.5, 2.5),
                   path=self.anim_sprite_path + 'red_light/0.png'))
        add_sprite(AnimatedSprite(game, pos=(2.5, 8.5),
                   path=self.anim_sprite_path + 'red_light/0.png'))
        add_sprite(AnimatedSprite(game, pos=(13.5, 0.5),
                   path=self.anim_sprite_path + 'red_light/0.png'))

        # npc map
        # add_npc(NPC(game))
        # add_npc(NPC(game, pos=(11.5, 4.5)))

    def spawn_npc(self):
        for i in range(self.enemies):
            npc = choices(self.npc_types, self.weights)[0]
            pos = x, y = randrange(
                self.game.map.cols), randrange(self.game.map.rows)
            while (pos in self.game.map.world_map) or (pos in self.restricted_area):
                pos = x, y = randrange(
                    self.game.map.cols), randrange(self.game.map.rows)
            self.add_npc(npc(self.game, pos=(x + 0.5, y + 0.5)))

    def check_win(self):
        if not len(self.npc_positions):
            self.game.object_renderer.win()
            pg.display.flip()
            pg.time.delay(1500)
            self.game.new_game()

    def update(self):
        self.npc_positions = {
            npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
