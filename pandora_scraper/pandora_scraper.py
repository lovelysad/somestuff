#  -*- coding: utf-8 -*-

from selenium import webdriver
import time, re
from secret import username, password
import pandas as pd

#python -i pandora_scraper.py

class pandoraBot:

    comment_tickets = []
    inbox_tickets = []

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\abc\PycharmProjects\chromedriver_win32\chromedriver.exe")

    def login(self):
        self.driver.get("https://space.sprinklr.com/new")

        time.sleep(7)

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


        ##########################
        ticket_ele = self.driver.find_elements_by_xpath('//article[@class = "streamEntity spr"]')
        for i in ticket_ele:
            ticket_name = i.find_element_by_xpath('.//div[@class="msgProfileName spr-text-01 text-13 font-700 text-overflow scp"]').text
            ticket_text = i.find_element_by_xpath('.//div[@class="msgContent"]').text
            try:
                ticket_link = i.find_element_by_xpath('.//a[@class = "msgTimeStamp msgHeaderSubText spr-text-02 txt-bd4 pull-xs-right m-l-1 msgTimeStampRenderAsLink"]').get_attribute("href")
            except:
                ticket_link = ""
            try:
                ticket_time = i.find_element_by_xpath('.//a[contains(@aria-label,"Posted on")]').get_attribute("aria-label")
            except:
                ticket_time = ""

            try:
                ticket_image = i.find_element_by_xpath('.//img[@class = "show mediaImgContent scp"]').get_attribute("src")
            except:
                ticket_image = None

            msgtime_regex = re.compile(r'Posted on(.*)')
            ticket_time = msgtime_regex.search(ticket_time).group()

            print(ticket_name,ticket_text,ticket_link,ticket_time,"\n")
            if ticket_image:
                print(ticket_image,"\n")
        ######################

    def getTicketContent(self):

        ticket_ele = self.driver.find_elements_by_xpath('//article[@class = "streamEntity spr"]')

        comment_tickets = []
        inbox_tickets = []

        for i in ticket_ele:
            ticket_name = i.find_element_by_xpath('.//div[@class="msgProfileName spr-text-01 text-13 font-700 text-overflow scp"]').text
            ticket_text = i.find_element_by_xpath('.//div[@class="msgContent"]').text

            try:
                ticket_link = i.find_element_by_xpath('.//a[@class = "msgTimeStamp msgHeaderSubText spr-text-02 txt-bd4 pull-xs-right m-l-1 msgTimeStampRenderAsLink"]').get_attribute("href")
                if "inbox" in ticket_link:
                    ticket_link = "Inbox"
            except:
                ticket_link = ""

            try:
                ticket_time = i.find_element_by_xpath('.//a[contains(@aria-label,"Posted on")]').get_attribute("aria-label")
                msgtime_regex = re.compile(r'Posted on(.*)')
                if ticket_time:
                    ticket_time = msgtime_regex.search(ticket_time).group(1)
            except:
                ticket_time = ""

            try:
                ticket_image = i.find_element_by_xpath('.//img[@class = "show mediaImgContent scp"]').get_attribute("src")
            except:
                ticket_image = None

            if ticket_image and ticket_text:
                ticket_text = ticket_text + "\n" + ticket_image
            elif ticket_image and ticket_text == "":
                ticket_text = ticket_image

            per_ticket_content = [ticket_time,ticket_name,ticket_text,ticket_link]
            if ticket_link == "Inbox":
                if per_ticket_content not in self.inbox_tickets:
                    self.inbox_tickets.append(per_ticket_content)
            elif ticket_link != "" and ticket_link != "Inbox":
                if per_ticket_content not in self.comment_tickets:
                    self.comment_tickets.append(per_ticket_content)


            #print(ticket_name,ticket_text,ticket_link,ticket_time,"\n")
            # if ticket_image:
            #     print(ticket_image,"\n")


    def print_dataframe(self):

        if len(self.comment_tickets) > 0:
            df_comment = pd.DataFrame(self.comment_tickets,columns=["Message_Time","Customer_Name","Enquiry","URL"])

            df_comment["Message_Time"] = pd.to_datetime(df_comment.Message_Time)
            df_comment = df_comment.sort_values(by='Message_Time', ascending=False)

            df_comment["Message_Time"] = df_comment["Message_Time"].dt.strftime("%A, %B %d, %Y %I:%M:%S %p")

            print(df_comment)
            print(self.comment_tickets)
        if len(self.inbox_tickets) > 0:
            df_inbox = pd.DataFrame(self.inbox_tickets,columns=["Message_Time","Customer_Name","Enquiry","URL"])

            df_inbox["Message_Time"] = pd.to_datetime(df_inbox.Message_Time)
            df_inbox = df_inbox.sort_values(by='Message_Time',ascending=False)

            df_inbox["Message_Time"] = df_inbox["Message_Time"].dt.strftime("%A, %B %d, %Y %I:%M:%S %p")

            print(df_inbox)
            print(self.inbox_tickets)

    def test(self,scrolls = 4 ):
        scroll_box_public = self.driver.find_element_by_xpath('//*[@id="sprEngagementWorkspace"]/div/div/div[2]/div/div[2]/div[2]/div/div/section/div')
        #scroll_box_private = a.driver.find_elements_by_xpath('//*[@id="sprEngagementWorkspace"]/div/div/div[3]/div/div[2]/div[2]/div/div/section/div')
        scroll_height = 0
        for _ in range(scrolls):
            scroll_height += 260
            self.driver.execute_script("arguments[0].scrollTo(0, {})".format(scroll_height), scroll_box_public)
            time.sleep(0.2)
            #a.driver.execute_script("arguments[0].scrollTo(0, {})".format(scroll_height), scroll_box_private)
            #a.driver.execute_script("arguments[0].scrollTo(0, 260)", scroll_box_private)
            time.sleep(0.2)
            self.getTicketContent()
        self.print_dataframe()



a = pandoraBot()
a.login()




