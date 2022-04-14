#include<stdio.h>

int main(){
    char str[100];
    //gets(str);
    scanf("%[^\n]c",str);
    int i = 0,count_char=0,count_word =1;
    while(str[i]!=NULL){
        count_char++;
        if(str[i]==' ')
            count_word++;
        i++;
    }
    printf("Number of char : %d\nNumber of word : %d",count_char,count_word);
    return 0;
}