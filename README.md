# DataAugmentation_NLP

Abstract:
Increasing the volume of data enhances model performance, yet annotating large datasets proves costly and time-intensive. Hence, effective data augmentation becomes crucial for enhancing model accuracy.
Text augmentation poses a challenge in NLP due to the intricate nature of language.
The nlpaug library offers various high-performance text augmentation algorithms, capable of substantially improving NLP model performance.

* Option 1: Pre-trained word embedding models like Word2Vec,FastText,GloVe are used,which are beneficial for various NLP tasks, as these models capture semantic information about words and can be used as feature 
  representations in downstream tasks like text classification, sentiment analysis, and machine translation.
* Option 2: Substitute or insert word by contextual word embeddings using transformer models like BERT,DistilBERT and RoBERTA.
* Option 3: Substitute or insert word by synonym using lexical database 'wordnet'.
* Option 4: Substitute or insert word using back translation (By translating the original text into another language and then translating it back to the original language, variations and potential errors introduced 
  during the translation process can create diverse versions of the original text. )



