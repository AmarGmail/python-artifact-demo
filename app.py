from datetime import datetime

print("python artifact demo")

with open("result.txt", "w") as file:
  file.write("Hello from github\n")
  file.write("This file create from github\n")
  file.write("Generated Time: {datetime.now()}\n")

print("print from result.txt\n")
