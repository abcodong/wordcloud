import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np

# 한글 폰트 설정
FONT_PATH = "./NanumGothic.ttf"

st.title("🧠 한글 워드클라우드 생성기")

text = st.text_area("🔤 워드클라우드를 만들 문장을 입력하세요:")

if st.button("워드클라우드 만들기"):
    if len(text.strip()) == 0:
        st.warning("텍스트를 입력해주세요!")
    else:
        # 워드클라우드 생성
        wc = WordCloud(
            font_path=FONT_PATH,
            background_color="white",
            width=800,
            height=400
        ).generate(text)

        # 출력
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.imshow(wc, interpolation="bilinear")
        ax.axis("off")

        st.pyplot(fig)

st.markdown("---")
st.markdown("💡 한글이 깨지지 않도록 **NanumGothic.ttf** 폰트를 프로젝트 폴더에 포함하세요!")
