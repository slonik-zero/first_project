from dotenv import load_dotenv
import os

def print_autor():
    load_dotenv(dotenv_path='name.env')
    autor = os.getenv("AUTOR")
    print(f"Autor: {autor}")

print_autor()
