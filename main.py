import os
import streamlit as st

from keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the previously saved model
model = load_model('best_performing_model2.h5')

def predict_next_word(model, tokenizer, text, num_words=1):
    """
    Predict the next set of words using the trained model.

    Args:
    - model (keras.Model): The trained model.
    - tokenizer (Tokenizer): The tokenizer object used for preprocessing.
    - text (str): The input text.
    - num_words (int): The number of words to predict.

    Returns:
    - str: The predicted words.
    """
    for _ in range(num_words):
        # Tokenize and pad the text
        sequence = tokenizer.texts_to_sequences([text])[0]
        sequence = pad_sequences([sequence], maxlen=5, padding='pre')

        # Predict the next word
        predicted_probs = model.predict(sequence, verbose=0)
        predicted = np.argmax(predicted_probs, axis=-1)

        # Convert the predicted word index to a word
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break

        # Append the predicted word to the text
        text += " " + output_word

    return ' '.join(text.split(' ')[-num_words:])



while(True):
  user_input = st.text_input("Nyora manzwi mashanu:")


  if st.text_input == "0":
      print("chiitiko ichi chaperera pano .....")
      break

  else:
   try:
    text = user_input.split(" ")
    text = user_input[-5:]
    print(text)

    predicted_word = predict_next_word(model, tokenizer, text, num_words=1)
    print(f"inzwi rawanikwa rinoteera manzwi amaisa ndeiro: {predicted_word}")




   except Exception as e:
    print("Error: ", e)
    continue