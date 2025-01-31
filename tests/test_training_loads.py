import os
from unittest import TestCase

from sport_activities_features import (
    BanisterTRIMP,
    EdwardsTRIMP,
    LuciaTRIMP,
    TCXFile
)


class BanisterTRIMPTestCase(TestCase):
    """
    Banister TRIMP test.
    """
    def setUp(self):
        """
        Setting up the test.
        """
        self.__banister = BanisterTRIMP(33.44, 165.22)

    def test_init_banister_trimp_works_fine(self):
        """
        Testing class arguments.
        """
        self.assertEqual(33.44, self.__banister.duration)
        self.assertEqual(165.22, self.__banister.average_heart_rate)

    def test_calculate_trimp_works_fine(self):
        """
        Testing Banister TRIMP.
        """
        val = self.__banister.calculate_TRIMP()
        self.assertEqual(5524.9568, val)


class EdwardsTRIMPTestCase(TestCase):
    """
    Edwards TRIMP test.
    """
    def setUp(self):
        """
        Setting up the test.
        """
        filename = os.path.join(os.path.dirname(__file__), 'data', '15.tcx')
        tcx_file = TCXFile()
        activity = tcx_file.read_one_file(filename)
        timestamps = activity['timestamps']
        heart_rates = activity['heartrates']
        self.__edwards = EdwardsTRIMP(heart_rates, timestamps, 200)

    def test_init_banister_trimp_works_fine(self):
        """
        Testing class arguments.
        """
        self.assertEqual(7799, len(self.__edwards.heart_rates))
        self.assertEqual(7799, len(self.__edwards.timestamps))
        self.assertEqual(200, self.__edwards.max_heart_rate)

    def test_calculate_trimp_works_fine(self):
        """
        Testing Edwards TRIMP.
        """
        val = self.__edwards.calculate_TRIMP()
        self.assertEqual(41458, val)


class LuciaTRIMPTestCase(TestCase):
    """
    Lucia's TRIMP test.
    """
    def setUp(self):
        """
        Setting up the test.
        """
        filename = os.path.join(os.path.dirname(__file__), 'data', '15.tcx')
        tcx_file = TCXFile()
        activity = tcx_file.read_one_file(filename)
        timestamps = activity['timestamps']
        heart_rates = activity['heartrates']
        self.__lucia = LuciaTRIMP(heart_rates, timestamps, VT1=160, VT2=180)

    def test_init_banister_trimp_works_fine(self):
        """
        Testing class arguments.
        """
        self.assertEqual(7799, len(self.__lucia.heart_rates))
        self.assertEqual(7799, len(self.__lucia.timestamps))
        self.assertEqual(160, self.__lucia.VT1)
        self.assertEqual(180, self.__lucia.VT2)

    def test_calculate_trimp_works_fine(self):
        """
        Testing Lucia's TRIMP.
        """
        val = self.__lucia.calculate_TRIMP()
        self.assertEqual(19251, val)
