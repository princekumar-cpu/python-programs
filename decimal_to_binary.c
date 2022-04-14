#include<stdio.h>

int main(){
    char str[100];
    int x,temp,rem,count = 0;
    int bin[10];
    scanf("%d",&x);
    temp = x;
    for(int i = 0; temp > 0; i++){
        bin[i] = temp%2;
        count++;
        temp = temp/2;
    }
    for(int j=count - 1; j>=0; j--){
        printf("%d",bin[j]);
    }
    return 0;
}