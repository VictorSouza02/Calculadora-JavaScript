print ('CALCULADORA FÓRMULA DE BHASKARA')
print (' ')
A = int (input('qual é o valor de A? '))
B = int (input('qual é o valor de B? '))
C = int (input('qual é o valor de C? '))

s = (B**2)-4*A*C

x1 =(-B + s ** (1/2))/ 2*A

x2 =(-B - s ** (1/2))/ 2*A

print (' ')

print ('■ fórmula de bhaskara (delta) é: Δ = B^2-4.A.C')
print (' ')
print ('■ fórmula de bhaskara (delta) é: Δ={}^2-4.{}.{}'.format(B,A,C))
print (' ')
print ('● o valor de delta é ',s)
print (' ')
print ('----------------- ')

print ('■ o valor de x é encontrado na fórmula: x = (-B (+-) √Δ)/ 2.A')
print (' ')
print ('■ o valor de x é:: x = (-({}) (+-) √{})/ 2.{}'.format(B,s,A))
print (' ')
print ('● o valor de x positivo é {}, e o valor do x negativo é {}'.format(x1,x2))

