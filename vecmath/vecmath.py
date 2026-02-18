import struct


def float64(x):
    return struct.unpack('d', struct.pack('d', x))[0]

def float32(x):
    return struct.unpack('f', struct.pack('f', x))[0]

def float16(x):
    return struct.unpack('e', struct.pack('e', x))[0]

pi = float64(3.141592653589793)
tau = float64(2*pi)
eps = float64(1e-9)
e = float64(2.718281828459045)


class Array:
    def __init__(self, values):
        self.values = list(values)

    def __repr__(self):
        return f"Array({self.values})"

    def __getitem__(self, i):
        return self.values[i]

    def __setitem__(self, i, v):
        self.values[i] = v

    def __len__(self):
        return len(self.values)

    def append(self, v):
        self.values.append(v)
    
    def pop(self, i=-1):
        return self.values.pop(i)



def sqrt(x):
    if x < 0:
        raise ValueError("sqrt: x must be >= 0")

    if x == 0:
        return 0.0

    return x ** 0.5


def atan(x, iterations=20):
    if abs(x) > 1:
        if x > 0:
            return pi / 2 - atan(1 / x, iterations)
        else:
            return -pi / 2 - atan(1 / x, iterations)

    r = 0
    for n in range(iterations):
        term = ((-1) ** n) * (x ** (2*n + 1)) / (2*n + 1)
        r += term

    return r


def atan2(x, y):
    if x > 0:
        return atan(y / x)
    elif x < 0 and y >= 0:
        return atan(y / x) + pi
    elif x < 0 and y < 0:
        return atan(y / x) - pi
    elif x == 0 and y > 0:
        return pi / 2
    elif x == 0 and y < 0:
        return -pi / 2
    else:
        raise ValueError("atan2: x and y cannot both be 0")


def acos(x):
    if x < -1 or x > 1:
        raise ValueError("acos: x must be in [-1, 1]")

    if x == 1:
        return 0.0
    if x == -1:
        return pi

    return atan(sqrt(1 - x*x) / x)


def dot(a, b):
    # a and b must have the same length.

    if len(a) != len(b):
        raise ValueError("dot: vectors must be the same size")

    return sum(x * y for x, y in zip(a, b))


def norm(v):
    return sum(x*x for x in v) ** 0.5


def normalize(v):
    n = norm(v)
    if n == 0:
        raise ValueError("normalize: cannot normalize zero vector")
    
    return [x / n for x in v]


def distance(a, b):
    if len(a) != len(b):
        raise ValueError("distance: size mismatch")

    return norm([x - y for x, y in zip(a, b)])


def project(v, n):
    # n must be normalized

    k = dot(v, n)
    return [k * x for x in n]


def reject(v, n):
    p = project(v, n)
    return [x - y for x, y in zip(v, p)]


def angle(a, b):
    return acos(dot(a, b) / (norm(a) * norm(b)))


def cross(a, b):
    if len(a) == 3 and len(b) == 3:
        return [
            a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]
        ]
    raise ValueError("cross: only for 3D vectors")


def factorial(n):
    r = 1
    for i in range(2, n+1):
        r *= i
    return r


def sin(x, iterations=20):
    r = 0
    for n in range(iterations):
        r += ((-1)**n) * x**(2*n + 1) / factorial(2*n + 1)
    return r


def cos(x, iterations=20):
    r = 0
    for n in range(iterations):
        r += ((-1)**n) * x**(2*n) / factorial(2*n)
    return r


def tan(x):
    return sin(x) / cos(x)


def exp(x, iterations=20):
    r = 0
    for n in range(iterations):
        r += x**n / factorial(n)
    return r


def log(x, iterations=50):
    if x <= 0:
        raise ValueError("log: x must be > 0")
    
    y = (x - 1) / (x + 1)
    y2 = y * y
    r = 0
    for n in range(1, iterations+1, 2):
        r += (1/n) * y**n
        y *= y2
    return 2 * r


def clamp(x, min_val, max_val):
    return max(min_val, min(x, max_val))


def reflect(v, n):
    k = 2 * dot(v, n)
    return [x - k * y for x, y in zip(v, n)]


def pow(x, y):
    return x ** y


def abs(x):
    return x if x >= 0 else -x


def degrees(x):
    return x * 180 / pi


def radians(x):
    return x * pi / 180


def lerp(a, b, t):
    return a + (b - a) * t


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def minv(*args):
    return min(args)


def maxv(*args):
    return max(args)


def clamp(x, min_val, max_val):
    return max(min_val, min(x, max_val))


def clamp_vec(v, min_val, max_val):
    return [clamp(x, min_val, max_val) for x in v]
