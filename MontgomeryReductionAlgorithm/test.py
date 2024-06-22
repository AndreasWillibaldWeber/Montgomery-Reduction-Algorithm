import unittest

from mmr import MMR


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



if __name__ == '__main__':
    unittest.main()