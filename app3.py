import streamlit as st

st.title("🗂️ Clean up the drive")
st.write("Delete the drafts. **Keep the final project.** Go fast!")

files = [f"draft_{n}.txt" for n in range(1, 12)] + ["FINAL_PROJECT.pdf", "draft_12.txt", "draft_13.txt"]

if "i" not in st.session_state:
    st.session_state.i = 0
    st.session_state.deleted = []


@st.dialog("Are you sure?")
def confirm(name):
    st.write(f"Delete **{name}**?")
    if st.button("Yes, delete"):
        st.session_state.deleted.append(name)
        st.session_state.i += 1
        st.rerun()


if st.session_state.i < len(files):
    name = files[st.session_state.i]
    st.subheader(f"📄 {name}")
    if st.button("🗑️ Delete"):
        confirm(name)
    if st.button("Keep"):
        st.session_state.i += 1
        st.rerun()
elif "FINAL_PROJECT.pdf" in st.session_state.deleted:
    st.error("You deleted FINAL_PROJECT.pdf! 😱")
else:
    st.success("You kept the final project. 🎉")
