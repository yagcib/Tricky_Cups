
import lib.stddraw as std # for drawing graphics onto canvas
from lib.color import Color # for creating a color with RGB values

class Button:
    # create a button with the given arguments
    def __init__(self, x, y, w=2.5, h=0.75, text="", bg_color=Color(255,255,255), contour_color=Color(0,0,0), text_color=Color(0,0,0), font_family="Serif", font_size=40) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.bg_color = bg_color
        self.contour_color = contour_color
        self.text_color = text_color
        self.font_family = font_family
        self.font_size = font_size

    # draw the button
    def draw(self):
        # draw the button background
        std.setPenColor(self.bg_color)
        std.filledRectangle(self.x, self.y, self.w, self.h)

        # draw the contour
        std.setPenColor(self.contour_color)
        std.rectangle(self.x, self.y, self.w, self.h)

        # draw the button text
        std.setPenColor(self.text_color)
        std.setFontSize(self.font_size)
        std.setFontFamily(self.font_family)
        std.boldText((self.x*2 + self.w)/2, (self.y*2 + self.h)/2 + 0.015, self.text)

    # check if the button is pressed with the given mouse coordinates
    def isPressed(self, x, y):
        # if the coordinates are in the boundaries of the button, return true
        if x < self.x + self.w and x > self.x and y < self.y + self.h and y > self.y:
            return True

        # false otherwise
        return False