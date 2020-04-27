# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkbillkpp.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem, QGraphicsPixmapItem
import requests
import shutil

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(999, 585)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("I:/python/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 221, 561))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 201, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.te_user = QtWidgets.QTextEdit(self.groupBox)
        self.te_user.setGeometry(QtCore.QRect(10, 50, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.te_user.setFont(font)
        self.te_user.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.te_user.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.te_user.setObjectName("te_user")
        self.te_password = QtWidgets.QTextEdit(self.groupBox)
        self.te_password.setGeometry(QtCore.QRect(10, 110, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.te_password.setFont(font)
        self.te_password.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.te_password.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.te_password.setObjectName("te_password")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 201, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.te_capcha = QtWidgets.QTextEdit(self.groupBox)
        self.te_capcha.setGeometry(QtCore.QRect(10, 240, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.te_capcha.setFont(font)
        self.te_capcha.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.te_capcha.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.te_capcha.setObjectName("te_capcha")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 180, 201, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lb_capcha = QtWidgets.QLabel(self.groupBox)
        self.lb_capcha.setGeometry(QtCore.QRect(80, 170, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lb_capcha.setFont(font)
        self.lb_capcha.setText("Capcha")
        self.lb_capcha.setPixmap(QtGui.QPixmap("capcha.jpg"))
        self.lb_capcha.setObjectName("lb_capcha")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 310, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.te_otp = QtWidgets.QTextEdit(self.groupBox)
        self.te_otp.setGeometry(QtCore.QRect(10, 340, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.te_otp.setFont(font)
        self.te_otp.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.te_otp.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.te_otp.setObjectName("te_otp")
        self.btn_capcha = QtWidgets.QPushButton(self.groupBox)
        self.btn_capcha.setGeometry(QtCore.QRect(120, 240, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.btn_capcha.setFont(font)
        self.btn_capcha.setObjectName("btn_capcha")
        self.btn_login = QtWidgets.QPushButton(self.groupBox)
        self.btn_login.setGeometry(QtCore.QRect(120, 380, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.btn_login.setFont(font)
        self.btn_login.setObjectName("btn_login")
        self.lb_statuslogin = QtWidgets.QLabel(self.groupBox)
        self.lb_statuslogin.setGeometry(QtCore.QRect(10, 440, 191, 16))
        self.lb_statuslogin.setObjectName("lb_statuslogin")
        self.btn_capcha_2 = QtWidgets.QPushButton(self.groupBox)
        self.btn_capcha_2.setGeometry(QtCore.QRect(10, 380, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.btn_capcha_2.setFont(font)
        self.btn_capcha_2.setObjectName("btn_capcha_2")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(450, 20, 541, 551))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tb_tatca = QtWidgets.QTableWidget(self.tab)
        self.tb_tatca.setGeometry(QtCore.QRect(10, 10, 511, 461))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.tb_tatca.setFont(font)
        self.tb_tatca.setRowCount(14)
        self.tb_tatca.setObjectName("tb_tatca")
        self.tb_tatca.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tb_tatca.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_tatca.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_tatca.setHorizontalHeaderItem(2, item)
        self.tb_tatca.horizontalHeader().setDefaultSectionSize(160)
        self.btn_check = QtWidgets.QPushButton(self.tab)
        self.btn_check.setGeometry(QtCore.QRect(440, 480, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.btn_check.setFont(font)
        self.btn_check.setObjectName("btn_check")
        self.btn_export = QtWidgets.QPushButton(self.tab)
        self.btn_export.setGeometry(QtCore.QRect(330, 480, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.btn_export.setFont(font)
        self.btn_export.setObjectName("btn_export")
        self.btn_clear = QtWidgets.QPushButton(self.tab)
        self.btn_clear.setGeometry(QtCore.QRect(240, 480, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.btn_clear.setFont(font)
        self.btn_clear.setObjectName("btn_clear")
        self.lb_status = QtWidgets.QLabel(self.tab)
        self.lb_status.setGeometry(QtCore.QRect(10, 490, 161, 21))
        self.lb_status.setObjectName("lb_status")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tb_nocuoc = QtWidgets.QTableWidget(self.tab_2)
        self.tb_nocuoc.setGeometry(QtCore.QRect(10, 10, 511, 461))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.tb_nocuoc.setFont(font)
        self.tb_nocuoc.setRowCount(14)
        self.tb_nocuoc.setObjectName("tb_nocuoc")
        self.tb_nocuoc.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tb_nocuoc.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_nocuoc.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_nocuoc.setHorizontalHeaderItem(2, item)
        self.tb_nocuoc.horizontalHeader().setDefaultSectionSize(160)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tb_khongno = QtWidgets.QTableWidget(self.tab_3)
        self.tb_khongno.setGeometry(QtCore.QRect(10, 10, 511, 461))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.tb_khongno.setFont(font)
        self.tb_khongno.setRowCount(14)
        self.tb_khongno.setObjectName("tb_khongno")
        self.tb_khongno.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tb_khongno.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_khongno.setHorizontalHeaderItem(1, item)
        self.tb_khongno.horizontalHeader().setDefaultSectionSize(240)
        self.tabWidget.addTab(self.tab_3, "")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(240, 10, 191, 561))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.te_makhachhang = QtWidgets.QTextEdit(self.groupBox_2)
        self.te_makhachhang.setGeometry(QtCore.QRect(10, 30, 171, 471))
        self.te_makhachhang.setObjectName("te_makhachhang")
        self.lb_tongbill = QtWidgets.QLabel(self.groupBox_2)
        self.lb_tongbill.setGeometry(QtCore.QRect(10, 530, 161, 21))
        self.lb_tongbill.setObjectName("lb_tongbill")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.btn_capcha.clicked.connect(self.getcapcha)
        self.btn_capcha_2.clicked.connect(self.getotp)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "CheckBill_ViettelPayPro_by_SimCongDanh"))
        self.groupBox.setTitle(_translate("Dialog", "Login"))
        self.label.setText(_translate("Dialog", "User :"))
        self.label_2.setText(_translate("Dialog", "Password :"))
        self.label_3.setText(_translate("Dialog", "Capcha :"))
        self.label_5.setText(_translate("Dialog", "OTP :"))
        self.btn_capcha.setText(_translate("Dialog", "Load Capcha"))
        self.btn_login.setText(_translate("Dialog", "Login"))
        self.lb_statuslogin.setText(_translate("Dialog", "Status :"))
        self.btn_capcha_2.setText(_translate("Dialog", "Get OTP"))
        item = self.tb_tatca.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Mã khách hàng"))
        item = self.tb_tatca.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Tên khách hàng"))
        item = self.tb_tatca.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Số tiền"))
        self.btn_check.setText(_translate("Dialog", "Check"))
        self.btn_export.setText(_translate("Dialog", "Xuất Excel"))
        self.btn_clear.setText(_translate("Dialog", "Xóa"))
        self.lb_status.setText(_translate("Dialog", "Status :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Tất cả"))
        item = self.tb_nocuoc.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Mã khách hàng"))
        item = self.tb_nocuoc.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Tên khách hàng"))
        item = self.tb_nocuoc.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Số tiền"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Nợ cước"))
        item = self.tb_khongno.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Mã khách hàng"))
        item = self.tb_khongno.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Số tiền"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Không nợ"))
        self.groupBox_2.setTitle(_translate("Dialog", "Mã khách hàng "))
        self.lb_tongbill.setText(_translate("Dialog", "Tổng bill :"))

    def getcapcha(self):
        self.lb_statuslogin.setText(f"Status : Loading . . .")
        url = "https://kpp.bankplus.vn/"
        r1 = requests.get(url)
        a = r1.headers
        b = a['Set-Cookie']
        if b != '':
            cookies = b[:-18]
        else:
            cookies = r1.cookies
        self.cookies = cookies
        headers = {
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'Connection': 'keep-alive',
            'Host': 'kpp.bankplus.vn',
            'Referer': 'https://kpp.bankplus.vn/',
            'Cookie': cookies,
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/85.0.134 Chrome/79.0.3945.134 Safari/537.36'
        }
        self.headers = headers
        url2 = 'https://kpp.bankplus.vn/captcha.png'
        file = open("capcha.jpg", "wb")
        r2 = requests.get(url2, headers=headers, stream=True)
        r2.raw.decode_content = True
        shutil.copyfileobj(r2.raw, file)
        self.lb_capcha.setPixmap(QtGui.QPixmap("capcha.jpg"))
        print(cookies)
    def getotp(self):
        cookies = self.te_makhachhang.toPlainText()
        capcha = self.te_capcha.toPlainText()
        url = 'https://kpp.bankplus.vn/faces/login.xhtml'
        headers = {
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'Connection': 'keep-alive',
            'Host': 'kpp.bankplus.vn',
            'Referer': 'https://kpp.bankplus.vn/',
            'Cookie': cookies,
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/85.0.134 Chrome/79.0.3945.134 Safari/537.36'
        }
        data = {
            'javax.faces.partial.ajax': 'true',
            'javax.faces.source': 'loginForm:btnLogin',
            'javax.faces.partial.execute':'@all',
            'javax.faces.partial.render': 'loginForm:msgError',
            'loginForm': 'accountPanel',
            'loginForm': 'confirmPanel',
            'loginForm': 'focusID',
            'loginForm': 'btnLogin: loginForm: btnLogin',
            'loginForm': 'loginForm',
            'userName': '1000849100_01858_DB',
            'password': '290797',
            'securityCode': capcha,
            'chkSaveInfo_input': 'on'
        }
        r1 = requests.post(url, data=data, headers=headers)
        print(r1.text)
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
