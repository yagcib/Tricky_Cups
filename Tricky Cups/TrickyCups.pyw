# Comp 204 - Programming Studio
# Project 3
# Tricky Cups
# Ali Büyükberber, Ataman Fedai, Bayram Yağcı
# Mef University


from random import randint, shuffle # for randomizing the cups
from lib.ball import Ball # ball class
from lib.button import Button # button class
from lib.color import Color # for creating a color with RGB values
from lib.cup import Cup # cup class
import lib.stddraw as std # for drawing graphics onto canvas

# game difficulty
diff = 2

BG_COLOR = Color(191, 172, 136) # canvas background color
THEME_COLOR = Color(224, 114, 56) # custom orange as theme color
WHITE = Color(255, 255, 255) # white
BLACK = Color(0, 0, 0) # black

# pause screen
def pause():
    # buttons dictionary
    buttons = {"continue": Button(0.75, 2, text="Continue", bg_color=THEME_COLOR), "menu": Button(
        0.75, 1, text="Main Menu", bg_color=THEME_COLOR)}

    # canvas loop
    while True:
        # clear the canvas with the background color
        std.clear(BG_COLOR)

        # draw the paused text onto canvas
        std.setFontSize(60)
        std.setPenColor(BLACK)
        std.setFontFamily("Serif")
        std.boldText(2, 4.75, "Paused")

        # draw every button
        for button in buttons.values():
            button.draw()

        # if mouse pressed
        if std.mousePressed():
            # get the mouse coordinates
            x = std.mouseX()
            y = std.mouseY()

            # if continue button is pressed
            if buttons["continue"].isPressed(x, y):
                # return continue value
                return True

            # if main menu button is pressed
            elif buttons["menu"].isPressed(x, y):
                # return continue value
                return False

        # show the canvas
        std.show(0)

# main menu screen
def main_menu():
    # get the difficulty
    global diff
    std.setFontFamily("Serif")
    # initialize the buttons
    buttons = {"start": Button(0.75, 1, text="START!", bg_color=THEME_COLOR),
               "easy": Button(0.75, 2.25, 0.5, 0.5, "Easy", font_size=16),
               "normal": Button(1.75, 2.25, 0.5, 0.5, "Normal", font_size=16),
               "hard": Button(2.75, 2.25, 0.5, 0.5, "Hard", font_size=16)}

    # canvas loop
    while True:
        # clear the screen with the background color
        std.clear(BG_COLOR)

        # draw the game name onto canvas
        std.setFontSize(70)
        std.setPenColor(Color(80,80,80))
        std.setFontFamily("Serif")
        std.text(2, 4.75, "TRICKY CUPS")
        std.setPenColor(Color(100, 100, 100))
        std.filledRectangle(0, 4.4, 4, 0.03)
        std.filledRectangle(0, 5.05, 4, 0.03)

        # set the difficulty buttons color based on the difficulty level
        if diff == 1:
            buttons["easy"].bg_color = THEME_COLOR
            buttons["normal"].bg_color = WHITE
            buttons["hard"].bg_color = WHITE
        elif diff == 2:
            buttons["easy"].bg_color = WHITE
            buttons["normal"].bg_color = THEME_COLOR
            buttons["hard"].bg_color = WHITE
        elif diff == 3:
            buttons["easy"].bg_color = WHITE
            buttons["normal"].bg_color = WHITE
            buttons["hard"].bg_color = THEME_COLOR

        # draw buttons
        for button in buttons.values():
            button.draw()

        # if mouse pressed
        if std.mousePressed():
            # get the mouse coordinates
            x = std.mouseX()
            y = std.mouseY()

            # change the difficuty if a diff button is pressed
            if buttons["easy"].isPressed(x, y):
                diff = 1
            elif buttons["normal"].isPressed(x, y):
                diff = 2
            elif buttons["hard"].isPressed(x, y):
                diff = 3

            # start the game is start button is pressed
            elif buttons["start"].isPressed(x, y):
                game()

        # show the canvas
        std.show(0)

# game screen
def game():
    # get the difficulty
    global diff

    # initialize the pause button
    button = Button(3.5, 5.5, 0.35, 0.35, "||", WHITE, font_size=28)

    # initialize the score of every game loop
    score = 0

    # main game loop
    while True:
        # initiliaze the cups for different difficulty levels
        if diff == 1 or diff == 2:
            cups = [Cup(1, 4), Cup(3, 4), Cup(2, 2.5)]
        else:
            cups = [Cup(1, 4), Cup(3, 4), Cup(1, 2.5), Cup(3, 2.5)]

        # initliaze the ball
        ball = Ball(2, 1)

        # place the ball into a random cup and get the index of it
        ball_index = randint(0, len(cups)-1)
        cups[ball_index].ball = True

        # animation step counter
        steps = 1

        sequence = [] # list of cup mix pairs
        indexes = [i for i in range(len(cups))] # cup indexes
        differences = [] # list of x and y pairs of differences between cups

        # mix the cups for difficulty * 5 times
        for i in range(5*diff):
            # shuffle the indexes
            shuffle(indexes)

            # get the first two indexes and add it into mixing sequence
            sequence.append((indexes[0], indexes[1]))

            # add the x and y differences between cups on selected indexes to the differences
            differences.append((cups[indexes[0]].x - cups[indexes[1]].x, cups[indexes[0]].y - cups[indexes[1]].y))

        # sequence index counter
        seq_counter = 0

        # step index counter for every sequence
        step_counter = 0

        # pressed cup
        pressed = None

        # game drawing loop
        while True:
            # clear the canvas with the background color
            std.clear(Color(160,160,160))

            # draw the score on top of the canvas
            std.setPenColor(BLACK)
            std.setFontSize(30)
            std.boldText(2, 5.675, "Score: " + str(score))

            # if there is no animation, draw the pause button
            if steps == -1 and pressed == None and seq_counter == len(sequence):
                button.draw()

            # draw the table
            std.setPenColor(Color(118, 74, 52))
            std.filledRectangle(0, -1, 4, 5)
            
            # draw the table contour
            std.setPenColor(BLACK)
            std.rectangle(-1, -1, 6, 5)

            # draw cups
            for cup in cups:
                cup.draw()

            # if a cup is pressed
            if pressed != None:
                # if the pressed cup has the ball
                if pressed.ball:
                    # draw the ball and give points
                    ball.draw()
                    score += diff
                # if the cup does not have the ball
                else:
                    # reset the score
                    score = 0

                # draw the result symbol
                pressed.draw_result()

                # show the canvas and wait
                std.show(600)
                # go to the next iteration of game loop
                break
            
            # if the animation is in step 1
            if steps == 1:
                # draw the ball
                ball.draw()
                # show the canvas and wait
                std.show(600)
                # lift the cup
                cups[ball_index].y += 0.6
                # set the animation counter to 2
                steps = 2
                # reset mouse presses
                std.mousePressed()
                # skip other parts of the current iteration
                continue
            
            # if the animation is in step 2
            elif steps == 2:
                # draw the ball
                ball.draw()
                # show the canvas and wait
                std.show(600)
                # move ball to the cup's place
                ball.x = cups[ball_index].x
                ball.y = cups[ball_index].y - 0.9
                # set the animation counter to 3
                steps = 3
                # reset mouse presses
                std.mousePressed()
                # skip other parts of the current iteration
                continue
            
            # if the animation is in step 3
            elif steps == 3:
                # draw the ball
                ball.draw()
                # show the canvas and wait
                std.show(600)
                # lower the cup
                cups[ball_index].y -= 0.6
                # set the animation counter to 4
                steps = 4
                # reset mouse presses
                std.mousePressed()
                # skip other parts of the current iteration
                continue
            
            # if the animation is in step 4
            elif steps == 4:
                # show the canvas and wait
                std.show(600)
                # finish the animation
                steps = -1
                # reset mouse presses
                std.mousePressed()
                # skip other parts of the current iteration
                continue
            
            # if the mixing sequence is not finished
            if seq_counter != len(sequence):
                # get the sequence pair
                i = sequence[seq_counter]

                # compute the step distance based on the difference between the cup pair
                x_step = differences[seq_counter][0] / 20
                y_step = differences[seq_counter][1] / 20
                
                # if the current mixing animation is not finished
                if step_counter != 20:
                    # set the x and y values of both pairs to move the cups step by step to the position of one another
                    cups[i[0]].x -= x_step
                    cups[i[1]].x += x_step
                    cups[i[0]].y -= y_step
                    cups[i[1]].y += y_step

                    # increase the step counter
                    step_counter += 1
                    # show the canvas and wait for an amount of time based on the difficulty
                    std.show(18 / diff)
                    # reset mouse presses
                    std.mousePressed()
                    # skip other parts of the current iteration
                    continue
                # if the current sequence animation is over
                else:
                    # swap the cups on list
                    cups[i[0]], cups[i[1]] = cups[i[1]], cups[i[0]]
                    # increase the sequence counter
                    seq_counter += 1
                    # reset the step counter
                    step_counter = 0
                    # show the canvas and wait for an amount of time based on the difficulty to give a break between cup swaps
                    std.show(180 / diff)
                    # reset mouse presses
                    std.mousePressed()
                    # skip other parts of the current iteration
                    continue

            # if mouse pressed
            if std.mousePressed():
                # get the mouse coordinates
                x = std.mouseX()
                y = std.mouseY()

                # if pause button is pressed
                if button.isPressed(x, y):
                    # pause and wait for the return that indicatesif the user continues the game
                    cont = pause()
                    
                    # if the user wants to go to main menu
                    if not cont:
                        # finish the game
                        return
                # if the user pressed on a different place
                else:
                    # check if the user pressed on a cup
                    for i in range(len(cups)):
                        if cups[i].isPressed(x, y):
                            # lift the pressed cup
                            cups[i].y += 0.6
                            # move the ball to the pressed cup's place
                            ball.x = cups[i].x
                            ball.y = cups[i].y - 0.9
                            # initalize the pressed cup variable
                            pressed = cups[i]
            
            # show the canvas
            std.show(0)

# if the user runs the script directly
if __name__ == '__main__':
    # set the x and y scales of the canvas
    std.setXscale(0, 4)
    std.setYscale(0, 6)
    # set the canvas size
    std.setCanvasSize(550, 770)
    # display the main menu
    main_menu()
