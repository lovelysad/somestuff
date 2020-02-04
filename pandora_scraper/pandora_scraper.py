#  -*- coding: utf-8 -*-

from selenium import webdriver
import time, re
from secret import username, password
import pandas as pd
import openpyxl

#python -i pandora_scraper.py

class pandoraBot:

    comment_tickets = []
    inbox_tickets = []

    export_colomns = ["Message_Time","Customer_Name","Enquiry","URL"]

    export_path = r"C:\Users\abc\PycharmProjects\somestuff\pandora_scraper\pandora_export.xlsx"

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\abc\PycharmProjects\chromedriver_win32\chromedriver.exe")

    def login_old(self):
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

    def login(self):
        self.driver.get("https://space.sprinklr.com/new")

        time.sleep(2)

        email_input_element_not_found = True
        while email_input_element_not_found:
            try:
                email_input = self.driver.find_element_by_xpath('//*[@id="root"]/div/section[2]/section/div[1]/div/div/div/div/div/div/form/div[1]/div/input')
                email_input_element_not_found = False
                print("email input element found")
            except:
                print("retry finding email input element...")
            time.sleep(0.5)

        email_input.send_keys(username)
        time.sleep(1)

        next_btn = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/section[2]/section/div[1]/div/div/div/div/div/div/form/div[1]/button')
        time.sleep(0.5)
        next_btn.click()
        time.sleep(1)

        pw_input_element_not_found = True
        while pw_input_element_not_found:
            try:
                pw_input = self.driver.find_element_by_xpath(
                    '//*[@id="root"]/div/section[2]/section/div[1]/div/div/div/div/div/div[2]/form/div[2]/div[1]/input')
                print("pw input element found")
                pw_input_element_not_found = False
            except:
                print("retry finding pw input element")
            time.sleep(0.5)

        pw_input.send_keys(password)
        time.sleep(1)

        login_btn = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/section[2]/section/div[1]/div/div/div/div/div/div[2]/form/div[2]/button')
        time.sleep(0.5)
        login_btn.click()

        time.sleep(2)

        engagement_open_element_not_found = True
        while engagement_open_element_not_found:
            try:
                engagement_open = self.driver.find_element_by_xpath(
                    '//*[@id="sprPage"]/div/div/div/div/div[2]/div/div/div/div/div/ul/li[1]/div[2]/div/div/div[1]/a[1]/div/div/div[1]')
                engagement_open_element_not_found = False
                print("engagement_open_element found")
            except:
                print("retry finding engagement_open_element")
            time.sleep(0.5)

        engagement_open.click()
        time.sleep(2)

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

    def get_dataframe(self):

        df_comment = pd.DataFrame(columns=self.export_colomns)
        df_inbox = pd.DataFrame(columns=self.export_colomns)

        if len(self.comment_tickets) > 0:
            df_comment = pd.DataFrame(self.comment_tickets,columns=self.export_colomns)

            df_comment["Message_Time"] = pd.to_datetime(df_comment.Message_Time)
            df_comment = df_comment.sort_values(by='Message_Time', ascending=True)

            df_comment["Message_Time"] = df_comment["Message_Time"].dt.strftime("%A, %B %d, %Y %I:%M:%S %p")

            print(df_comment)
            print(self.comment_tickets)
        if len(self.inbox_tickets) > 0:
            df_inbox = pd.DataFrame(self.inbox_tickets,columns=self.export_colomns)

            df_inbox["Message_Time"] = pd.to_datetime(df_inbox.Message_Time)
            df_inbox = df_inbox.sort_values(by='Message_Time',ascending=True)

            df_inbox["Message_Time"] = df_inbox["Message_Time"].dt.strftime("%A, %B %d, %Y %I:%M:%S %p")

            print(df_inbox)
            print(self.inbox_tickets)

        return df_comment,df_inbox


    def test(self,scrolls = 5 ):
        scroll_box_public = self.driver.find_element_by_xpath('//*[@id="sprEngagementWorkspace"]/div/div/div[2]/div/div[2]/div[2]/div/div/section/div')
        scroll_box_private = self.driver.find_elements_by_xpath('//*[@id="sprEngagementWorkspace"]/div/div/div[3]/div/div[2]/div[2]/div/div/section/div')
        #scroll_box_private[0].location_once_scrolled_into_view
        #scroll_box_public[0].location_once_scrolled_into_view
        # random_user_private = a.driver.find_elements_by_xpath('//*[@id="sprEngagementWorkspace"]/div/div/div[3]/div/div[2]/div[2]/div/div/section/div/div/div/div/article[2]/section/section/article/div/div/section[2]/div[1]/div/div[1]/div[1]/div/div')
        # random_user_private = a.driver.find_elements_by_xpath('//div[contains(text(),"Bleu Loi")]')
        # random_user_private[0].location_once_scrolled_into_view

        # from selenium.webdriver.common.action_chains import ActionChains
        # ActionChains(a.driver).move_to_element(scroll_box_private).perform()

        scroll_height = -260
        for _ in range(scrolls):
            scroll_height += 260
            self.driver.execute_script("arguments[0].scrollTo(0, {})".format(scroll_height), scroll_box_public)
            time.sleep(0.2)
            #a.driver.execute_script("arguments[0].scrollTo(0, {})".format(scroll_height), scroll_box_private)
            self.driver.execute_script("arguments[0].scrollTo(0, {})".format(scroll_height),scroll_box_private[0])
            time.sleep(0.2)
            self.getTicketContent()
        self.get_dataframe()


    def export_to_excel(self):

        export_sheet = ["Comment", "Inbox"]

        # delete the previous export sheets
        wb = openpyxl.load_workbook(self.export_path)
        sheets = wb.sheetnames
        for i in export_sheet:
            if i in sheets:
                wb.remove(wb[i])
        wb.save(self.export_path)


        df_comment, df_inbox = self.get_dataframe()

        dfs = [df_comment,df_inbox]

        for i,df in enumerate(dfs):
            wb = openpyxl.load_workbook(self.export_path)
            writer = pd.ExcelWriter(self.export_path, engine='openpyxl')
            writer.book = wb

            df.to_excel(writer, sheet_name=export_sheet[i], index=False)
            writer.save()
            writer.close()

    def export_with_openpyxl(self):

        #per_ticket_content = [ticket_time,ticket_name,ticket_text,ticket_link]

        df_comment, df_inbox = self.get_dataframe()

        if len(self.comment_tickets) > 0:

            ordered_comment_tickets = []
            for index, row in df_comment.iterrows():
                ticket = [row[self.export_colomns[0]],row[self.export_colomns[1]],row[self.export_colomns[2]],row[self.export_colomns[3]]]
                ordered_comment_tickets.append(ticket)

            wb = openpyxl.load_workbook(self.export_path)
            sheet_public = wb["Public"]

            sheet_public.delete_rows(2, 200)

            for i,each_ticket in enumerate(ordered_comment_tickets):
                for n,each_piece_of_info in enumerate(each_ticket):
                    sheet_public.cell(row=2+i,column=n+1).value = each_piece_of_info

            wb.save(self.export_path)

        if len(self.inbox_tickets) > 0:

            ordered_inbox_tickets = []
            for index, row in df_inbox.iterrows():
                ticket = [row[self.export_colomns[0]],row[self.export_colomns[1]],row[self.export_colomns[2]],row[self.export_colomns[3]]]
                ordered_inbox_tickets.append(ticket)

            wb = openpyxl.load_workbook(self.export_path)
            sheet_private = wb["Private"]

            sheet_private.delete_rows(2,200)

            for i, each_ticket in enumerate(ordered_inbox_tickets):
                for n, each_piece_of_info in enumerate(each_ticket):
                    sheet_private.cell(row=2+i,column=n+1).value = each_piece_of_info

            wb.save(self.export_path)





a = pandoraBot()
a.login()




