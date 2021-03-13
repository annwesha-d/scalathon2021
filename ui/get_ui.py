#import streamlit
import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import sys
from streamlit import cli as stcli
from PIL import Image
import  os

def img_to_bytes(img_path):
    img_bytes = os.path.isfile(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

def read_data(filename):
    df =pd.read_csv(filename)
    return df

def main():
# Your streamlit code
    #header
    st.title('Advanced Scalathon 2021')

    #body
    st.write("Data Profiling : ")
    st.write(read_data('../data/Profiling_Report_All_Columns.csv'))

    #wordcloud
    header_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(img_to_bytes("../data/img/wordcloud.png"))

    st.markdown(
        header_html, unsafe_allow_html=True,
    )
    

if __name__ == '__main__':
    if st._is_running_with_streamlit:
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())


