#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

/*Assumption:
	1. All data is in decimal.
*/



//name->variable name
//accumator/A->acc
//B->regB
//C->regC
//D->regD
//E->regE
//H->regH
//L->regL
//M->mem (mem=memory[regH*1000+regL])



//flag->variable
//Carry flag->flagC
//Zero flag->flagZ



//-------------------------------CONVERSION---------------------------------//
int hex_decimal(char *hexVal)//hex->decimal
{
	int len = strlen(hexVal); 
      
    // Initializing base value to 1, i.e 16^0 
    int base = 1; 
      
    int dec_val = 0; 
      
    // Extracting characters as digits from last character 
    for (int i=len-1; i>=0; i--) 
    {    
        // if character lies in '0'-'9', converting  
        // it to integral 0-9 by subtracting 48 from 
        // ASCII value. 
        if (hexVal[i]>='0' && hexVal[i]<='9') 
        { 
            dec_val += (hexVal[i] - 48)*base; 
                  
            // incrementing base by power 
            base = base * 16; 
        } 
  
        // if character lies in 'A'-'F' , converting  
        // it to integral 10 - 15 by subtracting 55  
        // from ASCII value 
        else if (hexVal[i]>='A' && hexVal[i]<='F') 
        { 
            dec_val += (hexVal[i] - 55)*base; 
          
            // incrementing base by power 
            base = base*16; 
        } 
    } 
      
    return dec_val; 
}
char * decimal_hex(int decimalNumber)//decimal->hex
{
	char *ch="00000";
	int quotient = decimalNumber;
	int temp;
	int i=0;
    while(quotient!=0)
    {
    	if(i>4)
    		break;
    	temp = quotient % 16;

      //To convert integer into character
    	if( temp < 10)
    		temp =temp + 48;
    	else
    		temp = temp + 55;

    	ch[i++]= temp;
    	quotient = quotient / 16;
    }
    return ch;
}



//---------------------------------------------------------------------------------------//
//---------------------------------------------------------------------------------------//
void function(char *ch)
{
//-------------------------------ADD-----------------------------//
	if(strcmp(ch, "87")==0)//add A
		acc+=acc;
	else if(strcmp(ch, "80")==0)//add B
		acc+=regB;
	else if(strcmp(ch, "81")==0)//add C
		acc+=regC;
	else if(strcmp(ch, "82")==0)//add D
		acc+=regD;
	else if(strcmp(ch, "83")==0)//add E
		acc+=regE;
	else if(strcmp(ch, "84")==0)//add H
		acc+=regH;
	else if(strcmp(ch, "85")==0)//add L
		acc+=regL;
	else if(strcmp(ch, "88")==0)//add M
		acc+=mem;
//----------------------------CMP--------------------------------//
	else if(strcmp(ch, "BF")==0)//CMP A
		flagZ=1;
	else if(strcmp(ch, "B8")==0)//CMP B
	{	
		if(acc>regB)
		{
			flagC=0;
			flagZ=0;
		}
		else if(acc<regB)
		{
			flagC=1;
		}
		else
			flagZ=1;
	}
	else if(strcmp(ch, "B9")==0)//CMP C
	{	
		if(acc>regC)
		{
			flagC=0;
			flagZ=0;
		}
		else if(acc<regC)
		{
			flagC=1;
		}
		else
			flagZ=1;
	}
	else if(strcmp(ch, "BA")==0)//CMP D
	{	
		if(acc>regD)
		{
			flagC=0;
			flagZ=0;
		}
		else if(acc<regD)
		{
			flagC=1;
		}
		else
			flagZ=1;
	}
	else if(strcmp(ch, "BB")==0)//CMP E
	{	
		if(acc>regE)
		{
			flagC=0;
			flagZ=0;
		}
		else if(acc<regE)
		{
			flagC=1;
		}
		else
			flagZ=1;
	}
	else if(strcmp(ch, "BC")==0)//CMP H
	{	
		if(acc>regH)
		{
			flagC=0;
			flagZ=0;
		}
		else if(acc<regH)
		{
			flagC=1;
		}
		else
			flagZ=1;
	}
	else if(strcmp(ch, "BD")==0)//CMP L
	{	
		if(acc>regL)
		{
			flagC=0;
			flagZ=0;
		}
		else if(acc<regL)
		{
			flagC=1;
		}
		else
			flagZ=1;
	}
	else if(strcmp(ch, "BE")==0)//CMP M
	{	
		if(acc>mem)
		{
			flagC=0;
			flagZ=0;
		}
		else if(acc<mem)
		{
			flagC=1;
		}
		else
			flagZ=1;
	}
//------------------------------------------------------//





}