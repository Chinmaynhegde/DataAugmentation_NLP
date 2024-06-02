# Import necessary libraries
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
    'हूँ': ['हूँ', 'हैं', 'रहे हैं'],
    'वह': ['वो', 'उसने', 'उसे'],
    'किताब': ['पुस्तक', 'ग्रंथ', 'पुस्तिका'],
    'खाना': ['भोजन', 'आहार', 'भोजन करना'],
    'खेल': ['खेलना', 'मैच', 'खेल-कूद'],
    'पानी': ['जल', 'नीर', 'पेय'],
    'घर': ['मकान', 'आवास', 'निवास'],
    'गाड़ी': ['वाहन', 'कार', 'मोटर'],
    'दोस्त': ['मित्र', 'सखा', 'मित्रता'],
    'पेड़': ['वृक्ष', 'तरु', 'पादप'],
    'बाजार': ['मार्केट', 'हाट', 'बाज़ार'],
    'काम': ['श्रम', 'कार्य', 'कार्यक्रम'],
    'बड़ा': ['विशाल', 'प्रचंड', 'विशालकाय'],
    'सुंदर': ['सुन्दर', 'खूबसूरत', 'मनोहर'],
    'तेज़': ['तेज', 'द्रुत', 'शीघ्र'],
    'धीरे': ['मंद', 'धीमा', 'शांत'],
    'लड़का': ['बालक', 'बच्चा', 'छात्र'],
    'लड़की': ['बालिका', 'बच्ची', 'छात्रा'],
    'सड़क': ['मार्ग', 'रास्ता', 'पथ'],
    'शहर': ['नगर', 'महानगर', 'कस्बा'],
    'गाना': ['गीत', 'संगीत', 'भजन'],
    'सोना': ['निद्रा लेना', 'विस्राम करना', 'आराम करना'],
    'माता': ['मां', 'माताजी', 'जननी'],
    'पिता': ['पिताजी', 'बाबा', 'जनक'],
    'भाई': ['भ्राता', 'सहोधर', 'अनुज'],
    'बहन': ['भगिनी', 'अनुजा', 'बहनजी'],
    'प्रेम': ['प्यार', 'मोहब्बत', 'स्नेह'],
    'अध्यापक': ['शिक्षक', 'गुरु', 'प्राध्यापक'],
    'विद्यार्थी': ['छात्र', 'शिष्य', 'विद्यार्थिनी'],
    'पुस्तकालय': ['लाइब्रेरी', 'ग्रंथालय', 'किताबघर'],
    'अस्पताल': ['चिकित्सालय', 'हॉस्पिटल', 'नर्सिंग होम'],
    'कंप्यूटर': ['संगणक', 'कम्प्यूटर', 'अभिकलक'],
    'मोबाइल': ['फोन', 'स्मार्टफोन', 'हैंडसेट'],
    'विमान': ['एरोप्लेन', 'हवाई जहाज', 'वायुयान'],
    'समाचार': ['खबर', 'समाचार पत्र', 'अखबार'],
    'आनंद': ['खुशी', 'मजा', 'सुख'],
    'खेलना': ['क्रीड़ा करना', 'मैदान में खेलना', 'खेल में भाग लेना'],
    'देखना': ['निहारना', 'ताकना', 'मुआयना करना'],
    'बोलना': ['कहना', 'बतियाना', 'प्रवचन देना'],
    'लिखना': ['लेखन करना', 'लिपिबद्ध करना', 'नोट करना'],
    'पढ़ना': ['अध्ययन करना', 'पाठ करना', 'ग्रंथ पढ़ना'],
    'चलना': ['गति करना', 'चाल करना', 'सैर करना'],
    'दौड़ना': ['भागना', 'धावन करना', 'तेज़ दौड़ना'],
    'संगीत': ['म्यूजिक', 'राग', 'स्वर'],
    'चित्र': ['फोटो', 'पेंटिंग', 'आकृति'],
    'नृत्य': ['डांस', 'नाचना', 'नृत्य करना'],
    'गपशप': ['बातचीत', 'चर्चा', 'वार्तालाप'],
    'यात्रा': ['सफर', 'सैर', 'ट्रिप'],
    'खुशी': ['मुस्कान', 'हर्ष', 'आनंद'],
    'दुख': ['ग़म', 'वेदना', 'पीड़ा'],
    'सुबह': ['प्रातः', 'प्रभात', 'बिहान'],
    'शाम': ['सायंकाल', 'संध्या', 'इवनिंग'],
    'रात': ['रात्रि', 'निशा', 'नाइट'],
    'दिन': ['दिवस', 'वार', 'डे'],
    'समय': ['वक्त', 'काल', 'टाइम'],
    'मित्र': ['दोस्त', 'सखा', 'साथी'],
    'परिवार': ['कुटुंब', 'परिजन', 'फैमिली'],
    'बचपन': ['बाल्यावस्था', 'शैशव', 'बालपन'],
    'युवा': ['किशोर', 'जवान', 'युवक'],
    'वृद्ध': ['बूढ़ा', 'प्राचीन', 'वयोवृद्ध'],
    'मृत्यु': ['देहांत', 'मौत', 'निधन'],
    'प्राकृतिक': ['नेचुरल', 'स्वाभाविक', 'प्राकृतिक'],
    'कला': ['आर्ट', 'कला-कौशल', 'शिल्प'],
    'विज्ञान': ['साइंस', 'विज्ञानशास्त्र', 'विज्ञान विधा'],
    'इतिहास': ['हिस्ट्री', 'अतीत', 'इतिहास-ग्रंथ'],
    'भविष्य': ['आगामी', 'आने वाला समय', 'प्रवृत्ति'],
    'वर्तमान': ['अभी', 'मौजूदा', 'प्रेसेंट'],
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

# Function to sequentially augment text using both synonym substitution and translation-based methods
def augment_text_sequentially(text, synonym_dict):
    # Augment text with synonym substitution
    augmented_text_synonym = augment_text_with_synonyms(text, synonym_dict)
    # Translate augmented text to Arabic
    arabic_text = translate_to_arabic(augmented_text_synonym)
    # Translate Arabic text back to Hindi
    augmented_text_translated = translate_to_hindi(arabic_text)
    return augmented_text_translated

# Streamlit app
def main():
    st.title("NLP Data Augmentation for Regional Languages")

    st.write(
        "This app performs data augmentation on text input using both synonym substitution and translation-based methods.")

    # Text input
    text = st.text_area("Enter Hindi text", "")

    # Select augmentation method
    method = st.selectbox("Choose augmentation method", ["Synonym Substitution", "Translation-Based", "Sequential"])

    if st.button("Augment Text"):
        if method == "Synonym Substitution":
            augmented_text = augment_text_with_synonyms(text, synonym_dict)
        elif method == "Translation-Based":
            # Translate to Arabic and back to Hindi
            arabic_text = translate_to_arabic(text)
            augmented_text = translate_to_hindi(arabic_text)
        elif method == "Sequential":
            augmented_text = augment_text_sequentially(text, synonym_dict)

        # Display results
        st.write("Original Text:", text)
        st.write("Augmented Text:", augmented_text)

# Run the app
if __name__ == "__main__":
    main()
