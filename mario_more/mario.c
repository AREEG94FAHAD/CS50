#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //enter number of staris
    int n=get_int("Height: ");
    //condition of input
    while(n>8||n<1)
    {
      n=get_int("Height: ");  
    }
    
    //for to rep
for(int i=0;i<n;i++)
{
    //for for space
    for(int w=n-1;w>i;w--)
    {
     printf(" ");   
    }
    for(int o=0;o<=i;o++)
    {
        printf("#");
        
    }
    
      for(int o=0;o<=i;o++)
    {
          if(o==0){
            printf("  ");
        }
        printf("#");
    } 
       printf("\n");
    
}
   
    
}
