import streamlit as st 
import cv2 as cv
import time 

st.title("Oii Butkii !!!")

st.markdown("I bet ur noob 😏")

c1 , c2 , c3 = st.columns(3)


with c1:
    first  = st.text_input("Enter 4 alphabets I like the most🧲" , key = "f1")
    second  = st.text_input("Hn + yes ? 👀" , key = "f2")
    third  = st.text_input("What am i doing now 😏 ?" , key = "f3")
    fourth  = st.text_input("UR CHOICE !!! ;-;" , key = "f4")

with c2:
    st.text("")
    st.text("")
    b1 = st.button("Hint 1")
    st.text("")
    st.text("")
    b2 = st.button("Hint 2")
    st.text("")
    st.text("")
    b3 = st.button("Hint 3")
    st.text("")
    st.text("")
    b4 = st.button("Hint 5")

b5 = st.button("Submit")

if b5:
    if first == "uuuu":
        st.success("Good bbg ur score for 1st is 0 😂 ")
    if second == "838":
         st.success("Good bbg ur score for 2nd is 0 lol!!!! ")
    if third == "not missing u":
         st.success("Good bbg ur score for 3rd is same as above ")
    if fourth:
        st.success("Good bbg ur score for 4th is.... i wont sayyy bcz its UrChoice ")
if b1 :
    st.info("u really think i will give ???? 😂😂 ok here is 🥚🥚🥚🥚")
if b2 :
    st.info("DM 🤡")
if b3 :
    st.info("  !(Missing U)   -_-")
if b4 :
    st.info("UR CHOICE fr")

fifth = st.text_input("Enter the code bbg")
ahem = st.button("Ahemmm")
if "count" not in st.session_state:
    st.session_state.count = 0
time_count = 5
if ahem or fifth:
    st.session_state.count +=1
    st.write(f"Ur count = {st.session_state.count}")
    if st.session_state.count >= 20 :
        st.info("Awww u already reached 20 counts")
        time.sleep(3)
        st.info("Ok le me give u a Crazy Hint")
        time.sleep(3)
        st.info("'I didnt do any numbering error'")
if fifth == "1235" :
    st.success("Finallllllllyyyyyyy!!!!!!!! btw..........")
    time.sleep(5)
    st.warning("Are u waitingggggggggggg!!!!!!!!!!")
    time.sleep(2)
    st.title("Ahemmmmmmm!!!!!!")
    time.sleep(5)
    img = cv.imread(r"C:\Users\suhai\Desktop\images.jpeg")
    img = cv.cvtColor(img , cv.COLOR_BGR2RGB)
    st.image(img)
    