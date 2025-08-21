def es_primo(n):
    """Verifica si un número es primo"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def encontrar_factores(numero):
    """Encuentra dos factores de un número compuesto (diferentes de 1 y el mismo número)"""
    if numero < 4:
        return None, None
    
    if es_primo(numero):
        return None, None
    
    # Buscar factores desde 2 hasta la raíz cuadrada del número
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            factor1 = i
            factor2 = numero // i
            return factor1, factor2
    
    return None, None

def main():
    print("=== CALCULADORA DE FACTORES DE NÚMEROS COMPUESTOS ===")
    print()
    
    while True:
        try:
            numero = int(input("Ingresa un número (0 para salir): "))
            
            if numero == 0:
                print("¡Hasta luego!")
                break
            
            if numero < 4:
                print(f"El número {numero} no es un número compuesto válido.")
                print("Un número compuesto debe ser mayor que 3.")
                continue
            
            if es_primo(numero):
                print(f"El número {numero} es primo, no es compuesto.")
                print("Los números primos solo tienen como factores 1 y ellos mismos.")
                continue
            
            factor1, factor2 = encontrar_factores(numero)
            
            if factor1 and factor2:
                print(f"✓ El número {numero} es compuesto")
                print(f"✓ Factores encontrados: {factor1} × {factor2} = {numero}")
                
                # Verificación
                if factor1 * factor2 == numero:
                    print("✓ Verificación correcta")
                else:
                    print("✗ Error en el cálculo")
            else:
                print(f"No se pudieron encontrar factores para {numero}")
            
            print("-" * 50)
            
        except ValueError:
            print("Por favor, ingresa un número entero válido.")
        except Exception as e:
            print(f"Error: {e}")

# Función adicional para mostrar todos los factores
def mostrar_todos_factores(numero):
    """Muestra todos los factores de un número"""
    print(f"\nTodos los factores de {numero}:")
    factores = []
    
    for i in range(1, numero + 1):
        if numero % i == 0:
            factores.append(i)
    
    print(f"Factores: {factores}")
    
    # Mostrar pares de factores (excluyendo 1 y el mismo número)
    pares = []
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            pares.append((i, numero // i))
    
    if pares:
        print("Pares de factores (diferentes de 1 y el número mismo):")
        for par in pares:
            print(f"  {par[0]} × {par[1]} = {numero}")

# Ejemplo de uso
if __name__ == "__main__":
    main()
