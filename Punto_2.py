def factores_primos_paso_a_paso(numero):
    """
    Calcula los factores primos de un número mostrando cada paso del proceso
    """
    if numero <= 1:
        print(f"El número {numero} no tiene factores primos válidos.")
        return []
    
    print(f"\n=== CALCULANDO FACTORES PRIMOS DE {numero} ===")
    print(f"Número original: {numero}")
    print("-" * 50)
    
    factores = []
    numero_actual = numero
    divisor = 2
    paso = 1
    
    # Buscar factores primos
    while divisor * divisor <= numero_actual:
        while numero_actual % divisor == 0:
            print(f"Paso {paso}: {numero_actual} ÷ {divisor} = {numero_actual // divisor}")
            print(f"  → {divisor} es un factor primo de {numero}")
            
            factores.append(divisor)
            numero_actual = numero_actual // divisor
            paso += 1
            
            if numero_actual == 1:
                break
        
        # Incrementar divisor (optimización: después del 2, solo números impares)
        if divisor == 2:
            divisor = 3
        else:
            divisor += 2
    
    # Si queda un número mayor que 1, también es primo
    if numero_actual > 1:
        print(f"Paso {paso}: {numero_actual} es primo y mayor que 1")
        print(f"  → {numero_actual} es un factor primo de {numero}")
        factores.append(numero_actual)
    
    print("-" * 50)
    print(f"RESULTADO: Los factores primos de {numero} son: {factores}")
    
    # Verificación
    producto = 1
    for factor in factores:
        producto *= factor
    
    print(f"VERIFICACIÓN: {' × '.join(map(str, factores))} = {producto}")
    
    if producto == numero:
        print("✓ Factorización correcta")
    else:
        print("✗ Error en la factorización")
    
    return factores


def es_primo(num):
    """Función auxiliar para verificar si un número es primo"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def mostrar_informacion_adicional(factores):
    """Muestra información adicional sobre los factores encontrados"""
    if not factores:
        return
    
    print(f"\n=== INFORMACIÓN ADICIONAL ===")
    
    # Contar frecuencias
    from collections import Counter
    frecuencias = Counter(factores)
    
    print("Factores únicos y sus exponentes:")
    for factor, freq in sorted(frecuencias.items()):
        if freq == 1:
            print(f"  {factor}¹")
        else:
            print(f"  {factor}^{freq}")
    
    # Forma exponencial
    exponencial = []
    for factor, freq in sorted(frecuencias.items()):
        if freq == 1:
            exponencial.append(str(factor))
        else:
            exponencial.append(f"{factor}^{freq}")
    
    print(f"Forma exponencial: {' × '.join(exponencial)}")
    
    # Verificar si los factores son primos
    print("\nVerificación de primalidad:")
    factores_unicos = set(factores)
    for factor in sorted(factores_unicos):
        estado = "es primo" if es_primo(factor) else "NO es primo"
        print(f"  {factor}: {estado}")


def main():
    """Función principal del programa"""
    print("=== CALCULADORA DE FACTORES PRIMOS ===")
    print("Este programa encuentra todos los factores primos de un número")
    print("y muestra el proceso paso a paso.\n")
    
    while True:
        try:
            # Solicitar número al usuario
            entrada = input("Ingresa un número entero positivo (o 'salir' para terminar): ")
            
            if entrada.lower() in ['salir', 'exit', 'quit']:
                print("¡Hasta luego!")
                break
            
            numero = int(entrada)
            
            if numero <= 0:
                print("Por favor, ingresa un número entero positivo.")
                continue
            
            # Calcular factores primos
            factores = factores_primos_paso_a_paso(numero)
            
            # Mostrar información adicional
            if factores:
                mostrar_informacion_adicional(factores)
            
            print("\n" + "="*60 + "\n")
            
        except ValueError:
            print("Por favor, ingresa un número válido.")
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego!")
            break


# Función para probar con ejemplos
def ejemplos():
    """Ejecuta algunos ejemplos demostrativos"""
    print("=== EJEMPLOS DEMOSTRATIVOS ===\n")
    
    numeros_ejemplo = [12, 24, 17, 100, 97, 60]
    
    for numero in numeros_ejemplo:
        factores = factores_primos_paso_a_paso(numero)
        if factores:
            mostrar_informacion_adicional(factores)
        print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    # Descomenta la siguiente línea si quieres ver ejemplos primero
    # ejemplos()
    
    # Ejecutar programa principal
    main()
