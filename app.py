# -*- coding: utf-8 -*-
"""app

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FadFQB95Rfu4dqqgHarggMmoo2gEnsS9
"""

import streamlit as st
import joblib

# Load model dan vectorizer
@st.cache_resource
def load_model_and_vectorizer():
    model = joblib.load('svm_model_smote_70.pkl')
    vectorizer = joblib.load('tfidf_vectorizer.pkl')
    return model, vectorizer

model, vectorizer = load_model_and_vectorizer()

# Judul aplikasi
st.title("SVM Model Deployment")

# Input dari pengguna
text_input = st.text_area("Masukkan teks untuk diprediksi:")

# Tombol prediksi
if st.button("Prediksi"):
    if text_input.strip():
        # Preprocessing dan prediksi
        input_vector = vectorizer.transform([text_input])
        prediction = model.predict(input_vector)
        st.write(f"Prediksi: **{'Positive' if prediction[0] == 1 else 'Negative'}**")
    else:
        st.write("Mohon masukkan teks untuk diprediksi.")