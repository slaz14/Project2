# Importing necessary modules
import pygame
import random

# Defining a player class
class Player:
     # Initialization function for the Player class
     def __init__(self, RES):
        # Defining the rectangle object for the player
         self.rect = pygame.rect.Rect([0, 0, RES // 3 - 1, RES // 3 - 1])
         self.ttt = False

     # Function to update the position of the player on the screen
     def update(self):
         mouse_xy = pygame.mouse.get_pos()
         self.rect.topleft = mouse_xy

     # Function to draw the player on the screen
     def draw(self, window, RED):
         pygame.draw.circle(window, RED, (self.rect.left + 25, self.rect.top + 25), 25, 5)

     # Function to handle player clicks on the screen
     def click(self, list_x200, list_grid, RES):
         click1 = pygame.mouse.get_pressed()
         if click1[0]:
             coord_xy = self.convert_coordinatesxy(RES)
             for i in range(9):
                 if list_x200[i] == coord_xy:
                     if list_grid[i] == '_':
                         list_grid[i] = 'O'
                         return False

         return True

     # Function to convert player coordinates to a grid coordinate
     def convert_coordinatesxy(self, RES):
         return (self.rect.left // (RES // 3)) * RES // 3, (self.rect.top // (RES // 3)) * RES // 3

# Function to check if the player has won the game
def compute_try_ttt(list_tic, list_grid):
     for i in range(9):
         if list_grid[i] == '_':
             list_grid[i] = 'X'
             for check in list_tic:
                 if list_grid[check[0]] == 'X' and list_grid[check[1]] == 'X' and list_grid[check[2]] == 'X':
                     return True

             list_grid[i] = '_'

     return False

# Function to defend against the player
def compute_defends(list_tic, list_grid):
     for i in range(9):
         if list_grid[i] == '_':
             list_grid[i] = 'O'
             for check in list_tic:
                 if list_grid[check[0]] == 'O' and list_grid[check[1]] == 'O' and list_grid[check[2]] == 'O':
                     list_grid[i] = 'X'
                     return True

             list_grid[i] = '_'

     return False

# Function to play randomly against the player
def play_compute_random(random_launch, list_grid):
     if list_grid[random_launch] == '_':
         list_grid[random_launch] = 'X'
         return True

     return False

# Function to return a random number
def returns_random_number(zero, eight):
     return random.randint(zero, eight)

# Function to check if the game has been won by a player
def check_ttt(list_tic, list_grid, xo):
     for i in list_tic:
         if list_grid[i[0]] == xo and list_grid[i[1]] == xo and list_grid[i[2]] == xo:
             return True

     return False

# Function to check if the game is tied
def check_tie(empty, list_grid):
     if empty not in list_grid:
         return True

     return False

# Function to draw the grid on the screen
def draw_grid(window, GRAY, RES, WHITE):
     window.fill(GRAY)
     for i in range(RES // 3, RES, RES // 3):
         pygame.draw.line(window, WHITE, (i, 0), (i, RES))
         pygame.draw.line(window, WHITE, (0, i), (RES, i))

     return None

# Function takes in several parameters to draw X's and O's on a grid
def draw_xo(list_grid, list_x200, window, RED, BLUE, RES):
    # calculate the radius of the circles and the thickness of the lines
     r = RES // 6
     r2 = RES // 30
     thickness = 25
     # loop through the grid and draw circles where there is an "O"
     for i in range(9):
         if list_grid[i] == 'O':
             pygame.draw.circle(window, RED, (list_x200[i][0] + r, list_x200[i][1] + r),
                                r - 10, thickness)
     # loop through the grid and draw lines where there is an "X"
     for i in range(9):
         if list_grid[i] == 'X':

             # draw a diagonal line from top-left to bottom-right
             pygame.draw.line(window, BLUE, (list_x200[i][0] + r2, list_x200[i][1] + r2),
                              (list_x200[i][0] + (r * 2) - r2, list_x200[i][1] + (r * 2) - r2), thickness)

             # draw a diagonal line from top-right to bottom-left
             pygame.draw.line(window, BLUE, (list_x200[i][0] + (r * 2) - r2, list_x200[i][1] + r2),
                              (list_x200[i][0] + r2, list_x200[i][1] + (r * 2) - r2), thickness)

     return None

# Function takes in several parameters to draw text on a Pygame surface
def draw_text(surface, text, size, x, y):
     # create a Pygame font object with the given size
     font = pygame.font.SysFont("serif", size)
     # render the text with the font and color and get its rect
     text_surface = font.render(text, True, (200, 220, 30))
     text_rect = text_surface.get_rect()
     # set the top-center of the rect to the given (x, y) coordinates
     text_rect.midtop = (x, y)
     # draw the text onto the surface at the rect position
     surface.blit(text_surface, text_rect)
