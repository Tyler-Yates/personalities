from typing import List

MBTI_PERSONALITIES = frozenset(
    [
        "ISTJ",
        "ISTP",
        "ISFJ",
        "ISFP",
        "INFJ",
        "INFP",
        "INTJ",
        "INTP",
        "ESTP",
        "ESTJ",
        "ESFP",
        "ESFJ",
        "ENFP",
        "ENFJ",
        "ENTP",
        "ENTJ",
    ]
)

FUNCTION_OPPOSITES = {
    "N": "S",
    "S": "N",
    "T": "F",
    "F": "T",
}


def convert_mbti_to_functions(mbti: str) -> List[str]:
    mbti = mbti.upper()
    if mbti not in MBTI_PERSONALITIES:
        raise ValueError(f"Input MBTI personality {mbti} is not correct.")

    # Function expressions ('i' vs 'e')
    function_expression = []
    check = 0 if mbti[0] == "E" else 1
    for i in range(4):
        if i % 2 == check:
            function_expression.append("e")
        else:
            function_expression.append("i")
    function_expression.extend(reversed(function_expression))

    # Primary functions
    functions = []
    extraverted_function = mbti[1] if mbti[3] == "P" else mbti[2]
    introverted_function = mbti[2] if mbti[3] == "P" else mbti[1]
    if mbti[0] == "E":
        functions.append(extraverted_function)
        functions.append(introverted_function)
    else:
        functions.append(introverted_function)
        functions.append(extraverted_function)
    functions.append(_get_opposite_function(functions[1]))
    functions.append(_get_opposite_function(functions[0]))

    # Shadow functions
    functions.extend(functions)

    return [f"{functions[i]}{function_expression[i]}" for i in range(8)]


def _get_opposite_function(function: str) -> str:
    return FUNCTION_OPPOSITES.get(function)
