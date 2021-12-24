from .personalities import convert_mbti_to_functions, MBTI_PERSONALITIES


def calculate_functions(mbti: str):
    functions = convert_mbti_to_functions(mbti)
    print(mbti)
    for function in functions:
        print(function)
    print()


def main():
    for mbti in MBTI_PERSONALITIES:
        calculate_functions(mbti)


if __name__ == "__main__":
    main()
