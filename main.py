import requests, streamlit as st, os
def news(keyword="technology"): return requests.get(f'https://newsapi.org/v2/everything?q={keyword}&apiKey={os.getenv("NEWS_API")}&language=en&searchIn=title').json()['articles']
st.set_page_config(page_title="Today in Tech", page_icon=":newspaper:")
st.markdown("""<style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} </style> <hr><hr><br><h1 style='text-align: center; color: red;'>🔥Current trending news in tech🔥</h1><br><hr><hr>""", unsafe_allow_html=True)
for random_news in list(news()):st.markdown(f"""<h2>{random_news['title']}</h2><h5>{random_news['description']}</h5>Link : <a href="{random_news['url']}">{random_news['url'][:50]}...</a><br>Author : {random_news['author']}, &nbsp; <i>{random_news['publishedAt'][:10]}</i> <hr>""", unsafe_allow_html=True)
