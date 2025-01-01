import subprocess

while True:  
    subprocess.run('ollama pull llama3', shell=True)
