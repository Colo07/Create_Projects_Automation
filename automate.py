import os
import subprocess
import sys

# Definir el directorio base donde se crearán los proyectos
BASE_DIR = "C:\\Users\\Lenovo\\Desktop\\Proyectos"

# Función para ejecutar comandos en la terminal
def run_command(command):
    process = subprocess.run(command, shell=True)
    if process.returncode != 0:
        print(f"Error ejecutando comando: {command}")
        sys.exit(1)

# Crear directorio del proyecto
def create_project_directory(project_name):
    project_path = os.path.join(BASE_DIR, project_name)
    os.makedirs(project_path, exist_ok=True)
    print(f"Directorio del proyecto '{project_path}' creado.")
    return project_path

# Inicializar repositorio Git
def initialize_git(project_path):
    os.chdir(project_path)
    run_command("git init")
    print("Repositorio Git inicializado.")

# Configurar entorno virtual
def setup_virtualenv(project_path):
    run_command(f"python -m venv {os.path.join(project_path, 'venv')}")
    print("Entorno virtual creado.")

# Crear archivos de configuración básicos
def create_basic_files(project_path):
    with open(os.path.join(project_path, ".gitignore"), "w") as f:
        f.write("venv/\n__pycache__/\n*.pyc\n")
    print(".gitignore creado.")
    
    with open(os.path.join(project_path, "requirements.txt"), "w") as f:
        f.write("# Agrega tus dependencias aquí\n")
    print("requirements.txt creado.")

# Instalar dependencias comunes
def install_dependencies(project_path):
    if os.name == 'nt':  # Windows
        pip_executable = os.path.join(project_path, "venv", "Scripts", "pip")
    else:  # Unix (Linux/Mac)
        pip_executable = os.path.join(project_path, "venv", "bin", "pip")

    run_command(f"{pip_executable} install -r {os.path.join(project_path, 'requirements.txt')}")
    print("Dependencias instaladas.")

# Instrucciones para activar el entorno virtual
def print_activation_instructions(project_path):
    if os.name == 'nt':  # Windows
        activation_command = f"{project_path}\\venv\\Scripts\\activate"
    else:  # Unix (Linux/Mac)
        activation_command = f"source {project_path}/venv/bin/activate"

    print(f"Para activar el entorno virtual, ejecuta el siguiente comando:")
    print(f"{activation_command}")

# Abrir el proyecto en Visual Studio Code
def open_in_vscode(project_path):
    run_command(f"code {project_path}")
    print("Proyecto abierto en Visual Studio Code.")

# Función principal
def main(project_name):
    project_path = create_project_directory(project_name)
    initialize_git(project_path)
    setup_virtualenv(project_path)
    create_basic_files(project_path)
    install_dependencies(project_path)
    print(f"Proyecto '{project_name}' configurado correctamente en {project_path}.")
    print_activation_instructions(project_path)
    open_in_vscode(project_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python automate.py <nombre_del_proyecto>")
        sys.exit(1)
    
    project_name = sys.argv[1]
    main(project_name)
