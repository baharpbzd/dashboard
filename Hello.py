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

st.header("Start of the Selectbox Section")
animal2 = st.selectbox("What animal is your favorite?", ("Lion","Tiger","Bear"))
button4 = st.button("Submit Animal 2")
if button4: 
    st.write(animal2)
    if animal == "Lion":
        st.write("ROAR!")

st.header("Start of the Multiselect Section")
options = st.multiselect("What Animals do you like?",["Lion","Tiger","Bear"])
button5 = st.button ("Print Animals")
if button5:
    st.write(options)

st.header("Start of the Slider Section")
epochs_num = st.slider("How many epochs?",1,100)






  

