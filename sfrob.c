#include <stdio.h>
#include <stdlib.h>

int frobcmp(char const * a, char const * b);
int fcmp(const void* a, const void* b);
void qsort(void *base, size_t nel, size_t width,
       int (*compar)(const void *, const void *));
int memcmp(const void *s1, const void *s2, size_t n);
int frobcmp(char const * a, char const * b)
{
    while ((*a) != ' ' && (*b) != ' ')
    {

        if (((*a)^42) > ((*b)^42))
            return 1;
        else if (((*a)^42) < ((*b)^42))
            return -1;
        else if (((*a) == ' ') && ((*b) != ' '))
            return -1;
        else if (((*a) != ' ') && ((*b) == ' '))
            return 1;
        else
            {
                a++;
                b++;
            }
    }
    //out of while loop means they are equal
    if (((*a) == ' ') && ((*b) != ' '))
        return -1;
    else if (((*a) != ' ') && ((*b) == ' '))
        return 1;
    else
        return 0;
}
int fcmp(const void* a, const void* b)
{
    return frobcmp(*(char**)a, *(char**)b);
}


//If p is a pointer to a character,
//and n is the amount of storage you wish to allocate ,
//then use the statement:
//p = (char*)malloc(n*sizeof(char));

//EOF = end of file
//our input is an obfuscated file

int main(void)
{
    int b = 0;
    //get space for one pointer to array of pointers
    char ** big = (char**)malloc(sizeof(char*));
    //malloc returns a null pointer on failure
    if (big == NULL)
        {
            fprintf(stderr, "%s", "could not allocate space\n");
            exit(1);
        }
    //our input is an obfuscated file
    int c;
    int i = 0; //declare and initialize line index
    int j = 0;
    //while char is not end of file
    if ((c = getchar()) == EOF)
    {
        if (feof(stdin))
        {
            fprintf(stderr, "%s", "getchar did not work .. \n");
            exit(1);
        }
        putchar(' ');
        return 0;
    }

    if (c != ' ')
    {

        big[0] = (char*)malloc(sizeof(char));
        big[0][j] = c;
        j++;

    }
    else if (c == ' ')
    {
        big[0] = (char*)malloc(sizeof(char));
        big[0][j] = c;
        j++;
        i++;
    }

    while((c = getchar())!= EOF )
    {
        if (feof(stdin))
        {
            fprintf(stderr, "%s", "getchar did not work .. \n");
            exit(1);
        }


        if (j == 0) //if first row (pointer already made)
        {
            if (i != 0)
                {
                    big = (char**)realloc(big, sizeof(char *)*(i+1));
                    if (big == NULL)
                    {
                        fprintf(stderr, "%s", "could not allocate space\n");
                        exit(1);
                    }
                }
           //creating pointer
            big[i] = (char*)malloc(sizeof(char));
            if (big[i] == NULL)
            {
                fprintf(stderr, "%s", "could not allocate space\n");
                exit(1);
            }
            big[i][j] = c; //fill space with char
            if (c == ' ')
                {
                    i++;
                    j=0;
                    b = 5;
                }
            else
            {
                j++; //increment word
                b = 0;
            }
            continue;
        }
        //not space; keep adding to row
        //make space for one more char in word
        big[i] = (char*)realloc(big[i], (j+1)*sizeof(char));
        if (big[i] == NULL)
            {
                fprintf(stderr, "%s", "could not allocate space\n");
                exit(1);
            }
        big[i][j] = c; //fill in char
        if (c == ' ')
                {
                    i++;
                    b = 5;
                    j=0;
                }
        else
        {
            j++; //increment word
            b = 0;
        }

    }//end of getchar() while loop

    if (b == 0) //means no space
    {
        if (big[i][j-1] != ' ')
            {
                big[i] = (char*)realloc(big[i], sizeof(char)+(j+1)*sizeof(char));
                if (big[i] == NULL)
                {
                    fprintf(stderr, "%s", "could not allocate space\n");
                    exit(1);
                }
                big[i][j] = ' ';
                i++;
            }
    }
    qsort(big, (size_t)(i), sizeof(char**), fcmp);

    //print

    for (int a = 0; a < i; a++)
    {
        for (int b = 0; ; b++)
        {
            putchar(big[a][b]);

            if (big[a][b] == ' ')
            {
                break;
            }
        }
    }
    //free
    for(int o = 0; o<i; o++)
    {
        free(big[o]);
    }
    free(big);
    return 0;
}
