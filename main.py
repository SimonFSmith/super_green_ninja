import pyglet
from welcome import Welcome
from game import Game
from score_board import ScoreBoard
from main_view import MainView

class Main():
    # static data #
    welcome = None
    game = None
    score_board = None

    # dynamic data #
    state = None
    transitions = None
    view = None


    def __init__(self):  
        self.reset()


    def start(self):
        pyglet.app.run()


    def test(self):
        self.reset()
        self.welcome.test()
        self.game.test()
        self.score_board.test()
        

    # behaviors (handlers) #
    def on_key_tab_pressed(self):
        if self.state == self.welcome:
            self.next_state()


    def on_key_space_bar_pressed(self):
        if self.state == self.game:
            self.game.on_key_space_bar_pressed()


    def on_key_right_pressed(self):
        if self.state == self.game:
            self.game.on_key_right_pressed()


    def on_key_left_pressed(self):
        if self.state == self.game:
            self.game.on_key_left_pressed()


    def on_enter_key_pressed(self):
        if self.state == self.score_board:
            self.score_board.on_enter_key_pressed()
            self.next_state()


    def on_enter_key_pressed_welcome(self):
        self.welcome.on_enter_key_pressed()


    def on_welcome_game_start_request(self):
        self.next_state()


    def on_game_end(self):
        self.score_board.display_final_time(self.game.total_time, self.game.player_lives)
        self.next_state()


    def on_score_board_welcome_back_request(self):
        self.next_state() 

    
    def reset(self):
        self.welcome = Welcome()
        self.game = Game()
        self.score_board = ScoreBoard()
        self.transitions = dict()
        self.transitions[self.welcome] = self.game
        self.transitions[self.game] = self.score_board
        self.transitions[self.score_board] = self.welcome
        self.view = MainView()
        # first/init state
        self.set_state(self.welcome)
        # attach behaviors / listen events
        self.listen_events()


    # shunting / routing / wiring / attach event to listeners #
    def listen_events(self):
        self.welcome.fan_club.register(Welcome.EV_GAME_START_REQUEST, self, self.on_welcome_game_start_request)
        self.game.fan_club.register(Game.EV_END_GAME, self, self.on_game_end)
        self.score_board.fan_club.register(ScoreBoard.EV_WELCOME_BACK_REQUEST, self, self.on_score_board_welcome_back_request)
        self.view.fan_club.register(MainView.EV_TAB_KEY_PRESSED, self, self.on_key_tab_pressed)
        self.view.fan_club.register(MainView.EV_SPACE_BAR_PRESSED, self, self.on_key_space_bar_pressed)
        self.view.fan_club.register(MainView.EV_RIGHT_KEY_PRESSED, self, self.on_key_right_pressed)
        self.view.fan_club.register(MainView.EV_LEFT_KEY_PRESSED, self, self.on_key_left_pressed)
        self.view.fan_club.register(MainView.EV_ENTER_KEY_PRESSED, self, self.on_enter_key_pressed)


    # utils #  
    # changing state will call the state start() method
    def set_state(self, new_state):
        self.state = new_state 
        self.state.start()
        self.view.set_batch(self.state.batch)


    def get_state(self):
        return self.state


    def next_state(self):
        new_state = self.transitions[self.state]
        self.set_state(new_state)
