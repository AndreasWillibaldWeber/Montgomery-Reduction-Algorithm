# Montgomery-Reduction-Algorithm
Montgomery Reduction Algorithm python package to verify and study hardware implementations.

## Montgomery Modular Reduction

RSA is defined for

 - encryption as $c = m^e \mod n$

 - decryption as $m = c^d \mod n$

where:

 - $m$: message with N-bits

 - $c$: ciphertext with N-bits

 - $n$: modulus with N-bits

 - $e$: public key with E-bits

 - $d$: private key with N-bits

## Pseudocode of the Montgomery Modular Multiplication

$\mathrm{MMM}(a,b,n) = a * b * 2^{-\mathrm{N}}$

**Hint**: $k$ constant is removed by $2^{-\mathrm{N}}$

```
s(0) = 0
for i = 0 to N-1
  q(i)   = ( s(i) + a(i) x b ) mod 2
  s(i+1) = ( s(i) + q(i) x n + a(i) x b ) / 2
end
if ( s(N) ≥ n )
  d = s(N) – n
else
  d = s(N)
end
MMM(a, b, n) = d
```

## Pseudocode of the Montgomery Modular Exponentiation!

$\mathrm{MME}(m,e,n) = c = m^e \mod n $

$k = 2^{2\mathrm{N}} \mod n$

```
m(0) = MMM(m, k, n)
r(0) = MMM(1, k, n)
for i = 0 to E-1
  if ( e(i) == 1 )
    r(i+1) = MMM(r(i), m(i), n)
  else
    r(i+1) = r(i)
  end
  m(i+1) = MMM(m(i), m(i), n)
end
c = MMM(r(E), 1, n)
```

# References

[1] Christof Paar, Jan Pelzl. Understanding Cryptography: A Textbook for Students and Practitioners, Springer, 2010.

[2] Christof Paar. Implementation of Cryptographic Schemes 1, Lecture Notes, 2015.

[3] https://www.emsec.ruhr-uni-bochum.de/media/attachments/files/2015/09/IKV-1_2015-04-28.pdf.

[4] Elif Bilge Kavun. Security Processor Design - Lecture and Exercise Slides, 2024.
