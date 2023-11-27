import pickle
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer

# load save model
model_fraud = pickle.load(open('model_fraud.sav','rb'))

tfidf = TfidfVectorizer

loaded_vec = TfidfVectorizer(decode_error="replace", vocabulary=set(pickle.load(open("new_selected_feature_tf-idf.sav", "rb"))))

with open("designing.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


# Menambahkan judul halaman
st.markdown("<h1 style= 'text-align: center;'>CHECK THIS</h1>", unsafe_allow_html=True )
st.markdown("---")
form=st.form("name")
clean_teks=form.text_input("Masukkan Teks SMS")



fraud_detection = ''
s_btn=form.form_submit_button(" Hasil Deteksi")
if s_btn:
    predict_fraud = model_fraud.predict(loaded_vec.fit_transform([clean_teks]))
    
    if (predict_fraud ==0):
        fraud_detection = 'SMS Normal'
    elif (predict_fraud ==1):
        fraud_detection = 'SMS Fraud'
    else :
        fraud_detection = 'SMS Promo'
        
s_scs=form.success(fraud_detection)
