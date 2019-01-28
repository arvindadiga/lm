

import pytest
from answer import text_search


sentence_1 = ("Peter told me that peter the "
              "pickle piper piped a pitted pickle "
              "before he petered out. Phew!")


@pytest.mark.parametrize(
    "text_to_search, subtext, expected",
    [
        (sentence_1, "Peter", [1, 20, 75]),
        (sentence_1, "peter", [1, 20, 75]),
        (sentence_1, "pi", [30, 37, 43, 51, 58]),
        (sentence_1, "pick", [30, 58]),
        (sentence_1, "z", []),
        (sentence_1, "Peterz", []),
        (sentence_1, "!", [92]),
        (sentence_1, "p", [1, 20, 30, 37, 39, 43, 45, 51, 58, 75, 88]),
        (sentence_1, "phew!", [88]),
        (sentence_1, "le", [34, 62])
    ]
)
def test_text_search(text_to_search,
                     subtext,
                     expected):
    indices = text_search(text_to_search, subtext)
    assert indices == expected


@pytest.mark.parametrize(
    "text_to_search, subtext, expected",
    [
        (456, "abc", []),
        ("abc", 456, []),
        (456, 123, [])
    ]
)
def test_invalid_input(text_to_search,
                       subtext,
                       expected):
    assert text_search(text_to_search, subtext) == expected