import pandas as pd
import os
import base64


def encode_to_base64(file_path):
    """
    Encodes file to base64
    Input: file path
    Return: base64 string with input file
    """
    with open(file_path, "rb") as file:
        binary_data = file.read()
        base64_data = base64.b64encode(binary_data)
    return base64_data


def get_files_from(folder):
    """
    Get files with specific extensions(".jpeg", ".jpg", ".png", ".pdf") from directory
    Input: folder name
    Return: list of files
    """
    list_of_files = []
    for file in os.listdir("data"):
        if file.endswith((".jpeg", ".jpg", ".png", ".pdf")):
            list_of_files.append(file)
    return list_of_files


def get_text_from(file_path):
    """
    Get text from .txt files
    Input: file path
    Return: text
    """
    with open(file_path, "r") as file:
        text = file.readlines()
    return text


def create_dataset(folder):
    """
    Create .csv file with columns(name, file_path, extension, base64, original_text) and fill it data from folder
    Input: folder name
    Return: saves .csv file
    """
    list_of_dicts = []

    for file in get_files_from(folder):
        name = file.split(".")[0]
        file_path = folder + "/" + file
        extension = file.split(".")[-1]
        file_in_base64 = encode_to_base64(file_path)
        original_text = get_text_from(folder + "/" + name + "-baseline" + ".txt")
        list_of_dicts.append({"name": name, "file_path": file_path, "extension": extension, "base64": file_in_base64, "original_text": original_text})

    df = pd.DataFrame(list_of_dicts)
    df.to_csv(folder + "/" + "data.csv", index=False)
    pass


FOLDER = "data"
create_dataset(FOLDER)