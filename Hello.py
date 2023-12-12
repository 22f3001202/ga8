# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Welcome to Largest Number calculator",
        page_icon="👋",
    )
    st.write("""
    # Graded Assignment 8
    This app finds the largest of the 3 given numbers
    """)

    #Get Input
    st.header('User Input Parameters')
    
    first_number = st.number_input("First Number:")
    second_number = st.number_input("Second Number:")
    third_number = st.number_input("Third Number:")
    
    largest_number=0
    if first_number > largest_number:
      largest_number=first_number
    if second_number > largest_number:
      largest_number=second_number
    if third_number > largest_number:
      largest_number=third_number
    
    st.subheader('Largest Number')
    st.write(largest_number)

if __name__ == "__main__":
    run()
