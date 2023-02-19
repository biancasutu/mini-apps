import PySimpleGUI as sg
from zip_file_module import make_archive, extract_archive


label1 = sg.Text('Browse files                 ')
input1 = sg.Input()
choose_button1 = sg.FilesBrowse('Choose', key='files')

# PySimpleGUI.FilesBrowse este un buton built-in care permite cautarea direct 
# prin fisierele din device (fara a da path ul), doar selectand fisierul
# !!!! se pot alege simultan mai multe fisiere (atentie intre FileBrowse si FilesBrowse)

label2 = sg.Text("Select destination folder")
input2 = sg.Input()
choose_buttton2 = sg.FolderBrowse("Choose", key='folder')  # cauta in fisiere pt a selecta fisierul de export(unde se salveaza arhiva)

compress_button = sg.Button("Compress")
extract_button = sg.Button('Extract')

output_label_after_compression = sg.Text(key='output_compr', text_color='green')
output_label_after_extraction = sg.Text(key='output_extr', text_color='green')

col1 = [[label1], [label2]]
col2 = [[input1], [input2]]
col3 = [[choose_button1], [choose_buttton2]]

window = sg.Window("File compressor & extractor", layout=[[sg.Column(col1), sg.Column(col2), sg.Column(col3)],
                                                        [compress_button, output_label_after_compression],
                                                        [extract_button, output_label_after_extraction]])


while True:
    event, values = window.read()
    match event:
        case 'Compress':
            print(event, values)
            filepaths = values['files'].split(";")
            folder = values['folder']
            make_archive(filepaths, folder)  # am apelat functia din zip_file_module
            window['output_compr'].update(value='Compression completed.')
        
        case 'Extract':
            archive_path = values['files']
            dest_dir = values['folder']
            extract_archive(archive_path, dest_dir)
            window['output_extr'].update(value='Extraction completed.')
        case sg.WINDOW_CLOSED:
            break


window.close()
