# Config

## Parse errors

- Configuración inválida
- Fichero no encontrado
- Mala sintaxis
- Parámetros imposibles

## Formato

- WIDTH (int)
- HEIGHT (int)
- ENTRY (pos)
- EXIT (pos)
- OUTPUT_FILE (str)
- PERFECT (bool)

### Adicionales

- SEED (int)

# Maze

## Reqs

- Reproducible via SEED
- Entrada y salida deben ser diferentes y estar dentro del laberinto
- Conectividad plena (no celdas aisladas, salvo el patron 42)
- Todo el laberinto rodeado de bordes
- Celdas vecinas coherentes
- No areas 3x3 (si 3x2 o 2x3)
- Visualmente 42 en el centro. ¡Cerrado!
    - puede omitirse si el mapa no lo admite, por ejemplo, por pequeño
    - Printar un error en ese caso!
- Si perfecto activado, solo un camino de entrada a salida (sin bucles)
- Por defecto, perfecto NO activado
- Si no, pacman-like:
    - conectividad plean
    - esquinas y centro abiertos (esquinas sin muros al menos)
    - al menos dos rutas independientes (bucles)
    - casi sin finales muertos (un par son tolerables)
        - ¡bonus! con 0 finales muertos

# Output

## File

- Un dígito hexadecimal por celda, representado los muros
- 0 N, 1 E, 2 S, 3 O (OSEN)
    - ej: 3 (0011) muros en este y norte
    - ej: A (1010) muros en oeste y este
- Una fila -> una linea
- Al final, linea vacía más (uno en cada línea):
    - pos entrada
    - pos salida
    - camino más corto de entrada a salida (usando solo letras N E S W)
- Todas las líneas acaban con "\n"
- Probar con "maze_analyzer.py"
    - Comprueba que muros coherentes
    - Dice si el laberinto es perfecto
    - Dice si es "jugable"

## Visual

- ASCII
- Mostrar muros, entrada, salida y solución
- Acciones:
    - Re-generar laberinto (y mostrar)
    - Mostrar/Ocultar solución más corta
    - Cambiar colores
    - (Opcional) cambiar colores al 42
    - (Opcional) Se pueden añadir más cosas si queremos
    - Salir

# Otros requirements

- La generación del laberinto debe ser una única clase (MazeGenerator) dentro de un módulo
- Documentación
    - Como instanciar y usar
    - Como pasar parametros personalizados
    - Como acceder a la estructura generada y solución
- Generar un ejecutable o instalable del mazegenerator
- Añadir licencia, readme, documentación

# README

- Lo de siempre, ver en subject por si acaso
- Tiene cosas que no hay en otros, ver subject

# BONUS

- Laberinto sin finales muertos (probar con: maze_analyzer.py --max-dead-ends 0)
- Diferentes algoritmos de generación
- Animaciones durante generación (callback)

# Desglose módulos

- Objetos
    - Config
    - Celda
        - muros
    - Laberinto
        - ruta
        - celdas
        - entrada
        - salida
    - Ruta
        - celdas
    - ConfigVisual
        - (color, laberinto, si mostrar ruta o no)
- Parseo de la config (parser)
- Generación laberinto (generator)
- Busqueda de ruta mas corta (solver) 
- Salida fichero (printer)
- Salida visual (drawer)
- Empaquetado del módulo de generación
- Documentación y demás
