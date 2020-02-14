// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

// Represents number of buckets in a hash table
#define N 26

// Represents a node in a hash table

int count=0;
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Represents a hash table
node *hashtable[N];

// Hashes word to a number between 0 and 25, inclusive, based on its first letter
unsigned int hash(const char *word)
{
    return tolower(word[0]) - 'a';
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Initialize hash table
    for (int i = 0; i < N; i++)
    {
        hashtable[i] = NULL;
    }

    // Open dictionary
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        unload();
        return false;
    }

    // Buffer for a word
    char word[LENGTH + 1];
    int wordsnumber=0;
    // Insert words into hash table
    while (fscanf(file, "%s", word) != EOF)
    {
        count++;
    int  x = hash (word);

      node *newnode=malloc(sizeof(node));
      strcpy(newnode->word, word);

     if(hashtable[x] == NULL)
     {
        hashtable[x]=newnode;
        newnode->next=NULL;
     }
     else
     {
        newnode->next = hashtable[x];
        hashtable[x]=newnode;

     }

    }

    // Close dictionary

    fclose(file);

    // Indicate success
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{

    return count;
}

// Returns true if word is in dictionary else false
bool check( char *word)
{


    for(int i = 0; i < strlen(word); i++)
    {
         word[i] = tolower(word[i]);
    }

    int c=hash(word);

    if (hashtable[c] == NULL)
    {
        return false;


    }
       node *location = hashtable[c];

       while(location!=NULL)
       {
            if (strcmp(word, location->word) == 0)
            {
                return true;
            }

        location=location->next;
       }
    return false;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
     for (int i = 0; i < N; i++)
    {


        if(hashtable[i]==NULL)
        {

            i++;
        }
        else{

      while(hashtable[i]!=NULL)
        {
         node *a=hashtable[i];
         hashtable[i]=a->next;
         free(a);
        }

        }

        }
    return true;
}
