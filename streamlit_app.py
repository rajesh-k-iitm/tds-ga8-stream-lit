# Edited by Rajesh K, IITM, TDS GA8 
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

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
c = int(input('Enter 3rd number: '))

print(f'Greatest of {a} {b} and {c} is {greatestOf3(a, b,c)}')
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

    st.write("# Tools for Data Science GA8")
    st.write("Welcome to RK's page on stream lit! 👋")

    st.sidebar.success("Success!! Select a demo above.")

    a = int(input('Enter 1st number: '))
    b = int(input('Enter 2nd number: '))
    c = int(input('Enter 3rd number: '))

    print(f'Greatest of {a} {b} and {c} is {greatestOf3(a, b,c)}')

    st.markdown(
        """
        IIT Madras Tools for Data Science Graded Assignment 8
        6th December 2023
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
