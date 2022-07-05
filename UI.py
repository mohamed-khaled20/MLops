import streamlit as st
import requests
import matplotlib.pyplot as plt
import seaborn as sns

from PIL import Image

URL = "https://khaled-covid19-mlops.herokuapp.com"

st.set_option('deprecation.showfileUploaderEncoding', False)

st.title("X-ray covid-19 detection service")
st.write("")

file_up = st.file_uploader("Upload an image", type=["jpg","png"])


if file_up:
    start_button_col1, image_col2 = st.columns(2)

    resized_img = Image.open(file_up).resize((400,400),resample=Image.BILINEAR)
    image_col2.image(resized_img, caption='Uploaded Image.')
    #st.write("")

    start_button = start_button_col1.button('Start Classification')

    if start_button:
        res = requests.post(URL + '/predict',files={'file': file_up.getvalue()}).json()

        st.subheader('Result')
        ## result
        if res['result'] == 'NORMAL':
            st.write('Model shows you do not have Covid-19')
        else:
            st.write('Model shows you have Covid-19')


        ## plotting
        data = []
        label = []
        for key in res['distribution']:
            data.append(float(res['distribution'][key].strip('%')))
            label.append(key)

        colors    = sns.color_palette('pastel')[0:len(label)]
        fig1, ax1 = plt.subplots()

        ax1.pie(data, labels=label, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')
        st.pyplot(fig1)

