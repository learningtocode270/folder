#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n;

// Ask question with a limited range of answers
// If input is less than one or greater than 8, do not advance
    do
    {
        {
            n = get_int("How many rows? ");
        }
    }
    while (n < 1 || n > 8);

// For loop that runs n times
    for (int i = 0; i < n; i++)
    {
        for (int x = i + 1; x < n; x++)
        {
            printf(" ");
        }

        for (int j = n + 1 - i; j <= n + 1; j++)
        {
            printf("#");
        }


        printf("\n");
    }
}
