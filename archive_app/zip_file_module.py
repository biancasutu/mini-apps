import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    destination_path = pathlib.Path(dest_dir, 'my_archive.zip')
    with zipfile.ZipFile(destination_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)   # trunchiaza/extrage din tot path-ul doar numele fisierelor de arhivat pt 
                                                # a nu arhiva si folderele in care se afla acestea -> arhiveaza direct fisierele
            archive.write(filepath, arcname=filepath.name)


def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


# 'w' - fol write mode pt a crea arhiva
# 'r' - fol read mode pt a citi arhiva si a extrage continutul ei

