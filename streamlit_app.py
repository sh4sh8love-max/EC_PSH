import streamlit as st
import pandas as pd
import numpy as np

import streamlit as st

timetable = {
    "요일": ["월", "화", "수", "목", "금"],
    "1교시": ["", "", "", "", ""],
    "2교시": ["", "죽과이", "", "전공", "컴퓨팅탐색"],
    "3교시": ["", "죽과이", "", "", "컴퓨팅탐색"],
    "4교시": ["", "죽과이", "", "사회복지정책", "컴퓨팅탐색"],
    "5교시": ["", "", "", "사회복지정책", ""],
    "6교시": ["", "빅데이터개론", "", "사회복지정책", ""],
    "7교시": ["", "빅데이터개론", "", "사회복지행정", ""],
    "8교시": ["", "빅데이터개론", "", "사회복지행정", ""],
    "9교시": ["", "", "", "사회복지행정", ""]
}

df = pd.DataFrame(timetable)

st.write("## 정적 시간표 (st.table)")
st.table(df)

# 수업 정보
class_info = {
    "컴탐": {
        "교수": "변해선",
        "강의실": "26동 104호"
    },
    "영어": {
        "교수": "이영희",
        "강의실": "10동 202호"
    },
    "전공": {
        "교수": "박민수",
        "강의실": "500동 303호"
    }
}

st.write("## 수업 정보 (st.json)")
st.json(class_info)

# 이번 학기 요약
st.write("## 이번 학기 요약 (st.metric)")

col1, col2 = st.columns(2)

with col1:
    st.metric(label="수강 과목 수", value="5")

with col2:
    st.metric(label="총 학점", value="15", delta="-3")
