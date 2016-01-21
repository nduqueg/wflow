__author__ = 'schelle'

import unittest
import logging
import sys
sys.path = ['../Scripts'] + ['../'] + sys.path
import bmi_runner_hydro_routing as bmi
import time
import os

"""
Simple test for wflow bmi framework
"""


class MyTest(unittest.TestCase):

    def testbmifuncs(self):

        bmiobj = bmi.wflowbmi_csdms()
        bmiobj.initialize('bmirunner.ini')

        print bmiobj.get_component_name().split(',')
        print bmiobj.get_input_var_names()
        print bmiobj.get_output_var_names()
        print bmiobj.get_start_time()
        print bmiobj.get_end_time()
        print bmiobj.get_current_time()
        print bmiobj.get_time_step()
        steps =  (bmiobj.get_end_time() -  bmiobj.get_start_time())/bmiobj.get_time_step() + 1
        print steps
        for a in range(0,steps):
            bmiobj.update()
        bmiobj.finalize()


if __name__ == '__main__':
    unittest.main()
