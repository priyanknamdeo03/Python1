#include <iostream>
using namespace std;

int main() {
    
    int i,j,v=0;
    cout<<"Enter Number ";
    cin>>v;
    for(i=1;i<v;i++)
    {
        for(j=i;j<v;j++)
        {
            cout<<j<<" ";
        }
        // for (int k=i;k<=v;k++)
        // {
        //     cout<<" ";
        // }
        cout<<endl;
        cout<<"  ";
    }

    return 0;
}