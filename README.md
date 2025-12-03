🦡 BadgerSec
The persisting penetration testing tool.
BadgerSec es una aplicación de terminal que se puede utilizar tanto en linux como en windows o ios.
Incluye escaneo TCP optimizado, banner grabbing, sistema de logs y soporte para instalación vía pip.


🚀 Características principales

- Escaneo rápido de puertos TCP comunes
- Banner grabbing inteligente
- Multithreading con ThreadPoolExecutor
- Instalable desde pip
- Sistema de logs automático en ~/.badgersec/logs/
- Arquitectura modular para que sea mas fácil de trabajar
- Fácil de extender con módulos adicionales
- Comando badgersec logs para revisar registros anteriores
- Uso de colores para que la visualizacion sea facil


📦 Instalación

  pip install badgersec


🎯 Uso básico





📄 Los logs se almacenan automáticamente en:

~/.badgersec/logs/

🧱 Estructura del proyecto
badgersec/
│── utils.py
│── main.py
│── logger.py
│── colors.py
│── __init__.py
│
├── scan/
│   ├── port_scanner.py
│   └── __init__.py
│
└── logs/


🧩 Añadir nuevos módulos

BadgerSec está a la espera de recibir nuevas versiones.

Para añadir un módulo nuevo:

Crear archivo dentro de la carpeta scan/
Exponerlo en scan/__init__.py
Añadir subcomando en main.py


⚠️ Aviso legal

BadgerSec es una herramienta creada con fines educativos y de auditoría.
El uso no autorizado contra sistemas que no te pertenecen es ilegal.
Úsala siempre con permiso.

🦡 Rafael Álvarez Muñoz

BadgerSec CLI Tool — The Persistence Penetration and Pentesting Hacking tool.
Versión: 1.0.0

