import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "DIGITE O CAMINHO DA PASTA DE DOWNLOAD (USE " / ") no VSC"
# to_dir = "DIGITE A PASTA DE CAMINHO DE DESTINO (USE " / ") no VSC"

from_dir = "C:/Users/USUARIO/Downloads"
to_dir = "C:/Users/USUARIO/Desktop/Luciano Filho Arquivos/Byjus/Aula 103 - Python Movendo Arquivos"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}


# Classe Gerenciadora de Eventos

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        raiz, ext = os.path.splitext(event.src_path)
        time.sleep(1)
        print(event)
        for chave, value in dir_tree.items(): 
            time.sleep(1)
            if ext in value:
                file = os.path.basename(event.src_path)
                shutil.move(from_dir + '/' + file, to_dir + '/' + chave + '/' + file)
                time.sleep(1)



# Inicialize a Classe Gerenciadora de Eventos
event_handler = FileMovementHandler()

# Inicialize o Observer
observer = Observer()

# Agende o Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Inicie o Observer
observer.start()


while True:
    time.sleep(5)
    print("executando...")
