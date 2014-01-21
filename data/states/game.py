import pygame as pg

from .. import prepare,tools


class Game(tools._State):
    """This state could represent the actual gameplay phase."""
    def __init__(self):
        tools._State.__init__(self)
        self.next = "INTRO"
        self.bgm = prepare.MUSIC["Anitek_-_07_-_Contact"]
        self.font = pg.font.Font(prepare.FONTS["Fixedsys500c"], 50)
        text = ["This is the game.", "Music should be playing",
                "to demonstrate", "that the intro movie",
                "has relinquished control", "of the mixer module.","",
                "Press escape to return", "to the intro movie"]
        self.rendered_text = self.make_text_list(self.font, text,
                                                 pg.Color("white"), 50, 50)
        self.escape = self.render_font(self.font, "Press Escape",
                                       pg.Color("yellow"),
                                       (prepare.SCREEN_RECT.centerx, 550))
        self.blink = False
        self.timer = 0.0

    def startup(self, current_time, persistant):
        """Load and play the music on scene start."""
        pg.mixer.music.load(self.bgm)
        pg.mixer.music.play(-1)
        return tools._State.startup(self, current_time, persistant)

    def cleanup(self):
        """Stop the music when scene is done."""
        pg.mixer.music.stop()
        return tools._State.cleanup(self)

    def make_text_list(self, font, strings, color, start_y, y_space):
        """
        Takes a list of strings and returns a list of
        (rendered_surface, rect) tuples. The rects are centered on the screen
        and their y coordinates begin at starty, with y_space pixels between
        each line.
        """
        rendered_text = []
        for i,string in enumerate(strings):
            msg_center = (prepare.SCREEN_RECT.centerx, start_y+i*y_space)
            msg_data = self.render_font(font, string, color, msg_center)
            rendered_text.append(msg_data)
        return rendered_text

    def get_event(self,event):
        """Go back to intro on escape key."""
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.done = True

    def draw(self, surface):
        """Blit all elements to surface."""
        surface.fill(pg.Color("lightslategrey"))
        for msg in self.rendered_text:
            surface.blit(*msg)
        if self.blink:
            surface.blit(*self.escape)

    def update(self, surface, keys, current_time, time_delta):
        """Update blink timer and draw everything."""
        self.current_time = current_time
        if self.current_time-self.timer > 1000.0/5.0:
            self.blink = not self.blink
            self.timer = self.current_time
        self.draw(surface)
