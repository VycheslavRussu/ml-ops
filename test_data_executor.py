from thefuzz import fuzz
import pandas as pd
from statistics import mean
from models_api.yandex_ocr.yandex_ocr_api import file_base64_to_text
import pytest


def test_create_dataset(file_path):
    """
    Run through dataset and compare original_text(text selected by hands) with found_text(text recieved from YandexOCR)
    Input: Path to .csv file with data
    Output: Mean score of similarity between all original_text and found_text values
    """
    ocr_score = float
    ocr_score_list = []

    df = pd.read_csv(file_path)

    for row in df.itertuples():
        found_text = file_base64_to_text(row.base64, row.extension)
        original_text = row.original_text
        score = fuzz.token_sort_ratio(original_text, found_text)
        ocr_score_list.append(score)

    ocr_score = round(mean(ocr_score_list))

    return ocr_score


FILE_PATH = "data/data.csv"
print(f"Точность модели: {test_create_dataset(FILE_PATH)}%")
