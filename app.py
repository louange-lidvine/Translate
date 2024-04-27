from translate import Translator;
def translated_text(text,target_language):
    translator=Translator(to_lang=target_language)
    translation=translator.translate(text);
    return translation;
    
if __name__ == "__main__":
    text_to_translate = input("Enter the text you want to translate: ")
    target_language = input("Enter the target language: ")
    translated_text = translated_text(text_to_translate, target_language)
    print(translated_text)
