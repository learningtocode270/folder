// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h>
#include <stdlib.h>
#include <stdio.h>
#include <cs50.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Declare variables
unsigned int word_count;
unsigned int hash_value;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    //Hash the word to get hash value
    hash_value = hash(word);

    //point to first node
    node *cursor = table[hash_value];

    //go through linked list
    while (cursor != 0)
    {
        if (strcasecmp(word, cursor-> word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    unsigned long total = 0;

    for (int i = 0; i < strlen(word); i++)
    {
        total += tolower(word[i]);
    }
    return total % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open dictionary.h
    FILE *file =fopen(dictionary, "r");
    if (file == NULL)
    {
        printf("File cannot be oppened");
        return false;
    }

    // Read strings
    char word[LENGTH + 1];
   while (fscanf(file, "%s", word) != EOF)
   {
    // New memory for each node
    node *n = malloc(sizeof(node));
    //return if there is no memory available
    if (n == NULL)
    {
        return 1;
    }

    strcpy(n->word, word);

    //get hash value
    hash_value = hash(word);
    //set pointer to beginning of linked list
    n->next = table[hash_value];
    table[hash_value] = n;
    word_count++;
   }
   fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // Return size of dictionary
    if (word_count > 0)
    {
        return word_count;
    }
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    //free each node in the buckets
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];

        while (cursor != NULL)
        {
            node *tmp = cursor;
            cursor = cursor-> next;
            free(tmp);
        }
    }
    return true;
}
