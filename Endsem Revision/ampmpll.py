#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: rohan
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

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
import pmt
from gnuradio import digital
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

class ampmpll(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
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

        self.settings = Qt.QSettings("GNU Radio", "ampmpll")

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
        self.variable_qtgui_range_0 = variable_qtgui_range_0 = 500000
        self.samp_rate = samp_rate = 1.5e6

        ##################################################
        # Blocks
        ##################################################
        self._variable_qtgui_range_0_range = Range(495000, 510000, 1000, 500000, 200)
        self._variable_qtgui_range_0_win = RangeWidget(self._variable_qtgui_range_0_range, self.set_variable_qtgui_range_0, "'variable_qtgui_range_0'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._variable_qtgui_range_0_win)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_fff(
                interpolation=44100,
                decimation=1500000,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=44100,
                decimation=1500000,
                taps=[],
                fractional_bw=0)
        self.low_pass_filter_0 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                9e3,
                700,
                window.WIN_HAMMING,
                6.76))
        self.hilbert_fc_0 = filter.hilbert_fc(65, window.WIN_HAMMING, 6.76)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(2*3.14/100, 4, False)
        self.dc_blocker_xx_0 = filter.dc_blocker_ff(32, True)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_float*1, '/home/rohan/Desktop/EE340/Endsem Revision/PM_AM_Modulated.dat', True, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_arg_0 = blocks.complex_to_arg(1)
        self.blocks_abs_xx_0 = blocks.abs_ff(1)
        self.audio_sink_0_0 = audio.sink(44100, '', True)
        self.analog_pll_carriertracking_cc_0 = analog.pll_carriertracking_cc(50e-3, 6.28, -6.28)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_pll_carriertracking_cc_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.blocks_abs_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_complex_to_arg_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_abs_xx_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.hilbert_fc_0, 0))
        self.connect((self.dc_blocker_xx_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.blocks_complex_to_arg_0, 0))
        self.connect((self.hilbert_fc_0, 0), (self.analog_pll_carriertracking_cc_0, 0))
        self.connect((self.hilbert_fc_0, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.dc_blocker_xx_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.audio_sink_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ampmpll")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_variable_qtgui_range_0(self):
        return self.variable_qtgui_range_0

    def set_variable_qtgui_range_0(self, variable_qtgui_range_0):
        self.variable_qtgui_range_0 = variable_qtgui_range_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_multiply_const_vxx_0.set_k(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 9e3, 700, window.WIN_HAMMING, 6.76))




def main(top_block_cls=ampmpll, options=None):

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
