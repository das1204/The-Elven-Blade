from sprite_object import *
from npc import *


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

        # sprite map
        add_sprite(SpriteObject(game))

        add_sprite(AnimatedSprite(game, pos=(1.2, 1.2), scale=1.5, shift=-0.1))
        add_sprite(AnimatedSprite(game, pos=(5.5, 1.2)))
        add_sprite(AnimatedSprite(game, pos=(9.5, 1.2)))

        add_sprite(AnimatedSprite(game, pos=(1.2, 7.8)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 7.8)))
        add_sprite(AnimatedSprite(game, pos=(9.5, 7.8)))

        add_sprite(AnimatedSprite(game, pos=(14.8, 4.5)))

        # npc map
        add_npc(NPC(game, pos=(9.5, 3.5)))
        add_npc(NPC(game, pos=(9.5, 5.5)))

    def update(self):
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
    
    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)