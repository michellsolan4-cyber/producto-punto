# ===== COMPROBACIÓN DE ORTOGONALIDAD =====
u1 = (1, 0, 1)
u2 = (1/2, 1, -1/2)
u3 = (-2/3, 2/3, 2/3)

def producto_interno(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

print("u1 • u2 =", producto_interno(u1, u2))  
print("u1 • u3 =", producto_interno(u1, u3))  
print("u2 • u3 =", producto_interno(u2, u3))   

# ===== Código original del profesor =====
# Programa para calcular el producto punto de dos vectores

n = int(input("Ingrese la dimensión de los vectores: "))

vector1 = []
vector2 = []

print("\nIngrese los datos del Vector )
for i in range(n):
    valor = float(input(f"Componente {i + 1}: "))
    vector1.append(valor)

print("\nIngrese los datos del Vector 2")
for i in range(n):
    valor = float(input(f"Componente {i + 1}: "))
    vector2.append(valor)

producto = 0
for i in range(n):
    producto += vector1[i] * vector2[i]

print("\nVector 1:", vector1)
print("Vector 2:", vector2)
print("Producto punto:", producto)
