#main.py
#Calculadora
#suma, resta, multiplicación, división, modulo
#trigonometrica, Sin Cos, Tan
#Probailidad
import func

dato1=float(input('Ingrese dato 1: '))
dato2=float(input('Ingrese dato 2: '))

print('La suma de los numeros es: ',func.suma(dato1, dato2))
print('La resta de los numeros es: ',func.resta(dato1, dato2))
print('La multiplicación de los numeros es: ',func.mul(dato1, dato2))
print('La división de los numeros es: ',func.div(dato1, dato2))
print('El modulo de x % y es: ', func.modulo(dato1,dato2))
print('El Seno es x es: ', func.sen(dato1))

