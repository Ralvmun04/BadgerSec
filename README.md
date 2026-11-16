Markdown
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:0d1117,100:161b22&height=180&section=header&text=BadgerSec&fontSize=40&fontColor=ff9e64&fontAlignY=50&desc=Plataforma%20de%20Seguridad%20y%20Auditoría%20Ofensiva&descSize=15&descColor=8b949e" alt="BadgerSec Banner" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Security-Offensive%20%2F%20Defensive-orange.svg?style=for-the-badge&logo=kalilinux&logoColor=white" alt="Security">
  <img src="https://img.shields.io/badge/Status-Active-success.svg?style=for-the-badge" alt="Status">
</p>

---
# 🦡 BadgerSec
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

<img width="639" height="465" alt="BadgerSec" src="https://github.com/user-attachments/assets/83e43a8b-7dab-4917-a86d-c47e17c789c9" />


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

