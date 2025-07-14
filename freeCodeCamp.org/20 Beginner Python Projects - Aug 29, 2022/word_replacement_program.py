def replace_word():
    str = "hi guys, how are you?"
    print("hi guys, how are you?")
    word_to_replace = input("Enter the word you want to replace from the sentence above: ")
    word_replacement = input("Enter the word replacement: ")
    print(str.replace(word_to_replace, word_replacement))
    
replace_word()