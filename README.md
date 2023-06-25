# Language-Detection-Web-App-with-Streamlit
This repository contains a Language Detection Web App built with Python and Streamlit. The web app allows users to enter a text string, and it utilizes the Google Translate API to detect the language of the input text

I have taken the API Key from Rapid API and you can also fetch from it which is free for 500 per month and it detects the language as like

![Screenshot 2023-06-25 232756](https://github.com/GuhanAein/Language-Detection-Web-App-with-Streamlit/assets/102289063/4e7f9970-6de6-4695-874f-f9500cbf8c76)

As it says en as english and you can see the codes at the end of this file

I have tried saying tamil words and telugu with english text it even detects it and also with the tamil letters like this
![image](https://github.com/GuhanAein/Language-Detection-Web-App-with-Streamlit/assets/102289063/3c5a515b-6a1e-4bb3-9476-44e99828f6ae)
The same in the tamil text
![image](https://github.com/GuhanAein/Language-Detection-Web-App-with-Streamlit/assets/102289063/435df2c1-d88e-42dc-8bd6-c6195ed3d4d3)

I am in idea of developing it by making it translate by other APIs

And the code for languages are:
- Afrikaans: af
- Albanian: sq
- Amharic: am
- Arabic: ar
- Armenian: hy
- Azerbaijani: az
- Basque: eu
- Belarusian: be
- Bengali: bn
- Bosnian: bs
- Bulgarian: bg
- Catalan: ca
- Cebuano: ceb (ISO-639-2)
- Chinese (Simplified): zh-CN (BCP-47)
- Chinese (Traditional): zh-TW (BCP-47)
- Corsican: co
- Croatian: hr
- Czech: cs
- Danish: da
- Dutch: nl
- English: en
- Esperanto: eo
- Estonian: et
- Finnish: fi
- French: fr
- Frisian: fy
- Galician: gl
- Georgian: ka
- German: de
- Greek: el
- Gujarati: gu
- Haitian Creole: ht
- Hausa: ha
- Hawaiian: haw (ISO-639-2)
- Hebrew: he**
- Hindi: hi
- Hmong: hmn (ISO-639-2)
- Hungarian: hu
- Icelandic: is
- Igbo: ig
- Indonesian: id
- Irish: ga
- Italian: it
- Japanese: ja
- Javanese: jw
- Kannada: kn
- Kazakh: kk
- Khmer: km
- Korean: ko
- Kurdish: ku
- Kyrgyz: ky
- Lao: lo
- Latin: la
- Latvian: lv
- Lithuanian: lt
- Luxembourgish: lb
- Macedonian: mk
- Malagasy: mg
- Malay: ms
- Malayalam: ml
- Maltese: mt
- Maori: mi
- Marathi: mr
- Mongolian: mn
- Myanmar (Burmese): my
- Nepali: ne
- Norwegian: no
- Nyanja (Chichewa): ny
- Pashto: ps
- Persian: fa
- Polish: pl
- Portuguese (Portugal, Brazil): pt
- Punjabi: pa
- Romanian: ro
- Russian: ru
- Samoan: sm
- Scots Gaelic: gd
- Serbian: sr
- Sesotho: st
- Shona: sn
- Sindhi: sd
- Sinhala (Sinhalese): si
- Slovak: sk
- Slovenian: sl
- Somali: so
- Spanish: es
- Sundanese: su
- Swahili: sw
- Swedish: sv
- Tagalog (Filipino): tl
- Tajik: tg
- Tamil: ta
- Telugu: te
- Thai: th
- Turkish: tr
- Ukrainian: uk
- Urdu: ur
- Uzbek: uz
- Vietnamese: vi
- Welsh: cy
- Xhosa: xh
- Yiddish: yi
- Yoruba: yo
- Zulu: zu



You can use this and use your Google Translate API Key and you can obtain it from rapid API from where i got that

Requirements:
streamlit : pip install steamlit
requests : pip install requests


Usage
Provide your RapidAPI key:

Replace the placeholder RapidAPI key in the headers dictionary of app.py with your own valid key.


Run the Streamlit app:
streamlit run app.py

Access the web app:
Open your web browser and visit http://localhost:8501.
