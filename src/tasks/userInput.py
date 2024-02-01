import streamlit as st
from streamlit_mic_recorder import mic_recorder,speech_to_text

st.title("Intelligent :red[Task Manager]")

state=st.session_state
final_user_input = ""

placeholder = st.empty()

user_text_area = placeholder.text_area(label="Please enter your Task: ")

    
if 'text_received' not in state:
    state.text_received=[]

c1,c2=st.columns(2)
with c1:
    st.write("Convert speech to text:")
with c2:
    user_text=speech_to_text(language='en',use_container_width=True,just_once=True,key='STT')

if user_text:       
    state.text_received.append(user_text)

for text in state.text_received:
    user_text_area = placeholder.text_area(label="Please enter your Task: ", value = user_text_area + text)
    

final_user_input = user_text_area  # User input which can be passed to the backend
    
if st.button("Submit") and final_user_input:
   
    user_text_area = state.text_received = []  
    st.success("Task submitted successfully!")
    st.text(final_user_input) #Used to view the strings on final_user_input


   

