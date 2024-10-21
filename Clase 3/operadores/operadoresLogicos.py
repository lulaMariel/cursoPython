# Operaciones lógicas: And (True solo si AMBOS sean verdaderas), or (True basta con que 1 sea verdadero), not (True si es falso y viceversa), (True solo si UNA es verdadera, "o" mutuamente excluyentes)

# And

print("\n")
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False
print("\n")

# Or

print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False
print("\n")

# Not

print(not True) # False
print(not False) # True
print("\n")

# ^ (or exclusivo)

print(True ^ True) # False
print(True ^ False) # True
print(False ^ True) # True
print(False ^ False) # False