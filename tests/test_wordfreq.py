from module1.wordfreq import count_words


def test_counts_are_case_insensitive():
    assert count_words("Data data DATA test") == [("data", 3), ("test", 1)]


def test_punctuation_is_ignored():
    assert count_words("Hello, world! Hello.") == [("hello", 2), ("world", 1)]


def test_top_limits_results():
    assert len(count_words("a b c d e f g", top=3)) == 3


def test_empty_text_returns_empty_list():
    assert count_words("") == []