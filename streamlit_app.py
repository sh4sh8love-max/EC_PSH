import streamlit as st
import pandas as pd
import numpy as np

import streamlit as st

st.title("나의 소개 페이지")

st.header("자기소개")
st.text("안녕하세요, 제 이름은 박수혁입니다.")
st.markdown("저는 **기계학습**과 *게임*에 관심이 있습니다.")

st.subheader("좋아하는 것")
st.markdown("저는 노래와 게임을 좋아합니다.")
st.markdown(
    "가장 자주 방문하는 사이트는 "
    "[서울대학교 etl](https://etl.snu.ac.kr/) 입니다."
)

st.subheader("앞으로의 목표")
st.markdown("앞으로 다양한 프로젝트를 진행하면서 컴퓨터와 관련된 흥미로운 활동을 계속해나가고 싶습니다.")

st.caption("제가 좋아하는 게임")
st.markdown("롤, 철권, 엘든링, 마인크래프트")

st.caption("피타고라스 정리")
st.latex(r"a^2 + b^2 = c^2")
