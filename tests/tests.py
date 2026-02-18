import vecmath as vc

x = vc.clamp(5, 0, 10)
print(x) # output: 5

a = [1, 2, 3]
b = [4, 5, 6]
print(vc.dot(a, b) == 1*4 + 2*5 + 3*6)  # output: True | =32

print("pi: " + str(vc.pi)) # output: pi: 3.141592653589793
print("tau: " + str(vc.tau)) # output: tau: 6.283185307179586
print("epsilon: " + str(vc.eps)) # output: epsilon: 2.220446049250313e-16
print("euler: " + str(vc.e)) # output: euler: 2.718281828459045


pi1 = vc.float64(3.14)
pi2 = vc.float32(3.14)
pi3 = vc.float16(3.14)

y = vc.Array([1, 2, 3])
print(y) # output: Array([1, 2, 3])
print(y[1]) # output: 2

y[1] = 42
y.append(4)
print(y) # output: Array([1, 42, 3, 4])

y.pop()
print(y) # output: Array([1, 2, 3])


try:
    vc.dot([1,2], [1])
except ValueError as e:
    print("Erro:", e) # output: Erro: dot: vectors must have the same length
