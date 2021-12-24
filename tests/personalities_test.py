import pytest

from personalities.personalities import convert_mbti_to_functions, MBTI_PERSONALITIES


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


def test_all_personalities():
    for personality in MBTI_PERSONALITIES:
        converted_personality = convert_mbti_to_functions(personality)
        assert len(converted_personality) == 8
        assert all((item[0] in ["N", "S", "F", "T"]) for item in converted_personality)
        assert all((item[1] in ["i", "e"]) for item in converted_personality)


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
