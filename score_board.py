import pyglet
from lib.publisher import Publisher

class ScoreBoard():
    # static data #
    EV_WELCOME_BACK_REQUEST = 'EV_WELCOME_BACK_REQUEST'
    EV_ENTER_KEY_PRESSED = 'EV_ENTER_KEY_PRESSED'
    
    # dynamic data #
    fan_club = None  
    total_time_label = None
    looser_label = None
    winner_label = None
    title_label = None
    main_menu_label = None

    # scene #
    batch = pyglet.graphics.Batch()


    def __init__(self):
        self.hard_reset()


    def hard_reset(self):
        self.fan_club = Publisher([ScoreBoard.EV_WELCOME_BACK_REQUEST])
        self.title_label = pyglet.text.Label(text="SCOREBOARD", font_name="Times New Roman", font_size=30, color=(100, 200, 0, 255), x=256, y=400, anchor_x='center', anchor_y='center', batch=self.batch)
        self.main_menu_label = pyglet.text.Label(text="Press ENTER to play again", font_name="Times New Roman", font_size=15, color=(255, 255, 255, 255), x=256, y=200, anchor_x='center', anchor_y='center', batch=self.batch)


    def display_final_time(self, total_time, player_lives):
        self.total_time_label = pyglet.text.Label(text=f"Your total time is {total_time} seconds", font_name="Times New Roman", font_size=15, color=(255, 255, 255, 255), x=256, y=300, anchor_x='center', anchor_y='center', batch=self.batch)
        if player_lives == 0:
            self.looser_label = pyglet.text.Label(text=f"BUT YOU LOST...", font_name="Times New Roman", font_size=20, color=(255, 255, 255, 255), x=256, y=250, anchor_x='center', anchor_y='center', batch=self.batch)
        else:
            self.winner_label = pyglet.text.Label(text=f"YOU WON!", font_name="Times New Roman", font_size=20, color=(255, 255, 255, 255), x=256, y=250, anchor_x='center', anchor_y='center', batch=self.batch)


    def start(self):
        pass


    def on_enter_key_pressed(self):
        self.total_time_label.delete()
        try:
            self.looser_label.delete()
        except:
            pass
        try:
            self.winner_label.delete()
        except:
            pass
        self.fan_club.dispatch_event(self.EV_WELCOME_BACK_REQUEST)


    def test(self):
        self.fan_club.dispatch_event(ScoreBoard.EV_WELCOME_BACK_REQUEST)
