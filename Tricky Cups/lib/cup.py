
import lib.stddraw as std # for drawing graphics onto canvas
from lib.color import Color # for creating a color with RGB values
from lib.picture import Picture # for creating a drawable image
from pathlib import Path # for getting a file's path

class Cup:
    # create a cup with x and y values
    def __init__(self, x, y) -> None:
        # initialize the fields
        self.x = x
        self.y = y

        # set the ball holding indicator as false
        self.ball = False

    # draw the cup
    def draw(self):
        # get the image from the src folder, create a drawable picture, and draw it
        std.picture(Picture(Path(__file__).parent.resolve().parent.resolve().joinpath("src", "cup.png")), self.x, self.y)

    # draw a symbol that indicates if the cup is holding the ball
    def draw_result(self):
        # if the cup has the ball
        if self.ball:

            std.picture(Picture(Path(__file__).parent.resolve().parent.resolve().joinpath("src", "tik.png")), self.x,
                        self.y-0.9)
        # if the cup does not have the ball
        else:
            # draw a red X below the cup
            std.setFontSize(50)
            std.setPenColor(Color(252,50,50))
            std.boldText(self.x, self.y - 0.9, "X")

    # check if the button is pressed with the given mouse coordinates
    def isPressed(self, x, y):
        # if the coordinates are in the boundaries of the button, return true
        if x < self.x + 0.4 and x > self.x - 0.4 and y < self.y + 0.6 and y > self.y - 0.6:
            return True

        # false otherwise
        return False