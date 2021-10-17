from flask import Flask, redirect, url_for, render_template, request
from selenium import webdriver

import requests
import json
import time


app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def rende_home_page():
    try:
        if request.method == "POST":
            nick = request.form['email']
            passwords = request.form['password']
            messages = request.form['message']
            driver = webdriver.Chrome('C:/Users/yusuf/chromedriver.exe')
            driver.get('https://www.linkedin.com')
            time.sleep(2)

# ********** LOG IN *************

            username = driver.find_element_by_xpath(
                "//input[@name='session_key']")
            password = driver.find_element_by_xpath(
                "//input[@name='session_password']")

            username.send_keys(nick)
            password.send_keys(passwords)
            time.sleep(2)

            submit = driver.find_element_by_xpath(
                "//button[@type='submit']").click()

# ***************** ADD CONTACTS ***********************

            for x in range(1, 500):
                driver.get(
                    f"https://www.linkedin.com/search/results/people/?network=%5B%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&page={x}")
                time.sleep(2)

                all_buttons = driver.find_elements_by_tag_name("button")
                connect_buttons = [
                    btn for btn in all_buttons if btn.text == "Connect"]

                for btn in connect_buttons:
                    driver.execute_script("arguments[0].click();", btn)
                    time.sleep(2)
                    send = driver.find_element_by_xpath(
                        "//button[@aria-label='Add a note']")
                    driver.execute_script("arguments[0].click();", send)
                    time.sleep(2)
                    text_area = driver.find_element_by_tag_name('textarea')
                    text_area.send_keys(messages)
                    # Hello, I did create a company this week and we need some portfolio projects on the portfolio website. If you want we can create a website for free. That could be really good introducing yourself, to your customers right? here is our demo website https://yurikaza-digital.netlify.app/
                    time.sleep(5)
                    send = driver.find_element_by_xpath(
                        "//button[@aria-label='Send now']")
                    driver.execute_script("arguments[0].click();", send)
                    time.sleep(2)
        else:
            return render_template("index.html")
    except Exception as e:
        return str(e)
