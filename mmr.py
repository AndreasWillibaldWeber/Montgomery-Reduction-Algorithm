import logging



class MMR():


    N = 32

    logging.basicConfig(
        format='%(message)s',
        level=logging.DEBUG, 
        filename="logfile", 
        filemode="w"
    )

    LOG_MMM = False
    LOG_MME = False

    @staticmethod
    def _hex_to_binary_array(hex):
        arr = [0 for _ in range(0, MMR.N)]
        for i, b in enumerate(reversed([int(b) for b in str(bin(int(hex)))[2:]])):
            arr[i] = b
        return arr
    

    @staticmethod
    def mmm(a, b, n):
        s, q = {}, {}
        s[0] = 0
        a, b, n = MMR._hex_to_binary_array(a), int(b), int(n)
        for i in range(0, MMR.N):
            q[i] = ( s[i] + a[i] * b ) % 2
            s[i+1] = ( s[i] + q[i] * n + a[i] * b) // 2
        if MMR.LOG_MMM:
            MMR._log("mmm", "q", [*q.values()])
            MMR._log("mmm", "s", [*s.values()])
        return s[MMR.N] - n if s[MMR.N] >= n else s[MMR.N]


    @staticmethod
    def mme(m, e, n, k):
        m_start = m
        m, r = {}, {}
        m[0] = MMR.mmm(m_start, k, n)
        r[0] = MMR.mmm(1, k, n)
        e = MMR._hex_to_binary_array(e)
        for i in range(0, MMR.N):
            r[i+1] = MMR.mmm(r[i], m[i], n) if e[i] == 1 else r[i]
            m[i+1] = MMR.mmm(m[i], m[i], n)
        if MMR.LOG_MME:
            MMR._log("mme", "m", [*m.values()])
            MMR._log("mme", "r", [*r.values()])
        return MMR.mmm(r[MMR.N], 1, n)


    @staticmethod
    def _log(f, v, logs):
        for i, l in enumerate(logs):
            logging.info("Func: %s, Var: %s, Iter: %i, Val: %s", f, v, i, str(hex(l)))



