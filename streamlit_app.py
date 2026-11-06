import streamlit as st
import pandas as pd
import numpy as np

# 단순한 텍스트를 표시
st.text("Hello, Streamlit!")

# Markdown 문법을 지원하여 헤더, 볼드, 이탤릭, 하이퍼링크 등 다양한 텍스트 스타일 가능
st.markdown("# 헤더 1")
st.markdown("## 헤더 2")
st.markdown("**굵은 텍스트**")
st.markdown("_기울임 텍스트_")
st.markdown("[링크로 이동](https://streamlit.io)")

# write()함수는 다목적 함수로 텍스트, 마크다운, 데이터, 객체 등 다양한 요소를 자동으로 감지하여 인식함
st.write("# 제목") 
st.write("Hello, Streamlit!")
st.write("**굵은 텍스트**와 *기울임 텍스트*를 함께 사용할 수 있습니다.")
st.write(12345)                        # 숫자
st.write({"이름": "홍길동", "나이": 23})   # 딕셔너리
st.write(pd.DataFrame({"A": [1,2,3]})) # 데이터프레임

st.title("대제목")
st.header("중제목")
st.subheader("소제목")
st.caption("설명 텍스트")
st.code("print('Hello')", language="python")
st.latex(r"E = mc^2")
