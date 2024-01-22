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
epochs_num = st.slider("How many epochs?",1,100,10)
if st.button("Slider Button"):
    st.write(epochs_num)

st.header("Start of the Text Input Section")
user_text = st.text_input("What's your favorite movie?")
if st.button("Text Button"):
  st.write(user_text)

user_num = st.number_input("What's your favorite number?")
if st.button ("Number Button"):
  st.write(user_num)

def clean_text(text):
  text = text.replace("'","").replace("\n"," ").strip()
  return (text)


st.sidebar.header("Options")
text = st.sidebar.text_area("Paste Text Here")  
st.write(text)
button7 = st.sidebar.button("Clean Text")
if button7:
    col1, col2 = st.columns(2)
    col1.header("Original Text")
    col1.write(text)
    col2.header("Cleaned Text")

    st.write(text)
    clean = clean_text(text)
    st.write(clean)
