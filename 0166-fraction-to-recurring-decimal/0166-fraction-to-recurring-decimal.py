class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        ans=[]
        if numerator < 0 and denominator > 0 or numerator > 0 and denominator < 0:
            ans.append('-')
        n,d = abs(numerator),abs(denominator)
        ans.append(str(n//d))
        remainder = n % d
        if remainder==0:
            return ''.join(ans)
        ans.append('.')
        dict1={}
        while remainder != 0 and remainder not in dict1:
            dict1[remainder]=len(ans)
            remainder *= 10
            ans += str(remainder // d)
            remainder %= d
        if remainder in dict1:
            ans.insert(dict1[remainder],'(')
            ans.append(')')
            return ''.join(ans)

        return ''.join(ans)