import streamlit as st
st.title ("Streamlit Tutorial App")
st.write ("This is my App")

button1 = st.button ("Click Me")
if button1: 
  st.write("This is some Text")

st.header ("Start of the Checkbox Section")
Like = st.checkbox ("Do you like this app?")
button2 = st.button ("Submit")
if button2:
    if Like:
      st.write ("Thanks! I like it too")
    else:
      st.write ("I'm sorry. You have bad tastes")

st.header("Start of the Radio Button Section")
animal = st.radio("What animal is your favorite?", ("Lion","Tiger","Bear"))
button3 = st.button("Submit Animal")
if button3: 
    st.write(animal)
    if animal == "Lion":
        st.write("ROAR!")
