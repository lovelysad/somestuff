#  -*- coding: utf-8 -*-

from selenium import webdriver
import time
from secret import username, password

#python -i pandora_scraper.py

class pandoraBot:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="D:\chromedriver_win32\chromedriver")

    def login(self):
        self.driver.get("https://space.sprinklr.com/new")

        time.sleep(5)

        email_input = self.driver.find_element_by_xpath('//*[@id="root"]/div/section[2]/section/div[1]/div/div/div/div/div/div/form/div[1]/div/input')
        time.sleep(0.5)
        email_input.send_keys(username)
        time.sleep(1)

        next_btn = self.driver.find_element_by_xpath('//*[@id="root"]/div/section[2]/section/div[1]/div/div/div/div/div/div/form/div[1]/button')
        time.sleep(0.5)
        next_btn.click()
        time.sleep(1)

        pw_input = self.driver.find_element_by_xpath('//*[@id="root"]/div/section[2]/section/div[1]/div/div/div/div/div/div[2]/form/div[2]/div[1]/input')
        time.sleep(0.5)
        pw_input.send_keys(password)
        time.sleep(1)

        login_btn = self.driver.find_element_by_xpath('//*[@id="root"]/div/section[2]/section/div[1]/div/div/div/div/div/div[2]/form/div[2]/button')
        time.sleep(0.5)
        login_btn.click()

        time.sleep(12)

        engagement_open = self.driver.find_element_by_xpath('//*[@id="sprPage"]/div/div/div/div/div[2]/div/div/div/div/div/ul/li[1]/div[2]/div/div/div[1]/a[1]/div/div/div[1]')
        time.sleep(0.5)
        engagement_open.click()
        time.sleep(2)

    def scrape_public_msgs(self):

        per_ticket = self.driver.find_element_by_xpath('//article[@class = "streamEntity spr"]').text

        scroll_box_public = self.driver.find_element_by_xpath('//*[@id="sprEngagementWorkspace"]/div/div/div[2]/div/div[2]/div[2]/div/div/section/div')
        scroll = self.driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight)",scroll_box_public)

        fb_username_ele = self.driver.find_element_by_xpath('//div[@class="msgProfileName spr-text-01 text-13 font-700 text-overflow scp"]')
        fb_username = fb_username_ele.text
        scroll_height = 0
        for _ in range(4):
            scroll_height += 260
            self.driver.execute_script("arguments[0].scrollTo(0, {})".format(scroll_height), scroll_box_public)
            time.sleep(0.1)
            fb_username_ele = self.driver.find_element_by_xpath('//div[@class="msgProfileName spr-text-01 text-13 font-700 text-overflow scp"]')
            time.sleep(0.1)
            fb_username = fb_username_ele.text
            print(fb_username)

        scroll_box_public = self.driver.find_element_by_xpath('//*[@id="sprEngagementWorkspace"]/div/div/div[2]/div/div[2]/div[2]/div/div/section/div')
        scroll = self.driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight)",scroll_box_public)

        names_ele = self.driver.find_elements_by_xpath('//div[@class="msgProfileName spr-text-01 text-13 font-700 text-overflow scp"]')
        names = [name.text for name in names_ele if name.text != '']

        #public_box = self.driver.find_element_by_xpath('//span[contains(text(),"Facebook - Public")]//*//div[@class="msgProfileName spr-text-01 text-13 font-700 text-overflow scp"]')
        public_box = self.driver.find_element_by_xpath('//span[contains(text(),"Facebook - Public")]')
        names_ele = public_box.find_elements_by_xpath('//div[@class="msgProfileName spr-text-01 text-13 font-700 text-overflow scp"]')

        ticket_ele = self.driver.find_elements_by_xpath('//article[@class = "streamEntity spr"]')
        for i in ticket_ele:
            ticket_name = i.find_element_by_xpath('.//div[@class="msgProfileName spr-text-01 text-13 font-700 text-overflow scp"]').text
            ticket_text = i.find_element_by_xpath('.//div[@class="msgContent"]').text
            try:
                ticket_link = i.find_element_by_xpath('.//a[@class = "msgTimeStamp msgHeaderSubText spr-text-02 txt-bd4 pull-xs-right m-l-1 msgTimeStampRenderAsLink"]').get_attribute("href")
            except:
                ticket_link = ""
            try:
                ticket_time = i.find_element_by_xpath('.//a[contains(@aria-label,"Added to Queue on")]').get_attribute("aria-label")
            except:
                ticket_time = ""

            try:
                ticket_image = i.find_element_by_xpath('.//img[@class = "show mediaImgContent scp"]').get_attribute("src")
            except:
                ticket_image = None

            print(ticket_name,ticket_text,ticket_link,ticket_time,"\n")
            if ticket_image:
                print(ticket_image,"\n")

# a = pandoraBot()
# a.login()




