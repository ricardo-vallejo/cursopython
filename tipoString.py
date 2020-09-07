#Cadenas
"""
Existen 4 formas de añadir una cadena.
'Cadena'
"Cadena"
'''Cadena'''
Y tripe comilla doble. 
Las dos ultimas permiten ingresar textos multilineas.
"""
comillaSimple = 'Cadena comilla simple'
comillaDoble = "Cadena comilla doble"
tripleComillaSimple = '''Cadena triple
comilla simple'''
tripleComillaDoble = """Cadena triple
comilla doble"""

print(comillaSimple)
print(comillaDoble)
print(tripleComillaSimple)
print(tripleComillaDoble)

#Operaciones con Cadenas
"""
len(cadena) Tamaño de la cadena
min(cadena) Caracter menor de la cadena en unicode
max(cadena) Caracter mayor de la cadena en unicode
+ Permite concatenar
* Permite multiplicar cadenas
"""
cadena = "Hola Compañeros"
print(len(cadena))
print(min(cadena))
print(max(cadena))

cadenaNueva = " de Italiano"
print(cadena + cadenaNueva)

cadenaMultiple = "Soy mas "
print(cadenaMultiple * 3)


#Indices
"""
Acceso a los caracteres de la cadena
Solo lectura
[i]
"""
cadenaIndices = "Hello world!"
print(cadenaIndices[3])

#Subcadenas
"""
cadena[:end]
cadena[start:]
cadena[start:end]
cadena[start:end:steps]
"""
subcadenas = "Hello world!"
print(subcadenas[:4])
print(subcadenas[5:])
print(subcadenas[2:7])
print(subcadenas[0:9:2])

#Metodos
cadenaTest = "hola mundo!"
cadenaStrip = "  Hola Mundo!  "
cadenaAlNum = "asd234kle456"
cadenaNonAlNum = " asd2$4kle456"
cadenaAlpha = "asldfjowejkls"
cadenaDigit = "123345"
cadenaUpper = "HOLA MUNDO!"
cadenaSpace = " "
cadenaSplit = "Karen,Bonita,Inteligente"
print(cadenaTest.capitalize())
print(cadenaTest.title())
print(cadenaTest.upper())
print(cadenaTest.lower())
print(cadenaTest.replace("o", "a"))
print(cadenaStrip.strip()) #Remueve espacios adelante y al final
print(cadenaAlNum.isalnum()) #Debe tener combinacion de numeros y letras solamente
print(cadenaNonAlNum.isalnum())
print(cadenaAlpha.isalpha()) #Todos los caracteres deben ser alfabeticos
print(cadenaTest.isalpha()) 
print(cadenaDigit.isdigit()) #Todos los caracteres deben ser digitos
print(cadenaTest.islower()) #Todos los caracteres deben estar en minuscula
print(cadenaStrip.islower())
print(cadenaUpper.isupper()) #Todos los caracteres deben estar en mayuscula
print(cadenaTest.isupper()) 
print(cadenaSpace.isspace()) #Funciona con espacios, tabulaciones y saltos de linea.
print(cadenaTest.count("o")) #Cuenta el numero de veces que aparece una subcadena
print(cadenaTest.endswith("do!")) #Valida si termina en una subcadena
print(cadenaTest.find("mun")) #Retorna la posicion de la subcadena. Es casesensitive.
print(cadenaTest.index("mun")) #Retorna la posicion de la subcadena. Retorna error cuando no encuentra nada
print(cadenaTest.split())
print(cadenaSplit.split(","))

#Formato de cadenas
"""
%s Corresponde a una cadena
%d Corresponde a numeros enteros
%<n>d Corresponde a numeros enteros. La n indica el numero de digitos. Rellana con espacios a la izquierda.
%0<n>d Corresponde a numeros enteros. La n indica el numero de digitos. Rellana con ceros a la izquierda.
%f Corresponde a numeros flotantes. Añade decimales si no los tiene.
%.<dec>f Corresponde a numeros flotantes. Se especifica el numero de decimales
%0<n>.<dec>f Corresponde a numeros flotantes. Se especifica el numero de decimales y numeros antes del decimal
%x | %X Corresponde a numero hexadecimales
-----------------------------------------
{}
{n} | {n:formato}
{k} | {k:formato}
"""
nombre = "Karen"
edad = 27
salida = "%s tiene %d años" % (nombre, edad)
print(salida)

salidaDos = "%s tiene %4d años" % (nombre, edad)
print(salidaDos)

salidaTres = "%s tiene %04d años" % (nombre, edad)
print(salidaTres)

precio = 20.95
salidaPrecio = "El precio es %f euros" % (precio)
salidaPrecioDos = "El precio es %.2f euros" % (precio)
salidaPrecioTres = "El precio es %7.2f euros" % (precio)
salidaPrecioCuatro = "El precio es %07.2f euros" % (precio)
print(salidaPrecio)
print(salidaPrecioDos)
print(salidaPrecioTres)
print(salidaPrecioCuatro)

numeroHex = 255
salidaHex = "El numero es %x" % (numeroHex)
print(salidaHex)


salidaFormat = "{} tiene {} años".format(nombre, edad)
print(salidaFormat)

salidaFormatIndex = "{1} tiene {0} años".format(edad, nombre)
print(salidaFormatIndex)

salidaFormatParams = "{name} tiene {age} años".format(name=nombre, age=edad)
print(salidaFormatParams)

salidaFormatNumber = "El precio es {0:.3f} euros".format(precio)
print(salidaFormatNumber)