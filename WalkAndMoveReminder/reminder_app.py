import reminder_design
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QFormLayout, QMessageBox
import traceback, sys, pyautogui, playsound, time, ast
from PyQt5.QtMultimedia import QSound
from PyQt5 import QtTest
from pydub import AudioSegment

class ReminderApp(reminder_design.Ui_MainWindow,QtWidgets.QMainWindow):

    def __init__(self):

        super(ReminderApp,self).__init__()
        self.setupUi(self)
        self.setFixedSize(534,354)
        self.setWindowTitle("Reminder")

        working_hour_items = [str(m) for m in range(0,4,1)]
        self.comboBox_workingh.addItems(working_hour_items)
        working_minutes_items = [str(mm) for mm in range(1,5,1)] + [str(m) for m in range(0,60,5)]
        self.comboBox_workingm.addItems(working_minutes_items)

        chilling_hour_items = [str(m) for m in range(0,4,1)]
        self.comboBox_chillingh.addItems(chilling_hour_items)
        chilling_minutes_items = [str(mm) for mm in range(1,5,1)] + [str(m) for m in range(0,60,5)]
        self.comboBox_chillingm.addItems(chilling_minutes_items)

        self.button_begin.clicked.connect(self.setReminder)

    def reminder(self,working_minutes, chilling_minutes, language):  # eng 0 chi 1

        working_seconds = 60 * working_minutes
        chilling_seconds = 60 * chilling_minutes

        while True:
            if self.button_begin.text() == "Begin":
                break

            QSound.play(r"work_sound.wav")
            work_start_time = time.ctime()
            eng_msg = "Working period: " + str(working_minutes) + " minutes"
            chi_msg = "工作时长 " + str(working_minutes) + " 分钟"
            msg = [eng_msg, chi_msg]
            print(msg[language])

            msgbox = QMessageBox()
            msgbox.setWindowTitle("Work alarm")
            msgbox.setText(msg[language])
            msgbox.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            msgbox.setDefaultButton(QMessageBox.Ok)
            result = msgbox.exec_()
            if result == QMessageBox.Cancel:
                print("Cancelled")
                self.button_begin.setText("Begin")
                break
            elif result == QMessageBox.Ok:
                pass

            print("work begin")
            QtTest.QTest.qWait(working_seconds*1000)

            if self.button_begin.text() == "Begin":
                break

            QSound.play(r'move_sound.wav')
            move_start_time = time.ctime()
            eng_msg = "Work done. Get your ass moving right now. You have " + str(
                chilling_minutes) + " minutes to stretch, beginning now at " + str(move_start_time)
            chi_msg = "好了，先放下工作，你现在有 " + str(chilling_minutes) + " 分钟松松筋骨, 从现在时间 " + str(move_start_time) + " 开始"
            msg = [eng_msg, chi_msg]
            print(msg[language])

            pyautogui.alert(title="Well...",text=msg[language],timeout=4000)
            print("chill begin")

            QtTest.QTest.qWait((chilling_seconds-4)*1000)

            if self.button_begin.text() == "Begin":
                break

            eng_msg = "Great, one round finished\n"
            chi_msg = "太好了，一轮结束了"
            msg = [eng_msg, chi_msg]
            print(msg[language])
            #QMessageBox.about(self,"Well...",msg[language])
            pyautogui.alert(title="Well...",text=msg[language],timeout=2000)

    def setReminder(self):

        if self.button_begin.text() == "Begin":

            self.button_begin.setText("End")

            working_h = ast.literal_eval(self.comboBox_workingh.currentText())
            working_m = ast.literal_eval(self.comboBox_workingm.currentText())
            chilling_h = ast.literal_eval(self.comboBox_chillingh.currentText())
            chilling_m = ast.literal_eval(self.comboBox_chillingm.currentText())

            ttl_working_minutes = working_h * 60 + working_m
            ttl_chilling_minutes = chilling_h * 60 + chilling_m

            self.reminder(ttl_working_minutes, ttl_chilling_minutes, 0)
            print("loop has ended")

        elif self.button_begin.text() == "End":
            self.button_begin.setText("Begin")
            print("You just clicked \"End\"")
            return

def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("error catched!:")
    print("error message:\n", tb)
    pyautogui.alert(title="E r r o r",text=tb)

if __name__ == '__main__':
    sys.excepthook = excepthook
    app = QtWidgets.QApplication(sys.argv)
    qt_app = ReminderApp()
    qt_app.show()
    ret = app.exec_()
    print("event loop exited")
    sys.exit(ret)




