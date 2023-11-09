/*077's notes:
count the difference variable between input a and input b
use dynamic programming (dp) to efficiently calculate the minimum number of changes
npc23_ontherun (cpp version)*/
//npc.schematics-its.com/contests/warmup-npc-senior-2023/problems/A

#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <algorithm>
#define forloop1 for(int i=0;i<=m;i++)
#define forloop2 for(int j=0;j<=n;j++)
#define elif else if
using namespace std;

int changes(string s1,string s2) {
    int m=s1.length();
    int n=s2.length();
    //create matrix to store min number of changes
    vector<vector<int>>dp(m+1,vector<int>(n+1,0));
    forloop1{
        dp[i][0]=i;
    }
    forloop2{
        dp[0][j]=j;
    }
    forloop1{
        forloop2{
            if(i==0){
                dp[i][j]=j;
            }elif(j==0){
                dp[i][j]=i;
            }elif(s1[i-1]==s2[j-1]){
                dp[i][j]=dp[i-1][j-1];
            }else{
                dp[i][j]=1+min({dp[i-1][j],dp[i][j-1],dp[i-1][j-1]});
            }
        }
    }
    return dp[m][n];
}

int main() {
    string s1,s2;
    getline(cin,s1);
    getline(cin,s2);
    int res=changes(s1,s2);
    cout<<res<<endl;
    return 0;
}
