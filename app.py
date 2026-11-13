import streamlit as st

st.set_page_config(page_title="HACKER FIND", layout="centered")

st.markdown("""
<style>
.stApp {background-color: #000000;}
h1 {color: #00ff00 !important;}
label {color: #00ff00 !important;}
.stButton>button {background-color: #00ff00; color: #000000; font-weight: bold;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; border:2px solid #00ff00; padding:10px;'>HACKER FIND</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:right; color:#00ff00;'>NIGHT MODE • PRACTICE • SAFE</p>", unsafe_allow_html=True)
st.markdown("<p style='color:#00ff00;'>• তৈরি</p>", unsafe_allow_html=True)

mobile = st.text_input("মোবাইল")
browser_count = st.number_input("ব্রাউজার সংখ্যা", min_value=1, value=1)
typing = st.selectbox("টাইপের ধরন", ["টাইপ করে লেখা", "রোল দিয়ে"])
method = st.selectbox("লগইন উপায়", ["Get code via SMS", "Get code via email"])
finder = st.selectbox("বাটন খোঁজার উপায়", ["role", "text", "xpath"])

same_mobile = st.checkbox("সব ব্রাউজারে একই মোবাইল")
sequential = st.checkbox("একটা শেষে আরেকটা খুলবে")
history_close = st.checkbox("কাজ শেষে হিস্ট্রি মুছে বন্ধ হবে")
view = st.checkbox("View", value=True)

if st.button("START"):
    st.markdown("<p style='color:#00ff00;'>>> শুরু হচ্ছে</p>", unsafe_allow_html=True)
    st.write(">>> মোবাইল লেখা হয়েছে")
    st.write(">>> ব্রাউজার সংখ্যা:", browser_count)
    st.write(">>> লগইন উপায়:", method)
    st.write(">>> এখানেই থামো, পরের ধাপে আসল কাজ বসাবো")
