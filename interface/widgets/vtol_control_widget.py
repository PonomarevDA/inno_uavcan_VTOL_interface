import uavcan
from functools import partial

from interface.panels.functions import make_icon_button, get_monospace_font, get_icon
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QLabel, QDialog, QSlider, QSpinBox, QDoubleSpinBox, \
    QPlainTextEdit, QGroupBox
from PyQt5.QtCore import QTimer, Qt
from logging import getLogger
from win32api import GetSystemMetrics


PANEL_NAME = 'Vtol Panel'


logger = getLogger(__name__)

_singleton = None


class PercentSlider(QWidget):
    def __init__(self, parent):
        super(PercentSlider, self).__init__(parent)

        self._slider = QSlider(Qt.Vertical, self)
        self._slider.setMinimum(-100)
        self._slider.setMaximum(100)
        self._slider.setValue(0)
        self._slider.setTickInterval(100)
        self._slider.setTickPosition(QSlider.TicksBothSides)
        self._slider.valueChanged.connect(lambda: self._spinbox.setValue(self._slider.value()))

        self._spinbox = QSpinBox(self)
        self._spinbox.setMinimum(-100)
        self._spinbox.setMaximum(100)
        self._spinbox.setValue(0)
        self._spinbox.valueChanged.connect(lambda: self._slider.setValue(self._spinbox.value()))

        self._zero_button = make_icon_button('hand-stop-o', 'Zero setpoint', self, on_clicked=self.zero)

        layout = QVBoxLayout(self)
        sub_layout = QHBoxLayout(self)
        sub_layout.addStretch()
        sub_layout.addWidget(self._slider)
        sub_layout.addStretch()
        layout.addLayout(sub_layout)
        layout.addWidget(self._spinbox)
        layout.addWidget(self._zero_button)
        self.setLayout(layout)

        self.setMinimumHeight(400)
        # self.setMinimumHeight(int(GetSystemMetrics(1) * 0.35))

    def zero(self):
        self._slider.setValue(0)

    def get_value(self):
        return self._slider.value()


class ControlWidget(QGroupBox):
    DEFAULT_INTERVAL = 0.1

    CMD_BIT_LENGTH = uavcan.get_uavcan_data_type(uavcan.equipment.esc.RawCommand().cmd).value_type.bitlen
    CMD_MAX = 2 ** (CMD_BIT_LENGTH - 1) - 1
    CMD_MIN = -(2 ** (CMD_BIT_LENGTH - 1))

    # def __init__(self, parent):
    def __init__(self, parent, node):
        super(ControlWidget, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)  # This is required to stop background timers!

        self._node = node

        self._sliders = [PercentSlider(self) for _ in range(8)]

        # self._num_sliders = QSpinBox(self)
        # self._num_sliders.setMinimum(len(self._sliders))
        # self._num_sliders.setMaximum(20)
        # self._num_sliders.setValue(len(self._sliders))
        # self._num_sliders.valueChanged.connect(self._update_number_of_sliders)

        self._bcast_interval = QDoubleSpinBox(self)
        self._bcast_interval.setMinimum(0.01)
        self._bcast_interval.setMaximum(1.0)
        self._bcast_interval.setSingleStep(0.1)
        self._bcast_interval.setValue(self.DEFAULT_INTERVAL)
        self._bcast_interval.valueChanged.connect(
            lambda: self._bcast_timer.setInterval(self._bcast_interval.value() * 1e3))

        self._stop_all = make_icon_button('hand-stop-o', 'Zero all channels', self, text='Stop All',
                                          on_clicked=self._do_stop_all)

        self._pause = make_icon_button('pause', 'Pause publishing', self, checkable=True, text='Pause')

        self._msg_viewer = QPlainTextEdit(self)
        self._msg_viewer.setReadOnly(True)
        self._msg_viewer.setLineWrapMode(QPlainTextEdit.NoWrap)
        self._msg_viewer.setFont(get_monospace_font())
        self._msg_viewer.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self._msg_viewer.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self._msg_viewer.setFixedHeight(self.height() * 5)

        self._bcast_timer = QTimer(self)
        self._bcast_timer.start(self.DEFAULT_INTERVAL * 1e3)
        self._bcast_timer.timeout.connect(self._do_broadcast)

        layout = QVBoxLayout(self)

        self._slider_layout = QHBoxLayout(self)
        for sl in self._sliders:
            self._slider_layout.addWidget(sl)
        layout.addLayout(self._slider_layout)

        layout.addWidget(self._stop_all)

        controls_layout = QHBoxLayout(self)
        controls_layout.addWidget(QLabel('Channels:', self))
        controls_layout.addWidget(QLabel('Broadcast interval:', self))
        controls_layout.addWidget(self._bcast_interval)
        controls_layout.addWidget(QLabel('sec', self))
        controls_layout.addStretch()
        controls_layout.addWidget(self._pause)
        layout.addLayout(controls_layout)

        layout.addWidget(QLabel('Generated message:', self))
        layout.addWidget(self._msg_viewer)

        self.setLayout(layout)
        self.resize(self.minimumWidth(), self.minimumHeight())

    def _do_broadcast(self):
        try:
            if not self._pause.isChecked():
                msg = uavcan.equipment.esc.RawCommand()
                for sl in self._sliders:
                    raw_value = sl.get_value() / 100
                    value = (-self.CMD_MIN if raw_value < 0 else self.CMD_MAX) * raw_value
                    msg.cmd.append(int(value))

                self._node.broadcast(msg)
                self._msg_viewer.setPlainText(uavcan.to_yaml(msg))
            else:
                self._msg_viewer.setPlainText('Paused')
        except Exception as ex:
            self._msg_viewer.setPlainText('Publishing failed:\n' + str(ex))

    def _do_stop_all(self):
        for sl in self._sliders:
            sl.zero()

    def __del__(self):
        global _singleton
        _singleton = None

    def closeEvent(self, event):
        global _singleton
        _singleton = None
        super(ControlWidget, self).closeEvent(event)


def spawn(parent, node):
    global _singleton
    if _singleton is None:
        _singleton = ControlWidget(parent, node)

    _singleton.show()
    _singleton.raise_()
    _singleton.activateWindow()

    return _singleton
