def calcular_mcd(a, b):
    """
    Calcula el MCD usando el algoritmo de Euclides iterativo
    """
    # Trabajamos con valores absolutos
    a = abs(a)
    b = abs(b)
    
    # Algoritmo de Euclides
    while b != 0:
        temp = b
        b = a % b
        a = temp
    
    return a

def calcular_mcm(a, b, mcd):
    """
    Calcula el MCM usando la fórmula: MCM(a,b) = |a*b| / MCD(a,b)
    """
    return abs(a * b) // mcd

def main():
    print("=== Calculadora de MCD y MCM ===")
    print()
    
    try:
        # Solicitar los números al usuario
        num1 = int(input("Ingresa el primer número entero: "))
        num2 = int(input("Ingresa el segundo número entero: "))
        
        # Verificar que no sean ambos cero
        if num1 == 0 and num2 == 0:
            print("Error: No se puede calcular MCD y MCM cuando ambos números son cero.")
            return
        
        # Calcular MCD
        mcd = calcular_mcd(num1, num2)
        
        # Calcular MCM
        if num1 == 0 or num2 == 0:
            mcm = 0  # MCM es 0 cuando uno de los números es 0
        else:
            mcm = calcular_mcm(num1, num2, mcd)
        
        # Mostrar resultados
        print()
        print(f"Números ingresados: {num1} y {num2}")
        print(f"MCD({num1}, {num2}) = {mcd}")
        print(f"MCM({num1}, {num2}) = {mcm}")
        
        # Verificación
        print()
        print("=== Verificación ===")
        print(f"MCD × MCM = {mcd} × {mcm} = {mcd * mcm}")
        print(f"|a × b| = |{num1} × {num2}| = {abs(num1 * num2)}")
        
        if num1 != 0 and num2 != 0:
            if mcd * mcm == abs(num1 * num2):
                print("✓ Verificación correcta: MCD × MCM = |a × b|")
            else:
                print("✗ Error en los cálculos")
    
    except ValueError:
        print("Error: Por favor ingresa números enteros válidos.")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Función adicional para mostrar el proceso paso a paso
def mostrar_proceso_mcd(a, b):
    """
    Muestra el proceso paso a paso del algoritmo de Euclides
    """
    print(f"\n=== Proceso para calcular MCD({a}, {b}) ===")
    
    a = abs(a)
    b = abs(b)
    paso = 1
    
    print(f"Trabajando con valores absolutos: {a} y {b}")
    
    while b != 0:
        cociente = a // b
        residuo = a % b
        print(f"Paso {paso}: {a} = {b} × {cociente} + {residuo}")
        
        a = b
        b = residuo
        paso += 1
    
    print(f"MCD = {a}")
    return a

if __name__ == "__main__":
    main()
    
    # Opción para ver el proceso detallado
    print("\n" + "="*50)
    respuesta = input("¿Deseas ver el proceso paso a paso? (s/n): ").lower()
    
    if respuesta == 's':
        try:
            num1 = int(input("Primer número: "))
            num2 = int(input("Segundo número: "))
            mostrar_proceso_mcd(num1, num2)
        except ValueError:
            print("Error: Números inválidos.")
