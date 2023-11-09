/*077's notes:
reverse the string(i.e. abc to cba)
-uji coba dasar pemograman 2023 (en)*/
//https://www.its.ac.id/informatika/domjudge/public/problems/223/text

#include <stdio.h>
#include <string.h>

int main(){
    char s[101];
    scanf("%s",s);
    int len=strlen(s);
    for(int i=0;i<len/2;i++){
        char temp=s[i];
        s[i]=s[len-i-1];
        s[len-i-1]=temp;
    }
    printf("%s\n",s);
    return 0;
}

/*void reverse(char s[],int len){
    int start=0,end=len-1,temp;
    while (start<end){
        temp=s[start];
        s[start]=s[end];
        s[end]=temp;
        start++;
        end--;
    }
}

int main(){
    char s[101];
    scanf("%s",s);
    //reverse the string
    int len=strlen(s);
    reverse(s,len);
    printf("%s\n",s);
    return 0;
}*/
