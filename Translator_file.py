from translate import Translator
translator = Translator(to_lang="ja")
with open("Translator_file.txt",mode='r') as my_file:
    text = my_file.read()
    translation = translator.translate(text)
    print(translation)
    # print(my_file.readlines())