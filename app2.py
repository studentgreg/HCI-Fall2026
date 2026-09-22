import random
import streamlit as st

st.title("🧠 How much can you hold in your head?")

length = st.slider("Code length", 3, 10, 4)

if "step" not in st.session_state:
    st.session_state.step = "show"

if st.session_state.step == "show":
    if st.button("New code"):
        st.session_state.code = "".join(random.choices("ABCDEFGHJKLMNPQRSTUVWXYZ23456789", k=length))
    if "code" in st.session_state:
        st.header(st.session_state.code)
        if st.button("Next screen →"):
            st.session_state.step = "type"
            st.rerun()
else:
    guess = st.text_input("Type the code from the previous screen")
    if guess:
        if guess.upper() == st.session_state.code:
            st.success("Correct!")
        else:
            st.error(f"It was {st.session_state.code}")
    if st.button("Try again"):
        st.session_state.step = "show"
        del st.session_state.code
        st.rerun()
