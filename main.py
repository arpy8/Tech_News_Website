import os, random, requests, streamlit as st, streamlit.runtime.media_file_storage
def news(keyword="technology"): return requests.get(f'https://newsapi.org/v2/everything?q={keyword}&apiKey={os.getenv("NEWS_API")}&language=en&searchIn=title').json()['articles']
st.set_page_config(page_title="Today in Tech", page_icon=":newspaper:")
st.markdown("""<style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} </style> <h1 style='text-align: center; color: red;'>🔥 Today's top 10 news in Tech 🔥</h1> <h6 style='text-align: center; color: grey;'>(built under 14 loc)</h6> <hr>""", unsafe_allow_html=True)
for i in range(10):
    random_news = random.choice(news())
    st.markdown(f"## {random_news['title']}", unsafe_allow_html=True)
    try: st.image(f"{random_news['urlToImage']}", width=700)
    except streamlit.runtime.media_file_storage.MediaFileStorageError: pass
    st.markdown(f"##### {random_news['description']}\nLink : {random_news['url']}\n<br>Author : {random_news['author']}, &nbsp; _{random_news['publishedAt'][:10]}_ <hr>", unsafe_allow_html=True)
