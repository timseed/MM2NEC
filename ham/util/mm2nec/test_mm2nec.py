from unittest import TestCase
from ham.util.mm2nec import mm2nec

class Testmm2nec(TestCase):

    ant="""*
14.15
***Wires***
11
0.0,	0.0,	0.0,	0.0,	-4.06586,	4.06586,	8.000e-04,	-1
0.0,	4.06586,	4.06586,	0.0,	0.0,	0.0,	8.000e-04,	-1
0.0,	4.06586,	4.06586,	0.0,	-0.0,	8.13173,	8.000e-04,	-1
0.0,	-0.0,	8.13173,	0.0,	-4.06586,	4.06586,	8.000e-04,	-1
0.0,	0.0,	0.0,	0.0,	0.0,	0.0,	8.000e-04,	-1
2.65,	0.1,	0.0,	2.65,	0.1,	8.1317,	8.000e-04,	-1
2.65,	-0.1,	0.0,	2.65,	-0.1,	8.1317,	8.000e-04,	-1
2.65,	0.1,	8.1317,	2.65,	4.04586,	4.06586,	8.000e-04,	-1
2.65,	-0.1,	8.1317,	2.65,	-4.04586,	4.06586,	8.000e-04,	-1
2.65,	4.04586,	4.06586,	2.65,	0.1,	0.0,	8.000e-04,	-1
2.65,	-4.04586,	4.06586,	2.65,	-0.1,	0.0,	8.000e-04,	-1
***Source***
2,	0
w7c,	0.0,	1.0
w6c,	0.0,	1.0
***Load***
0,	0
***Segmentation***
800,	80,	2.0,	2
***G/H/M/R/AzEl/X***
2,	10.0,	0,	50.0,	120,	60,	0.0
"""

    nec_format = """Wire	1	-1.0	0.0	0.0	0.0	0.0	-4.06586	4.06586	0.0008
Wire	2	-1.0	0.0	4.06586	4.06586	0.0	0.0	0.0	0.0008
Wire	3	-1.0	0.0	4.06586	4.06586	0.0	-0.0	8.13173	0.0008
Wire	4	-1.0	0.0	-0.0	8.13173	0.0	-4.06586	4.06586	0.0008
Wire	5	-1.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0008
Wire	6	-1.0	2.65	0.1	0.0	2.65	0.1	8.1317	0.0008
Wire	7	-1.0	2.65	-0.1	0.0	2.65	-0.1	8.1317	0.0008
Wire	8	-1.0	2.65	0.1	8.1317	2.65	4.04586	4.06586	0.0008
Wire	9	-1.0	2.65	-0.1	8.1317	2.65	-4.04586	4.06586	0.0008
Wire	10	-1.0	2.65	4.04586	4.06586	2.65	0.1	0.0	0.0008
Wire	11	-1.0	2.65	-4.04586	4.06586	2.65	-0.1	0.0	0.0008
"""

    test_parts={'Load': ['0,\t0'],
 'Segmentation': ['800,\t80,\t2.0,\t2',
                  '***G/H/M/R/AzEl/X***',
                  '2,\t10.0,\t0,\t50.0,\t120,\t60,\t0.0',
                  ''],
 'Source': ['2,\t0', 'w7c,\t0.0,\t1.0', 'w6c,\t0.0,\t1.0'],
 'Wires': ['11',
           '0.0,\t0.0,\t0.0,\t0.0,\t-4.06586,\t4.06586,\t8.000e-04,\t-1',
           '0.0,\t4.06586,\t4.06586,\t0.0,\t0.0,\t0.0,\t8.000e-04,\t-1',
           '0.0,\t4.06586,\t4.06586,\t0.0,\t-0.0,\t8.13173,\t8.000e-04,\t-1',
           '0.0,\t-0.0,\t8.13173,\t0.0,\t-4.06586,\t4.06586,\t8.000e-04,\t-1',
           '0.0,\t0.0,\t0.0,\t0.0,\t0.0,\t0.0,\t8.000e-04,\t-1',
           '2.65,\t0.1,\t0.0,\t2.65,\t0.1,\t8.1317,\t8.000e-04,\t-1',
           '2.65,\t-0.1,\t0.0,\t2.65,\t-0.1,\t8.1317,\t8.000e-04,\t-1',
           '2.65,\t0.1,\t8.1317,\t2.65,\t4.04586,\t4.06586,\t8.000e-04,\t-1',
           '2.65,\t-0.1,\t8.1317,\t2.65,\t-4.04586,\t4.06586,\t8.000e-04,\t-1',
           '2.65,\t4.04586,\t4.06586,\t2.65,\t0.1,\t0.0,\t8.000e-04,\t-1',
           '2.65,\t-4.04586,\t4.06586,\t2.65,\t-0.1,\t0.0,\t8.000e-04,\t-1']}

    def setUp(self):
        self.calc = mm2nec.mm2nec()

    def test_init(self):
        self.assertIsInstance(self.calc, mm2nec.mm2nec)

    def test_convert(self):
        self.calc.convert(self.ant)
        self.assertEqual(self.calc.parts,self.test_parts)


    def test_convert_wire(self):
        self.assertEqual(self.calc.convert_wire('\n'.join(self.test_parts['Wires'])),self.nec_format)