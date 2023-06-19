import subprocess
import glob, os

folder_path = r"needchating"
file_pattern = "*.pdf"
pdf_paths = glob.glob(os.path.join(folder_path, file_pattern))

for pdf_path in pdf_paths:
    subprocess.run(["python", "chat_paper.py", "--pdf_path", pdf_path])
