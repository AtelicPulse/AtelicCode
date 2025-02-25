import subprocess


def detect_bugs(code):
    with open("temp.py", "w") as f:
        f.write(code)

    result = subprocess.run(["pylint", "temp.py"], 
                            capture_output=True, text=True)
    return result.stdout
