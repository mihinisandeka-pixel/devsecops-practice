import subprocess

def greet(name):
    return f"Hello, {name}!"

print(greet("DevSecOps Learner"))

subprocess.run(["echo ","Hello"], check=True)
