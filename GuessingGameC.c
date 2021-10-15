/* Purpose: Guessing Game Written In C */

#include <stdio.h>  // Standard input and output header file to access print,scanf
#include <stdlib.h> // For extra functions such as system("pause"), rand()
#include <time.h>   // For updating of random number

// guessing game function
void guess_number(int R)
{
    //Variables
    int guess, number = 0;
    int numOfguess = 10; //Guessing Attemps
    srand(time(NULL));   // Updates the random generator to a new value
    number = rand() % R;
    printf("Welcome to the Guessing Game!\nGuess a number between 1 and %d\n", R);
    do
    {
        if (numOfguess == 0)
        {
            printf("\nMax Attempt Reached\nYOU LOSE!");
            break;
        }
        printf("\nEnter your Guess: ");
        scanf("%d", &guess);
        if (guess > R)
        {
            printf("Guessed Number Exceeded the Range!\n");
        }

        if (guess > number)
        {
            printf("Number must be Lower!\n");
            numOfguess--;
        }
        else if (guess < number)
        {
            printf("Number must be higher!\n");
            numOfguess--;
        }
        else
        {
            printf("Congratulations \nYou have guessed the correct number!!\nThank you for playing the game");
        }
        printf("\n%d Attemps Left\n", numOfguess);
    } while (guess != number);
}

int main()
{
    int R = 50;
    guess_number(R);
    system("pause"); //Prevents console window from automatically exiting
    return 0;
}
