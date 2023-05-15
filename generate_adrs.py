import subprocess
import pathlib
import shutil

def cli_main():
    script_path = pathlib.Path(__file__).parent.resolve()

    # Set the path to the directory containing your .qmd files
    qmd_directory = script_path.joinpath('decisions')

    # Set the path to the text file to which you want to append the filenames
    output_file = script_path.joinpath('decision_list.qmd')

    # Get a list of .qmd files in the directory
    qmd_files = qmd_directory.glob('*.qmd')

    # Get the filenames and append them to the output file
    with output_file.open('w') as output:
        for qmd_file in qmd_files:
            output.write(f'{{{{< include decisions/{qmd_file.name} >}}}}\n\n')

if __name__ == '__main__':
    cli_main()