import pyglet

from lib.publisher import Publisher


class MainView(pyglet.window.Window):
    # static data #
    EV_TAB_KEY_PRESSED = 'EV_TAB_KEY_PRESSED'
    EV_SPACE_BAR_PRESSED = 'EV_SPACE_BAR_PRESSED'
    EV_RIGHT_KEY_PRESSED = 'EV_RIGHT_KEY_PRESSED'
    EV_LEFT_KEY_PRESSED = 'EV_LEFT_KEY_PRESSED'
    EV_ENTER_KEY_PRESSED = 'EV_ENTER_KEY_PRESSED'
    
    # dynamic data #
    fan_club = None

    # primary stage #
    batch = pyglet.graphics.Batch()


    def __init__(self): 
        super().__init__(width=512, height=512,visible=True)
        self.reset()
    

    def set_batch(self, new_batch):
        self.batch = new_batch
    

    def reset(self):
        self.fan_club = Publisher(
            [MainView.EV_TAB_KEY_PRESSED, 
                MainView.EV_SPACE_BAR_PRESSED, 
                MainView.EV_RIGHT_KEY_PRESSED, 
                MainView.EV_LEFT_KEY_PRESSED,
                MainView.EV_ENTER_KEY_PRESSED]
            )
        self.clear()


    # behaviors # 
    def on_key_press(self, symbol, modifiers):  
        if symbol == pyglet.window.key.TAB:
            self.fan_club.dispatch_event(MainView.EV_TAB_KEY_PRESSED) 
        if symbol == pyglet.window.key.SPACE:
            self.fan_club.dispatch_event(MainView.EV_SPACE_BAR_PRESSED)
        if symbol == pyglet.window.key.ENTER:
            self.fan_club.dispatch_event(MainView.EV_ENTER_KEY_PRESSED)


    def on_text_motion(self, motion):
        if motion == pyglet.window.key.MOTION_RIGHT:
            self.fan_club.dispatch_event(MainView.EV_RIGHT_KEY_PRESSED)
        if motion == pyglet.window.key.MOTION_LEFT:
            self.fan_club.dispatch_event(MainView.EV_LEFT_KEY_PRESSED)
        

    def on_draw(self):
        self.clear()
        self.batch.draw()
