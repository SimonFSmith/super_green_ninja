import pyglet
from lib.publisher import Publisher
from util import collides_with

class Game():
    # static data #
    EV_END_GAME = 'EV_END_GAME'
    gravity = 5
    acceleration_increment = 1
    maximum_speed = 5
    right_side_screen_limit = 300
    left_side_screen_limit = 150

    # dynamic data #
    fan_club = None
    game_view = None
    speed_x = 3
    total_time = 0
    player_lives = 3
    
    # game scene #
    batch = pyglet.graphics.Batch()
    
    # game assets #
    player_asset = None
    slime_ennemy_asset = None
    bunny_ennemy_asset = None
    ground_asset = None
    finish_asset = None
    background_asset = None
    
    # HUD (Head-up Display) #
    collision_label_top = None
    collision_label_bottom = None
    
    # FRAME / make-up / decor / environnement / terrain / ciel / fond etc.
    background = None
    ground = None
    finish = None
    
    # playables
    player = None
    slime_ennemy = None
    bunny_ennemy = None


    def __init__(self):
        self.hard_reset()
        

    # keyboard behaviors #
    def on_key_space_bar_pressed(self):
        if self.player.y < 50 and self.player.y > 40:
            self.player.y += 85


    def on_key_right_pressed(self):
        if self.player.visible:
            if self.speed_x < self.maximum_speed:
                self.speed_x += self.acceleration_increment
            if self.player.x < self.right_side_screen_limit:
                self.player.x += self.speed_x
            else:
                self.slime_ennemy.x -= self.speed_x
                self.bunny_ennemy.x -= self.speed_x
                self.bird_ennemy_one.x -= self.speed_x
                self.bird_ennemy_two.x -= self.speed_x
                self.bird_ennemy_three.x -= self.speed_x
                self.bird_ennemy_four.x -= self.speed_x
                self.bird_ennemy_five.x -= self.speed_x
                self.bird_ennemy_six.x -= self.speed_x
                self.ground.x -= self.speed_x
                self.finish.x -= self.speed_x
                self.saw_ennemy_one.x -= self.speed_x
                self.saw_ennemy_two.x -= self.speed_x
                self.saw_ennemy_three.x -= self.speed_x
                self.background.x -= self.speed_x
            if collides_with(self.player, self.slime_ennemy):
                if self.slime_ennemy.visible:
                    self.player_lives -= 1
                    self.player_lives_show.text = f"Lives: {self.player_lives}"
                    self.slime_ennemy.visible = False
                    if self.player_lives == 0:
                        self.make_assets_disappear()
                        self.stop_timer()
                        self.fan_club.dispatch_event(self.EV_END_GAME)
            if collides_with(self.player, self.bunny_ennemy):
                if self.bunny_ennemy.visible:
                    self.player_lives -= 1
                    self.player_lives_show.text = f"Lives: {self.player_lives}"
                    self.bunny_ennemy.visible = False
                    if self.player_lives == 0:
                        self.make_assets_disappear()
                        self.stop_timer()
                        self.fan_club.dispatch_event(self.EV_END_GAME)
            # Game ends on this collision if it's a win
            if collides_with(self.player, self.finish):
                self.stop_timer()
                self.make_assets_disappear()
                self.fan_club.dispatch_event(self.EV_END_GAME)
            if collides_with(self.player, self.saw_ennemy_one):
                if self.saw_ennemy_one.visible:
                    self.player_lives -= 1
                    self.player_lives_show.text = f"Lives: {self.player_lives}"
                    self.saw_ennemy_one.visible = False
                    if self.player_lives == 0:
                        self.make_assets_disappear()
                        self.stop_timer()
                        self.fan_club.dispatch_event(self.EV_END_GAME)
            if collides_with(self.player, self.saw_ennemy_two):
                if self.saw_ennemy_two.visible:
                    self.player_lives -= 1
                    self.player_lives_show.text = f"Lives: {self.player_lives}"
                    self.saw_ennemy_two.visible = False
                    if self.player_lives == 0:
                        self.make_assets_disappear()
                        self.stop_timer()
                        self.fan_club.dispatch_event(self.EV_END_GAME)
            if collides_with(self.player, self.saw_ennemy_three):
                if self.saw_ennemy_three.visible:
                    self.player_lives -= 1
                    self.player_lives_show.text = f"Lives: {self.player_lives}"
                    self.saw_ennemy_three.visible = False
                    if self.player_lives == 0:
                        self.make_assets_disappear()
                        self.stop_timer()
                        self.fan_club.dispatch_event(self.EV_END_GAME)

    def on_key_left_pressed(self):
        if self.player.visible:
            if self.speed_x < self.maximum_speed:
                self.speed_x += self.acceleration_increment
            if self.player.x > self.left_side_screen_limit:
                self.player.x -= self.speed_x
            else:
                self.slime_ennemy.x += self.speed_x
                self.bunny_ennemy.x += self.speed_x
                self.bird_ennemy_one.x += self.speed_x
                self.bird_ennemy_two.x += self.speed_x
                self.bird_ennemy_three.x += self.speed_x
                self.bird_ennemy_four.x += self.speed_x
                self.bird_ennemy_five.x += self.speed_x
                self.bird_ennemy_six.x += self.speed_x
                self.finish.x += self.speed_x
                self.saw_ennemy_one.x += self.speed_x
                self.saw_ennemy_two.x += self.speed_x
                self.saw_ennemy_three.x += self.speed_x
                self.ground.x += self.speed_x
                self.background.x += self.speed_x
            if collides_with(self.player, self.slime_ennemy):
                if self.slime_ennemy.visible:
                    self.player_lives -= 1
                    self.player_lives_show.text = f"Lives: {self.player_lives}"
                    self.slime_ennemy.visible = False
                    if self.player_lives == 0:
                        self.make_assets_disappear()
                        self.stop_timer()
                        self.fan_club.dispatch_event(self.EV_END_GAME)
            if collides_with(self.player, self.bunny_ennemy):
                if self.bunny_ennemy.visible:
                    self.player_lives -= 1
                    self.player_lives_show.text = f"Lives: {self.player_lives}"
                    self.bunny_ennemy.visible = False
                    if self.player_lives == 0:
                        self.make_assets_disappear()
                        self.stop_timer()
                        self.fan_club.dispatch_event(self.EV_END_GAME)
            # Game ends on this collision if it's a win
            if collides_with(self.player, self.finish):
                self.make_assets_disappear()
                self.stop_timer()
                self.fan_club.dispatch_event(self.EV_END_GAME)
            if collides_with(self.player, self.saw_ennemy_one):
                if self.saw_ennemy_one.visible:
                    self.player_lives -= 1
                    self.player_lives_show.text = f"Lives: {self.player_lives}"
                    self.saw_ennemy_one.visible = False
                    if self.player_lives == 0:
                        self.make_assets_disappear()
                        self.stop_timer()
                        self.fan_club.dispatch_event(self.EV_END_GAME)
            if collides_with(self.player, self.saw_ennemy_two):
                if self.saw_ennemy_two.visible:
                    self.player_lives -= 1
                    self.player_lives_show.text = f"Lives: {self.player_lives}"
                    self.saw_ennemy_two.visible = False
                    if self.player_lives == 0:
                        self.make_assets_disappear()
                        self.stop_timer()
                        self.fan_club.dispatch_event(self.EV_END_GAME)
            if collides_with(self.player, self.saw_ennemy_three):
                if self.saw_ennemy_three:
                    self.player_lives -= 1
                    self.player_lives_show.text = f"Lives: {self.player_lives}"
                    self.saw_ennemy_three.visible = False
                    if self.player_lives == 0:
                        self.make_assets_disappear()
                        self.stop_timer()
                        self.fan_club.dispatch_event(self.EV_END_GAME)

    # time behaviors #
    def apply_gravity_down(self, dt):
        if self.player.y > self.ground.y + 24:
            self.player.y -= 3

    def stop_timer(self):
        pyglet.clock.unschedule(self.apply_gravity_down)
        pyglet.clock.unschedule(self.make_ennemies_move)
        pyglet.clock.unschedule(self.calculate_time)

    def make_ennemies_move(self, dt):
        self.slime_ennemy.x -= 1
        self.bunny_ennemy.x -= 1
        self.bird_ennemy_one.x -= 2
        self.bird_ennemy_two.x -= 3
        self.bird_ennemy_three.x -= 5
        self.bird_ennemy_four.x -= 2
        self.bird_ennemy_five.x -= 3
        self.bird_ennemy_six.x -= 4
        if self.player.visible:
            if collides_with(self.player, self.slime_ennemy):
                if self.slime_ennemy.visible:
                    self.player_lives -= 1
                    self.player_lives_show.text = f"Lives: {self.player_lives}"
                    self.slime_ennemy.visible = False
                    if self.player_lives == 0:
                        self.make_assets_disappear()
                        self.stop_timer()
                        self.fan_club.dispatch_event(self.EV_END_GAME)
            if collides_with(self.player, self.bunny_ennemy):
                if self.bunny_ennemy.visible:
                    self.player_lives -= 1
                    self.player_lives_show.text = f"Lives: {self.player_lives}"
                    self.bunny_ennemy.visible = False
                    if self.player_lives == 0:
                        self.make_assets_disappear()
                        self.stop_timer()
                        self.fan_club.dispatch_event(self.EV_END_GAME)
            if collides_with(self.player, self.saw_ennemy_one):
                if self.saw_ennemy_one.visible:
                    self.player_lives -= 1
                    self.player_lives_show.text = f"Lives: {self.player_lives}"
                    self.saw_ennemy_one.visible = False
                    if self.player_lives == 0:
                        self.make_assets_disappear()
                        self.stop_timer()
                        self.fan_club.dispatch_event(self.EV_END_GAME)
            if collides_with(self.player, self.saw_ennemy_two):
                if self.saw_ennemy_two.visible:
                    self.player_lives -= 1
                    self.player_lives_show.text = f"Lives: {self.player_lives}"
                    self.saw_ennemy_two.visible = False
                    if self.player_lives == 0:
                        self.make_assets_disappear()
                        self.stop_timer()
                        self.fan_club.dispatch_event(self.EV_END_GAME)
            if collides_with(self.player, self.saw_ennemy_three):
                if self.saw_ennemy_three.visible:
                    self.player_lives -= 1
                    self.player_lives_show.text = f"Lives: {self.player_lives}"
                    self.saw_ennemy_three.visible = False
                    if self.player_lives == 0:
                        self.make_assets_disappear()
                        self.stop_timer()
                        self.fan_club.dispatch_event(self.EV_END_GAME)


    def calculate_time(self, dt):
        if self.player.visible:
            self.total_time += 1
            self.game_time.text = f"Time: {self.total_time}"


    # routing / shunting #
    def listen_events(self):
        pass


    # tools #
    def start(self):
        self.soft_reset()


    def hard_reset(self):
        self.fan_club = Publisher([Game.EV_END_GAME])
        # charging assets #  
        pyglet.resource.path = ['./asset']
        pyglet.resource.reindex()
        # groups to load assets in order
        self.background_group = pyglet.graphics.OrderedGroup(0)
        self.other_group = pyglet.graphics.OrderedGroup(1)

        # loading images
        self.background_asset = pyglet.resource.image('background.png')
        self.ground_asset = pyglet.resource.image('ground.png')
        self.player_asset = pyglet.resource.image('main_character_run.png')
        self.slime_ennemy_asset = pyglet.resource.image('slime_ennemy.png')
        self.bunny_ennemy_asset = pyglet.resource.image('bunny_ennemy.png')
        self.finish_asset = pyglet.resource.image('finish.png')
        self.bat_ennemy_asset = pyglet.resource.image('bat_ennemy.png')
        self.saw_ennemy_one_asset = pyglet.resource.image('saw_ennemy.png')
        self.saw_ennemy_two_asset = pyglet.resource.image('saw_ennemy.png')
        self.saw_ennemy_three_asset = pyglet.resource.image('saw_ennemy.png')
        self.bird_ennemy_one_asset = pyglet.resource.image('bird_ennemy.png')
        self.bird_ennemy_two_asset = pyglet.resource.image('bird_ennemy.png')
        self.bird_ennemy_three_asset = pyglet.resource.image('bird_ennemy.png')
        self.bird_ennemy_four_asset = pyglet.resource.image('bird_ennemy.png')
        self.bird_ennemy_five_asset = pyglet.resource.image('bird_ennemy.png')
        self.bird_ennemy_six_asset = pyglet.resource.image('bird_ennemy.png')


    def make_assets_disappear(self):
        self.bird_ennemy_one.visible = False
        self.bird_ennemy_two.visible = False
        self.bird_ennemy_three.visible = False
        self.bird_ennemy_four.visible = False
        self.bird_ennemy_five.visible = False
        self.bird_ennemy_six.visible = False
        self.saw_ennemy_one.visible = False
        self.saw_ennemy_two.visible = False
        self.saw_ennemy_three.visible = False
        self.bat_ennemy.visible = False
        self.player_lives_show.visible = False
        self.game_time.visible = False
        self.finish.visible = False
        self.bunny_ennemy.visible = False
        self.slime_ennemy.visible = False
        self.player.visible = False


    def soft_reset(self):
        self.total_time = 0
        self.time = 0
        self.player_lives = 3

        pyglet.clock.schedule_interval(self.apply_gravity_down, .075)
        pyglet.clock.schedule_interval(self.make_ennemies_move, .05)
        pyglet.clock.schedule_interval(self.calculate_time, 1)

        # center images
        self.center_image(self.background_asset)
        self.center_image(self.ground_asset)
        self.center_image(self.player_asset)
        self.center_image(self.slime_ennemy_asset)
        self.center_image(self.bunny_ennemy_asset)
        self.center_image(self.finish_asset)
        self.center_image(self.bat_ennemy_asset)
        self.center_image(self.saw_ennemy_one_asset)
        self.center_image(self.saw_ennemy_two_asset)
        self.center_image(self.saw_ennemy_three_asset)
        self.center_image(self.bird_ennemy_one_asset)
        self.center_image(self.bird_ennemy_two_asset)
        self.center_image(self.bird_ennemy_three_asset)
        self.center_image(self.bird_ennemy_four_asset)
        self.center_image(self.bird_ennemy_five_asset)
        self.center_image(self.bird_ennemy_six_asset)

        # init visual objects AND put them on the scene (aka batch) #
        # background
        self.background = pyglet.sprite.Sprite(img=self.background_asset, x=450, y=256, batch=self.batch, group=self.background_group)
        # ground
        self.ground = pyglet.sprite.Sprite(img=self.ground_asset, x=450, y=22, batch=self.batch, group=self.other_group)
        # make player animated when standing
        self.player_grid = pyglet.image.ImageGrid(self.player_asset, rows=1, columns=12)
        self.player_animation = pyglet.image.Animation.from_image_sequence(self.player_grid, duration=0.1)
        self.player = pyglet.sprite.Sprite(img=self.player_animation, x=200, y=45, batch=self.batch, group=self.other_group)
        # make slime ennemy animated
        self.slime_ennemy_grid = pyglet.image.ImageGrid(self.slime_ennemy_asset, rows=1, columns=10)
        self.slime_ennemy_animation = pyglet.image.Animation.from_image_sequence(self.slime_ennemy_grid, duration=0.1)
        self.slime_ennemy = pyglet.sprite.Sprite(img=self.slime_ennemy_animation, x=450, y=45, batch=self.batch, group=self.other_group)
        # make bunny ennemy animated
        self.bunny_ennemy_grid = pyglet.image.ImageGrid(self.bunny_ennemy_asset, rows=1, columns=12)
        self.bunny_ennemy_animation = pyglet.image.Animation.from_image_sequence(self.bunny_ennemy_grid, duration=0.1)
        self.bunny_ennemy = pyglet.sprite.Sprite(img=self.bunny_ennemy_animation, x=850, y=45, batch=self.batch, group=self.other_group)
        # make finish flag animated
        self.finish_grid = pyglet.image.ImageGrid(self.finish_asset, rows=1, columns=10)
        self.finish_animation = pyglet.image.Animation.from_image_sequence(self.finish_grid, duration=0.1)
        self.finish = pyglet.sprite.Sprite(img=self.finish_animation, x=1400, y=45, batch=self.batch, group=self.other_group)
        # time
        self.game_time = pyglet.text.Label(text=f"Time: {self.total_time}", x=256, y=498,color=(0, 0, 0, 255), anchor_x='center', anchor_y='center', batch=self.batch, group=self.other_group)
        # lives
        self.player_lives_show = pyglet.text.Label(text=f"Lives: {self.player_lives}", x=475, y=498,color=(0, 0, 0, 255), anchor_x='center', anchor_y='center', batch=self.batch, group=self.other_group)
        # bat ennemy
        self.bat_ennemy_grid = pyglet.image.ImageGrid(self.bat_ennemy_asset, rows=1, columns=7)
        self.bat_ennemy_animation = pyglet.image.Animation.from_image_sequence(self.bat_ennemy_grid, duration=0.1)
        self.bat_ennemy = pyglet.sprite.Sprite(img=self.bat_ennemy_animation, x=650, y=140, batch=self.batch, group=self.other_group)
        # saw ennemy one
        self.saw_ennemy_one_grid = pyglet.image.ImageGrid(self.saw_ennemy_one_asset, rows=1, columns=8)
        self.saw_ennemy_one_animation = pyglet.image.Animation.from_image_sequence(self.saw_ennemy_one_grid, duration=0.1)
        self.saw_ennemy_one = pyglet.sprite.Sprite(img=self.saw_ennemy_one_animation, x=850, y=100, batch=self.batch, group=self.other_group)
        # saw ennemy two
        self.saw_ennemy_two_grid = pyglet.image.ImageGrid(self.saw_ennemy_two_asset, rows=1, columns=8)
        self.saw_ennemy_two_animation = pyglet.image.Animation.from_image_sequence(self.saw_ennemy_two_grid, duration=0.1)
        self.saw_ennemy_two = pyglet.sprite.Sprite(img=self.saw_ennemy_two_animation, x=950, y=45, batch=self.batch, group=self.other_group)
        # saw ennemy three
        self.saw_ennemy_three_grid = pyglet.image.ImageGrid(self.saw_ennemy_three_asset, rows=1, columns=8)
        self.saw_ennemy_three_animation = pyglet.image.Animation.from_image_sequence(self.saw_ennemy_three_grid, duration=0.1)
        self.saw_ennemy_three = pyglet.sprite.Sprite(img=self.saw_ennemy_three_animation, x=980, y=140, batch=self.batch, group=self.other_group)
        # bird ennemy one
        self.bird_ennemy_one_grid = pyglet.image.ImageGrid(self.bird_ennemy_one_asset, rows=1, columns=9)
        self.bird_ennemy_one_animation = pyglet.image.Animation.from_image_sequence(self.bird_ennemy_one_grid, duration=0.1)
        self.bird_ennemy_one = pyglet.sprite.Sprite(img=self.bird_ennemy_one_animation, x=540, y=240, batch=self.batch, group=self.other_group)
        # bird ennemy two
        self.bird_ennemy_two_grid = pyglet.image.ImageGrid(self.bird_ennemy_two_asset, rows=1, columns=9)
        self.bird_ennemy_two_animation = pyglet.image.Animation.from_image_sequence(self.bird_ennemy_two_grid, duration=0.1)
        self.bird_ennemy_two = pyglet.sprite.Sprite(img=self.bird_ennemy_two_animation, x=600, y=310, batch=self.batch, group=self.other_group)
        # bird ennemy three
        self.bird_ennemy_three_grid = pyglet.image.ImageGrid(self.bird_ennemy_three_asset, rows=1, columns=9)
        self.bird_ennemy_three_animation = pyglet.image.Animation.from_image_sequence(self.bird_ennemy_three_grid, duration=0.1)
        self.bird_ennemy_three = pyglet.sprite.Sprite(img=self.bird_ennemy_three_animation, x=625, y=185, batch=self.batch, group=self.other_group)
        # bird ennemy four
        self.bird_ennemy_four_grid = pyglet.image.ImageGrid(self.bird_ennemy_four_asset, rows=1, columns=9)
        self.bird_ennemy_four_animation = pyglet.image.Animation.from_image_sequence(self.bird_ennemy_four_grid, duration=0.1)
        self.bird_ennemy_four = pyglet.sprite.Sprite(img=self.bird_ennemy_four_animation, x=700, y=410, batch=self.batch, group=self.other_group)
        # bird ennemy five
        self.bird_ennemy_five_grid = pyglet.image.ImageGrid(self.bird_ennemy_five_asset, rows=1, columns=9)
        self.bird_ennemy_five_animation = pyglet.image.Animation.from_image_sequence(self.bird_ennemy_five_grid, duration=0.1)
        self.bird_ennemy_five = pyglet.sprite.Sprite(img=self.bird_ennemy_five_animation, x=830, y=200, batch=self.batch, group=self.other_group)
        # bird ennemy six
        self.bird_ennemy_six_grid = pyglet.image.ImageGrid(self.bird_ennemy_six_asset, rows=1, columns=9)
        self.bird_ennemy_six_animation = pyglet.image.Animation.from_image_sequence(self.bird_ennemy_six_grid, duration=0.1)
        self.bird_ennemy_six = pyglet.sprite.Sprite(img=self.bird_ennemy_six_animation, x=910, y=250, batch=self.batch, group=self.other_group)


    def center_image(self, image):
        """Sets an image's anchor point to its center"""
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2


    def test(self):
        self.fan_club.dispatch_event(Game.EV_END_GAME)
