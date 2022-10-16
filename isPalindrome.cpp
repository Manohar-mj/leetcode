class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0)
            return false;
        int res=0;
        int temp=x;
        while(temp !=0){
            int ld=temp%10;
            res=res*10+ld;
            temp=temp/10;
        }
        return (res==x);
    }
};
