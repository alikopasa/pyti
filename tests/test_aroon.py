from __future__ import absolute_import
import unittest
import numpy as np

from tests.sample_data import SampleData
from pyti import aroon


class TestAroon(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.data = SampleData().get_sample_close_data()

        self.aroon_up_period_6_expected = np.array([np.nan, np.nan, np.nan, np.nan,
        np.nan, 50.0, 16.666666666666664, 16.666666666666664, 33.333333333333329, 
        50.0, 16.666666666666664, 16.666666666666664, 33.333333333333329, 50.0, 
        66.666666666666657, 83.333333333333343, 100.0, 100.0, 83.333333333333343, 
        100.0, 100.0, 100.0, 16.666666666666664, 33.333333333333329, 50.0, 
        66.666666666666657, 83.333333333333343, 100.0, 100.0, 16.666666666666664, 
        33.333333333333329, 50.0, 66.666666666666657, 83.333333333333343, 100.0, 
        16.666666666666664, 16.666666666666664, 33.333333333333329, 50.0, 
        66.666666666666657, 83.333333333333343, 100.0, 16.666666666666664, 
        16.666666666666664, 33.333333333333329, 16.666666666666664, 16.666666666666664, 
        16.666666666666664, 33.333333333333329, 50.0, 66.666666666666657, 
        83.333333333333343, 100.0, 66.666666666666657, 83.333333333333343, 100.0, 100.0, 
        16.666666666666664, 33.333333333333329, 50.0, 66.666666666666657, 
        83.333333333333343, 100.0, 16.666666666666664, 33.333333333333329, 
        16.666666666666664, 16.666666666666664, 33.333333333333329, 16.666666666666664, 
        16.666666666666664, 33.333333333333329, 50.0, 66.666666666666657, 
        83.333333333333343, 100.0, 100.0, 50.0, 66.666666666666657, 83.333333333333343, 
        16.666666666666664, 16.666666666666664, 16.666666666666664, 33.333333333333329, 
        50.0, 66.666666666666657, 83.333333333333343, 100.0, 100.0, 50.0, 
        66.666666666666657, 16.666666666666664, 16.666666666666664, 16.666666666666664, 
        16.666666666666664, 16.666666666666664, 33.333333333333329, 16.666666666666664, 
        16.666666666666664, 16.666666666666664, 16.666666666666664, 33.333333333333329, 
        50.0, 66.666666666666657, 83.333333333333343, 100.0, 100.0, 83.333333333333343, 
        100.0, 50.0, 66.666666666666657, 83.333333333333343, 100.0, 100.0, 100.0, 100.0, 
        66.666666666666657, 83.333333333333343, 100.0, 83.333333333333343, 100.0, 100.0, 
        100.0, 83.333333333333343, 100.0, 83.333333333333343, 100.0, 100.0])

        self.aroon_down_period_14_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 100.0, 100.0, 
        7.1428571428571423, 7.1428571428571423, 7.1428571428571423, 14.285714285714285, 
        7.1428571428571423, 7.1428571428571423, 14.285714285714285, 21.428571428571427, 
        28.571428571428569, 35.714285714285715, 42.857142857142854, 50.0, 57.142857142857139, 
        64.285714285714292, 71.428571428571431, 78.571428571428569, 85.714285714285708, 
        7.1428571428571423, 14.285714285714285, 21.428571428571427, 28.571428571428569, 
        35.714285714285715, 42.857142857142854, 50.0, 57.142857142857139, 64.285714285714292, 
        71.428571428571431, 78.571428571428569, 85.714285714285708, 92.857142857142861, 
        100.0, 100.0, 100.0, 78.571428571428569, 85.714285714285708, 92.857142857142861, 
        100.0, 100.0, 100.0, 7.1428571428571423, 14.285714285714285, 21.428571428571427, 
        28.571428571428569, 7.1428571428571423, 14.285714285714285, 21.428571428571427, 
        28.571428571428569, 7.1428571428571423, 14.285714285714285, 21.428571428571427, 
        28.571428571428569, 35.714285714285715, 42.857142857142854, 50.0, 57.142857142857139, 
        64.285714285714292, 7.1428571428571423, 7.1428571428571423, 14.285714285714285, 
        21.428571428571427, 7.1428571428571423, 7.1428571428571423, 14.285714285714285, 
        7.1428571428571423, 14.285714285714285, 21.428571428571427, 28.571428571428569, 
        35.714285714285715, 42.857142857142854, 50.0, 57.142857142857139, 64.285714285714292, 
        71.428571428571431, 78.571428571428569, 85.714285714285708, 92.857142857142861, 
        100.0, 64.285714285714292, 71.428571428571431, 78.571428571428569, 85.714285714285708, 
        92.857142857142861, 100.0, 78.571428571428569, 85.714285714285708, 92.857142857142861, 
        100.0, 100.0, 100.0, 100.0, 21.428571428571427, 28.571428571428569, 7.1428571428571423, 
        7.1428571428571423, 7.1428571428571423, 7.1428571428571423, 7.1428571428571423, 
        14.285714285714285, 7.1428571428571423, 14.285714285714285, 7.1428571428571423, 
        7.1428571428571423, 7.1428571428571423, 14.285714285714285, 7.1428571428571423, 
        14.285714285714285, 7.1428571428571423, 7.1428571428571423, 7.1428571428571423, 
        14.285714285714285, 7.1428571428571423, 14.285714285714285]

    def test_aroon_up_period_6(self):
        period = 6
        aroon_up = aroon.aroon_up(self.data, period)
        np.testing.assert_array_equal(aroon_up, self.aroon_up_period_6_expected)

    def test_aroon_down_period_14(self):
        period = 14
        aroon_down = aroon.aroon_down(self.data, period)
        np.testing.assert_array_equal(aroon_down, self.aroon_down_period_14_expected)

    def test_aroon_up_invalid_period(self):
        period = 128
        with self.assertRaises(Exception) as cm:
            aroon.aroon_up(self.data, period)
        expected = "Error: data_len < period"
        self.assertEqual(str(cm.exception), expected)

    def test_aroon_down_invalid_period(self):
        period = 128
        with self.assertRaises(Exception) as cm:
            aroon.aroon_down(self.data, period)
        expected = "Error: data_len < period"
        self.assertEqual(str(cm.exception), expected)
