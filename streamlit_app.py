import streamlit as st
import pandas as pd
import numpy as np

import streamlit as st

data = pd.DataFrame({
    'city': ['Mokpo', 'Busan'],
    'lat': [34.8110, 35.1796],
    'lon': [126.3925, 129.0756],
    'population': [240000, 3400000]    
})

st.write("가보고 싶은 도시 위치")
st.map(data) 
