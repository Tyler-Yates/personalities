from .personalities import convert_mbti_to_functions


def calculate_functions(mbti: str):
    functions = convert_mbti_to_functions(mbti)
    print(mbti)
    for function in functions:
        print(function)


def main():
    calculate_functions("INTJ")


if __name__ == "__main__":
    main()
