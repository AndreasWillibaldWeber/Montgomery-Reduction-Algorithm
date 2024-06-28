import argparse
from MontgomeryReductionAlgorithm.mmr import MMR
from MontgomeryReductionAlgorithm.srsa import RSA


def setup_argparse():
    parser = argparse.ArgumentParser(prog='MontgomeryReductionAlgorithm')
    parser.add_argument('-v', action='store_true', help='version')
    
    subparsers = parser.add_subparsers(dest="cmd", help='help for commands')

    parser_mme = subparsers.add_parser('mme', help='montgomery modular multiplication')
    parser_mme.add_argument('-m', required=True, type=lambda x: int(x,0), help='message with N-bits')
    parser_mme.add_argument('-e', required=True, type=lambda x: int(x,0), help='public key with E-bits')
    parser_mme.add_argument('-n', required=True, type=lambda x: int(x,0), help='modulus with N-bits')
    parser_mme.add_argument('-k', required=True, type=lambda x: int(x,0), help='k=2^{2N}')

    parser_mmm = subparsers.add_parser('mmm', help='montgomery modular exponentiation')
    parser_mmm.add_argument('-a', required=True, type=lambda x: int(x,0), help='natural number')
    parser_mmm.add_argument('-b', required=True, type=lambda x: int(x,0), help='natural number')
    parser_mmm.add_argument('-n', required=True, type=lambda x: int(x,0), help='modulus with N-bits')

    parser_gcd = subparsers.add_parser('gcd', help='greatest common divisor')
    parser_gcd.add_argument('-p', required=True, type=lambda x: int(x,0), help='natural number')
    parser_gcd.add_argument('-q', required=True, type=lambda x: int(x,0), help='natural number')

    parser_lcm = subparsers.add_parser('lcm', help='least common multiple')
    parser_lcm.add_argument('-p', required=True, type=lambda x: int(x,0), help='natural number')
    parser_lcm.add_argument('-q', required=True, type=lambda x: int(x,0), help='natural number')

    parser_soe = subparsers.add_parser('soe', help='sieve of eratosthenes')
    parser_soe.add_argument('--qmin', default=2, type=lambda x: int(x,0), help='natural number')
    parser_soe.add_argument('--qmax', default=100, type=lambda x: int(x,0), help='natural number')

    parser_n = subparsers.add_parser('n', help='n = p * q where p and q are distinct primes')
    parser_n.add_argument('-p', required=True, type=lambda x: int(x,0), help='prime distinct to q')
    parser_n.add_argument('-q', required=True, type=lambda x: int(x,0), help='prime distinct to p')

    parser_tot = subparsers.add_parser('tot', help="euler's totient function tot(n) = φ(n) = (p - 1) * (q - 1)")
    parser_tot.add_argument('-p', required=True, type=lambda x: int(x,0), help='prime distinct to q')
    parser_tot.add_argument('-q', required=True, type=lambda x: int(x,0), help='prime distinct to p')

    parser_cop = subparsers.add_parser('cop', help='check if p is coprime to q')
    parser_cop.add_argument('-p', required=True, type=lambda x: int(x,0), help='prime number.')
    parser_cop.add_argument('-q', required=True, type=lambda x: int(x,0), help='prime number.')

    parser_e = subparsers.add_parser('e', help='greatest e where 1 < e < tot(n), common choices are the Fermat primes 2, 17, 65537, ...')
    parser_e.add_argument('--totn', required=True, type=lambda x: int(x,0), help="Euler's totient function tot(n) = φ(n) = (p - 1) * (q - 1)")

    parser_chke = subparsers.add_parser('chke', help='check if e is coprime to tot(n) and between 1 and tot(n)')
    parser_chke.add_argument('-e', required=True, type=lambda x: int(x,0), help='greatest e where 1 < e < tot(n), common choices are the Fermat primes 2, 17, 65537, ...')
    parser_chke.add_argument('--totn', required=True, type=lambda x: int(x,0), help="Euler's Totient Function tot(n) = φ(n) = (p - 1) * (q - 1).")

    parser_d = subparsers.add_parser('d', help='modular multiplicative inverse of e (mod tot(n)).')
    parser_d.add_argument('-e', required=True, type=lambda x: int(x,0), help='greatest e where 1 < e < tot(n), common choices are the Fermat primes 2, 17, 65537, ...')
    parser_d.add_argument('-n', required=True, type=lambda x: int(x,0), help='n = p * q where p and q are distinct primes')

    parser_muli = subparsers.add_parser('muli', help='multiplicative inverse')
    parser_muli.add_argument('-e', required=True, type=lambda x: int(x,0), help='greatest e where 1 < e < tot(n), common choices are the Fermat primes 2, 17, 65537, ...')
    parser_muli.add_argument('-n', required=True, type=lambda x: int(x,0), help='n = p * q where p and q are distinct primes.')

    parser_egcd = subparsers.add_parser('egcd', help='extended greatest common divisor.')
    parser_egcd.add_argument('-n', required=True, type=lambda x: int(x,0), help='n = p * q where p and q are distinct primes')
    parser_egcd.add_argument('-e', required=True, type=lambda x: int(x,0), help='greatest e where 1 < e < tot(n), common choices are the Fermat primes 2, 17, 65537, ...')

    parser_encrypt = subparsers.add_parser('encrypt', help='RSA encryption.')
    parser_encrypt.add_argument('-m', required=True, type=lambda x: int(x,0), help='message with N-bits.')
    parser_encrypt.add_argument('-e', required=True, type=lambda x: int(x,0), help='public key with E-bits, greatest e where 1 < e < tot(n), common choices are the Fermat primes 2, 17, 65537, ...')
    parser_encrypt.add_argument('-n', required=True, type=lambda x: int(x,0), help='modulus with N-bits, n = p * q where p and q are distinct primes')

    parser_decrypt = subparsers.add_parser('decrypt', help='RSA decryption.')
    parser_decrypt.add_argument('-c', required=True, type=lambda x: int(x,0), help='ciphertext with N-bits.')
    parser_decrypt.add_argument('-d', required=True, type=lambda x: int(x,0), help='private key with N-bits, modular multiplicative inverse of e (mod tot(n))')
    parser_decrypt.add_argument('-n', required=True, type=lambda x: int(x,0), help='modulus with N-bits, n = p * q where p and q are distinct primes')

    return parser.parse_args()


def run_mmm(a, b, n):
    r = MMR.mmm(a, b, n)
    print(r, hex(r))


def run_mme(m, e, n ,k):
    r = MMR.mme(m, e, n, k)
    print(r, hex(r))


def run_gcd(p, q):
    r = RSA.gcd(p, q)
    print(r, hex(r))


def run_lcm(p, q):
    r = RSA.lcm(p, q)
    print(r, hex(r))


def run_sieve_of_eratosthenes(q_min, q_max):
    rs = RSA.sieve_of_eratosthenes(q_min, q_max)
    for r in rs:
        print(r, hex(r))


def run_n(p, q):
    r = RSA.n(p, q)
    print(r, hex(r))


def run_tot(p, q):
    r = RSA.tot(p, q)
    print(r, hex(r))


def run_is_coprime(p, q):
    r = RSA.is_coprime(p, q)
    print(r, hex(r))


def run_e(tot_n):
    r = RSA.e(tot_n)
    print(r, hex(r))


def run_check_e(e, tot_n):
    r = RSA.check_e(e, tot_n)
    print(r, hex(r))


def run_d(e, n):
    r = RSA.n(e, n)
    print(r, hex(r))


def run_multiplicative_inverse(e, n):
    r = RSA.multiplicative_inverse(e, n)
    print(r, hex(r))


def run_egcd(n, e):
    r = RSA.extened_gcd(n, e)
    print(r, hex(r))


def run_encrypt(m, e, n):
    r = RSA.encrypt(m, e, n)
    print(r, hex(r))


def run_decrypt(c, d, n):
    r = RSA.decrypt(c, d, n)
    print(r, hex(r))


def main():
    args = setup_argparse()
    if args.v:
        print("v0.0.3-alpha")
    if args.cmd == 'mmm':
        run_mmm(args.a, args.b, args.n)
    if args.cmd == 'mme':
        run_mme(args.m,  args.e, args.n, args.k)
    if args.cmd == 'gcd':
        run_gcd(args.p, args.q)
    if args.cmd == 'lcm':
        run_lcm(args.p, args.q)
    if args.cmd == 'soe':
        run_sieve_of_eratosthenes(args.qmin, args.qmax)
    if args.cmd == 'n':
        run_n(args.p, args.q)
    if args.cmd == 'tot':
        run_tot(args.p, args.q)
    if args.cmd == 'cop':
        run_is_coprime(args.p, args.q)
    if args.cmd == 'e':
        run_e(args.totn)
    if args.cmd == 'chke':
        run_check_e(args.e, args.totn)
    if args.cmd == 'd':
        run_d(args.e, args.n)
    if args.cmd == 'muli':
        run_multiplicative_inverse(args.e, args.n)
    if args.cmd == 'egcd':
        run_egcd(args.n, args.e)
    if args.cmd == 'encrypt':
        run_encrypt(args.m, args.e, args.n)
    if args.cmd == 'decrypt':
        run_decrypt(args.c, args.d, args.n)


if __name__ == '__main__':
    main()
