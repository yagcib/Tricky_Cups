
import lib.stddraw as std # for drawing graphics onto canvas
from lib.color import Color # for creating a color with RGB values

class Ball:
    # create a ball with x, y, and r values
    def __init__(self, x, y, r=0.25) -> None:
        # initialize fields
        self.x = x
        self.y = y
        self.r = r

    # draw the ball
    def draw(self):
        # draw the gray ball
        std.setPenColor(Color(208,208,208))
        std.filledCircle(self.x, self.y, self.r)

        # draw the contour
        std.setPenColor(Color(0,0,0))
        std.circle(self.x, self.y, self.r)
    