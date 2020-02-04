# -*- coding: utf-8 -*-

import re
import pandas as pd
import openpyxl

# posted = "Posted onMonday, February 03, 2020 12:07:21 AM"
#
# msgtime_regex = re.compile(r'Posted on(.*)')
# ticket_time = msgtime_regex.search(posted).group(1)
#
# time = "Monday, February 03, 2020 12:07:32 AM"
#
# comment_tickets = [['Sunday, February 02, 2020 10:45:40 AM', 'Y L Chan', 'How much?', 'https://www.facebook.com/153753694819713/posts/1249108418617563/?comment_id=1250340885160983'],['Monday, February 03, 2020 11:29:26 AM', 'Chan Wing Yiu', r'https://scontent.xx.fbcdn.net/v/t1.0-9/s720x720/84003939_10157382231709440_3622552945624612864_n.jpg?_nc_cat=102&_nc_oc=AQlq6wf-34Mj-fjynxxUsqUjMdrT_ekpFIBT2Az0-3416A_X124IBKikqCPAeGvuhfY&_nc_ht=scontent.xx&oh=0fa985bb028b65bc4aaf3662ee0bddf4&oe=5EBB5493', r'https://www.facebook.com/153753694819713/posts/1249085878619817/?comment_id=1251058991755839'
# ],['Monday, February 02, 2020 9:29:26 AM', 'Chan Wing Yiu', r'https://scontent.xx.fbcdn.net/v/t1.0-9/s720x720/84003939_10157382231709440_3622552945624612864_n.jpg?_nc_cat=102&_nc_oc=AQlq6wf-34Mj-fjynxxUsqUjMdrT_ekpFIBT2Az0-3416A_X124IBKikqCPAeGvuhfY&_nc_ht=scontent.xx&oh=0fa985bb028b65bc4aaf3662ee0bddf4&oe=5EBB5493', r'https://www.facebook.com/153753694819713/posts/1249085878619817/?comment_id=1251058991755839']]
#
# inbox_tickets = [['Monday, February 03, 2020 12:07:32 AM', 'HoWai Lam', '門市有得買？', 'Inbox'], ['Monday, February 03, 2020 12:07:21 AM', 'HoWai Lam', 'https://s3.amazonaws.com/spr-uploads-prod/815/FACEBOOK/82906/media/192A7B70A2A4B7997448C1AB747EE185', 'Inbox']]
#
# df_comment = pd.DataFrame(comment_tickets,columns=["Message_Time","Customer Name","Enquiry","URL"])
#
# df_inbox = pd.DataFrame(inbox_tickets,columns=["Message Time","Customer Name","Enquiry","URL"])
#
# df_comment["Message_Time"] = pd.to_datetime(df_comment.Message_Time)
#
# df_comment = df_comment.sort_values(by ='Message_Time',ascending=False)
#
# df_comment["Message_Time"] = df_comment["Message_Time"].dt.strftime("%A, %B %d, %Y %I:%M:%S %p")
#
# """print(x.strftime("%b %d %Y %H:%M:%S"))
# Output:
#
# Sep 15 2018 00:00:00"""
#
# print(df_comment)

def delete_sheets():

    export_sheet = ["Comment", "Inbox"]
    wb_path = r'C:\Users\abc\PycharmProjects\somestuff\pandora_scraper\pandora_export.xlsx'
    wb = openpyxl.load_workbook(wb_path)
    sheets = wb.sheetnames
    for i in export_sheet:
        if i in sheets:
            wb.remove(wb[i])
    wb.save(wb_path)

def df_to_list():
    df = pd.DataFrame({'a': [1, 2, 3, 4],
                       'b': [5, 6, 7, 8]})

    print(df)
    print(df.iterrows())
    liss = []
    for index,row in df.iterrows():
        a = [row["a"],row["b"]]
        liss.append(a)
        print(a)
    print(liss)
    #print('list', [df[i].tolist() for i in df.iterrows()])

df_to_list()



