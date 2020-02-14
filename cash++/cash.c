#include <cs50.h>
#include <stdio.h>
 #include <math.h>

    
    
  int count(void){
int counter=0;
    float cash=0;
    int quarter = 25;
    int dime = 10;
    int nickel = 5;
    int penny = 1;
  
    do{
        cash=get_float("Change owed: ");
    }
    
      while(cash<0);
    
    int cents = round(cash * 100);
    while(cents!=0)
    {
        if(cents/quarter!=0)
        {
          cents=cents-quarter;
              counter++;
        }
        else if(cents/dime!=0)
        {
          cents=cents-dime;
              counter++;
        }
        else if(cents/nickel!=0)
        {
          cents=cents-nickel;
              counter++;
        }
        else
        {
          cents=cents-penny;
              counter++;  
        }
    }
  
   return counter;
  }
int main(void)
{
        printf("%i\n", count());

}
