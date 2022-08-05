#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: equalizer
# GNU Radio version: 3.9.5.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from gnuradio import audio
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore



from gnuradio import qtgui

class expt_3(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "equalizer", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("equalizer")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "expt_3")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 48000
        self.g5 = g5 = 5
        self.g4 = g4 = 5
        self.g3 = g3 = 5
        self.g2 = g2 = 5
        self.g1 = g1 = 5

        ##################################################
        # Blocks
        ##################################################
        self._g5_range = Range(0, 10, 1, 5, 200)
        self._g5_win = RangeWidget(self._g5_range, self.set_g5, "'g5'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._g5_win)
        self._g4_range = Range(0, 10, 1, 5, 200)
        self._g4_win = RangeWidget(self._g4_range, self.set_g4, "'g4'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._g4_win)
        self._g3_range = Range(0, 10, 1, 5, 200)
        self._g3_win = RangeWidget(self._g3_range, self.set_g3, "'g3'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._g3_win)
        self._g2_range = Range(0, 10, 1, 5, 200)
        self._g2_win = RangeWidget(self._g2_range, self.set_g2, "'g2'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._g2_win)
        self._g1_range = Range(0, 10, 1, 5, 200)
        self._g1_win = RangeWidget(self._g1_range, self.set_g1, "'g1'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._g1_win)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/rohan/Desktop/EE340/Lab1/Bach.wav', True)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.band_pass_filter_0_3 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                g5,
                samp_rate,
                9200,
                14800,
                400,
                window.WIN_RECTANGULAR,
                6.76))
        self.band_pass_filter_0_2 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                g4,
                samp_rate,
                6100,
                8900,
                200,
                window.WIN_RECTANGULAR,
                6.76))
        self.band_pass_filter_0_1 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                g3,
                samp_rate,
                3000,
                6000,
                100,
                window.WIN_RECTANGULAR,
                6.76))
        self.band_pass_filter_0_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                g2,
                samp_rate,
                550,
                3000,
                100,
                window.WIN_RECTANGULAR,
                6.76))
        self.band_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                g1,
                samp_rate,
                20,
                500,
                20,
                window.WIN_RECTANGULAR,
                6.76))
        self.audio_sink_0 = audio.sink(samp_rate, '', True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.band_pass_filter_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.band_pass_filter_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.band_pass_filter_0_1, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.band_pass_filter_0_2, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.band_pass_filter_0_3, 0), (self.blocks_add_xx_0, 4))
        self.connect((self.blocks_add_xx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0_1, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0_2, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0_3, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "expt_3")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.band_pass_filter_0.set_taps(firdes.band_pass(self.g1, self.samp_rate, 20, 500, 20, window.WIN_RECTANGULAR, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(self.g2, self.samp_rate, 550, 3000, 100, window.WIN_RECTANGULAR, 6.76))
        self.band_pass_filter_0_1.set_taps(firdes.band_pass(self.g3, self.samp_rate, 3000, 6000, 100, window.WIN_RECTANGULAR, 6.76))
        self.band_pass_filter_0_2.set_taps(firdes.band_pass(self.g4, self.samp_rate, 6100, 8900, 200, window.WIN_RECTANGULAR, 6.76))
        self.band_pass_filter_0_3.set_taps(firdes.band_pass(self.g5, self.samp_rate, 9200, 14800, 400, window.WIN_RECTANGULAR, 6.76))

    def get_g5(self):
        return self.g5

    def set_g5(self, g5):
        self.g5 = g5
        self.band_pass_filter_0_3.set_taps(firdes.band_pass(self.g5, self.samp_rate, 9200, 14800, 400, window.WIN_RECTANGULAR, 6.76))

    def get_g4(self):
        return self.g4

    def set_g4(self, g4):
        self.g4 = g4
        self.band_pass_filter_0_2.set_taps(firdes.band_pass(self.g4, self.samp_rate, 6100, 8900, 200, window.WIN_RECTANGULAR, 6.76))

    def get_g3(self):
        return self.g3

    def set_g3(self, g3):
        self.g3 = g3
        self.band_pass_filter_0_1.set_taps(firdes.band_pass(self.g3, self.samp_rate, 3000, 6000, 100, window.WIN_RECTANGULAR, 6.76))

    def get_g2(self):
        return self.g2

    def set_g2(self, g2):
        self.g2 = g2
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(self.g2, self.samp_rate, 550, 3000, 100, window.WIN_RECTANGULAR, 6.76))

    def get_g1(self):
        return self.g1

    def set_g1(self, g1):
        self.g1 = g1
        self.band_pass_filter_0.set_taps(firdes.band_pass(self.g1, self.samp_rate, 20, 500, 20, window.WIN_RECTANGULAR, 6.76))




def main(top_block_cls=expt_3, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
