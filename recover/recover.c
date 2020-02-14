#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }
FILE *file = fopen(argv[1], "r");
unsigned char buffer[512];

FILE *image=NULL;
int count=0;
char name[8];


        while(fread(buffer,512, 1, file)==1)
        {
            if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && buffer[3] >= 0xe0 && buffer[3] <= 0xef)
            {
                if(image)
                {
                   fclose(image);
                }
                 sprintf(name, "%03d.jpg",count++);

                 image=fopen(name,"w");
            }

            if(image)
            {
                fwrite(buffer,512,1,image);

            }

            }

            fclose(image);

            fclose(file);


return 0;
        }


