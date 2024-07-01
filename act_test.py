from datetime import datetime

now_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
content = f"Last update: {now_string}"

with open("README.md", "w") as file:
    file.write(content)