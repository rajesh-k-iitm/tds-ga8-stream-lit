# Edited by Rajesh K, IITM, TDS GA8  Version 6
# Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def greatestOf3(a, b,c):
    greatest = a
    if ((b>a) and (b>c) ):
        greatest = b
    else:
        if(c>a):
            greatest =c
    return greatest





def run():
    st.set_page_config(
        page_title="Hello RK",
        page_icon="👋",
    )

    st.write("# Tools for Data Science GA8 = 23ds1xyz33- LARGEST OF 3 - Ver 5")
    st.write("Welcome to RK's page on stream lit! 👋")

    st.sidebar.success("Success!! Enter 3 numbers.")

    a = st.number_input('Enter 1st number ')
    b = st.number_input('Enter 2nd number ')
    c = st.number_input('Enter 3rd number ')

    result = 0.0
    result = greatestOf3(a, b,c)
    resultString = 'Greatest of 3: '+str(result)
    st.title(resultString)
    st.write('Greatest of ', a, ', ', b, ', ', c,' is :',result)
    st.sidebar.success(resultString)

    st.markdown(
        """
        IIT Madras Tools for Data Science Graded Assignment 8
        20 April 2024 
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.
        **👈 Select a demo from the sidebar** to see some examples
        of what Streamlit can do!
      
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )


if __name__ == "__main__":
    run()
