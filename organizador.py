from pathlib import Path
import shutil 

base_path Path.home() / "carpeta_personal" / "appdepeliculas"
base_path.mkdir(parents=True, exist_ok=True)    


for ext in ["txt", "jpg", "png", "mp4"]:
    for i in range(3):
        file_path = base_path / f"archivo_{i + 1}.{ext}"
        file_path.touch()  # Create an empty file

orden_personalizado = {
    "txt": "documentos",
    "jpg": "imagenes",
    "png": "imagenes",
    "mp4": "videos"

}

for carpeta in set (orden_personalizado.values()):
    folder = base_path / carpeta
    folder.mkdir(exist_ok=True)
    
for archivo in base_path.glob("*.*"):
    extension = archivo.suffix[1:]  # quitar el punto "."
    if extension in orden_personalizado:
        carpeta_destino = base_path / orden_personalizado[extension]
        destino = carpeta_destino / archivo.name
        shutil.move(str(archivo), str(destino))

print("Archivos organizados según el orden personalizado.")