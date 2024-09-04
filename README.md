# Manejo de Archivos en Python.
- El repositorio tiene dos archvios: el main.py es el script principal para ejecutar la funciones
- El archivo func.py tiene las funciones a ejecura desde el main.py

# Archivos
- main.py
```python
import func

dato1=float(input('Ingrese dato 1: '))
dato2=float(input('Ingrese dato 2: '))

print('La suma de los numeros es: ',func.suma(dato1, dato2))
print('La resta de los numeros es: ',func.resta(dato1, dato2))
print('La multiplicación de los numeros es: ',func.mul(dato1, dato2))
print('La división de los numeros es: ',func.div(dato1, dato2))
print('El modulo de x % y es: ', func.modulo(dato1,dato2))
print('El Seno es x es: ', func.sen(dato1))

```

- func.py
```python
import math

def suma(x,y):
	return x+y 

def resta(x,y):
	return x-y 

def mul(x,y):
	return x*y 

def div(x,y):
	if y==0:
		return 'ERROR'
	else:
		return x/y 

def modulo(x,y):
	return x%y

def sen(x):
	return math.sin(x)

#funciones que pase de grados a radianes
```

# Trabajo
- Agregue la función de grados a radianes