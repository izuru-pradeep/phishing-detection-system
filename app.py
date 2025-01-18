import streamlit as st
import content_model.feature_extraction as fe
import url_model.urlModel as url_model
import content_model.cntModel as cnt_model
import requests as re

st.title('Phishing Emails Detection')


url = st.text_input('Enter the URL')

# check the URL & content of the URL
if st.button('Check'):
    if url == '':
        st.warning('Please enter the URL!')
    else:
        try:
            response = re.get(url, verify=False, timeout=4)
            if response.status_code != 200:
                print(". HTTP connection was not successful for the URL: ", url)
                st.error("HTTP connection was not successful for the URL: " + url)
            else:
                url_result = url_model.predict(url)
                cnt_result = cnt_model.predict(response)
                if url_result['prediction_label'] == 0:
                    st.success("This URL seems a legitimate!")
                else:
                    st.warning("Attention! URL is a potential PHISHING!")
                if cnt_result[0] == 0:
                    st.success("This web page seems a legitimate!")
                else:
                    st.warning("Attention! This web page is a potential PHISHING!")

        except re.exceptions.RequestException as e:
            st.error("HTTP connection was not successful for the URL: " + url)
            print("--> ", e)





