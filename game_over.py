# /usr/bin/env python3

# Created by: Marwan Mashaly
# Created on: October 2019
# This programs shows a sprite, makes a sound,
# shoots a laser and shows an alien

import ugame
import stage
import constants
import time
import random


def splash_scene():
    # this function is the splash scene game loop

    # an image bank for CircuitPython
    image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, 160, 120)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # Wait for 1 seconds
        time.sleep(1.00)
        menu_scene()

        # redraw sprite list


def menu_scene():
    # this function is a scene

    score = 0

    # an image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)

    # used this program to split the iamge
    # into tile: https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    # a list of sprites
    sprites = []

    # add text objects
    text = []

    text1 = stage.Text(width=29, height=14, font=None,
                       palette=constants.NEW_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

    text2 = stage.Text(width=29, height=14, font=None,
                       palette=constants.NEW_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + sprites + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic
        keys = ugame.buttons.get_pressed()
        # print(keys)

        if keys & ugame.K_START != 0:  # Start button
            game_scene()

        # redraw sprite list


def game_scene():
    # This function shows a sprite and makes a sound

    score = 0
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    def show_alien():
        # make an alien show up on screen in the x-axis
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x < 0:
                aliens[alien_number].move(random.randint(0 +
                                          constants.SPRITE_SIZE,
                                          constants.SCREEN_X -
                                          constants.SPRITE_SIZE),
                                          constants.OFF_TOP_SCREEN)
                break

    # an image bank for circuitpython
    image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")
    # a list of sprites that will be updated every frame
    sprites = []

    # create lasers for when you shoot
    lasers = []
    for lasers_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(image_bank_1, 10,
                                      constants.OFF_SCREEN_X,
                                      constants.OFF_SCREEN_Y)
        lasers.append(a_single_laser)

    # create aliens
    aliens = []
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        a_single_alien = stage.Sprite(image_bank_1, 9,
                                      constants.OFF_SCREEN_X,
                                      constants.OFF_SCREEN_Y)
        aliens.append(a_single_alien)

    # current number of aliens that should be moving down screen,
    # start with just 1
    alien_count = 1
    show_alien()

    # Add text at top of the screen
    score_text = stage.Text(width=29, height=29, font=None,
                            palette=constants.NEW_PALETTE, buffer=None)
    score_text.clear()
    score_text.cursor(0, 0)
    score_text.move(1, 1)
    score_text.text("Score: {0}".format(score))

    # get sound ready
    crash_sound = open("crash.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    boom_sound = open("boom.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(boom_sound)
    # sprites in the scene
    # parameters (image_bank, image # in bank, x, y)
    ship = stage.Sprite(image_bank_1, 5, int(constants.SCREEN_X / 2),
                        int(constants.SCREEN_Y - constants.SPRITE_SIZE))
    sprites.append(ship)  # insert at the top of the sprite list

    # sets the background to image 0 in the bank
    # backgrounds do not have magents as a transparent color
    background = stage.Grid(image_bank_1, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(1, 3)
            background.tile(x_location, y_location, tile_picked)

    # create a stage for the background to show up on
    #  and set the frame rate to 60
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers, items show up in order
    game.layers = [score_text] + sprites + lasers + aliens + [background]
    # render the background and initial location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, or you turn it off
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_X != 0:  # a button (fire)
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
        if keys & ugame.K_X:
            # print("A")
            pass
        if keys & ugame.K_O:
            # print("B")
            pass
        if keys & ugame.K_START:
            # print("K_START")
            pass
        if keys & ugame.K_SELECT:
            # print("K_SELECT")
            pass
        # update_game_logic
        # move ship to the right and the left
        if keys & ugame.K_RIGHT != 0:
            if ship.x > constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
            else:
                ship.move(ship.x + 1, ship.y)

        if keys & ugame.K_LEFT != 0:
            if ship.x < 0:
                ship.move(0, ship.y)
            else:
                ship.move(ship.x - 1, ship.y)
            pass
        # move ship up and down
        if keys & ugame.K_UP:
            ship.move(ship.x, ship.y - 1)
        elif keys & ugame.K_DOWN:
            ship.move(ship.x, ship.y + 1)
            pass
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        if a_button == constants.button_state["button_just_pressed"]:
            # firea laser
            for lasers_number in range(len(lasers)):
                if lasers[lasers_number].x < 0:
                    lasers[lasers_number].move(ship.x, ship.y)
                    sound.stop()
                    sound.play(pew_sound)
                    break
        # each frame move the lasers, that have been fired
        for lasers_number in range(len(lasers)):
            if lasers[lasers_number].x > 0:
                lasers[lasers_number].move(lasers[lasers_number].x,
                                           lasers[lasers_number].y
                                           - constants.LASER_SPEED)
                if lasers[lasers_number].y < constants.OFF_TOP_SCREEN:
                    lasers[lasers_number].move(constants.OFF_SCREEN_X,
                                               constants.OFF_SCREEN_Y)

        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                aliens[alien_number].move(aliens[alien_number].x,
                                          aliens[alien_number].y +
                                          constants.ALIEN_SPEED)
                if aliens[alien_number].y > constants.SCREEN_Y:
                    aliens[alien_number].move(constants.OFF_SCREEN_X,
                                              constants.OFF_SCREEN_Y)
                    show_alien()  # make it randomly show up at top again

        # Each frame check if any lasers are touching any of the aliens
        for lasers_number in range(len(lasers)):
            if lasers[lasers_number].x > 0:
                for alien_number in range(len(aliens)):
                    if aliens[alien_number].x > 0:
                        # the first 4 numbers are the coordinates of A box
                        # since the laser is thin, it made it thinner
                        # and slightly smaller

                        # the second 4 numbers are the alien, it is more of
                        # a box so I just made it slightly smaller
                        #
                        if stage.collide(lasers[lasers_number].x + 6,
                                         lasers[lasers_number].y + 2,
                                         lasers[lasers_number].x + 11,
                                         lasers[lasers_number].y + 12,
                                         aliens[alien_number].x + 1,
                                         aliens[alien_number].y,
                                         aliens[alien_number].x + 15,
                                         aliens[alien_number].y + 15):
                            # you hit an alien
                            aliens[alien_number].move(constants.OFF_SCREEN_X,
                                                      constants.OFF_SCREEN_Y)
                            lasers[lasers_number].move(constants.OFF_SCREEN_X,
                                                       constants.OFF_SCREEN_Y)

                            # add 1 to the score
                            score += 1
                            score_text.clear()
                            score_text.cursor(0, 0)
                            score_text.move(1, 1)
                            score_text.text("Score: {0}".format(score))
                            game.render_block()

                            # play sound effect
                            sound.stop()
                            sound.play(boom_sound)
                            show_alien()
                            show_alien()
                            alien_count = alien_count + 1

        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                if stage.collide(aliens[alien_number].x + 1, aliens[alien_number].y,
                                 aliens[alien_number].x + 15, aliens[alien_number].y + 15,
                                 ship.x, ship.y,
                                 ship.x + 15, ship.y + 15):
                    # alien hit the ship
                    sound.stop()
                    sound.play(crash_sound)
                    # wait for 4 seconds
                    time.sleep(4.0)
                    sound.stop()
                    game_over_scene

        # redraw sprite list
        game.render_sprites(sprites + lasers + aliens)
        game.tick()  # wait until refresh rate finishes


def game_over_scene(final_score):
    # This function is the game over scene
    # on image bank for circuitpython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio")

    # sets the background to image 0 in hte bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    text = []

    text0 = stage.Text(width=29, height=14, font=None, palette=constants.NEW_PALETTE, buffer=None)
    text0.move(22, 20)
    text0.text("Final Score: {0>2d}".format(final_score))
    text.append(text0)

    text1 = stage.Text(width=29, height=14, font=None, palette=constants.NEW_PALETTE, buffer=None)
    text1.move(43, 60)
    text1.move("Game Over")
    text.append(text1)
    

    text2 = stage.Text(width=29, height=14, font=None, palette=constants.NEW_PALETTE, buffer=None)
    text2.move(32, 110)
    text2.text("PRESS SELECT")
    text.append(text2)

    # create a stage for the background to show up on
    # and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers to show up in order
    game.layers = text + [background]
    # render the background and intial location of the sprite list
    game.render_block()

    while True:
        # update game logic
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_SELECT != 0:
            keys = 0
            menu_scene()



if __name__ == "__main__":
    splash_scene()
