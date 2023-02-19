"""
Tests for the Count Words Program
"""

from main import text_as_a_list, count_words_in_text, sort_word_counts

SAMPLE = """Hello world. Welcome to the World Wide Web where everyone in the world says hello!"""


def test_text_as_a_list():
    """Tests that we get back a list with no punctuation in it"""

    clean_text = text_as_a_list(SAMPLE)
    for word in clean_text:
        assert "." not in word
        assert "!" not in word


def test_count_words():
    """Test that the counts of the top words is as expected"""
    text = text_as_a_list(SAMPLE)
    counts = count_words_in_text(text)
    assert counts.get("world") == 3
    assert counts.get("hello") == 2
    assert counts


def test_sort_words():
    """Test that the sort order is correct"""
    text = text_as_a_list(SAMPLE)
    counts = count_words_in_text(text)
    sorted_words = sort_word_counts(counts)
    assert sorted_words[0] == ("world", 3)
    assert sorted_words[1] == ("hello", 2)
