#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

double count_letters(string text);
double count_words(string text);
double count_sentences(string text);
void round_grade (int grade_level);

int main(void)
{
    string text = get_string("Text: ");
    double letters = count_letters(text);
    double words = count_words(text);
    double sentences = count_sentences(text);

    double L =  letters / words * 100;
    double S = sentences / words * 100;
    double index = 0.0588 * L - 0.296 * S - 15.8;

    int grade_level = round(index);

    round_grade(grade_level);
}


double count_letters(string text)
{
    int letters = 0;

    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (isalpha(text[i]))
        {
            letters += 1;
        }
    }
    return letters;
}


double count_words(string text)
{
    int words = 1;

    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (isspace(text[i]))
        {
            words += 1;
        }
    }
    return words;
}


double count_sentences(string text)
{
    int sentences = 0;

    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (text[i] == '.')
        {
            sentences += 1;
        }
        if (text[i] == '!')
        {
            sentences += 1;
        }
        if (text[i] == '?')
        {
            sentences += 1;
        }
    }
    return sentences;
}


void round_grade (int grade_level)
{
    if (grade_level < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade_level > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grade_level);
    }
}

