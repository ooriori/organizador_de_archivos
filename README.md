# 🗂️ Organizador de Archivos por Extensión Personalizada

Este proyecto es un script en Python que organiza automáticamente archivos en carpetas específicas según su extensión, siguiendo un orden personalizado que puedes modificar fácilmente.

## 📌 ¿Qué hace este script?

1. Crea una carpeta base en tu sistema (`~/carpeta_personal/appdepeliculas`).
2. (Opcional) Crea archivos de ejemplo con extensiones `.txt`, `.pdf`, `.jpg`, y `.png`.
3. Usa un diccionario para decidir en qué carpeta debe ir cada tipo de archivo.
4. Mueve los archivos a las carpetas correspondientes, agrupándolos por tipo.

## 🧠 Ejemplo de organización

Con esta configuración:

```python
orden_personalizado = {
    "txt": "documentos",
    "pdf": "documentos",
    "jpg": "imagenes",
    "png": "imagenes"
}

Los archivos se organizan así:

appdepeliculas/
├── documentos/
│   ├── archivo_1.txt
│   ├── archivo_2.pdf
│   └── ...
├── imagenes/
│   ├── archivo_1.jpg
│   ├── archivo_3.png
│   └── ...

🚀 Cómo usar
1. Clona este repositorio o copia el script

git clone https://github.com/ooriori/organizador_de_archivos
cd organizador-archivos

2. Ejecuta el script

python3 organizador.py

    Asegúrate de tener Python 3 instalado.

3. Personaliza la organización

Edita el diccionario orden_personalizado en el script:

orden_personalizado = {
    "mp3": "musica",
    "zip": "comprimidos",
    "py": "scripts",
    ...
}

4. Usa con tus propios archivos

    Copia archivos reales a la carpeta ~/carpeta_personal/appdepeliculas/.

    (Opcional) Comenta la parte del script que crea archivos de ejemplo.

    Vuelve a ejecutar el script.

🛠️ Requisitos

    Python 3.x

    Compatible con Linux (probado en Ubuntu), Windows y macOS

📄 Licencia

Este proyecto es de uso libre. Puedes modificarlo o integrarlo a tus flujos personales o empresariales.
