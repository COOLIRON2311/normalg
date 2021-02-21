from unittest import TestCase
from .MarkovAlgorithm import MarkovAlgorithm


class TestMarkovAlgorithm(TestCase):
    def test_prepend(self):
        alg = MarkovAlgorithm(
            '''
            E .1
            '''
        )
        self.assertEqual(alg.apply('E').str, '1')
        self.assertEqual(alg.apply('1').str, '11')
        self.assertEqual(alg.apply('11').str, '111')
    def test_sort(self):
        alg = MarkovAlgorithm(
            '''
            ba ab
            ca ac
            cb bc
            ''')
        self.assertEqual(alg.apply('bca').str, 'abc')
        self.assertEqual(alg.apply('bbaacc').str, 'aabbcc')
        self.assertEqual(alg.apply('bcaacbca').str, 'aaabbccc')

    def test_div(self):
        alg = MarkovAlgorithm(
            '''
            ba 1b
            b .E
            11 a
            1 E
            a ba
            ''')
        self.assertEqual(alg.apply('111').str, '1')
        self.assertEqual(alg.apply('1111').str, '11')
        self.assertEqual(alg.apply('E').str, '')

    def test_divmod(self):
        alg = MarkovAlgorithm(
            '''
            ba 1b
            b .#
            b1 .#1
            11 a
            a ba
            1 .#1
            E .#
            '''
        )
        self.assertEqual(alg.apply('111').str, '1#1')
        self.assertEqual(alg.apply('1111').str, '11#')
        self.assertEqual(alg.apply('E').str, '#')

    def test_mul(self):
        alg = MarkovAlgorithm(
            '''
            ba 11b
            b .E
            1 a
            a ba
            '''
        )
        self.assertEqual(alg.apply('1').str, '11')
        self.assertEqual(alg.apply('11').str, '1111')
        self.assertEqual(alg.apply('E').str, '')
