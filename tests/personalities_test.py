import pytest

from personalities.personalities import convert_mbti_to_functions


def test_personality_conversion_intj():
    assert [
        "Ni",
        "Te",
        "Fi",
        "Se",
        "Ne",
        "Ti",
        "Fe",
        "Si",
    ] == convert_mbti_to_functions("INTJ")


def test_personality_conversion_enfp():
    assert [
        "Ne",
        "Fi",
        "Te",
        "Si",
        "Ni",
        "Fe",
        "Ti",
        "Se",
    ] == convert_mbti_to_functions("ENFP")


def test_personality_conversion_case():
    assert (
        convert_mbti_to_functions("EnTJ")
        == convert_mbti_to_functions("entj")
        == convert_mbti_to_functions("ENTJ")
    )


def test_invalid_mbti_input():
    with pytest.raises(ValueError):
        convert_mbti_to_functions("Blah")
    with pytest.raises(ValueError):
        convert_mbti_to_functions("JETN")
