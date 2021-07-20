import streamlit as st # 外部ライブラリ > Requirements.txt　へ記載必要
import numpy as np
import time # Python 標準ライブラリ > Requirementsには記載不要

st.title('Streamlit 超入門')

st.write('Progress Bar!!')

'start'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Status {i+1} %')
    bar.progress(i+1)
    time.sleep(0.1)

'Done..!!'

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('こちらは右カラムになります。')

expander1 = st.beta_expander('お問い合わせ１')
expander1.write('1への回答')
expander2 = st.beta_expander('お問い合わせ2')
expander2.write('2への回答')
expander3 = st.beta_expander('お問い合わせ3')
expander3.write('3 への回答')