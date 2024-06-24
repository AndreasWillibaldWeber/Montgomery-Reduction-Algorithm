import unittest

from mmr import MMR
from srsa import RSA


class TestMMR(unittest.TestCase):


    def setUp(self) -> None:
        MMR.LOG_MMM = True
        MMR.LOG_MME = True
        MMR.N = 32
        return super().setUp()


    def test_mmm_vec_1(self):
        a = 0x00112233
        b = 0x44556677
        n = 0x93849ca7
        expected = 0x6551c2cd

        result = MMR.mmm(a, b, n)
        print("Result:", hex(result), hex(expected), result == expected)
        self.assertEqual(expected, result)


    def test_mmm_vec_2(self):
        a = 0x01234567
        b = 0x89abcdef
        n = 0x93849ca7
        expected = 0x93817349

        result = MMR.mmm(a, b, n)
        print("Result:", hex(result), hex(expected), result == expected)
        self.assertEqual(expected, result)


    def test_mme_vec_1(self):
        m = 0x00112233
        e = 0x44556677
        n = 0x93849ca7
        k = 0x8c8d9129
        expected = 0x2490d130

        result = MMR.mme(m, e, n, k)
        print("Result:", hex(result), hex(expected), result == expected)
        self.assertEqual(expected, result)


    def test_mme_vec_2(self):
        m = 0x01234567
        e = 0x89abcdef
        n = 0x93849ca7
        k = 0x8c8d9129
        expected = 0x31a9137c

        result = MMR.mme(m, e, n, k)
        print("Result:", hex(result), hex(expected), result == expected)
        self.assertEqual(expected, result)



class TestRSA(unittest.TestCase):


    def setUp(self) -> None:
        return super().setUp()


    def test_gcd_1(self):
        p = 3
        q = 5
        expected = 1

        result = RSA.gcd(p, q)
        print("Result:", result, expected, result == expected)
        self.assertEqual(expected, result) 


    def test_gcd_2(self):
        p = 9
        q = 15
        expected = 3

        result = RSA.gcd(p, q)
        print("Result:", result, expected, result == expected)
        self.assertEqual(expected, result)       


    def test_lcm_1(self):
        p = 12
        q = 15
        expected = 60

        result = RSA.lcm(p, q)
        print("Result:", result, expected, result == expected)
        self.assertEqual(expected, result)  


    def test_lcm_2(self):
        p = 3
        q = 5
        expected = 15

        result = RSA.lcm(p, q)
        print("Result:", result, expected, result == expected)
        self.assertEqual(expected, result)

    
    def test_sieve_of_eratosthenes_1(self):
        q_min = 2
        q_max = 21
        expected = [2, 3, 5, 7, 11, 13, 17, 19]

        result = list(RSA.sieve_of_eratosthenes(q_min, q_max))
        print("Result:", result, expected, sum(result) == sum(expected))
        self.assertEqual(sum(expected), sum(list(result)))  


    def test_sieve_of_eratosthenes_2(self):
        q_min = 6
        q_max = 42
        expected = [
            6, 7, 8, 9, 10, 11, 12, 13, 
            14, 15, 16, 17, 18, 19, 20, 
            21, 22, 23, 24, 25, 26, 27, 
            28, 29, 30, 31, 32, 33, 34, 
            35, 37, 38, 39, 40, 41
        ]

        result = list(RSA.sieve_of_eratosthenes(q_min, q_max))
        print("Result:", result, expected, sum(result) == sum(expected))
        self.assertEqual(sum(expected), sum(list(result)))  


    def test_n_1(self):
        p = 3
        q = 5
        expected = 15

        result = RSA.n(p, q)
        print("Result:", result, expected, result == expected)
        self.assertEqual(expected, result)


    def test_n_2(self):
        p = 7
        q = 11
        expected = 77

        result = RSA.n(p, q)
        print("Result:", result, expected, result == expected)
        self.assertEqual(expected, result)


    def test_tot_1(self):
        p = 3
        q = 5
        expected = 8

        result = RSA.tot(p, q)
        print("Result:", result, expected, result == expected)
        self.assertEqual(expected, result)


    def test_tot_2(self):
        p = 7
        q = 11
        expected = 60

        result = RSA.tot(p, q)
        print("Result:", result, expected, result == expected)
        self.assertEqual(expected, result)


    def test_is_coprime_1(self):
        p = 3
        q = 21
        expected = False

        result = RSA.is_coprime(p, q)
        print("Result:", result, expected, result == expected)
        self.assertEqual(expected, result)


    def test_is_coprime_2(self):
        p = 7
        q = 11
        expected = True

        result = RSA.is_coprime(p, q)
        print("Result:", result, expected, result == expected)
        self.assertEqual(expected, result)


    def test_e_1(self):
        tot = 7
        expected = 3

        result = RSA.e(tot)
        print("Result:", result, expected, result == expected)
        self.assertEqual(expected, result)


    def test_e_1(self):
        tot = 4294967298
        expected = 4294967297

        result = RSA.e(tot)
        print("Result:", result, expected, result == expected)
        self.assertEqual(expected, result)


    def test_check_e_1(self):
        e = 3
        tot = 21
        expected = False

        result = RSA.check_e(e, tot)
        print("Result:", result, expected, result == expected)
        self.assertEqual(expected, result)

    
    def test_check_e_2(self):
        e = 7
        tot = 11
        expected = True

        result = RSA.check_e(e, tot)
        print("Result:", result, expected, result == expected)
        self.assertEqual(expected, result)


    def test_d_1(self):
        e = 65537
        n = 21
        expected = 5

        result = RSA.d(e, n)
        print("Result:", result, expected, result == expected)
        self.assertEqual(expected, result)

    
    def test_d_2(self):
        e = 257
        n = 21
        expected = 17

        result = RSA.d(e, n)
        print("Result:", result, expected, result == expected)
        self.assertEqual(expected, result)


    def test_encrypt_decrypt_1(self):
        m = 18
        e = 257
        n = 21
        d = 17

        c = RSA.encrypt(m, e, n)
        print(c)
        result = RSA.decrypt(c, d, n)
        print("Result:", result, m, result == m)
        self.assertEqual(m, result)


    def test_encrypt_decrypt_2(self):
        m = 76
        e = 65537
        n = 77 
        d = 23

        c = RSA.encrypt(m, e, n)
        print(c)
        result = RSA.decrypt(c, d, n)
        print("Result:", result, m, result == m)
        self.assertEqual(m, result)



if __name__ == '__main__':
    unittest.main()