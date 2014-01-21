import pygame as pg


class Movie(object):
    """A helper class for playing movies with pygame.  Automatically disables
    mixer on creation and can reenable the mixer module on stop.  Ideally this
    class would inherit from pygame.movie.Movie but this is not allowed."""
    def __init__(self, filename, position, scale=1, autoplay=True):
        pg.mixer.quit()
        self._movie = pg.movie.Movie(filename)
        w, h = [size*scale for size in self.get_size()]
        self.image = pg.Surface((w,h)).convert()
        self.set_display(self.image, pg.Rect(0,0,w,h))
        self.rect = pg.Rect(position, (w,h))
        if autoplay:
            self.play()

    def __getattr__(self, attribute):
        """This lets us act like Movie is a subclass of pygame.movie.Movie."""
        return getattr(self._movie, attribute)

    def stop(self, delete=False):
        """If delete is True re-enable the mixer after stopping playback and
        delete the actual movie attribute (seems necessary in some cases)."""
        self._movie.stop()
        if delete:
            del self._movie
            pg.mixer.init()

    def pause(self):
        """Pauses and unpauses the movie."""
        if self.get_busy():
            self.stop()
        else:
            self.play()

    def draw(self, surface):
        """Draw the current image to the target surface."""
        surface.blit(self.image, self.rect)
