#include <stdio.h>
#include <stdlib.h>
#include <time.h>

char board[3][3];

/* Initialize board */
void initializeBoard()
{
    int i, j;

    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            board[i][j] = ' ';
        }
    }
}

/* Display board */
void displayBoard()
{
    printf("\n");

    printf(" %c | %c | %c\n",
           board[0][0], board[0][1], board[0][2]);

    printf("---|---|---\n");

    printf(" %c | %c | %c\n",
           board[1][0], board[1][1], board[1][2]);

    printf("---|---|---\n");

    printf(" %c | %c | %c\n",
           board[2][0], board[2][1], board[2][2]);

    printf("\n");
}

/* Check winner */
int checkWinner(char player)
{
    int i;

    /* Rows and columns */
    for (i = 0; i < 3; i++)
    {
        if (board[i][0] == player &&
            board[i][1] == player &&
            board[i][2] == player)
            return 1;

        if (board[0][i] == player &&
            board[1][i] == player &&
            board[2][i] == player)
            return 1;
    }

    /* Diagonals */
    if (board[0][0] == player &&
        board[1][1] == player &&
        board[2][2] == player)
        return 1;

    if (board[0][2] == player &&
        board[1][1] == player &&
        board[2][0] == player)
        return 1;

    return 0;
}

/* Check draw */
int isDraw()
{
    int i, j;

    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            if (board[i][j] == ' ')
                return 0;
        }
    }

    return 1;
}

/* Human move */
void humanMove()
{
    int position;
    int row, col;

    while (1)
    {
        printf("Enter position (1-9): ");
        scanf("%d", &position);

        if (position < 1 || position > 9)
        {
            printf("Invalid position!\n");
            continue;
        }

        row = (position - 1) / 3;
        col = (position - 1) % 3;

        if (board[row][col] != ' ')
        {
            printf("Position already occupied!\n");
        }
        else
        {
            board[row][col] = 'X';
            break;
        }
    }
}

/* Computer move */
void computerMove()
{
    int position;
    int row, col;

    do
    {
        position = rand() % 9 + 1;

        row = (position - 1) / 3;
        col = (position - 1) % 3;

    } while (board[row][col] != ' ');

    board[row][col] = 'O';

    printf("Computer selected position: %d\n", position);
}

/* Main function */
int main()
{
    srand(time(NULL));

    initializeBoard();

    printf("===== TIC-TAC-TOE GAME =====\n");
    printf("Human = X\n");
    printf("Computer = O\n");

    while (1)
    {
        displayBoard();

        /* Human turn */
        humanMove();

        if (checkWinner('X'))
        {
            displayBoard();
            printf("Human Wins!\n");
            break;
        }

        if (isDraw())
        {
            displayBoard();
            printf("Game Draw!\n");
            break;
        }

        /* Computer turn */
        computerMove();

        if (checkWinner('O'))
        {
            displayBoard();
            printf("Computer Wins!\n");
            break;
        }

        if (isDraw())
        {
            displayBoard();
            printf("Game Draw!\n");
            break;
        }
    }

    return 0;
}