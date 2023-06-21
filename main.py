from pathlib import Path

chemin = Path("X:\Docstring\projet tri fichiers\sources_enonce\data")

extensions = {".mp3": "Musique",
              ".wav": "Musique",
              ".flac": "Musique",
              ".avi": "Videos",
              ".mp4": "Videos",
              ".gif": "Videos",  
              ".bmp": "Images",
              ".png": "Images",
              ".jpg": "Images",
              ".txt": "Documents",
              ".pptx": "Documents",
              ".csv": "Documents",
              ".xls": "Documents",
              ".odp": "Documents",
              ".pages": "Documents",
            }

chemin_dossier_source = r"X:\Docstring\projet tri fichiers\sources_enonce\data"
dossier_source = Path(chemin_dossier_source)

def transfert_fichier(chemin_cible):
  dossier_cible = Path(chemin_cible)
  dossier_cible.mkdir(exist_ok=True)
  fichier.rename(dossier_cible / fichier.name)

for fichier in dossier_source.iterdir():  # Sert à itérer sur les fichiers d'un dossier Path
  suffixe = fichier.suffix
  if suffixe in extensions:
    transfert_fichier(fr"X:\Docstring\projet tri fichiers\sources_enonce\data\{extensions[suffixe]}")
  else:
    transfert_fichier(chemin_dossier_source + "\divers")
