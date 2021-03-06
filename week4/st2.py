import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

st.title('Hello my friends')


st.write("Here's a link on [google](https://google.com)")


df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.write(df)

'''
line chart
'''

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


st.write('### dot chart')


map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

'=========================================='

cb = st.sidebar.checkbox('Show dataframe')

st.write('your choice {}'.format(cb))
if cb:
    chart_data2 = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data2)


option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

@st.cache 
def foo():
  return st.write(df[df['first column']==option])

