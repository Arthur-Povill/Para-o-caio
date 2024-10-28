import pygame
import sys
import time
import tictactoe as ttt

pygame.init()
size = width, height = 600, 400

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode(size)

try:
    mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
    largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
    moveFont = pygame.font.Font("OpenSans-Regular.ttf", 60)
except:
    # Fallback to default font if the specified font is not found
    mediumFont = pygame.font.SysFont(None, 28)
    largeFont = pygame.font.SysFont(None, 40)
    moveFont = pygame.font.SysFont(None, 60)

user = None
board = ttt.initial_state()
ai_turn = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(black)

    # Let user choose a player
    if user is None:
        # Draw title
        title = largeFont.render("Play Tic-Tac-Toe", True, white)
        titleRect = title.get_rect(center=(width / 2, 50))
        screen.blit(title, titleRect)

        # Draw buttons
        playXButton = pygame.Rect(width / 8, height / 2, width / 4, 50)
        playOButton = pygame.Rect(5 * (width / 8), height / 2, width / 4, 50)

        pygame.draw.rect(screen, white, playXButton)
        pygame.draw.rect(screen, white, playOButton)

        playX = mediumFont.render("Play as X", True, black)
        playO = mediumFont.render("Play as O", True, black)
        playXRect = playX.get_rect(center=playXButton.center)
        playORect = playO.get_rect(center=playOButton.center)
        screen.blit(playX, playXRect)
        screen.blit(playO, playORect)

        # Check if button is clicked
        if pygame.mouse.get_pressed()[0]:
            mouse = pygame.mouse.get_pos()
            if playXButton.collidepoint(mouse):
                time.sleep(0.2)
                user = ttt.X
            elif playOButton.collidepoint(mouse):
                time.sleep(0.2)
                user = ttt.O

    else:
        # Draw game board
        tile_size = 80
        tile_origin = (width / 2 - 1.5 * tile_size, height / 2 - 1.5 * tile_size)
        tiles = []

        for i in range(3):
            row = []
            for j in range(3):
                rect = pygame.Rect(
                    tile_origin[0] + j * tile_size,
                    tile_origin[1] + i * tile_size,
                    tile_size, tile_size
                )
                pygame.draw.rect(screen, white, rect, 3)

                if board[i][j] != ttt.EMPTY:
                    move = moveFont.render(board[i][j], True, white)
                    moveRect = move.get_rect(center=rect.center)
                    screen.blit(move, moveRect)
                row.append(rect)
            tiles.append(row)

        game_over = ttt.terminal(board)
        current_player = ttt.player(board)

        # Show title
        if game_over:
            winner = ttt.winner(board)
            if winner is None:
                title_text = "Game Over: Tie."
            else:
                title_text = f"Game Over: {winner} wins."
        elif user == current_player:
            title_text = f"Your Turn ({user})"
        else:
            title_text = "Computer's Turn"

        title = largeFont.render(title_text, True, white)
        titleRect = title.get_rect(center=(width / 2, 30))
        screen.blit(title, titleRect)

        # Handle AI move
        if user != current_player and not game_over:
            if ai_turn:
                time.sleep(0.5)
                move = ttt.minimax(board)
                board = ttt.result(board, move)
                ai_turn = False
            else:
                ai_turn = True

        # Handle user move
        if pygame.mouse.get_pressed()[0] and user == current_player and not game_over:
            mouse = pygame.mouse.get_pos()
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ttt.EMPTY and tiles[i][j].collidepoint(mouse):
                        board = ttt.result(board, (i, j))
                        break

        # Handle game over and restart
        if game_over:
            againButton = pygame.Rect(width / 3, height - 65, width / 3, 50)
            pygame.draw.rect(screen, white, againButton)
            again = mediumFont.render("Play Again", True, black)
            againRect = again.get_rect(center=againButton.center)
            screen.blit(again, againRect)

            if pygame.mouse.get_pressed()[0]:
                mouse = pygame.mouse.get_pos()
                if againButton.collidepoint(mouse):
                    time.sleep(0.2)
                    user = None
                    board = ttt.initial_state()
                    ai_turn = False

    pygame.display.flip()
