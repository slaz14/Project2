# Importing necessary modules
import pygame
import sys
import tictac

# Setting up initial variables
RESOLUTION = 600
RES = RESOLUTION
FPS = 60

# Setting up colors
WHITE = (200, 200, 200)
RED = (230, 0, 0)
BLUE = (0, 210, 220)
GRAY = (65, 65, 65)

# Initializing Pygame
pygame.init()

# Creating game window and setting caption
window = pygame.display.set_mode((RES, RES + 20))
pygame.display.set_caption('Tic Tac Toe Game')

# Filling the window with gray color
window.fill(GRAY)

# Initializing clock
clock = pygame.time.Clock()

# Initializing Sound
pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\Sandra\Desktop\Program 2\Tic_Tac_Toe_Sound.mp3")

pygame.mixer.music.play(-1)


# Initializing variables for keeping score and exit state
won = 0
lost = 0
ties = 0
exit = False

# Main game loop
while not exit:

     # Initializing variables for a new game
     list_grid = ['_'] * 9
     list_tic = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)
    ]

     list_x200 = [
         (0, 0), (RES // 3, 0), (RES // 3 * 2, 0),
         (0, RES // 3), (RES // 3, RES // 3), (RES // 3 * 2, RES // 3),
         (0, RES // 3 * 2), (RES // 3, RES // 3 * 2),
         (RES // 3 * 2, RES // 3 * 2),
     ]

     empty = '_'

     # Initializing player object if this is the first game
     if won == 0 == lost == ties:
         player = tictac.Player(RES)

     # Initializing variables for each game
     compute_ttt = False
     tie = False
     turn = tictac.returns_random_number(0, 9)

     # Randomly assigning the first turn
     if turn < 5:
         turn = True
     else:
         turn = False

     # Main game loop
     while not tie:

         # Checking for Pygame events
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 tie = True
                 exit = True
                 sys.exit()

         # Drawing the grid and X/O's on the window
         tictac.draw_grid(window, GRAY, RES, WHITE)
         tictac.draw_xo(list_grid, list_x200, window, RED, BLUE, RES)

         # Checking for win, tie or if it's the player's turn
         player.ttt = tictac.check_ttt(list_tic, list_grid, 'O')
         compute_ttt = tictac.check_ttt(list_tic, list_grid, 'X')
         tie = tictac.check_tie(empty, list_grid)

         # Breaking out of the loop if the player or the computer wins or if it's a tie
         if player.ttt:
             print('WIN Player!!!', player.ttt, compute_ttt, tie)
             won += 1
             break
         elif compute_ttt:
             print('COMPUTE PLAYER WINS!!!', player.ttt, compute_ttt, tie)
             lost += 1
             break
         elif tie:
             print('Tie! ', player.ttt, compute_ttt, tie)
             ties += 1
             break

         if turn:
            # Handle player move
             turn = player.click(list_x200, list_grid, RES)
             player.update()
             player.draw(window, RED)
         else:
            # Handle computer move
             compute_ttt = tictac.compute_try_ttt(list_tic, list_grid)
             if not compute_ttt:
                 turn = tictac.compute_defends(list_tic, list_grid)
                 if not turn:
                     random_launch = tictac.returns_random_number(0, 8)
                     turn = tictac.play_compute_random(random_launch, list_grid)

         # Update the screen
         clock.tick(FPS)
         pygame.display.update()

     # Stop the background music after the game is over
     pygame.mixer.music.stop()  

     # Handle end of game events
     other_game = False
     while not other_game:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 sys.exit()
             elif event.type == pygame.KEYDOWN:
                 if pygame.K_SPACE:
                     other_game = True

         # Draw the grid and X's and O's
         tictac.draw_grid(window, GRAY, RES, WHITE)
         tictac.draw_xo(list_grid, list_x200, window, RED, BLUE, RES)

         # Display the appropriate win/loss/tie message
         if player.ttt:
             tictac.draw_text(window,' Player WIN!!! ', 50, RES // 2, RES //2 - 100)
         elif compute_ttt:
             tictac.draw_text(window,' COMPUTE PLAYER WINS !!! ', 50, RES // 2, RES //2 - 100)
         elif tie:
             tictac.draw_text(window,' TIE! ', 50, RES // 2, RES //2 - 100)

        # Display the message to prompt the user to play agai
         tictac.draw_text(window, 'Press <space> to play again...',
             25, RES // 2, RES - 50)

         tictac.draw_text(window, 'Won: {} Lost: {} Ties: {} '.format(won, lost, tie),
                      20, RES // 2, RES)

         clock.tick(FPS)
         pygame.display.update()

     # Reset the player's Tic-Tac-Toe status
     player.ttt = False

# Exit the game
sys.exit()
