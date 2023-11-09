/*077's notes:
res=the total of the digits (in a digit)
read the test cases,
process each test case,
print the result of summing the digits until a single-digit is obtained
npc23_menjadisatu (cpp version)*/
//npc.schematics-its.com/contests/warmup-npc-senior-2023/problems/B

#include <bits/stdc++.h>
#include <iostream>
#include <string>
using namespace std;

//function to sum the digits of a number until a single-digit result is obtained
int tot(int x) {
    while(x>=10) {
        int sum=0;
        while(x>0){
            sum+=x%10;//add last digit to sum
            x/=10;//remove last digit
        }
        x=sum;//set xnto the sum of digits
    }
    return x;//return single-digit result
}

int main() {
    int t;
    cin>>t;//testcase

    for(int i=0;i<t;i++){
        int n;
        cin>>n;//number

        int res=tot(n);//get the sum of digits
        cout<<res<<endl;
    }

    return 0;
}
