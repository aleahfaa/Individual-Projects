/*077's notes:
print all the even numbers from start to n in a single line
-uji coba dasar pemograman 2023 (en)*/
//https://www.its.ac.id/informatika/domjudge/public/problems/222/text

#include <stdio.h>

int main(){
    int n;
    scanf("%d",&n);
    //print even numbers from start to n
    for(int i=2;i<=n;i+=2){
        if(i%2==0){
            printf("%d",i);
        }
        if(i<n){//if i is not the last even number
            printf(" ");//then print a space
        }
    }
    return 0;
}