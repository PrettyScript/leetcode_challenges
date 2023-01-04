def convert_question_to_camel_case(question: str):
    question = question.lower().replace(".", "").split(" ")

    new_str = ""
    for i in question:
        new_str += i + "_"

    return new_str


print(convert_question_to_camel_case("819. Most Common Word"))
