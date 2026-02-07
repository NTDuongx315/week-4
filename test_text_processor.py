import pytest
from text_processor import (
    count_words,
    capitalize_words,
    reverse_text,
    get_word_count,
    contains_word,
    find_longest_word,
    filter_short_words,
    save_text_to_file,
    read_text_from_file,
    count_sentences,
    get_average_word_length,
    remove_punctuation
)

# Part 1: Basic Fixture

@pytest.fixture
def sample_text():
    return "the quick brown fox"


def test_count_words(sample_text):
    assert count_words(sample_text) == 4


def test_capitalize_words(sample_text):
    assert capitalize_words(sample_text) == "The Quick Brown Fox"


def test_reverse_text(sample_text):
    assert reverse_text(sample_text) == "xof nworb kciuq eht"


# Part 2: Multiple Fixtures

@pytest.fixture
def paragraph():
    return "Python is great. Python is powerful. Python is fun."


@pytest.fixture
def search_word():
    return "python"


def test_get_word_count(paragraph):
    expected = {
        'python': 3,
        'is': 3,
        'great.': 1,
        'powerful.': 1,
        'fun.': 1
    }
    assert get_word_count(paragraph) == expected


def test_contains_word(paragraph, search_word):
    assert contains_word(paragraph, search_word) is True


# Part 3: List Fixture

@pytest.fixture
def word_list():
    return ["cat", "elephant", "dog", "butterfly", "ant"]


def test_find_longest_word(word_list):
    assert find_longest_word(word_list) == "butterfly"


def test_filter_short_words(word_list):
    assert filter_short_words(word_list, 4) == ["elephant", "butterfly"]


# Part 4: Built-in Fixture tmp_path

def test_save_text_to_file(tmp_path):
    file_path = tmp_path / "test.txt"
    save_text_to_file("Hello, World!", file_path)

    content = file_path.read_text()
    assert content == "Hello, World!"


def test_read_text_from_file(tmp_path):
    file_path = tmp_path / "input.txt"
    file_path.write_text("Test content")

    result = read_text_from_file(file_path)
    assert result == "Test content"


# Part 5: Fixture Using Another Fixture

@pytest.fixture
def greeting():
    return "Hello"


@pytest.fixture
def name():
    return "Alice"


@pytest.fixture
def full_greeting(greeting, name):
    return f"{greeting}, {name}!"


def test_full_greeting(full_greeting):
    assert full_greeting == "Hello, Alice!"


# Part 6: Challenge - Text Analysis

@pytest.fixture
def essay():
    return "The cat sat. The dog ran. The bird flew."


@pytest.fixture
def simple_sentence():
    return "Hello, world! How are you?"


@pytest.fixture
def cleaned_text():
    return "Hello world How are you"


def test_count_sentences(essay):
    assert count_sentences(essay) == 3


def test_get_average_word_length(essay):
    avg = get_average_word_length(essay)
    assert pytest.approx(avg, 0.01) == 29 / 9


def test_remove_punctuation(simple_sentence, cleaned_text):
    assert remove_punctuation(simple_sentence) == cleaned_text
