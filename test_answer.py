import pytest
from answer import text_search


SENTENCE = ("Peter told me that peter the "
            "pickle piper piped a pitted pickle "
            "before he petered out. Phew!")


@pytest.mark.parametrize(
    "text_to_search, subtext, expected",
    [
        (SENTENCE, "Peter", [1, 20, 75]),
        (SENTENCE, "peter", [1, 20, 75]),
        (SENTENCE, "pi", [30, 37, 43, 51, 58]),
        (SENTENCE, "pick", [30, 58]),
        (SENTENCE, "z", []),
        (SENTENCE, "Peterz", [])
    ]
)
def test_text_search(text_to_search,
                     subtext,
                     expected):
    indices = text_search(text_to_search, subtext)
    assert indices == expected
