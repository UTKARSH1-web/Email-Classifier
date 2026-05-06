import streamlit as st
from src.preprocess import load_data, preprocess_data
from src.model import train_model, predict

# Add aesthetic styling
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #0f172a;
    background-image: 
        radial-gradient(at 0% 0%, hsla(253,16%,7%,1) 0, transparent 50%), 
        radial-gradient(at 50% 0%, hsla(225,39%,30%,1) 0, transparent 50%), 
        radial-gradient(at 100% 0%, hsla(339,49%,30%,1) 0, transparent 50%);
}
[data-testid="stHeader"] {
    background: transparent;
}
[data-testid="stMarkdownContainer"] p, [data-testid="stMarkdownContainer"] h1, [data-testid="stMarkdownContainer"] h3 {
    color: #f8fafc !important;
}
.stTextArea textarea {
    background-color: rgba(255, 255, 255, 0.05) !important;
    color: white !important;
    border-radius: 10px;
    border: 1px solid rgba(255, 255, 255, 0.2);
}
.stButton > button {
    background: linear-gradient(90deg, #4f46e5, #ec4899);
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: bold;
    transition: all 0.3s ease;
}
.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0 5px 15px rgba(236, 72, 153, 0.4);
    color: white;
    border-color: transparent;
}
</style>
""", unsafe_allow_html=True)

# Load data
df = load_data("data/spam.csv")
df = preprocess_data(df)

# Train model
model, tfidf = train_model(df)

# UI
st.title("📧 Spam Email Classifier")

st.write("Enter a message to check whether it's spam or not")

user_input = st.text_area("Message")

if st.button("Check"):
    if user_input.strip() != "":
        result = predict(user_input, model, tfidf)
        st.subheader(result)
    else:
        st.warning("Please enter a message")