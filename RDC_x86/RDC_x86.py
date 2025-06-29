#-*- coding:utf-8 -*-
# ... Made By Mukho
# ... 2020-07-16 THU
# ... 2022-06-23 THU: Update(23div->23bde)
# ... VSCode 가상환경 참조: https://redfox.tistory.com/21#32%EB%B9%84%ED%8A%B8%EC%9A%A9_%ED%8C%8C%EC%9D%B4%EC%8D%AC_%EC%84%A4%EC%B9%98
# ... Window XP 환경에서 돌아가야 하는 프로그램 -> 가상머신에 Window 7 32bit를 설치 후, 그 환경에서 제작하여 해결
# ... 폴더 다운로드 후, 바로가기 파일을 이용해 프로그램 실행
# ... 23Bde Reservation Date Calculator

# Import
import sys
from PyQt4 import QtGui
from PyQt4.QtGui import QIcon, QApplication, QWidget, QLabel, QVBoxLayout, QCalendarWidget
from PyQt4.QtCore import QDate

class MyApp(QWidget):
    # MyApp 생성자
    def __init__(self):
        super(MyApp, self).__init__()
        self.initUI()
    
    # 초기 UI
    def initUI(self):
        # Made By Mukho
        self.lbl = QLabel(self)
        self.lbl.setText("Made By Mukho")

        # 메인 달력
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.setVerticalHeaderFormat(0)
        cal.clicked.connect(self.showDate)

        # 글자 크기 변경
        font = QtGui.QFont()
        font.setPointSize(18)

        # 오늘 날짜
        self.lbl_today = QLabel(self)
        today = QDate.currentDate()
        self.lbl_today.setText(u"◇오늘 날짜 : " + today.toString('yyyy-MM-dd dddd'))
        self.lbl_today.setFont(font)

        # 오늘 기준 23여단 간부 예약일자 계산
        self.lbl_bde23 = QLabel(self)
        bde23 = today.addDays(12)
        self.lbl_bde23.setText(u"◆오늘 기준 23여단 예약 가능한 날짜 : ~" + bde23.toString('yyyy-MM-dd dddd'))
        self.lbl_bde23.setFont(font)

        # 오늘 기준 타 여단 간부 예약일자 계산
        self.lbl_bdeAnother = QLabel(self)
        bdeAnother = today.addDays(8)
        self.lbl_bdeAnother.setText(u"◆오늘 기준 타부대 예약 가능한 날짜 : ~" + bdeAnother.toString('yyyy-MM-dd dddd'))
        self.lbl_bdeAnother.setFont(font)

        # 결계
        self.bungsye = QLabel(self)
        self.bungsye.setText("--------------------------------------------------")
        self.bungsye.setFont(font)

        # 선택된 날짜
        self.lbl_select_day = QLabel(self)
        date = cal.selectedDate()
        self.lbl_select_day.setText(u"☆선택된 날짜 : " + date.toString('yyyy-MM-dd dddd'))
        self.lbl_select_day.setFont(font)

        # 23여단 간부의 경우 선택된 날짜는 언제 예약이 가능한가?
        self.lbl_select_bde23 = QLabel(self)
        bde23_select = date.addDays(-12)
        self.lbl_select_bde23.setText(u"★23여단 예약 가능한 날짜 : " + bde23_select.toString('yyyy-MM-dd dddd')+"~")
        self.lbl_select_bde23.setFont(font)

        # 타여단 간부의 경우 선택된 날짜는 언제 예약이 가능한가?
        self.lbl_select_bdeAnother = QLabel(self)
        bdeAnother_select = date.addDays(-8)
        self.lbl_select_bdeAnother.setText(u"★타부대 예약 가능한 날짜 : " + bdeAnother_select.toString('yyyy-MM-dd dddd') + "~")
        self.lbl_select_bdeAnother.setFont(font)

        # 위젯들을 수직 방향으로 배치하는 레이아웃 사용
        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl)
        vbox.addWidget(cal)
        vbox.addWidget(self.lbl_today)
        vbox.addWidget(self.lbl_bde23)
        vbox.addWidget(self.lbl_bdeAnother)
        vbox.addWidget(self.bungsye)
        vbox.addWidget(self.lbl_select_day)
        vbox.addWidget(self.lbl_select_bde23)
        vbox.addWidget(self.lbl_select_bdeAnother)

        # 설정
        self.setLayout(vbox)

        # 제목, 아이콘, 초기 위치 + 창 크기 설정 및 프로그램 실행
        self.setWindowTitle(u'철벽레스텔 예약 일자 계산기')
        self.setWindowIcon(QIcon('23Bde.png'))
        self.setGeometry(300, 300, 350, 450)
        self.show()

    # 달력에서 날짜를 선택했을 때, 출력되는 날짜들 계산
    def showDate(self, date):
        self.lbl_select_day.setText(u"☆선택된 날짜 : " + date.toString('yyyy-MM-dd dddd'))

        # 23여단 간부
        bde23_select = date.addDays(-12)
        self.lbl_select_bde23.setText(u"★23여단 예약 가능한 날짜 : " + bde23_select.toString('yyyy-MM-dd dddd') + "~")

        # 타여단 간부
        bdeAnother_select = date.addDays(-8)
        self.lbl_select_bdeAnother.setText(u"★타부대 예약 가능한 날짜 : " + bdeAnother_select.toString('yyyy-MM-dd dddd') + "~")

# Main
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
