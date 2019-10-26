"""
SnakeGame is a representation of the classic game snake
"""
import sys

import pygame

from src.RenderHandler import RenderHandler
from src.State import State


class SnakeGame:
    """
    Handles running the game and defining the pygame stage

    Attributes
    ==========
    state: State
        represents what state the game currently is in
    scene: Screen
        where the data will be rendered to
    b_color: Tuple (int, int, int)
        rgb representation of the background colour
    handler: RenderHandler
        object that renders all the items onto the screen
    """

    state: State
    scene: pygame.Surface
    b_color: tuple
    handler: RenderHandler

    running = True

    # DIMENSIONS FOR THE GAME BOARD
    BOARD_HEIGHT = 10
    BOARD_WIDTH = 10

    def __init__(self):
        pygame.init()
        self.b_color = 0, 0, 0
        self.state = State()
        self.scene = pygame.display.set_mode((300, 300))
        self.handler = RenderHandler([], self.scene)

    # Todo get this to use states and render handler also remove test map
    def run(self) -> None:
        """
        Starts the game and keeps running it, updating game logic and rendering
        items

        """
        self.state.set_to_running()
        print(self.state == "running")
        test_map = [[1, 2, 3],
                    [0, 1, 0],
                    [1, 3, 1]]

        clock = pygame.time.Clock()
        self.scene.fill(self.b_color)

        while self.running:
            # Ensure game runs at same speed across all devices
            clock.tick(50)

            # Exit game if player presses close button
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Todo add the menu and pause functions
            # Display the game while the state is running
            if self.state == "running":

                self.scene.fill(self.b_color)
                self.handler.update(test_map)
                self.handler.render()
                pygame.display.flip()

            elif self.state == "menu":
                pass
            elif self.state == "pause":
                pass


if __name__ == "__main__":
    game = SnakeGame()
    game.run()
    pygame.display.flip()