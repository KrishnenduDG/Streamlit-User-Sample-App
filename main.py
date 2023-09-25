import streamlit as st 
import requests
import json


st.header("Hello from Data Fetching App!")


num_user = st.number_input(placeholder="Enter the Number of users..",value=None,label="Hello",step=1.0)

button = st.button("Get Users!")

if button:
    data = json.loads(requests.get(f"https://random-data-api.com/api/v2/users?size={int(num_user)}").text)


    for i in data:
        user_list = "<div>"
        user_list += f'''
            <h3>{i["first_name"]} {i["last_name"]}</h3>
            <img src={i["avatar"]} style="vertical-align: middle;
  width: 50px;
  height: 50px;
  border-radius: 50%;"></img>
        '''
        user_list += "</div>"
        st.markdown(user_list,unsafe_allow_html=True)