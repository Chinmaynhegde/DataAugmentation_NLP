import streamlit as st
from indicnlp.tokenize import indic_tokenize
from googletrans import Translator

# Hypothetical synonym dictionary for demonstration purposes
synonym_dict = {
    'मैं': ['मै', 'मुझे', 'मुझको'],
    'आज': ['इस दिन', 'आज के दिन'],
    'स्कूल': ['विद्यालय', 'स्कूल इंडिया'],
    'नहीं': ['नही', 'नहीं है', 'ना'],
    'जा': ['चला जा', 'जाना', 'चला', 'बाहर निकल'],
    'रहा': ['रह', 'रहे', 'रहे हैं'],
    'हूँ': ['हूँ', 'हैं', 'रहे हैं']
}

# Function to perform data augmentation by token substitution using synonym dictionary
def augment_text_with_synonyms(text, synonym_dict):
    tokens = indic_tokenize.trivial_tokenize(text, lang='hi')
    augmented_tokens = []
    for token in tokens:
        # Substitute token with a random synonym if available, else keep the original token
        augmented_token = synonym_dict.get(token, [token])[0]
        augmented_tokens.append(augmented_token)
    return ' '.join(augmented_tokens)

# Function to translate text from Hindi to Arabic
def translate_to_arabic(text):
    translator = Translator()
    translated_text = translator.translate(text, src='hi', dest='ar')
    return translated_text.text

# Function to translate text from Arabic to Hindi
def translate_to_hindi(text):
    translator = Translator()
    translated_text = translator.translate(text, src='ar', dest='hi')
    return translated_text.text

# Function for back translation
def back_translate(text, src_lang, target_lang):
    if src_lang != target_lang:
        translated_text = translate_to_arabic(text) if src_lang == 'hi' else translate_to_hindi(text)
        translated_back = translate_to_hindi(translated_text) if target_lang == 'hi' else translate_to_arabic(translated_text)
    else:
        translated_back = augment_text_with_synonyms(text, synonym_dict)
    return translated_back

# Streamlit app
def main():
    st.title("NLP Data Augmentation for Regional Languages")

    st.write(
        "This app performs data augmentation on text input using different methods such as synonym substitution, translation, and back translation.")

    # Text input
    text = st.text_area("Enter Hindi text", "")

    # Select augmentation method
    method = st.selectbox("Choose augmentation method", ["Synonym Substitution", "Translation-Based", "Back Translation"])

    if st.button("Augment Text"):
        if method == "Synonym Substitution":
            augmented_text = augment_text_with_synonyms(text, synonym_dict)
        elif method == "Translation-Based":
            # Translate to Arabic and back to Hindi
            arabic_text = translate_to_arabic(text)
            augmented_text = translate_to_hindi(arabic_text)
        elif method == "Back Translation":
            # Back translate the text
            augmented_text = back_translate(text, 'hi', 'hi')  # Just an example 
        # Display results
        st.write("Original Text:", text)
        st.write("Augmented Text:", augmented_text)

if __name__ == "__main__":
    main()
