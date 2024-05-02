import subprocess
import os
import sys


def run_command(command):
    subprocess.run(command, shell=True)


def main(project_directory):
    # Create the directory if it doesn't exist
    if not os.path.exists(project_directory):
        os.makedirs(project_directory)

    # Change to the specified directory
    os.chdir(project_directory)

    # Create virtual environment
    run_command(f'python -m venv myenv')

    # Activate virtual environment
    run_command('.\\myenv\\Scripts\\activate')

    # Install setuptools
    run_command('python -m pip install setuptools')

    # Create requirements.txt and .env files
    with open('requirements.txt', 'w') as f:
        f.write('python-dotenv')

    open('.env', 'a').close()
    open('create_project.py', 'a').close()
    open('README.MD', 'a').close()

    # Install requirements
    run_command('pip install -r requirements.txt')

    # List installed packages
    run_command('pip list')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python app_setup.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    main(directory)
