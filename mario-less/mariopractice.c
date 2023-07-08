#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n;

// Ask question with a limited range of answers
    do
    {
        {
            n = get_int("How many rows? ");
        }
    }
    while (n < 1 || n > 8);

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
