import argparse
from MontgomeryReductionAlgorithm.mmr import MMR
from MontgomeryReductionAlgorithm.srsa import RSA


def setup_argparse():
    parser = argparse.ArgumentParser(prog='MontgomeryReductionAlgorithm')
    parser.add_argument('-v', action='store_true', help='version')
    
    subparsers = parser.add_subparsers(dest="cmd", help='sub help')

    parser_mme = subparsers.add_parser('mme', help='mme help')
    parser_mme.add_argument('-m', required=True, type=lambda x: int(x,0), help='m help')
    parser_mme.add_argument('-e', required=True, type=lambda x: int(x,0), help='e help')
    parser_mme.add_argument('-n', required=True, type=lambda x: int(x,0), help='n help')
    parser_mme.add_argument('-k', required=True, type=lambda x: int(x,0), help='k help')

    parser_mmm = subparsers.add_parser('mmm', help='mmm help')
    parser_mmm.add_argument('-a', required=True, type=lambda x: int(x,0), help='a help')
    parser_mmm.add_argument('-b', required=True, type=lambda x: int(x,0), help='b help')
    parser_mmm.add_argument('-n', required=True, type=lambda x: int(x,0), help='n help')

    #parser_rsa = subparsers.add_parser('rsa', help='rsa help')
    #parser_rsa.add_argument('-n', choices='XYZ', help='baz help')

    #parser_tvec = subparsers.add_parser('tvec', help='tvec help')
    #parser_tvec.add_argument('--baz', choices='XYZ', help='baz help')

    return parser.parse_args()


def run_mmm(a, b, n):
    r = MMR.mmm(a, b, n)
    print(r, hex(r))


def run_mme(m, e, n ,k):
    r = MMR.mme(m, e, n, k)
    print(r, hex(r))


def main():
    args = setup_argparse()
    if args.v:
        print("v0.0.2-alpha")
    if args.cmd == 'mmm':
        run_mmm(args.a, args.b, args.n)
    if args.cmd == 'mme':
        run_mme(args.m,  args.e, args.n, args.k)


if __name__ == '__main__':
    main()
