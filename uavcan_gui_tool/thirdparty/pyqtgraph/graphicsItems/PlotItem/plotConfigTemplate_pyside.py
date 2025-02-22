# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './pyqtgraph/graphicsItems/PlotItem/plotConfigTemplate.ui'
#
# Created: Mon Dec 23 10:10:52 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(481, 840)
        self.averageGroup = QtGui.QGroupBox(Form)
        self.averageGroup.setGeometry(QtCore.QRect(0, 640, 242, 182))
        self.averageGroup.setCheckable(True)
        self.averageGroup.setChecked(False)
        self.averageGroup.setObjectName("averageGroup")
        self.gridLayout_5 = QtGui.QGridLayout(self.averageGroup)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.avgParamList = QtGui.QListWidget(self.averageGroup)
        self.avgParamList.setObjectName("avgParamList")
        self.gridLayout_5.addWidget(self.avgParamList, 0, 0, 1, 1)
        self.decimateGroup = QtGui.QFrame(Form)
        self.decimateGroup.setGeometry(QtCore.QRect(10, 140, 191, 171))
        self.decimateGroup.setObjectName("decimateGroup")
        self.gridLayout_4 = QtGui.QGridLayout(self.decimateGroup)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.clipToViewCheck = QtGui.QCheckBox(self.decimateGroup)
        self.clipToViewCheck.setObjectName("clipToViewCheck")
        self.gridLayout_4.addWidget(self.clipToViewCheck, 7, 0, 1, 3)
        self.maxTracesCheck = QtGui.QCheckBox(self.decimateGroup)
        self.maxTracesCheck.setObjectName("maxTracesCheck")
        self.gridLayout_4.addWidget(self.maxTracesCheck, 8, 0, 1, 2)
        self.downsampleCheck = QtGui.QCheckBox(self.decimateGroup)
        self.downsampleCheck.setObjectName("downsampleCheck")
        self.gridLayout_4.addWidget(self.downsampleCheck, 0, 0, 1, 3)
        self.peakRadio = QtGui.QRadioButton(self.decimateGroup)
        self.peakRadio.setChecked(True)
        self.peakRadio.setObjectName("peakRadio")
        self.gridLayout_4.addWidget(self.peakRadio, 6, 1, 1, 2)
        self.maxTracesSpin = QtGui.QSpinBox(self.decimateGroup)
        self.maxTracesSpin.setObjectName("maxTracesSpin")
        self.gridLayout_4.addWidget(self.maxTracesSpin, 8, 2, 1, 1)
        self.forgetTracesCheck = QtGui.QCheckBox(self.decimateGroup)
        self.forgetTracesCheck.setObjectName("forgetTracesCheck")
        self.gridLayout_4.addWidget(self.forgetTracesCheck, 9, 0, 1, 3)
        self.meanRadio = QtGui.QRadioButton(self.decimateGroup)
        self.meanRadio.setObjectName("meanRadio")
        self.gridLayout_4.addWidget(self.meanRadio, 3, 1, 1, 2)
        self.subsampleRadio = QtGui.QRadioButton(self.decimateGroup)
        self.subsampleRadio.setObjectName("subsampleRadio")
        self.gridLayout_4.addWidget(self.subsampleRadio, 2, 1, 1, 2)
        self.autoDownsampleCheck = QtGui.QCheckBox(self.decimateGroup)
        self.autoDownsampleCheck.setChecked(True)
        self.autoDownsampleCheck.setObjectName("autoDownsampleCheck")
        self.gridLayout_4.addWidget(self.autoDownsampleCheck, 1, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 2, 0, 1, 1)
        self.downsampleSpin = QtGui.QSpinBox(self.decimateGroup)
        self.downsampleSpin.setMinimum(1)
        self.downsampleSpin.setMaximum(100000)
        self.downsampleSpin.setProperty("value", 1)
        self.downsampleSpin.setObjectName("downsampleSpin")
        self.gridLayout_4.addWidget(self.downsampleSpin, 1, 1, 1, 1)
        self.transformGroup = QtGui.QFrame(Form)
        self.transformGroup.setGeometry(QtCore.QRect(0, 0, 154, 79))
        self.transformGroup.setObjectName("transformGroup")
        self.gridLayout = QtGui.QGridLayout(self.transformGroup)
        self.gridLayout.setObjectName("gridLayout")
        self.fftCheck = QtGui.QCheckBox(self.transformGroup)
        self.fftCheck.setObjectName("fftCheck")
        self.gridLayout.addWidget(self.fftCheck, 0, 0, 1, 1)
        self.logXCheck = QtGui.QCheckBox(self.transformGroup)
        self.logXCheck.setObjectName("logXCheck")
        self.gridLayout.addWidget(self.logXCheck, 1, 0, 1, 1)
        self.logYCheck = QtGui.QCheckBox(self.transformGroup)
        self.logYCheck.setObjectName("logYCheck")
        self.gridLayout.addWidget(self.logYCheck, 2, 0, 1, 1)
        self.pointsGroup = QtGui.QGroupBox(Form)
        self.pointsGroup.setGeometry(QtCore.QRect(10, 550, 234, 58))
        self.pointsGroup.setCheckable(True)
        self.pointsGroup.setObjectName("pointsGroup")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.pointsGroup)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.autoPointsCheck = QtGui.QCheckBox(self.pointsGroup)
        self.autoPointsCheck.setChecked(True)
        self.autoPointsCheck.setObjectName("autoPointsCheck")
        self.verticalLayout_5.addWidget(self.autoPointsCheck)
        self.gridGroup = QtGui.QFrame(Form)
        self.gridGroup.setGeometry(QtCore.QRect(10, 460, 221, 81))
        self.gridGroup.setObjectName("gridGroup")
        self.gridLayout_2 = QtGui.QGridLayout(self.gridGroup)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.xGridCheck = QtGui.QCheckBox(self.gridGroup)
        self.xGridCheck.setObjectName("xGridCheck")
        self.gridLayout_2.addWidget(self.xGridCheck, 0, 0, 1, 2)
        self.yGridCheck = QtGui.QCheckBox(self.gridGroup)
        self.yGridCheck.setObjectName("yGridCheck")
        self.gridLayout_2.addWidget(self.yGridCheck, 1, 0, 1, 2)
        self.gridAlphaSlider = QtGui.QSlider(self.gridGroup)
        self.gridAlphaSlider.setMaximum(255)
        self.gridAlphaSlider.setProperty("value", 128)
        self.gridAlphaSlider.setOrientation(QtCore.Qt.Horizontal)
        self.gridAlphaSlider.setObjectName("gridAlphaSlider")
        self.gridLayout_2.addWidget(self.gridAlphaSlider, 2, 1, 1, 1)
        self.label = QtGui.QLabel(self.gridGroup)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.alphaGroup = QtGui.QGroupBox(Form)
        self.alphaGroup.setGeometry(QtCore.QRect(10, 390, 234, 60))
        self.alphaGroup.setCheckable(True)
        self.alphaGroup.setObjectName("alphaGroup")
        self.horizontalLayout = QtGui.QHBoxLayout(self.alphaGroup)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.autoAlphaCheck = QtGui.QCheckBox(self.alphaGroup)
        self.autoAlphaCheck.setChecked(False)
        self.autoAlphaCheck.setObjectName("autoAlphaCheck")
        self.horizontalLayout.addWidget(self.autoAlphaCheck)
        self.alphaSlider = QtGui.QSlider(self.alphaGroup)
        self.alphaSlider.setMaximum(1000)
        self.alphaSlider.setProperty("value", 1000)
        self.alphaSlider.setOrientation(QtCore.Qt.Horizontal)
        self.alphaSlider.setObjectName("alphaSlider")
        self.horizontalLayout.addWidget(self.alphaSlider)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.averageGroup.setToolTip(QtGui.QApplication.translate("Form",
                                                                  "Display averages of the curves displayed in this plot. The parameter list allows you to choose parameters to average over (if any are available).",
                                                                  None, QtGui.QApplication.UnicodeUTF8))
        self.averageGroup.setTitle(
            QtGui.QApplication.translate("Form", "Average", None, QtGui.QApplication.UnicodeUTF8))
        self.clipToViewCheck.setToolTip(QtGui.QApplication.translate("Form",
                                                                     "Plot only the portion of each curve that is visible. This assumes X values are uniformly spaced.",
                                                                     None, QtGui.QApplication.UnicodeUTF8))
        self.clipToViewCheck.setText(
            QtGui.QApplication.translate("Form", "Clip to View", None, QtGui.QApplication.UnicodeUTF8))
        self.maxTracesCheck.setToolTip(QtGui.QApplication.translate("Form",
                                                                    "If multiple curves are displayed in this plot, check this box to limit the number of traces that are displayed.",
                                                                    None, QtGui.QApplication.UnicodeUTF8))
        self.maxTracesCheck.setText(
            QtGui.QApplication.translate("Form", "Max Traces:", None, QtGui.QApplication.UnicodeUTF8))
        self.downsampleCheck.setText(
            QtGui.QApplication.translate("Form", "Downsample", None, QtGui.QApplication.UnicodeUTF8))
        self.peakRadio.setToolTip(QtGui.QApplication.translate("Form",
                                                               "Downsample by drawing a saw wave that follows the min and max of the original data. This method produces the best visual representation of the data but is slower.",
                                                               None, QtGui.QApplication.UnicodeUTF8))
        self.peakRadio.setText(QtGui.QApplication.translate("Form", "Peak", None, QtGui.QApplication.UnicodeUTF8))
        self.maxTracesSpin.setToolTip(QtGui.QApplication.translate("Form",
                                                                   "If multiple curves are displayed in this plot, check \"Max Traces\" and set this value to limit the number of traces that are displayed.",
                                                                   None, QtGui.QApplication.UnicodeUTF8))
        self.forgetTracesCheck.setToolTip(QtGui.QApplication.translate("Form",
                                                                       "If MaxTraces is checked, remove curves from memory after they are hidden (saves memory, but traces can not be un-hidden).",
                                                                       None, QtGui.QApplication.UnicodeUTF8))
        self.forgetTracesCheck.setText(
            QtGui.QApplication.translate("Form", "Forget hidden traces", None, QtGui.QApplication.UnicodeUTF8))
        self.meanRadio.setToolTip(
            QtGui.QApplication.translate("Form", "Downsample by taking the mean of N samples.", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.meanRadio.setText(QtGui.QApplication.translate("Form", "Mean", None, QtGui.QApplication.UnicodeUTF8))
        self.subsampleRadio.setToolTip(QtGui.QApplication.translate("Form",
                                                                    "Downsample by taking the first of N samples. This method is fastest and least accurate.",
                                                                    None, QtGui.QApplication.UnicodeUTF8))
        self.subsampleRadio.setText(
            QtGui.QApplication.translate("Form", "Subsample", None, QtGui.QApplication.UnicodeUTF8))
        self.autoDownsampleCheck.setToolTip(QtGui.QApplication.translate("Form",
                                                                         "Automatically downsample data based on the visible range. This assumes X values are uniformly spaced.",
                                                                         None, QtGui.QApplication.UnicodeUTF8))
        self.autoDownsampleCheck.setText(
            QtGui.QApplication.translate("Form", "Auto", None, QtGui.QApplication.UnicodeUTF8))
        self.downsampleSpin.setToolTip(
            QtGui.QApplication.translate("Form", "Downsample data before plotting. (plot every Nth sample)", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.downsampleSpin.setSuffix(QtGui.QApplication.translate("Form", "x", None, QtGui.QApplication.UnicodeUTF8))
        self.fftCheck.setText(
            QtGui.QApplication.translate("Form", "Power Spectrum (FFT)", None, QtGui.QApplication.UnicodeUTF8))
        self.logXCheck.setText(QtGui.QApplication.translate("Form", "Log X", None, QtGui.QApplication.UnicodeUTF8))
        self.logYCheck.setText(QtGui.QApplication.translate("Form", "Log Y", None, QtGui.QApplication.UnicodeUTF8))
        self.pointsGroup.setTitle(QtGui.QApplication.translate("Form", "Points", None, QtGui.QApplication.UnicodeUTF8))
        self.autoPointsCheck.setText(QtGui.QApplication.translate("Form", "Auto", None, QtGui.QApplication.UnicodeUTF8))
        self.xGridCheck.setText(
            QtGui.QApplication.translate("Form", "Show X Grid", None, QtGui.QApplication.UnicodeUTF8))
        self.yGridCheck.setText(
            QtGui.QApplication.translate("Form", "Show Y Grid", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Opacity", None, QtGui.QApplication.UnicodeUTF8))
        self.alphaGroup.setTitle(QtGui.QApplication.translate("Form", "Alpha", None, QtGui.QApplication.UnicodeUTF8))
        self.autoAlphaCheck.setText(QtGui.QApplication.translate("Form", "Auto", None, QtGui.QApplication.UnicodeUTF8))
