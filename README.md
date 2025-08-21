🐍 Snake Game
Este proyecto es una implementación del clásico juego de la serpiente (Snake) utilizando Python y la librería Pygame.
Incluye:
Gráficos personalizados (cabeza, cuerpo, cola y fruta).
Sonidos que se reproducen al comer frutas.
Fuentes externas para la interfaz del puntaje.
Diagramas de flujo que explican visualmente las principales funcionalidades y la arquitectura lógica del juego.

🎮 Características principales
✅ Control de la serpiente con las teclas de flecha.
✅ Crecimiento al comer frutas.
✅ Finalización al chocar con los bordes o consigo misma.
✅ Sonido de "crunch" al comer.
✅ Interfaz visual con sprites de serpiente y fruta.
✅ Diagramas de flujo documentando procesos clave.

📁 Estructura del repositorio
Snake-Game/
│── Snake1.py               # Código fuente principal
│── README.md              # Documentación del proyecto
│
├── diagramas/             # Diagramas de flujo de las funcionalidades
│   ├── diagrama_inicio.png
│   ├── diagrama_movimiento.png
│   ├── diagrama_fruta.png
│   └── ...
│
├── Graficos/              # Sprites del juego
│   ├── head_up.png
│   ├── head_down.png
│   ├── head_left.png
│   ├── head_right.png
│   ├── body_vertical.png
│   ├── body_horizontal.png
│   ├── body_tl.png
│   ├── body_tr.png
│   ├── body_bl.png
│   ├── body_br.png
│   ├── tail_up.png
│   ├── tail_down.png
│   ├── tail_left.png
│   ├── tail_right.png
│   └── apple.png
│
├── Sound/                 # Efectos de sonido
│   └── crunch.wav
│
└── Font/                  # Tipografía utilizada
    └── PoetsenOne-Regular.ttf

🛠️ Requisitos
Python 3.7 o superior
Pygame (2.6.1 o superior)
Instala Pygame con:
pip install pygame==2.6.1

🚀 Cómo ejecutar el juego
Clona este repositorio o descarga el proyecto:
git clone [https://github.com/davidegui/Snake-Game-.git]
cd Snake1-Game
Asegúrate de tener Python y Pygame instalados.
Ejecuta el juego con:
python Snake1.py

📊 Diagramas de flujo
En la carpeta diagramas/ encontrarás ilustraciones de los principales procesos:
Proceso de inicio del juego.
Movimiento de la serpiente.
Detección de colisiones (fruta, bordes y cuerpo propio).
Generación de frutas.
Condición de victoria (sin espacio para frutas nuevas).

👤 Autor
David Eguiguren
