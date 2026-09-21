#include <stdio.h>

int main()
{
    int roomA, roomB;
    int position;

    printf("===== VACUUM CLEANER AGENT =====\n");

    printf("\nEnter status of Room A:\n");
    printf("1 = Dirty, 0 = Clean: ");
    scanf("%d", &roomA);

    printf("\nEnter status of Room B:\n");
    printf("1 = Dirty, 0 = Clean: ");
    scanf("%d", &roomB);

    printf("\nEnter vacuum cleaner position:\n");
    printf("1 = Room A, 2 = Room B: ");
    scanf("%d", &position);

    printf("\n--- Agent Actions ---\n");

    if (position == 1)
    {
        /* Vacuum is in Room A */

        if (roomA == 1)
        {
            printf("Room A is dirty.\n");
            printf("Action: SUCK\n");
            roomA = 0;
        }
        else
        {
            printf("Room A is already clean.\n");
        }

        printf("Action: MOVE RIGHT to Room B\n");
        position = 2;

        if (roomB == 1)
        {
            printf("Room B is dirty.\n");
            printf("Action: SUCK\n");
            roomB = 0;
        }
        else
        {
            printf("Room B is already clean.\n");
        }
    }

    else if (position == 2)
    {
        /* Vacuum is in Room B */

        if (roomB == 1)
        {
            printf("Room B is dirty.\n");
            printf("Action: SUCK\n");
            roomB = 0;
        }
        else
        {
            printf("Room B is already clean.\n");
        }

        printf("Action: MOVE LEFT to Room A\n");
        position = 1;

        if (roomA == 1)
        {
            printf("Room A is dirty.\n");
            printf("Action: SUCK\n");
            roomA = 0;
        }
        else
        {
            printf("Room A is already clean.\n");
        }
    }

    else
    {
        printf("Invalid position!\n");
        return 0;
    }

    /* Goal test */
    if (roomA == 0 && roomB == 0)
    {
        printf("\nGoal achieved!\n");
        printf("Both rooms are clean.\n");
    }

    return 0;
}
