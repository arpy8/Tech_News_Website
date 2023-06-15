from datetime import datetime
import random, requests, streamlit as st
from streamlit.runtime.media_file_storage import MediaFileStorageError

current_date = datetime.now().strftime("%Y-%m-%d")
api_key = st.secrets["NEWS_API"]


def news(keyword="anime"):
    url = f'https://newsapi.org/v2/everything?q={keyword}&apiKey={api_key}&language=en&searchIn=title'
    response = requests.get(url)
    return response.json()['articles']


st.set_page_config(page_title="Anime News", page_icon=":newspaper:")
hide_streamlit_style = """ <style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} </style> """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: red;'>🔥Today in  Anime World🔥</h1> <hr>", unsafe_allow_html=True)

for i in range(5):
    random_news = random.choice(news())
    with st.container():
        st.markdown(f"## {random_news['title']}")
        try: st.image(f"{random_news['urlToImage']}", width=700)
        except MediaFileStorageError: pass
        st.markdown(f"##### {random_news['description']}\nLink : {random_news['url']}")
        st.markdown(f"Author : {random_news['author']}, &nbsp; _{random_news['publishedAt'][:10]}_ <hr>",
                    unsafe_allow_html=True)
