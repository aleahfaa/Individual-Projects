/*077's notes:
find the average of 5 intergers with a precision of 2 decimal places
-uji coba dasar pemograman 2023 (en)*/
//https://www.its.ac.id/informatika/domjudge/public/problems/225/text

#include <stdio.h>

int main(){
    int a,b,c,d,e;
    scanf("%d %d %d %d %d", &a,&b,&c,&d,&e);
    int sum=a+b+c+d+e;
    double avg=(double)sum/5.00;
    /*double avg;
    avg=(a+b+c+d+e)/5.00;*/
    printf("%.2lf",avg);
    return 0;
}