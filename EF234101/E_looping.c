/*077's notes:
how many times interger k appears
-uji coba dasar pemograman 2023 (en)*/
//https://www.its.ac.id/informatika/domjudge/public/problems/221/text

#include <stdio.h>

int main(){
    int n,m,k;
    int count=0;
    scanf("%d %d", &n,&m);
    //input n intergers a
    int a[n];//string
    for(int i=0;i<n;i++){
        scanf("%d", &a[i]);
    }
    scanf("%d", &k);
    //count how many k appears
    for(int i=0;i<n;i++){
        if(a[i]==k){
            count++;
        }
    }
    printf("%d\n",count);
    return 0;
}