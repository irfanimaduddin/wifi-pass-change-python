from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import time
import argparse

def change_password(freq):
    if freq == '5g':
        # Select Basic 5 GHz Tab
        get_freq = driver.find_element(By.NAME, 'subdiv_WlanBasic5G')
        get_freq.click()

        # Wait for the page to load after login
        time.sleep(3)

    # Switch to the iframe that contains the settings
    iframe = driver.find_element(By.ID, "frameContent")
    driver.switch_to.frame(iframe)

    # # Make selection for SSID (if more than one SSID)
    # if freq == '2g':
    #     # Select Secondary 2.4 Hz Tab
    #     wifi_choose_button = driver.find_element(By.XPATH, '//*[@id="record_1"]')
    #     wifi_choose_button.click()

    # Check Wifi SSID Name
    ssid_name = driver.find_element(By.XPATH, '//*[@id="wlSsid"]')
    ssid = ssid_name.get_attribute('value')

    # Go to hide password checkbox 
    pass_checkbox = driver.find_element(By.XPATH, '//*[@id="hidewlWpaPsk"]')

    # Uncheck the hide password checkbox
    if pass_checkbox.is_selected():
        pass_checkbox.click()

    # Go to hide password textbox 
    pass_text = driver.find_element(By.XPATH, '//*[@id="twlWpaPsk"]')
    prev_pass = pass_text.get_attribute('value')

    # Wait for the page to load
    time.sleep(2)

    # Clear the existing password and enter a new one
    pass_text.clear()
    pass_text.send_keys(NEW_PASS)
    new_pass = pass_text.get_attribute('value')

    # Wait for the page to load
    time.sleep(2)

    # Submit the changes
    submit_button = driver.find_element(By.XPATH, '//*[@id="btnApplySubmit"]')
    submit_button.click()

    # Wait for the page to load
    time.sleep(3)

    # Switch back to the default content
    driver.switch_to.default_content()

    # Wait for the page to load
    time.sleep(3)    

    return ssid, prev_pass, new_pass

if __name__ == "__main__":
    # Set argument parser
    parser = argparse.ArgumentParser(
        description='Change WiFi password on a router using a web interface'
    )

    parser.add_argument("--ip", required=True, type=str, help="IP address of the router")
    parser.add_argument("--auser", required=True, type=str, help="Admin username to login to the router")
    parser.add_argument("--apass", required=True, type=str, help="Admin password to login to the router")
    parser.add_argument("--nwpass", required=True, type=str, help="New WiFi password")
    args = parser.parse_args()

    URL, username, password, NEW_PASS = f"http://{args.ip}", args.auser, args.apass, args.nwpass

    # Initialize the Chrome WebDriver
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # if you want to run the browser in headless mode
    chrome_options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the URL
    driver.get(URL)

    # Wait for the page to load
    time.sleep(3)

    # Find the username and password fields
    username_input = driver.find_element(By.XPATH, '//*[@id="txt_Username"]')
    password_input = driver.find_element(By.XPATH, '//*[@id="txt_Password"]')  # Update the name if different

    # Enter the credentials in the form fields
    username_input.send_keys(username)
    password_input.send_keys(password)

    # Find the login button and click it
    login_button = driver.find_element(By.XPATH, '//*[@id="button"]')
    login_button.click()

    # Wait for the page to load after login
    time.sleep(3)

    wlan_tab_button = driver.find_element(By.NAME, 'maindiv_WlanBasic2G')
    wlan_tab_button.click()

    # Wait for the page to load
    time.sleep(3)

    ssid, prev_pass, new_pass = change_password(freq='2g')
    print(f"Changing pass for SSID: {ssid}")
    print(f"Current Password: {prev_pass}")
    print(f"New Password: {new_pass}")

    ssid, prev_pass, new_pass = change_password(freq='5g')
    print(f"Changing pass for SSID: {ssid}")
    print(f"Current Password: {prev_pass}")
    print(f"New Password: {new_pass}")

    # Close the browser
    driver.quit()

