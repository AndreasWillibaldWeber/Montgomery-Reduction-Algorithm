
[![spec](https://github.com/AndreasWillibaldWeber/Montgomery-Reduction-Algorithm/actions/workflows/main.yml/badge.svg)](https://github.com/AndreasWillibaldWeber/Montgomery-Reduction-Algorithm/actions/workflows/main.yml)

# Montgomery-Reduction-Algorithm
Montgomery Reduction Algorithm python package to verify and study hardware implementations.

## Setup, Build and Installation

- Setup: `pip install -r requirements.txt`
- Build: `python -m build`
- Installation: `pip install <path-to-wheel>`

## Config MMR Package

- `MMR.N`: Default value is `32`
- `MMR.MME_LOG`: Default is `False`. Set to `True` to log the mme m and r values for each calculation step.
- `MMR.MMM_LOG`: Default is `False`. Set to `True` to log the mmm q and s values for each calculation step.

## CLI

The CLI-script is currently placed in the `main.py` file.

### MMR

* **mmm** -a *{int}*, -b *{int}*, -n *{int}* &emsp; Montgomery Modular Multiplication
* **mme** -m *{int}*, -e *{int}*, -n *{int}*, -k *{int}* &emsp; Montgomery Modular Exponentiation

##### Example 1:

Call Montgomery Modular Multiplication from the command line interface
```bash
mra mmm -a 0x00112233 -b 0x44556677 -n 0x93849ca7
```
Output: `1699857101 0x6551c2cd`

##### Example 2

Call Montgomery Modular Exponentiation from the command line interface
```bash
mra mme -m 0x00112233 -e 0x44556677 -n 0x93849ca7 -k 0x8c8d9129
```
Output: `613470512 0x2490d130`

### RSA

* **gcd** -p *{int}*, -q *{int}* &emsp; Greatest Common Divisor
* **lcm** -p *{int}*, -q *{int}* &emsp; Least Common Multiple
* **soe** [--qmin *{int}*, --qmax *{int}*] &emsp; Sieve of Eratosthenes
* **n** -p *{int}*, -q *{int}* &emsp; n
* **tot** -p *{int}*, -q *{int}* &emsp; tot
* **cop** -p *{int}*, -q *{int}* &emsp; Coprime
* **e** --totn *{int}* &emsp; e
* **chke** -e *{int}*, --totn *{int}* &emsp; Check e
* **d** -e *{int}*, -n *{int}* &emsp; d
* **muli** -e *{int}*, -n *{int}* &emsp; Multiplicative Inverse
* **egcd** -n *{int}*, -e *{int}* &emsp; Extended Greatest Common Divisor
* **encrypt** -m *{int}*, -e *{int}*, -n *{int}* &emsp; Encrypt
* **decrypt** -c *{int}*, -d *{int}*, -n *{int}* &emsp; Decrypt


##### Example 1

Call Greatest Common Divisor from the command line interface
```bash
mra gcd -p 2 -q 4 
```
Output: `2 0x2`

##### Example 2

Call Least Common Multiple from the command line interface
```bash
mra lcm -p 2 -q 4
```
Output: `10 0xa`

##### Example 3

Call encrypt from the command line interface
```bash
mra encrypt -m 18 -e 257 -n 21
```
Output: `9 0x9`

##### Example 4

Call decrypt from the command line interface
```bash
mra decrypt -c 9 -d 17 -n 21
```
Output: `18 0x12`

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

# Roadmap to v1.0.0-alpha

- [x] implement Montgomery Modular Multiplication (MMM)
- [x] implement Montgomery Modular Exponentiation (MME)
- [x] implement logging of calculation steps
- [x] implement tests
- [x] implement the calculation of rsa values for encrypting and decrypting
- [ ] implement the calculation of test vectors
- [ ] implement the generation of random test vectors
- [x] implement a cli for standalone usage (MMR, RSA)
- [ ] add help text for MMR and RSA cli
- [ ] implement a cli for standalone usage (test vector generator)
- [ ] add use description to readme.md
- [ ] add an example and description of how to use the package
- [x] add build description to readme.md
- [ ] implement build, test and release workflow
- [ ] enhance logging
- [ ] enhance package structure
- [ ] enhance testing

# References

[1] Christof Paar, Jan Pelzl. Understanding Cryptography: A Textbook for Students and Practitioners, Springer, 2010.

[2] Christof Paar. Implementation of Cryptographic Schemes 1, Lecture Notes, 2015.

[3] https://www.emsec.ruhr-uni-bochum.de/media/attachments/files/2015/09/IKV-1_2015-04-28.pdf.

[4] Elif Bilge Kavun. Security Processor Design - Lecture and Exercise Slides, 2024.

[5] https://www.extendedeuclideanalgorithm.com

[6] https://www.geeksforgeeks.org
