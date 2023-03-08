class Number:

    def base(self, n1, b1, b2):
        ans = n1
        if b1 != 10:
            s = str(n1)
            c = len(s) - 1
            ans = 0
            for i in s:
                ans += int(i) * b1 ** c
                c -= 1
        if b2 != 10:
            n2 = ans
            ans = ''
            while n2 > 0:
                ans = str(n2 % b2) + ans
                n2 //= b2
        return ans
        
    def gcd(self, n1, n2):
        while n2 != 0:
            n1, n2 = n2, n1 % n2
        return n1 + n2

    def lcm(self, n1, n2):
        return int(n1 * n2 / self.gcd(n1, n2))

    def dividers(self, n1):
        lis = []
        for i in range(1, int(n1 ** 0.5) + 1):
            if n1 % i == 0:
                lis.append(i)
                if n1 / i != i:
                    lis.append(n1 // i)
        return sorted(lis)
