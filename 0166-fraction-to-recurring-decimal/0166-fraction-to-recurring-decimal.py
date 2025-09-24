class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        # Sign
        sign = "-" if (numerator < 0) ^ (denominator < 0) else ""
        n, d = abs(numerator), abs(denominator)

        # Integer part
        integer = n // d
        rem = n % d
        if rem == 0:
            return sign + str(integer)

        # Fractional part via long division
        res = [sign, str(integer), "."]
        seen = {}  # remainder -> index in res where its digit started

        while rem:
            if rem in seen:
                idx = seen[rem]
                res.insert(idx, "(")
                res.append(")")
                break
            seen[rem] = len(res)
            rem *= 10
            res.append(str(rem // d))
            rem %= d

        return "".join(res)
