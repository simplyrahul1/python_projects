## Change limiter from "space" to "-"

def change_limiter(my_sentence):
    new_sentence = my_sentence.split(" ")
    new_sentence = "-".join(new_sentence)
    return (new_sentence)

if __name__ == '__main__':
    input_sentences = ["This is great day", "meeting is boring", "Awesome !!!"]
    for input_element in input_sentences:
        RETURN_ELEMENT = change_limiter(input_element)
        print(RETURN_ELEMENT)
