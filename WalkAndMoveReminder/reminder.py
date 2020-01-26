# -*- coding: utf-8 -*-

import time, pyautogui, playsound, os,sys
from pydub import AudioSegment

def reminder(working_minutes,chilling_minutes,language):  # eng 0 chi 1

    working_seconds = 60 * working_minutes
    chilling_seconds = 60 * chilling_minutes

    while True:
        playsound.playsound(r"work_sound.mp3")
        work_start_time = time.ctime()
        eng_msg = "Starting time: " + str(work_start_time) + "\nWorking period: " + str(working_minutes) + " minutes"
        chi_msg = "开始时间: " + str(work_start_time) + "\n工作时长 " + str(working_minutes) + " 分钟"
        msg = [eng_msg,chi_msg]
        print(msg[language])
        time.sleep(working_seconds)

        playsound.playsound("move_sound.mp3")
        move_start_time = time.ctime()
        eng_msg = "Work done. Get your ass moving right now. You have " + str(chilling_minutes) + " minutes to stretch, beginning now at " + str(move_start_time)
        chi_msg = "好了，先放下工作，你现在有 " + str(chilling_minutes) + " 分钟松松筋骨, 从现在时间 " + str(move_start_time) + " 开始"
        msg = [eng_msg,chi_msg]
        print(msg[language])
        time.sleep(chilling_seconds)
        eng_msg = "Great, one round finished\n"
        chi_msg = "太好了，一轮结束了"
        msg = [eng_msg,chi_msg]
        print(msg[language])


def audioConvert(source, destination):
    sound = AudioSegment.from_mp3(source)
    sound.export(destination,format="wav")



if __name__ == "__main__":
    #reminder(2,1,0)

    source = "work_sound.mp3"
    destination = "work_sound.wav"
    #audioConvert(source, destination)










