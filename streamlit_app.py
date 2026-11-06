import streamlit as st
import pandas as pd
import numpy as np

import streamlit as st

data = pd.DataFrame({
    "city": ["Haeundae-gu, Busan"],
    "lat": [35.1631],
    "lon": [129.1635],
})

st.write("가보고 싶은 장소(부산 해운대구")
st.map(data)
