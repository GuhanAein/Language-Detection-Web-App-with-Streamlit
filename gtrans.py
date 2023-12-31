import requests
import streamlit as st

url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"
api_key = "YOUR_API_KEY"  # Replace with your own RapidAPI key

st.title("Language Detection Web App")
text = st.text_input("Enter a text string")

if st.button("Detect Language"):
    payload = {"q": text}
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)

    if response.ok:
        result = response.json()
        detections = result["data"]["detections"]
        if detections:
            language = detections[0][0]["language"]
            confidence = detections[0][0]["confidence"]
            is_reliable = detections[0][0]["isReliable"]

            st.success("Language detected: {}".format(language))
            st.info("Confidence: {}".format(confidence))
            st.info("Is Reliable: {}".format(is_reliable))
        else:
            st.warning("No language detected.")
    else:
        st.error("Error occurred. Please try again.")
