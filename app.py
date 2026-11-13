import streamlit as st
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

st.set_page_config(page_title="HACKER FIND", layout="centered")

st.markdown("""
<style>
.stApp {background-color: #000000;}
h1 {color: #00ff00 !important;}
label {color: #00ff00 !important;}
.stButton>button {background-color: #00ff00; color: #000000; font-weight: bold;}
.logbox {background-color: #000000; border: 1px solid #00ff00; color: #00ff00; font-family: monospace; padding: 10px; white-space: pre-wrap;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; border:2px solid #00ff00; padding:10px;'>HACKER FIND</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:right; color:#00ff00;'>NIGHT MODE • PRACTICE • SAFE</p>", unsafe_allow_html=True)
st.markdown("<p style='color:#00ff00;'>• তৈরি</p>", unsafe_allow_html=True)

mobile_text = st.text_input("মোবাইল", placeholder="01700000000,01700000001,01700000002")
browser_count = st.number_input("ব্রাউজার সংখ্যা", min_value=1, value=1)
typing = st.selectbox("টাইপের ধরন", ["টাইপ করে লেখা", "রোল দিয়ে"])
method = st.selectbox("লগইন উপায়", ["Get code via SMS", "Get code via email"])
finder = st.selectbox("বাটন খোঁজার উপায়", ["role", "text", "xpath"])
same_mobile = st.checkbox("সব ব্রাউজারে একই মোবাইল")
sequential = st.checkbox("একটা শেষে আরেকটা খুলবে", value=True)
history_close = st.checkbox("কাজ শেষে হিস্ট্রি মুছে বন্ধ হবে")
view = st.checkbox("View", value=True)
want_shot = st.checkbox("প্রতিটার স্ক্রিনশট চাই")

log_lines = []
log_box = st.empty()

def log(msg):
    log_lines.append(msg)
    txt = "\n".join(log_lines)
    log_box.markdown(f"<div class='logbox'>{txt}</div>", unsafe_allow_html=True)

def get_mobile(i, mobiles):
    if same_mobile:
        return mobiles[0]
    if i < len(mobiles):
        return mobiles[i]
    try:
        base = int(mobiles[0])
        return str(base + i).zfill(11)
    except:
        return mobiles[0]

def shot(driver, no, name):
    if want_shot:
        path = f"/tmp/shot_{no}_{name}.png"
        driver.save_screenshot(path)
        st.image(path, caption=f"ব্রাউজার {no} - {name}")

def click_continue(driver):
    try:
        btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[normalize-space()='Continue']")))
        btn.click()
        return True
    except:
        return False

def run_one(no, mob):
    log(f">>> ব্রাউজার {no} খুলছে")
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
        log(">>> পাতা খুলেছে")
        shot(driver, no, "1-পাতা-খুলেছে")
        boxes = driver.find_elements(By.TAG_NAME, "input")
        box = None
        for b in boxes:
            if b.is_displayed():
                box = b
                break
        box.click()
        box.send_keys(mob)
        log(">>> বক্সে লেখা হয়েছে")
        shot(driver, no, "2-বক্সে-লেখা")
        time.sleep(2)
        if click_continue(driver):
            log(">>> প্রথম Continue চাপা হয়েছে")
        else:
            log(">>> প্রথম Continue পাওয়া যায়নি")
        time.sleep(10)
        text = driver.find_element(By.TAG_NAME, "body").text
        log(text[:300])
        shot(driver, no, "3-প্রথম-Continue-র-পর")
        if "Choose your account" in text:
            log(">>> Choose your account পাতা এসেছে")
            rows = driver.find_elements(By.XPATH, "//*[@role='button']")
            accounts = []
            for r in rows:
                t = r.text.strip()
                if t == "":
                    continue
                if t in ["বাংলা", "অসমীয়া", "हिन्दी", "नेपाली", "Bahasa Indonesia", "العربية", "More languages…"]:
                    continue
                accounts.append(r)
            log(f">>> অ্যাকাউন্ট সংখ্যা: {len(accounts)}")
            pick = 1
            if len(accounts) <= 1:
                pick = 0
            driver.execute_script("arguments[0].scrollIntoView(true);", accounts[pick])
            time.sleep(1)
            driver.execute_script("arguments[0].click();", accounts[pick])
            log(">>> যেকোনো একটা সিলেক্ট হয়েছে")
            time.sleep(5)
            shot(driver, no, "4-অ্যাকাউন্ট-সিলেক্ট")
            text = driver.find_element(By.TAG_NAME, "body").text
            log(text[:300])
            if "Choose your account" in text:
                log(">>> এখনো Choose your account পাতায় আছে, Continue চাপছি")
                if click_continue(driver):
                    log(">>> অ্যাকাউন্ট পাতার Continue চাপা হয়েছে")
                time.sleep(5)
                text = driver.find_element(By.TAG_NAME, "body").text
                log(text[:300])
                shot(driver, no, "5-অ্যাকাউন্ট-Continue-র-পর")
        log(f">>> তুমি বেছেছো: {method}")
        log(f">>> পাতায় {method} আছে কি: {method in text}")
        if method in text:
            log(f">>> {method} পাতায় আছে")
            els = driver.find_elements(By.XPATH, f"//*[contains(text(), '{method}')]")
            if len(els) > 0:
                driver.execute_script("arguments[0].click();", els[0])
                log(f">>> {method} সিলেক্ট করলাম")
            shot(driver, no, "6-উপায়-সিলেক্ট")
            time.sleep(2)
            if click_continue(driver):
                log(">>> দ্বিতীয় Continue চাপা হয়েছে")
            else:
                log(">>> দ্বিতীয় Continue পাওয়া যায়নি")
            time.sleep(4)
            text2 = driver.find_element(By.TAG_NAME, "body").text
            log(text2[:300])
            shot(driver, no, "7-দ্বিতীয়-Continue-র-পর")
        else:
            log(f">>> {method} পাতায় নেই, বাদ দিলাম")
        log(">>> এখানেই থামো")
    except Exception as e:
        log(f">>> ভুল হয়েছে: {str(e)[:200]}")
    finally:
        driver.quit()
        log(f">>> ব্রাউজার {no} এর কাজ শেষ")

if st.button("START"):
    mobiles = [m.strip() for m in mobile_text.split(",") if m.strip() != ""]
    if len(mobiles) == 0:
        log(">>> মোবাইল লেখো, বক্স খালি আছে")
    else:
        log(">>> শুরু হচ্ছে")
        log(f">>> মোট নম্বর: {len(mobiles)}, ব্রাউজার: {browser_count}")
        for i in range(int(browser_count)):
            mob = get_mobile(i, mobiles)
            run_one(i+1, mob)
            if sequential:
                log(f">>> ব্রাউজার {i+1} পুরো শেষ, তারপর পরেরটা")
