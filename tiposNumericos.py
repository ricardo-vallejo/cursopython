#Enteros
"""
Sin decimales
Positivos y negativos o 0
No hay tamaño limite
"""
numeroEntero = 33
type(numeroEntero)


#Booleanos
"""
True o False
Subclase del tipo entero (1, 0)
"""
verdadero = True
falso = False
print(verdadero)
print(falso)

verdNum = int(verdadero) #Se puede convertir el valor booleano a entero
falNum = int(falso)
print(verdNum)
print(falNum)

verBool = bool(verdNum) #Se puede convertir el valor entero a booleano
falBool = bool(falNum)
print(verBool)
print(falBool)


#Reales
"""
Punto flotante
Estan limitados a 64 bits
Signo, exponente y mantisa
"""
precio = 5.34
print(precio)

notacionCientifica = 2.5e-6
print(notacionCientifica)


#Decimales
"""
Punto flotante(mayor precision)
Importar: from decimal import Decimal
Decimal('valor punto flotante')
"""
from decimal import Decimal

numeroDecimal = Decimal('3.6')
print(numeroDecimal)


print(0.3 - 0.1 * 3) #Los flotantes no tienen precision
print(Decimal('0.3') - Decimal('0.1') * Decimal('3.0')) #Los decimales tienen mayor precision


#Fracciones
"""
Numerador/Denominador
Minimo termino
Importar: from fractions import Fraction
Fraction(numerador,denominador)
 -numerator
 -denominator
"""
from fractions import Fraction

fraccion = Fraction(15,5)
print(fraccion)

print(fraccion.numerator)
print(fraccion.denominator)


#Complejos
"""
a + bj
- real 
- imag
"""
numeroComplejo = 5 + 8j
print(type(numeroComplejo))
print(numeroComplejo)
print(numeroComplejo.real)
print(numeroComplejo.imag)
