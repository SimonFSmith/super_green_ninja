import pyglet

from param import Param
from lib.publisher import Publisher

class Welcome():
    # static data #
    EV_GAME_START_REQUEST = 'EV_GAME_START_REQUEST'

    # dynamic data #
    fan_club = None
    
    # scene #
    batch = pyglet.graphics.Batch()
    
    # visual objects #
    start_animation_asset = None
    start_animation = None


    def __init__(self):
        self.reset()


    def reset(self):
        self.fan_club = Publisher([Welcome.EV_GAME_START_REQUEST])
        self.title_label = pyglet.text.Label(text="SUPER GREEN NINJA", font_name="Times New Roman", font_size=30, color=(100, 200, 0, 255), x=256, y=400, anchor_x='center', anchor_y='center', batch=self.batch)
        self.goal_label = pyglet.text.Label(text="Reach the flag without touching the ennemies", font_name="Times New Roman", font_size=15, color=(255, 255, 255, 255), x=256, y=315, anchor_x='center', anchor_y='center', batch=self.batch)
        self.right_arrow_label = pyglet.text.Label(text="→ Right arrow: go forward", font_name="Times New Roman", font_size=15, color=(255, 255, 255, 255), x=256, y=235, anchor_x='center', anchor_y='center', batch=self.batch)
        self.left_arrow_label = pyglet.text.Label(text="← Left arrow: go backward", font_name="Times New Roman", font_size=15, color=(255, 255, 255, 255), x=256, y=210, anchor_x='center', anchor_y='center', batch=self.batch)
        self.space_bar_label = pyglet.text.Label(text="__ Space bar: jump", font_name="Times New Roman", font_size=15, color=(255, 255, 255, 255), x=256, y=185, anchor_x='center', anchor_y='center', batch=self.batch)
        self.start_animation_asset = pyglet.image.load_animation('asset/start_animation.gif')
        self.start_animation = pyglet.sprite.Sprite(img=self.start_animation_asset, x=0, y=55, batch=self.batch)


    def start(self):
        if Param.DEBUG == 1:
            print("")


    def on_enter_key_pressed(self):
        self.fan_club.dispatch_event(self.EV_GAME_START_REQUEST)


    def test(self):
        self.fan_club.dispatch_event(Welcome.EV_GAME_START_REQUEST)


    def center_image(self, image):
        """Sets an image's anchor point to its center"""
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
