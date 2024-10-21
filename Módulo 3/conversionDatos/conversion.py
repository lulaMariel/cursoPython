# Casting: Es el proceso de convertir un tipo de dato en otro tipo de dato. Esto se hace utilizando funciones incorporadas como "int()", "float()", "str()", "bool()", entre otras.

# int

print("\n")
num = 3.5
print(type(num)) # Float

int(num) # Entero

# int("Hola") # Error

num1 = "8"
print(type(num1)) # String

int(num1) # Entero

num1 = int(num1) # Modifica la variable original, en vez de ser str pasa a int
print(type(num1))
print("\n")

# Float

num2 = "8.5"
print(type(num2)) # String
num3 = float(num2) # Convertimos el str a float y guardamos en una nueva variable
print(type(num3))
num4 = 5
print(type(num4)) # Entero
num5 = float(num4)
print(type(num5)) # Float
print("\n")

# Str

x = 10
print(type(x)) # Entero
y = str(x) # Conversión
print(type(y)) # String
w = 5.5
print(type(w)) # Float
z = str(w) # Conversión
print(type(z)) # String