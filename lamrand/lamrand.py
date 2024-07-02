import os
import math
import time
import secrets

class LamRand:
    def __init__(self, seed=None):
        if seed is None:
            self.seed = self._generate_seed()
        else:
            self.seed = seed
        self.state = self.seed
        self.increment = (self.seed << 1) | 1  # Must be odd
        self.multiplier = 6364136223846793005

    def _generate_seed(self):
        return int.from_bytes(os.urandom(16), byteorder='big') ^ int(time.time() * 1000)

    def _pcg_step(self):
        self.state = self.state * self.multiplier + self.increment
        self.state &= 0xFFFFFFFFFFFFFFFF  # Force to 64 bits
        xorshifted = ((self.state >> 18) ^ self.state) >> 27
        rot = self.state >> 59
        return (xorshifted >> rot) | (xorshifted << ((-rot) & 31)) & 0xFFFFFFFFFFFFFFFF

    def next(self):
        return self._pcg_step()

    def next_int(self, min_val, max_val):
        return min_val + self.next() % (max_val - min_val + 1)

    def next_float(self):
        return self.next() / float(0xFFFFFFFFFFFFFFFF)

    def next_gaussian(self, mean=0, stddev=1):
        u1 = self.next_float()
        u2 = self.next_float()
        z0 = (-2 * math.log(u1)) ** 0.5 * math.cos(2 * math.pi * u2)
        return mean + z0 * stddev

    def next_gaussian_box_muller(self, mean=0, stddev=1):
        u1 = self.next_float()
        u2 = self.next_float()
        z0 = (-2 * math.log(u1)) ** 0.5 * math.cos(2 * math.pi * u2)
        return mean + z0 * stddev

    def next_poisson(self, lam):
        L = math.exp(-lam)
        k = 0
        p = 1.0
        while p > L:
            k += 1
            p *= self.next_float()
        return k - 1

    def next_bool(self):
        return self.next() % 2 == 0

    def next_string(self, length):
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        return ''.join([characters[self.next_int(0, len(characters) - 1)] for _ in range(length)])

    def shuffle(self, data):
        n = len(data)
        for i in range(n-1, 0, -1):
            j = self.next_int(0, i)
            data[i], data[j] = data[j], data[i]
        return data

    def save_state(self):
        return (self.state, self.increment)

    def load_state(self, state):
        self.state, self.increment = state


class LamRandSecure:
    @staticmethod
    def next_int(min_val, max_val):
        return secrets.randbelow(max_val - min_val + 1) + min_val

    @staticmethod
    def next_float():
        return secrets.randbelow(10**18) / 10**18

    @staticmethod
    def next_bool():
        return secrets.randbelow(2) == 0

    @staticmethod
    def next_string(length):
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        return ''.join(secrets.choice(characters) for _ in range(length))