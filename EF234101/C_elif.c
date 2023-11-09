/*077's notes:
else if grades
0 − 40: E
41 − 55: D
56 − 60: C
61 − 65: BC
66 − 75: B
76 − 85: AB
86 − 100: A
-uji coba dasar pemograman 2023 (en)*/
//https://www.its.ac.id/informatika/domjudge/public/problems/224/text

#include <stdio.h>
#define elif else if

int main(){
    int x;
    scanf("%d",&x);
    //elif
    if(x>=0&&x<=40){
        printf("E\n");
    }elif(x>=41&&x<=55){
        printf("D\n");
    }elif(x>=56&&x<=60){
        printf("C\n");
    }elif(x>=61&&x<=65){
        printf("BC\n");
    }elif(x>=66&&x<=75){
        printf("B\n");
    }elif(x>=76&&x<=85){
        printf("AB\n");
    }elif(x>=86&&x<=100){
        printf("A\n");
    }
    return 0;
}