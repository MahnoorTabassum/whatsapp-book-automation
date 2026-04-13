import time
import pyautogui
import streamlit as st 
import pandas as pd
import pywhatkit as kit

st.set_page_config(page_title="WhatsApp Book Automation")

st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
h1 {
    text-align: center;
    color: #25D366;
}
.stButton>button {
    background-color: #25D366;
    color: white;
    border-radius: 8px;
    height: 45px;
    width: 100%;
    font-size: 16px;
}
.stTextInput, .stTextArea {
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

st.title("WhatsApp Book Automation System")

st.markdown("---")

upload = st.file_uploader(" Upload Excel or CSV", type=["xlsx", "csv"])

storeName = st.text_input("Store Name", "Liberty Books Store")
customMessage = st.text_area("Custom Message", "Check out this amazing book!")

st.markdown("---")

if upload is not None:
    if upload.name.endswith(".csv"):
        df = pd.read_csv(upload)
    else:
        df = pd.read_excel(upload)

    st.success("Contacts Uploaded Successfully")
    st.dataframe(df)

    if st.button(" Send Message"):
        for index, row in df.iterrows():
            phoneNumber = f"+92{row['Phone']}"
            message = f"""Hi {row['Name']}
Book: {row['Book_Name']}
Price: {row['Price']}pkr
Buy Here: {row['Link']}
From: {storeName}
Limited stock!!"""

            kit.sendwhatmsg_instantly(phoneNumber, message, wait_time=35)
            time.sleep(15)  
            pyautogui.click()  
            pyautogui.press("enter")
            print("Sent")
            time.sleep(5)
            pyautogui.press("enter")