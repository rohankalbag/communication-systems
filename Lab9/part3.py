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

from PyQt5 import Qt
from gnuradio import qtgui
import sip
from gnuradio import analog
from gnuradio import blocks
import numpy
from gnuradio import digital
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.filter import pfb



from gnuradio import qtgui

class part3(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "part3")

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
        self.symb_rate = symb_rate = 20e3
        self.sps = sps = 5
        self.samp_rate = samp_rate = symb_rate*sps
        self.ntaps = ntaps = 11*sps
        self.nfilts = nfilts = 32
        self.gain = gain = 2
        self.excess_bw = excess_bw = 0.5

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccf(
                interpolation=1,
                decimation=20,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=20,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_ccf(
            sps,
            taps=firdes.root_raised_cosine(gain,sps*symb_rate,symb_rate,excess_bw,ntaps),
            flt_size=32)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(0)
        self.low_pass_filter_0_1 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                2e6,
                60e3,
                5000,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0_0_0 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                2e6,
                60e3,
                5000,
                window.WIN_HAMMING,
                6.76))
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, (2*3.1415)/100, firdes.root_raised_cosine(gain,nfilts*sps*symb_rate,symb_rate,excess_bw,ntaps), nfilts, 16, 1.5, 1)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc([-1 + 1j,1 - 1j, 1 +1j, -1 -1j], 2)
        self.blocks_multiply_xx_1_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_ff(0.5)
        self.blocks_multiply_const_vxx_0_0_3_0 = blocks.multiply_const_ff(-0.5)
        self.blocks_multiply_const_vxx_0_0_3 = blocks.multiply_const_ff(-0.5)
        self.blocks_multiply_const_vxx_0_0_2_0_0 = blocks.multiply_const_ff(0.0625)
        self.blocks_multiply_const_vxx_0_0_2_0 = blocks.multiply_const_ff(0.0625)
        self.blocks_multiply_const_vxx_0_0_1_0_0 = blocks.multiply_const_ff(-0.125)
        self.blocks_multiply_const_vxx_0_0_1_0 = blocks.multiply_const_ff(-0.125)
        self.blocks_multiply_const_vxx_0_0_0_0_0 = blocks.multiply_const_ff(0.25)
        self.blocks_multiply_const_vxx_0_0_0_0 = blocks.multiply_const_ff(0.25)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(0.5)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_delay_0_1 = blocks.delay(gr.sizeof_float*1, 1)
        self.blocks_delay_0_0_2_0 = blocks.delay(gr.sizeof_float*1, 1)
        self.blocks_delay_0_0_2 = blocks.delay(gr.sizeof_float*1, 1)
        self.blocks_delay_0_0_1_0_0 = blocks.delay(gr.sizeof_float*1, 2)
        self.blocks_delay_0_0_1_0 = blocks.delay(gr.sizeof_float*1, 2)
        self.blocks_delay_0_0_0_1_0 = blocks.delay(gr.sizeof_float*1, 3)
        self.blocks_delay_0_0_0_1 = blocks.delay(gr.sizeof_float*1, 3)
        self.blocks_delay_0_0_0_0_0_0 = blocks.delay(gr.sizeof_float*1, 4)
        self.blocks_delay_0_0_0_0_0 = blocks.delay(gr.sizeof_float*1, 4)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, 1)
        self.blocks_complex_to_float_1 = blocks.complex_to_float(1)
        self.blocks_add_xx_1_0_0 = blocks.add_vff(1)
        self.blocks_add_xx_1_0 = blocks.add_vff(1)
        self.blocks_add_xx_0_0 = blocks.add_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_0_1 = analog.sig_source_f(2e6, analog.GR_COS_WAVE, 100e3, 1, 0, 90)
        self.analog_sig_source_x_0_0_0 = analog.sig_source_f(2e6, analog.GR_COS_WAVE, 100e3, 1, 0, 90)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(2e6, analog.GR_COS_WAVE, 100e3, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(2e6, analog.GR_COS_WAVE, 100e3, 1, 0, 0)
        self.analog_random_source_x_0 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, 2, 1000))), True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_multiply_xx_1_0, 0))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.blocks_multiply_xx_1_0, 1))
        self.connect((self.blocks_add_xx_1_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_add_xx_1_0_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_complex_to_float_1, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_complex_to_float_1, 1), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_delay_0_0_0_0_0, 0), (self.blocks_multiply_const_vxx_0_0_2_0, 0))
        self.connect((self.blocks_delay_0_0_0_0_0_0, 0), (self.blocks_multiply_const_vxx_0_0_2_0_0, 0))
        self.connect((self.blocks_delay_0_0_0_1, 0), (self.blocks_multiply_const_vxx_0_0_1_0, 0))
        self.connect((self.blocks_delay_0_0_0_1_0, 0), (self.blocks_multiply_const_vxx_0_0_1_0_0, 0))
        self.connect((self.blocks_delay_0_0_1_0, 0), (self.blocks_multiply_const_vxx_0_0_0_0, 0))
        self.connect((self.blocks_delay_0_0_1_0_0, 0), (self.blocks_multiply_const_vxx_0_0_0_0_0, 0))
        self.connect((self.blocks_delay_0_0_2, 0), (self.blocks_multiply_const_vxx_0_0_3, 0))
        self.connect((self.blocks_delay_0_0_2_0, 0), (self.blocks_multiply_const_vxx_0_0_3_0, 0))
        self.connect((self.blocks_delay_0_1, 0), (self.blocks_multiply_const_vxx_0_1, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0_0_0_0, 0), (self.blocks_add_xx_1_0, 2))
        self.connect((self.blocks_multiply_const_vxx_0_0_0_0_0, 0), (self.blocks_add_xx_1_0_0, 2))
        self.connect((self.blocks_multiply_const_vxx_0_0_1_0, 0), (self.blocks_add_xx_1_0, 3))
        self.connect((self.blocks_multiply_const_vxx_0_0_1_0_0, 0), (self.blocks_add_xx_1_0_0, 3))
        self.connect((self.blocks_multiply_const_vxx_0_0_2_0, 0), (self.blocks_add_xx_1_0, 4))
        self.connect((self.blocks_multiply_const_vxx_0_0_2_0_0, 0), (self.blocks_add_xx_1_0_0, 4))
        self.connect((self.blocks_multiply_const_vxx_0_0_3, 0), (self.blocks_add_xx_1_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0_0_3_0, 0), (self.blocks_add_xx_1_0_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.blocks_add_xx_0_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_add_xx_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_delay_0_1, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.low_pass_filter_0_1, 0))
        self.connect((self.blocks_multiply_xx_1_0, 0), (self.low_pass_filter_0_0_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.low_pass_filter_0_0_0, 0), (self.blocks_add_xx_1_0, 0))
        self.connect((self.low_pass_filter_0_0_0, 0), (self.blocks_delay_0_0_0_0_0, 0))
        self.connect((self.low_pass_filter_0_0_0, 0), (self.blocks_delay_0_0_0_1, 0))
        self.connect((self.low_pass_filter_0_0_0, 0), (self.blocks_delay_0_0_1_0, 0))
        self.connect((self.low_pass_filter_0_0_0, 0), (self.blocks_delay_0_0_2, 0))
        self.connect((self.low_pass_filter_0_1, 0), (self.blocks_add_xx_1_0_0, 0))
        self.connect((self.low_pass_filter_0_1, 0), (self.blocks_delay_0_0_0_0_0_0, 0))
        self.connect((self.low_pass_filter_0_1, 0), (self.blocks_delay_0_0_0_1_0, 0))
        self.connect((self.low_pass_filter_0_1, 0), (self.blocks_delay_0_0_1_0_0, 0))
        self.connect((self.low_pass_filter_0_1, 0), (self.blocks_delay_0_0_2_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_complex_to_float_1, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.digital_pfb_clock_sync_xxx_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "part3")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_symb_rate(self):
        return self.symb_rate

    def set_symb_rate(self, symb_rate):
        self.symb_rate = symb_rate
        self.set_samp_rate(self.symb_rate*self.sps)
        self.digital_pfb_clock_sync_xxx_0.update_taps(firdes.root_raised_cosine(self.gain,self.nfilts*self.sps*self.symb_rate,self.symb_rate,self.excess_bw,self.ntaps))
        self.pfb_arb_resampler_xxx_0.set_taps(firdes.root_raised_cosine(self.gain,self.sps*self.symb_rate,self.symb_rate,self.excess_bw,self.ntaps))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_ntaps(11*self.sps)
        self.set_samp_rate(self.symb_rate*self.sps)
        self.digital_pfb_clock_sync_xxx_0.update_taps(firdes.root_raised_cosine(self.gain,self.nfilts*self.sps*self.symb_rate,self.symb_rate,self.excess_bw,self.ntaps))
        self.pfb_arb_resampler_xxx_0.set_taps(firdes.root_raised_cosine(self.gain,self.sps*self.symb_rate,self.symb_rate,self.excess_bw,self.ntaps))
        self.pfb_arb_resampler_xxx_0.set_rate(self.sps)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.digital_pfb_clock_sync_xxx_0.update_taps(firdes.root_raised_cosine(self.gain,self.nfilts*self.sps*self.symb_rate,self.symb_rate,self.excess_bw,self.ntaps))
        self.pfb_arb_resampler_xxx_0.set_taps(firdes.root_raised_cosine(self.gain,self.sps*self.symb_rate,self.symb_rate,self.excess_bw,self.ntaps))

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.digital_pfb_clock_sync_xxx_0.update_taps(firdes.root_raised_cosine(self.gain,self.nfilts*self.sps*self.symb_rate,self.symb_rate,self.excess_bw,self.ntaps))

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.digital_pfb_clock_sync_xxx_0.update_taps(firdes.root_raised_cosine(self.gain,self.nfilts*self.sps*self.symb_rate,self.symb_rate,self.excess_bw,self.ntaps))
        self.pfb_arb_resampler_xxx_0.set_taps(firdes.root_raised_cosine(self.gain,self.sps*self.symb_rate,self.symb_rate,self.excess_bw,self.ntaps))

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw
        self.digital_pfb_clock_sync_xxx_0.update_taps(firdes.root_raised_cosine(self.gain,self.nfilts*self.sps*self.symb_rate,self.symb_rate,self.excess_bw,self.ntaps))
        self.pfb_arb_resampler_xxx_0.set_taps(firdes.root_raised_cosine(self.gain,self.sps*self.symb_rate,self.symb_rate,self.excess_bw,self.ntaps))




def main(top_block_cls=part3, options=None):

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
