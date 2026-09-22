import streamlit as st

st.title("✍️ Write, get interrupted, come back")

if "on_break" not in st.session_state:
    st.session_state.on_break = False

if st.session_state.on_break:
    st.header("☕ Break time")
    if st.button("Back to work"):
        st.session_state.on_break = False
        st.rerun()
else:
    st.text_area("Your essay", key="essay")
    if st.button("Take a break"):
        st.session_state.on_break = True
        st.rerun()
