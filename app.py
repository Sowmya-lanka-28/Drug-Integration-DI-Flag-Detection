import streamlit as st
import pickle

# load model
model = pickle.load(open("di_flag_model.pkl", "rb"))
tfidf = pickle.load(open("tfidf.pkl", "rb"))

st.title("Healthcare DI Flag Detection")

st.write("Enter patient prescription description")

text = st.text_area("Enter description")

if st.button("Predict"):

    data = [text]

    vector = tfidf.transform(data)

    prediction = model.predict(vector)

    if prediction[0] == 1:
        st.error("⚠ Drug Interaction Risk Detected")
    else:
        st.success("✅ No Drug Interaction Risk")