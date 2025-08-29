Perfecto 🚀. Aquí tienes el contenido completo del README.md:

# Equivalencias Lógicas Interactivas

Mini-aplicación web para explorar y comprender **equivalencias lógicas** comunes entre proposiciones (P y Q).

## 🎯 Objetivos
- Mostrar visualmente propiedades y equivalencias lógicas.
- Permitir interacción directa para probar valores de verdad.
- Servir como apoyo didáctico en la materia de Lógica.

## 🚀 Tecnologías utilizadas
- HTML5
- CSS3
- JavaScript (Vanilla)

No requiere servidor: basta abrir `index.html` en un navegador moderno.

## 📂 Estructura del proyecto

/(proyecto) 
├─ index.html // Interfaz y estructura
├─ styles.css // Estilos visuales 
└─ script.js        // Lógica de cálculo e interacción

## 🧑‍💻 Guía de uso
1. Abrir `index.html` en el navegador.
2. Seleccionar la equivalencia deseada (ej: doble negación, Morgan, etc.).
3. Ajustar P y Q con los botones (VERDADERO / FALSO).
4. Hacer clic en **CALCULAR EQUIVALENCIA**.
5. Ver resultados: expresiones, valores y si son equivalentes.

## 📘 Equivalencias implementadas
1. Doble Negación → ¬¬p ⇐⇒ p  
2. Conmutativa (∧) → (p ∧ q) ⇐⇒ (q ∧ p)  
3. Conmutativa (∨) → (p ∨ q) ⇐⇒ (q ∨ p)  
4. Ley de Morgan (∨) → ¬(p ∨ q) ⇐⇒ (¬p ∧ ¬q)  
5. Ley de Morgan (∧) → ¬(p ∧ q) ⇐⇒ (¬p ∨ ¬q)  
6. Negación de la implicación → ¬(p → q) ⇐⇒ (p ∧ ¬q)  
7. Definición de implicación → p → q ⇐⇒ (¬p ∨ q)  
8. Contrarrecíproco → (p → q) ⇐⇒ (¬q → ¬p)  
9. Principio de doble implicación → (p ↔ q) ⇐⇒ (p → q) ∧ (q → p)  

## 🔧 Mejoras futuras
- Generar tablas de verdad completas.  
- Soporte para más variables (P, Q, R).  
- Guardar configuraciones (LocalStorage).  
- Separar lógica y UI en distintos módulos.  
- Internacionalización (multi-idioma).  

## 👩‍🎓 Autores
- Andres Felipe Martinez Henao
- Tecnologia en Desarrollo de Software y Ingeniería en sistemas y computación 