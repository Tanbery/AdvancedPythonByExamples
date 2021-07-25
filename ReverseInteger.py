class Solution:
    def reverse(self, x):
        sign= 1 if x >= 0 else -1
        
        dec=1 
        orgTmp=0
        newNum=0
        revNum= 0.0
        while True:
            remain = x % (10**dec)
            orgTmp = (remain - orgTmp) 
            newNum= newNum + orgTmp 
            revNum= revNum + ((orgTmp //(10**(dec-1)) ) / (10**dec)) 
            if remain == x: 
                break
            dec = dec + 1
        retNum = int(revNum*(10**dec)*sign) 
        return 0 if retNum > (2)**31 else retNum

sol= Solution()
print(sol.reverse(123))