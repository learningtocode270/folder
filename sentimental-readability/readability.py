def main():
    text = input("Text: ")

    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    L = letters / words * 100
    S = sentences / words * 100
    index = 0.0588 * L - 0.296 * S - 15.8

    grade_level = round(index)

    updated_level(grade_level)

def count_letters(text):
    letters_counter = 0

    for i in range(len(text)):
        if (text[i].isalpha() == True):
            letters_counter += 1
    return letters_counter

def count_words(text):
    words_counter = 1

    for i in range(len(text)):
        if (text[i].isspace() == True):
            words_counter += 1
    return words_counter

def count_sentences(text):
    sentence_counter = 0

    punctuation = ['.', '!', '?']

    for i in range(len(text)):
        if (text[i] in punctuation):
            sentence_counter += 1
    return sentence_counter

def updated_level(grade_level):

    if (grade_level < 1):
        print("Before Grade 1")

    elif (grade_level > 16):
        print("Grade 16+")

    else:
        print(f"Grade: {grade_level}")



main()