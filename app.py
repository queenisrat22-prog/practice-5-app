import streamlit as st
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

st.set_page_config(page_title="HACKER FIND", layout="centered")
st.markdown("<h1 style='text-align:center; border:2px solid #00ff00; padding:10px; color:#00ff00;'>HACKER FIND</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:right; color:#00ff00;'>NIGHT MODE • PRACTICE • SAFE</p>", unsafe_allow_html=True)

mobile = st.text_input("মোবাইল")
browser_count = st.number_input("ব্রাউজার সংখ্যা", min_value=1, value=1)
typing = st.selectbox("টাইপের ধরন", ["টাইপ করে লেখা", "রোল দিয়ে"])
method = st.selectbox("লগইন উপায়", ["Get code via SMS", "Get code via email"])
finder = st.selectbox("বাটন খোঁজার উপায়", ["role", "text", "xpath"])
same_mobile = st.checkbox("সব ব্রাউজারে একই মোবাইল")
sequential = st.checkbox("একটা শেষে আরেকটা খুলবে")
history_close = st.checkbox("কাজ শেষে হিস্ট্রি মুছে বন্ধ হবে")
view = st.checkbox("View", value=True)

def run_one(no, mob):
    st.write(f">>> ব্রাউজার {no} খুলছে")
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.binary_location = "/usr/bin/chromium"
    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)
    try:
        driver.get("https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0")
        time.sleep(5)
        st.write(">>> পাতা খুলেছে")
        boxes = driver.find_elements(By.TAG_NAME, "input")
        box = None
        for b in boxes:
            if b.is_displayed():
                box = b
                break
        box.click()
        box.send_keys(mob)
        st.write(">>> বক্সে লেখা হয়েছে")
        time.sleep(2)
        btn1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[normalize-space()='Continue']")))
        btn1.click()
        st.write(">>> প্রথম Continue চাপা হয়েছে")
        time.sleep(10)
        text = driver.find_element(By.TAG_NAME, "body").text
        st.write(text[:400])
        if "Choose your account" in text:
            st.write(">>> Choose your account পাতা এসেছে")
            rows = driver.find_elements(By.XPATH, "//*[@role='button']")
            accounts = []
            for r in rows:
                t = r.text.strip()
                if t == "":
                    continue
                if t in ["বাংলা", "অসমীয়া", "हिन्दी", "नेपाली", "Bahasa Indonesia", "العربية", "More languages…"]:
                    continue
                accounts.append(r)
            st.write(">>> অ্যাকাউন্ট সংখ্যা:", len(accounts))
            pick = 1
            if len(accounts) <= 1:
                pick = 0
            driver.execute_script("arguments[0].scrollIntoView(true);", accounts[pick])
            time.sleep(1)
            driver.execute_script("arguments[0].click();", accounts[pick])
            st.write(">>> যেকোনো একটা সিলেক্ট হয়েছে")
            time.sleep(5)
        els = driver.find_elements(By.XPATH, "//*[normalize-space()='Get code via SMS']")
        if len(els) > 0:
            st.write(">>> Get code via SMS পাতায় আছে")
            driver.execute_script("arguments[0].click();", els[0])
            st.write(">>> Get code via SMS সিলেক্ট করলাম")
        else:
            st.write(">>> Get code via SMS পাতায় নেই, বাদ দিলাম")
            driver.quit()
            return
        time.sleep(2)
        btn2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[normalize-space()='Continue']")))
        btn2.click()
        st.write(">>> দ্বিতীয় Continue চাপা হয়েছে")
        time.sleep(4)
        text2 = driver.find_element(By.TAG_NAME, "body").text
        st.write(text2[:500])
        st.write(">>> এখানেই থামো")
    except Exception as e:
        st.write(">>> ভুল হয়েছে:", str(e)[:300])
    finally:
        driver.quit()
        st.write(f">>> ব্রাউজার {no} এর কাজ শেষ")

if st.button("START"):
    if mobile.strip() == "":
        st.write(">>> মোবাইল লেখো, বক্স খালি আছে")
    else:
        st.write(">>> শুরু হচ্ছে")
        run_one(1, mobile.strip())
