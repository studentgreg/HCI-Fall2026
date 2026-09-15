import streamlit as st # st is an alias

st.title("My First Web App")
st.header("Dr. Reis")
st.subheader("Human-Computer Interaction (HCI)")
# To run, go to the terminal and execute: streamlit run fileName.py
# or, alternatively, execute in the terminal:
#  python -m streamlit run fileName.py
# To stop the process, press Control + C

# 2. Show Text

st.write("Any text, number, or even pandas dataframe")
st.markdown("**Bold**, *italic*, [links](https://fiu.edu")

# 3. Collect input from the user (here, HCI becomes more evident)
name = st.text_input("Enter your name", value="Greg")
cups = st.slider("Cups of coffee today",0,10,2)
decaf = st.checkbox("Decaf")
clicked = st.button("Save data")

# 4. React to input

if clicked:
    st.success(f"Saved {cups} cup(s) of coffee today.")
if cups > 5:
    st.warning("Too much caffeine")

st.info("Tip: use decaf after 3pm.")

#