# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_bealuna_eng.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.other_f = QtWidgets.QLineEdit(Form)
        self.other_f.setAlignment(QtCore.Qt.AlignCenter)
        self.other_f.setObjectName("other_f")
        self.gridLayout.addWidget(self.other_f, 12, 2, 1, 2)
        self.sludge_f = QtWidgets.QLineEdit(Form)
        self.sludge_f.setAlignment(QtCore.Qt.AlignCenter)
        self.sludge_f.setObjectName("sludge_f")
        self.gridLayout.addWidget(self.sludge_f, 11, 2, 1, 2)
        self.slops_f = QtWidgets.QLineEdit(Form)
        self.slops_f.setAlignment(QtCore.Qt.AlignCenter)
        self.slops_f.setObjectName("slops_f")
        self.gridLayout.addWidget(self.slops_f, 10, 2, 1, 2)
        self.fw_l = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.fw_l.setFont(font)
        self.fw_l.setObjectName("fw_l")
        self.gridLayout.addWidget(self.fw_l, 6, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.ballast_f = QtWidgets.QLineEdit(Form)
        self.ballast_f.setAlignment(QtCore.Qt.AlignCenter)
        self.ballast_f.setObjectName("ballast_f")
        self.gridLayout.addWidget(self.ballast_f, 5, 2, 1, 2)
        self.hfo_l = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.hfo_l.setFont(font)
        self.hfo_l.setObjectName("hfo_l")
        self.gridLayout.addWidget(self.hfo_l, 7, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.lo_f = QtWidgets.QLineEdit(Form)
        self.lo_f.setAlignment(QtCore.Qt.AlignCenter)
        self.lo_f.setObjectName("lo_f")
        self.gridLayout.addWidget(self.lo_f, 9, 2, 1, 2)
        self.hfo_f = QtWidgets.QLineEdit(Form)
        self.hfo_f.setAlignment(QtCore.Qt.AlignCenter)
        self.hfo_f.setObjectName("hfo_f")
        self.gridLayout.addWidget(self.hfo_f, 7, 2, 1, 2)
        self.mgo_f = QtWidgets.QLineEdit(Form)
        self.mgo_f.setAlignment(QtCore.Qt.AlignCenter)
        self.mgo_f.setObjectName("mgo_f")
        self.gridLayout.addWidget(self.mgo_f, 8, 2, 1, 2)
        self.fw_f = QtWidgets.QLineEdit(Form)
        self.fw_f.setAlignment(QtCore.Qt.AlignCenter)
        self.fw_f.setObjectName("fw_f")
        self.gridLayout.addWidget(self.fw_f, 6, 2, 1, 2)
        self.slops_l = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.slops_l.setFont(font)
        self.slops_l.setObjectName("slops_l")
        self.gridLayout.addWidget(self.slops_l, 10, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.M_ps_line = QtWidgets.QLineEdit(Form)
        self.M_ps_line.setAlignment(QtCore.Qt.AlignCenter)
        self.M_ps_line.setObjectName("M_ps_line")
        self.gridLayout.addWidget(self.M_ps_line, 2, 0, 1, 1)
        self.F_ss_line = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.F_ss_line.sizePolicy().hasHeightForWidth())
        self.F_ss_line.setSizePolicy(sizePolicy)
        self.F_ss_line.setMinimumSize(QtCore.QSize(0, 0))
        self.F_ss_line.setAlignment(QtCore.Qt.AlignCenter)
        self.F_ss_line.setObjectName("F_ss_line")
        self.gridLayout.addWidget(self.F_ss_line, 1, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 1, 1, 2, QtCore.Qt.AlignHCenter)
        self.ship = QtWidgets.QLabel(Form)
        self.ship.setText("")
        self.ship.setPixmap(QtGui.QPixmap("ship.jpg"))
        self.ship.setObjectName("ship")
        self.gridLayout.addWidget(self.ship, 1, 1, 3, 2)
        self.drafts_label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drafts_label.sizePolicy().hasHeightForWidth())
        self.drafts_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.drafts_label.setFont(font)
        self.drafts_label.setMidLineWidth(1)
        self.drafts_label.setObjectName("drafts_label")
        self.gridLayout.addWidget(self.drafts_label, 0, 1, 1, 2, QtCore.Qt.AlignHCenter)
        self.F_ps_line = QtWidgets.QLineEdit(Form)
        self.F_ps_line.setAlignment(QtCore.Qt.AlignCenter)
        self.F_ps_line.setObjectName("F_ps_line")
        self.gridLayout.addWidget(self.F_ps_line, 1, 0, 1, 1)
        self.A_ss_line = QtWidgets.QLineEdit(Form)
        self.A_ss_line.setAlignment(QtCore.Qt.AlignCenter)
        self.A_ss_line.setObjectName("A_ss_line")
        self.gridLayout.addWidget(self.A_ss_line, 3, 3, 1, 1)
        self.A_ps_line = QtWidgets.QLineEdit(Form)
        self.A_ps_line.setAlignment(QtCore.Qt.AlignCenter)
        self.A_ps_line.setObjectName("A_ps_line")
        self.gridLayout.addWidget(self.A_ps_line, 3, 0, 1, 1)
        self.M_ss_line = QtWidgets.QLineEdit(Form)
        self.M_ss_line.setAlignment(QtCore.Qt.AlignCenter)
        self.M_ss_line.setObjectName("M_ss_line")
        self.gridLayout.addWidget(self.M_ss_line, 2, 3, 1, 1)
        self.ballast_l = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.ballast_l.setFont(font)
        self.ballast_l.setObjectName("ballast_l")
        self.gridLayout.addWidget(self.ballast_l, 5, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.mgo_l = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.mgo_l.setFont(font)
        self.mgo_l.setObjectName("mgo_l")
        self.gridLayout.addWidget(self.mgo_l, 8, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.lo_l = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.lo_l.setFont(font)
        self.lo_l.setObjectName("lo_l")
        self.gridLayout.addWidget(self.lo_l, 9, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.sludge_l = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.sludge_l.setFont(font)
        self.sludge_l.setObjectName("sludge_l")
        self.gridLayout.addWidget(self.sludge_l, 11, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.other_l = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.other_l.setFont(font)
        self.other_l.setObjectName("other_l")
        self.gridLayout.addWidget(self.other_l, 12, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 2, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dens_l = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dens_l.sizePolicy().hasHeightForWidth())
        self.dens_l.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.dens_l.setFont(font)
        self.dens_l.setObjectName("dens_l")
        self.horizontalLayout_2.addWidget(self.dens_l)
        self.dens_f = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dens_f.sizePolicy().hasHeightForWidth())
        self.dens_f.setSizePolicy(sizePolicy)
        self.dens_f.setAlignment(QtCore.Qt.AlignCenter)
        self.dens_f.setObjectName("dens_f")
        self.horizontalLayout_2.addWidget(self.dens_f)
        self.countBtn = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.countBtn.sizePolicy().hasHeightForWidth())
        self.countBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.countBtn.setFont(font)
        self.countBtn.setObjectName("countBtn")
        self.horizontalLayout_2.addWidget(self.countBtn)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.result_l = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.result_l.setFont(font)
        self.result_l.setObjectName("result_l")
        self.gridLayout_2.addWidget(self.result_l, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.result_lables = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result_lables.sizePolicy().hasHeightForWidth())
        self.result_lables.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.result_lables.setFont(font)
        self.result_lables.setFrameShape(QtWidgets.QFrame.Box)
        self.result_lables.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.result_lables.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.result_lables.setObjectName("result_lables")
        self.gridLayout_2.addWidget(self.result_lables, 1, 0, 1, 1)
        self.result = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result.sizePolicy().hasHeightForWidth())
        self.result.setSizePolicy(sizePolicy)
        self.result.setMinimumSize(QtCore.QSize(200, 480))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.result.setFont(font)
        self.result.setFrameShape(QtWidgets.QFrame.Box)
        self.result.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.result.setText("")
        self.result.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.result.setObjectName("result")
        self.gridLayout_2.addWidget(self.result, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.F_ps_line, self.F_ss_line)
        Form.setTabOrder(self.F_ss_line, self.M_ps_line)
        Form.setTabOrder(self.M_ps_line, self.M_ss_line)
        Form.setTabOrder(self.M_ss_line, self.A_ps_line)
        Form.setTabOrder(self.A_ps_line, self.A_ss_line)
        Form.setTabOrder(self.A_ss_line, self.ballast_f)
        Form.setTabOrder(self.ballast_f, self.fw_f)
        Form.setTabOrder(self.fw_f, self.hfo_f)
        Form.setTabOrder(self.hfo_f, self.mgo_f)
        Form.setTabOrder(self.mgo_f, self.lo_f)
        Form.setTabOrder(self.lo_f, self.slops_f)
        Form.setTabOrder(self.slops_f, self.sludge_f)
        Form.setTabOrder(self.sludge_f, self.other_f)
        Form.setTabOrder(self.other_f, self.dens_f)
        Form.setTabOrder(self.dens_f, self.countBtn)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Draft survey HC Bea-Luna"))
        self.fw_l.setText(_translate("Form", "Fresh water:"))
        self.hfo_l.setText(_translate("Form", "Heavy fuel:"))
        self.slops_l.setText(_translate("Form", "Slop stores:"))
        self.label_10.setText(_translate("Form", "Consumables:"))
        self.drafts_label.setText(_translate("Form", "Drafts:"))
        self.ballast_l.setText(_translate("Form", "Ballast:"))
        self.mgo_l.setText(_translate("Form", "Diesel oil:"))
        self.lo_l.setText(_translate("Form", "Lube oil:"))
        self.sludge_l.setText(_translate("Form", "Sludge:"))
        self.other_l.setText(_translate("Form", "Other:"))
        self.dens_l.setText(_translate("Form", "Water density:"))
        self.countBtn.setText(_translate("Form", "Calculate\n"
"displacement"))
        self.result_l.setText(_translate("Form", "Results:"))
        self.result_lables.setText(_translate("Form", "Fwd, Mid, Aft mean draft, m:\n"
"Fwd mark misplacement, m:\n"
"Mid mark misplacement, m:\n"
"Aft mark misplacement, m:\n"
"Apparent trim, m:\n"
"Fwd draft correction, m:\n"
"Mid draft correction, m:\n"
"Aft draft correction, m:\n"
"Fwd corrected draft, m:\n"
"Mid corrected draft, m:\n"
"Aft corrected draft, m:\n"
"True trim, m:\n"
"Deflection:\n"
"Mean of means corrected, m:\n"
"Displacement by MOMC, mt:\n"
"TPC, mt:\n"
"LCF, m:\n"
"First trim correction, mt:\n"
"MTC by MOMC:\n"
"MTC + / -:\n"
"MTC difference:  \n"
"Second trim correction, mt:\n"
"Disp. corrected by trim, mt: \n"
"Constant, mt:\n"
"\n"
"Displacement corrected, mt:"))

