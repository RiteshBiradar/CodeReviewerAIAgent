import subprocess

def run_flake8(file_path):
    result = subprocess.run(["flake8", file_path], capture_output=True, text=True)
    return result.stdout.strip().split("\n")

def run_bandit(file_path):
    result = subprocess.run(["bandit", "-r", file_path, "-f", "json"], capture_output=True, text=True)
    return result.stdout
