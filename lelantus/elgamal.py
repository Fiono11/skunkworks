# Hashed ElGamal encryption
#
# Avoids the need for mapping a message onto the curve

from common import *
from dumb25519 import Scalar, Point, random_scalar, hash_to_scalar

# Encryption
class Ciphertext:
    K = None
    M = None

# Encrypt a message
#
# INPUT
#   m: message (Scalar)
#   A: recipient public key (Point)
# OUTPUT
#   Ciphertext
def encrypt(m,A):
    k = Scalar(0)
    while k == Scalar(0):
        k = random_scalar()

    output = Ciphertext()
    output.K = G*k
    output.M = m + hash_to_scalar(A*k)
    return output

# Decrypt a message
#
# INPUT
#   c: Ciphertext
#   a: private key (Scalar)
# OUTPUT
#   message (Scalar)
def decrypt(c,a):
    return c.M - hash_to_scalar(c.K*a)
