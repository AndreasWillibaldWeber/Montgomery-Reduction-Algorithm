
class RSA():


    @staticmethod
    def gcd(p, q):
        while q != 0:
            p, q = q, p % q
        return p
    

    @staticmethod
    def lcm(p, q):
        return (p * q) // RSA.gcd(p, q)


    @staticmethod
    def sieve_of_eratosthenes(q_min=2, q_max=100):
        z = {}
        for q in range(q_min, q_max + 1):
            if q not in z:
                yield q
                z[q * q] = [q]
                continue
            for p in z[q]:
                z.setdefault(p + q, []).append(p)
            del z[q]


    @staticmethod
    def n(p, q):
        return p * q


    @staticmethod
    def tot(p, q):
        return (p - 1) * (q - 1)
    
    
    @staticmethod
    def is_coprime(p, q):
        return RSA.gcd(p, q) == 1
    

    @staticmethod
    def e(tot_n):
        for p_fermat in [18446744073709551617, 4294967297, 65537, 257, 17, 5, 3]:
            if RSA.check_e(p_fermat, tot_n):
                return p_fermat
        raise Exception("e must be coprime to tot(n) and between 1 and tot(n)")


    @staticmethod
    def check_e(e, tot_n):
        return RSA.is_coprime(e, tot_n) and 1 < e < tot_n


    @staticmethod
    def d(e, tot_n):
        return RSA.multiplicative_inverse(e, tot_n)


    @staticmethod
    def multiplicative_inverse(e, tot_n):
        gcd, _, y = RSA.extened_gcd(tot_n, e)
        if(gcd == 1):
            return y % tot_n
        raise Exception("gcd has no multiplicative inverse")


    @staticmethod
    def extened_gcd(tot_n, e):
        q, r, a, c, y, b, x, z = 0, 1, 1, 1, 1, 0, 0, 0
        while r > 0:
            q = tot_n // e
            r, c, z = tot_n - q * e, a - q * b, x - q * y
            if(r > 0):
                tot_n, e, a, b, x, y = e, r, b, c, y, z
        return abs(e), b, y


    @staticmethod
    def encrypt(m, e, n):
        if not 1 < m < n:
            raise Exception("n must greater than m and m must be greater than 1")
        return (m ** e) % n


    @staticmethod
    def decrypt(c, d, n):
        if not 1 < c < n:
            raise Exception("n must greater than c and c must be greater than 1")
        return (c ** d) % n
