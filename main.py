import sys
import mainwindow
from PyQt5.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)
win = QMainWindow()

ui = mainwindow.Ui_MainWindow()
ui.setupUi(win)

ui.btn_del.clicked.connect(lambda: ui.ans.setText(ui.ans.text()[:-1]))
ui.btn_clr.clicked.connect(lambda: ui.ans.setText(""))

ui.btn_div.clicked.connect(lambda: ui.ans.setText(ui.ans.text() + "/"))
ui.btn_mul.clicked.connect(lambda: ui.ans.setText(ui.ans.text() + "*"))
ui.btn_min.clicked.connect(lambda: ui.ans.setText(ui.ans.text() + "-"))
ui.btn_plus.clicked.connect(lambda: ui.ans.setText(ui.ans.text() + "+"))

ui.btn_1.clicked.connect(lambda: ui.ans.setText(ui.ans.text() + "1"))
ui.btn_2.clicked.connect(lambda: ui.ans.setText(ui.ans.text() + "2"))
ui.btn_3.clicked.connect(lambda: ui.ans.setText(ui.ans.text() + "3"))
ui.btn_4.clicked.connect(lambda: ui.ans.setText(ui.ans.text() + "4"))
ui.btn_5.clicked.connect(lambda: ui.ans.setText(ui.ans.text() + "5"))
ui.btn_6.clicked.connect(lambda: ui.ans.setText(ui.ans.text() + "6"))
ui.btn_7.clicked.connect(lambda: ui.ans.setText(ui.ans.text() + "7"))
ui.btn_8.clicked.connect(lambda: ui.ans.setText(ui.ans.text() + "8"))
ui.btn_9.clicked.connect(lambda: ui.ans.setText(ui.ans.text() + "9"))
ui.btn_0.clicked.connect(lambda: ui.ans.setText(ui.ans.text() + "0"))

def answer_ts_shit():
    try:
        return str(eval(ui.ans.text()))
    except ZeroDivisionError:
        return "Can't divide by 0"
    except SyntaxError:
        return "Invalid expresion"

ui.btn_dec.clicked.connect(lambda: ui.ans.setText(ui.ans.text() + "."))
ui.btn_ans.clicked.connect(lambda: ui.ans.setText(answer_ts_shit()))

win.show()
sys.exit(app.exec_())
