import subprocess
import pathlib
import shutil


def convert_puml_to_png(jar_location, input_file, output_folder, width):
    command = ['java', '-jar', jar_location, f'-p{width}', '-tpng', f'-o{output_folder}', input_file]
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = p.communicate()

    if p.returncode != 0:
        print('Error:', error.decode())
    else:
        print('Conversion successful. PNG saved at:', output_folder)


def cli_main():
    plantuml_path = pathlib.Path("D:/Programs/plantuml/plantuml-1.2023.6.jar")
    convert_list = {
        'diagram1': { 'source': 'diagram1.puml', 'width': 400, 'output': 'test1/diagram1_400.png' },
        'diagram2': { 'source': 'diagram2.puml', 'width': 800, 'output': 'test2/diagram2_800.png' },
    }

    script_path = pathlib.Path(__file__).parent.resolve()
    temp_output_folder = script_path.joinpath('tmp')
    output_folder_path = script_path.joinpath('../images/gen').resolve()
    output_folder_path.mkdir(exist_ok = True)
    width = 800  # Specify the desired width in pixels

    for key, value in convert_list.items():
        print(f'rendering {key}...')
        
        file_base_name = str(pathlib.Path(value['source']).stem)
        print(file_base_name)
        source_path = script_path.joinpath(value['source'])
        png_width = value['width']
        temp_path = temp_output_folder.joinpath(f'{file_base_name}.png')
        output_path = output_folder_path.joinpath(value['output'])

        convert_puml_to_png(
            jar_location = plantuml_path, 
            input_file = source_path, 
            output_folder = temp_output_folder, 
            width = png_width)

        output_path_folder = output_path.parent
        output_path_folder.mkdir(exist_ok = True)
        shutil.move(temp_path, output_path)


if __name__ == '__main__':
    cli_main()
