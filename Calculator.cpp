/*077's notes:
just a simple calculator made by me :)
when i was in middle school, i alr made one using html
so this is the cpp version
calculator (cpp version)*/

#include <bits/stdc++.h>
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    //declare variables to store user inputs and result
    double n1,n2,res;
    char op;
    //prompt user for input
    cout<<"welcome to calculator!";
    cout<<"notes: + means plus, - means minus, * means multiple by, / means divided by, sqrt means square root, p means power";
    cout<<"enter an operator: ";
    cin>>op;
    //perform calculation based on the operator
    if(op=='sqrt'||op=='p'){
        cout<<"enter a number: ";
        cin>>n1;
    }
    if(op=='sqrt'){
        res=sqrt(n1);
        cout<<"result: "<<res<<endl;
    }
    switch(op){
        case '+':
            res=n1+n2;
            break;
        case '-':
            res=n1-n2;
            break;
        case '*':
            res=n1*n2;
            break;
        case '/':
            if(n2!=0){
                res=n1/n2;
            } else{
                cout<<"error"<<endl;
                return 1;//exit with an error code
            }
            break;
        default:
            cout<<"invalid operator"<<endl;
            return 1;//exit with an error code
    }
    //display the result
    cout<<"result: "<<res<<endl;
    return 0; //exit successfully
}
