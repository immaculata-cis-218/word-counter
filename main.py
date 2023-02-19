"""
Program to count Words
Andrew Bowman
"""
import json
from string import punctuation


def text_as_a_list(input_text: str) -> list:
    """
    Return the text as a list removing any punctuation.
    """
    input_text = input_text.lower()
    input_text = input_text.replace(".", "")
    input_text = input_text.strip(punctuation)
    input_text = input_text.split(" ")
    return input_text


def count_words_in_text(words_list: list) -> dict:
    """
    Returns a list of words in the text and how many times that they appear.
    """

    counts = {}
    for word in words_list:
        if not counts.get(word):
            counts[word] = 0
        counts[word] += 1
    return counts


def sort_word_counts(counts: dict) -> list:
    """
    Create a list of the top words used
    """

    def sort_by_count(item: tuple):
        return item[1]

    counts = sorted(counts.items(), key=sort_by_count, reverse=True)
    return counts


if __name__ == "__main__":
    with open("war-and-peace.txt", "r", encoding="UTF-8") as file:
        text = file.read()
    words = text_as_a_list(text)
    unique_words = count_words_in_text(words)
    top_words = sort_word_counts(unique_words)
    formatted = json.dumps(top_words[0:25], indent=4)
    print(formatted)
