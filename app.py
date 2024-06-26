from PyQt5 import QtCore, QtGui, QtWidgets
from realtimepBloodPressure import RealTimeBloodPressure
from Utilities import*


class Ui_DialogBox(object):
    def setupUi(self, DialogBox):
        DialogBox.setObjectName("DialogBox")
        DialogBox.setWindowModality(QtCore.Qt.NonModal)
        DialogBox.resize(800, 495)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 234, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 234, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 234, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 234, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        DialogBox.setPalette(palette)
        font = QtGui.QFont()
        font.setUnderline(False)
        DialogBox.setFont(font)
        DialogBox.setModal(False)
        self.name_label = QtWidgets.QLabel(DialogBox)
        self.name_label.setGeometry(QtCore.QRect(130, 50, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.name_label.setFont(font)
        self.name_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name_label.setObjectName("name_label")
        self.Name_Text = QtWidgets.QTextEdit(DialogBox)
        self.Name_Text.setGeometry(QtCore.QRect(200, 50, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Name_Text.setFont(font)
        self.Name_Text.setObjectName("Name_Text")
        self.age_label = QtWidgets.QLabel(DialogBox)
        self.age_label.setGeometry(QtCore.QRect(140, 90, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.age_label.setFont(font)
        self.age_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.age_label.setObjectName("age_label")
        self.age_spinbox = QtWidgets.QSpinBox(DialogBox)
        self.age_spinbox.setGeometry(QtCore.QRect(200, 100, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.age_spinbox.setFont(font)
        self.age_spinbox.setMinimum(40)
        self.age_spinbox.setMaximum(150)
        self.age_spinbox.setObjectName("age_spinbox")
        self.gender_label = QtWidgets.QLabel(DialogBox)
        self.gender_label.setGeometry(QtCore.QRect(110, 250, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.gender_label.setFont(font)
        self.gender_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.gender_label.setObjectName("gender_label")
        self.smoking_status_label = QtWidgets.QLabel(DialogBox)
        self.smoking_status_label.setGeometry(QtCore.QRect(30, 300, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.smoking_status_label.setFont(font)
        self.smoking_status_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.smoking_status_label.setObjectName("smoking_status_label")
        self.diabetic_status_label = QtWidgets.QLabel(DialogBox)
        self.diabetic_status_label.setGeometry(QtCore.QRect(40, 350, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.diabetic_status_label.setFont(font)
        self.diabetic_status_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.diabetic_status_label.setObjectName("diabetic_status_label")
        self.blood_pressure_spinbox = QtWidgets.QSpinBox(DialogBox)
        self.blood_pressure_spinbox.setGeometry(QtCore.QRect(200, 150, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.blood_pressure_spinbox.setFont(font)
        self.blood_pressure_spinbox.setMinimum(120)
        self.blood_pressure_spinbox.setMaximum(400)
        self.blood_pressure_spinbox.setObjectName("blood_pressure_spinbox")
        self.blood_pressure_label = QtWidgets.QLabel(DialogBox)
        self.blood_pressure_label.setGeometry(QtCore.QRect(30, 140, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.blood_pressure_label.setFont(font)
        self.blood_pressure_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.blood_pressure_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.blood_pressure_label.setObjectName("blood_pressure_label")
        self.gender_comboBox = QtWidgets.QComboBox(DialogBox)
        self.gender_comboBox.setGeometry(QtCore.QRect(200, 250, 74, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gender_comboBox.setFont(font)
        self.gender_comboBox.setObjectName("gender_comboBox")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.smoking_status_comboBox = QtWidgets.QComboBox(DialogBox)
        self.smoking_status_comboBox.setGeometry(QtCore.QRect(200, 300, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.smoking_status_comboBox.setFont(font)
        self.smoking_status_comboBox.setObjectName("smoking_status_comboBox")
        self.smoking_status_comboBox.addItem("")
        self.smoking_status_comboBox.addItem("")
        self.diabetic_status_comboBox = QtWidgets.QComboBox(DialogBox)
        self.diabetic_status_comboBox.setGeometry(QtCore.QRect(200, 350, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.diabetic_status_comboBox.setFont(font)
        self.diabetic_status_comboBox.setObjectName("diabetic_status_comboBox")
        self.diabetic_status_comboBox.addItem("")
        self.diabetic_status_comboBox.addItem("")
        self.predicted_risk_label = QtWidgets.QLabel(DialogBox)
        self.predicted_risk_label.setGeometry(QtCore.QRect(530, 150, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setUnderline(False)
        self.predicted_risk_label.setFont(font)
        self.predicted_risk_label.setObjectName("predicted_risk_label")
        self.line = QtWidgets.QFrame(DialogBox)
        self.line.setGeometry(QtCore.QRect(430, 50, 21, 431))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.enter_pushButton = QtWidgets.QPushButton(DialogBox)
        self.enter_pushButton.setGeometry(QtCore.QRect(290, 440, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enter_pushButton.setFont(font)
        self.enter_pushButton.setAutoFillBackground(False)
        self.enter_pushButton.setStyleSheet("background-color:rgb(215, 224, 255)")
        self.enter_pushButton.setObjectName("enter_pushButton")
        self.enter_pushButton.clicked.connect(self.on_enter_button_clicked) # enter button clicked
        self.predicted_output_value_label = QtWidgets.QLabel(DialogBox)
        self.predicted_output_value_label.setGeometry(QtCore.QRect(590, 240, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.predicted_output_value_label.setFont(font)
        self.predicted_output_value_label.setStyleSheet("border: 2px solid black")
        self.predicted_output_value_label.setAlignment(QtCore.Qt.AlignCenter)
        self.predicted_output_value_label.setObjectName("predicted_output_value_label")
        self.color_label = QtWidgets.QLabel(DialogBox)
        self.color_label.setGeometry(QtCore.QRect(480, 240, 71, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.color_label.setPalette(palette)
        self.color_label.setStyleSheet("border: 2px solid black;background-color:rgb(255, 255, 255)")
        self.color_label.setText("")
        self.color_label.setObjectName("color_label")
        self.cholesterol_spinbox = QtWidgets.QSpinBox(DialogBox)
        self.cholesterol_spinbox.setGeometry(QtCore.QRect(200, 200, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cholesterol_spinbox.setFont(font)
        self.cholesterol_spinbox.setMinimum(4)
        self.cholesterol_spinbox.setMaximum(8)
        self.cholesterol_spinbox.setSingleStep(1)
        self.cholesterol_spinbox.setProperty("value", 4)
        self.cholesterol_spinbox.setObjectName("cholesterol_spinbox")
        self.cholesterol_label = QtWidgets.QLabel(DialogBox)
        self.cholesterol_label.setGeometry(QtCore.QRect(80, 190, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cholesterol_label.setFont(font)
        self.cholesterol_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cholesterol_label.setObjectName("cholesterol_label")
        self.clear_pushButton = QtWidgets.QPushButton(DialogBox)
        self.clear_pushButton.setGeometry(QtCore.QRect(110, 440, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.clear_pushButton.setFont(font)
        self.clear_pushButton.setAutoFillBackground(False)
        self.clear_pushButton.setStyleSheet("background-color:rgb(215, 224, 255)")
        self.clear_pushButton.setObjectName("clear_pushButton")
        self.clear_pushButton.clicked.connect(self.on_clear_button_clicked) # clear button clicked
        self.save_checkBox = QtWidgets.QCheckBox(DialogBox)
        self.save_checkBox.setGeometry(QtCore.QRect(310, 400, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.save_checkBox.setFont(font)
        self.save_checkBox.setObjectName("save_checkBox")
        self.label_2 = QtWidgets.QLabel(DialogBox)
        self.label_2.setGeometry(QtCore.QRect(610, 470, 171, 16))
        self.label_2.setObjectName("label_2")
        self.automode_pushButton = QtWidgets.QPushButton(DialogBox)
        self.automode_pushButton.setGeometry(QtCore.QRect(290, 150, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.automode_pushButton.setFont(font)
        self.automode_pushButton.setAutoFillBackground(False)
        self.automode_pushButton.setStyleSheet("background-color:rgb(215, 224, 255)")
        self.automode_pushButton.setObjectName("automode_pushButton")
        self.automode_pushButton.clicked.connect(self.on_auto_button_clicked) # auto push button clicked

        self.retranslateUi(DialogBox)
        QtCore.QMetaObject.connectSlotsByName(DialogBox)

        # Initialize auto mode window attribute
        self.auto_mode_window = None

    def retranslateUi(self, DialogBox):
        _translate = QtCore.QCoreApplication.translate
        DialogBox.setWindowTitle(_translate("DialogBox", "Cardiovascular Risk Predictor"))
        self.name_label.setText(_translate("DialogBox", "Name"))
        self.age_label.setText(_translate("DialogBox", " Age"))
        self.gender_label.setText(_translate("DialogBox", " Gender"))
        self.smoking_status_label.setText(_translate("DialogBox", " Smoking Status"))
        self.diabetic_status_label.setText(_translate("DialogBox", "Diabetic Status"))
        self.blood_pressure_label.setText(_translate("DialogBox", "  Blood Pressure"))
        self.gender_comboBox.setItemText(0, _translate("DialogBox", "Male"))
        self.gender_comboBox.setItemText(1, _translate("DialogBox", "Female"))
        self.smoking_status_comboBox.setItemText(0, _translate("DialogBox", "Smoker"))
        self.smoking_status_comboBox.setItemText(1, _translate("DialogBox", "Non-Smoker"))
        self.diabetic_status_comboBox.setItemText(0, _translate("DialogBox", "Diabetes"))
        self.diabetic_status_comboBox.setItemText(1, _translate("DialogBox", "Non-Diabetes"))
        self.predicted_risk_label.setText(_translate("DialogBox", "Predicted Risk"))
        self.enter_pushButton.setText(_translate("DialogBox", "Enter"))
        self.predicted_output_value_label.setText(_translate("DialogBox", "----"))
        self.cholesterol_label.setText(_translate("DialogBox", "Cholesterol"))
        self.clear_pushButton.setText(_translate("DialogBox", "Clear"))
        self.save_checkBox.setText(_translate("DialogBox", "save details"))
        self.label_2.setText(_translate("DialogBox", "Copyright © 2024 Vihanga Herath"))
        self.automode_pushButton.setText(_translate("DialogBox", "Auto"))

    def on_auto_button_clicked(self):
        if self.auto_mode_window is None:
            self.auto_mode_window = RealTimeBloodPressure()
            self.auto_mode_window.averageValueUpdated.connect(self.update_blood_pressure_spinbox)
            self.auto_mode_window.show()
            self.auto_mode_window.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.auto_mode_window.destroyed.connect(self.on_auto_window_closed)
        else:
            self.auto_mode_window.show()

    def on_auto_window_closed(self):
        self.auto_mode_window = None

    def update_blood_pressure_spinbox(self, avg_value):
        self.blood_pressure_spinbox.setValue(round(avg_value))
    
    def on_enter_button_clicked(self):
        print("predicting...")

        name = self.Name_Text.toPlainText()
        gender = self.gender_comboBox.currentText()
        smoking_status = self.smoking_status_comboBox.currentText()
        diabetic_status = self.diabetic_status_comboBox.currentText()
        age = self.age_spinbox.value()
        blood_pressure = self.blood_pressure_spinbox.value()
        cholesterol = self.cholesterol_spinbox.value()

        if True:
            print()
            print("Name:", name)
            print("age:", age)
            print("Gender:", gender)
            print("Smoking Status:", smoking_status)
            print("Diabetic Status:", diabetic_status)
            print("blood_pressure:", blood_pressure)
            print("cholesterol:", cholesterol)

        is_Male = on_gender(gender)
        diabetic_status = on_diabetic_status(diabetic_status)
        smoking_status = on_smoking_status(smoking_status)
        risk_level = predict_risk(name, age, is_Male, diabetic_status, smoking_status, blood_pressure, cholesterol)
        risk_level_color, risk_level_percentage = get_risk_level_details(risk_level)
        print(risk_level_color)
        print(risk_level_percentage)
        self.color_label.setStyleSheet(f"border: 2px solid black;background-color:{risk_level_color};")
        self.predicted_output_value_label.setText(f"{risk_level_percentage}")

        if self.save_checkBox.isChecked():
            save_details(name, age, is_Male, diabetic_status, smoking_status, blood_pressure, cholesterol, risk_level_color, risk_level_percentage)
            self.save_checkBox.setChecked(False)

    def on_clear_button_clicked(self):
        print("User interface is cleared!")
        self.Name_Text.clear()
        self.gender_comboBox.setCurrentIndex(0)
        self.smoking_status_comboBox.setCurrentIndex(0)
        self.diabetic_status_comboBox.setCurrentIndex(0)
        self.age_spinbox.setValue(40)
        self.blood_pressure_spinbox.setValue(120)
        self.cholesterol_spinbox.setValue(4)
        self.predicted_output_value_label.setText("----")
        self.color_label.setStyleSheet("border: 2px solid black;background-color:rgb(255, 255, 255);")
        self.save_checkBox.setChecked(False)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogBox = QtWidgets.QDialog()
    ui = Ui_DialogBox()
    ui.setupUi(DialogBox)
    DialogBox.show()
    sys.exit(app.exec_())
