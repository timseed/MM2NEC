"""
MMANA-GAL to NEC conversion.

MMANA-GAL is nice to use for drawing - but I want to use some NEC processing

"""
import logging
import re
from collections import namedtuple

import daiquiri

mm_line = namedtuple(
    "mm_line", ["sx", "sy", "sz", "ex", "ey", "ez", "thickness", "seg"]
)
nec_line = namedtuple(
    "nec_line",
    [
        "wire",
        "line_no",
        "seg",
        "sx",
        "sy",
        "sz",
        "ex",
        "ey",
        "ez",
        "thickness",
    ],
)

class mm2nec:
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)
        self.LOGGER = daiquiri.getLogger(__name__)
        self.LOGGER.info(f"{__name__} Starting")
        self.section_head = re.compile(r"[\*]{2}([\w]+)[\*]{2}")
        self.mm_str = ""
        self._parts = {}



    @property
    def parts(self):
        return self._parts

    def _section(self) -> dict:
        """
        Chop the MMANA definition into parts....
        :return:
        """
        cur_part = None
        for n in self.mm_str.split("\n"):
            header = self.section_head.findall(n)
            if header:
                cur_part = header[0]
                self.LOGGER.debug(f"Line is {cur_part}")
                self._parts[cur_part] = []
            else:
                if cur_part:
                    self._parts[cur_part].append(n)
        return self._parts

    def convert(self, mm_str: str, segments: int = 21) -> str:
        """
        Convert the input String into a NEC Format
        :param mm_str:
        :return:
        """
        self.mm_str = mm_str
        self._section()
        return self.convert_wire("\n".join(self._parts['Wires']))

    def nec_tuple_to_str(self, nt) -> str:
        if isinstance(nt,nec_line):
            return "{}\t{:3d}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(nt.wire,
            nt.line_no,
            nt.seg,
            nt.sx,
            nt.sy,
            nt.sz,
            nt.ex,
            nt.ey,
            nt.ez,
            nt.thickness)
        else:
            self.LOGGER.error(f"Not type nec_line")
            return None

    def convert_wire(self, mm_str: str, segments: int = 21) -> str:
        """
        Convert the Wire

        A Wire Definition looks like this

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

        This format seems to be
        <Header>
        <Number of Wires>
        <Start X>,<Start Y>,<Start Z>,<End X>,<End Y>,<End Z>,<Thickness>,<Segments ?>

        :param mm_str:
        :return:
        """
        converted = ""
        cnt = 1
        # Miss the count
        for line in mm_str.split("\n")[1:]:
            l = mm_line(*[float(field.strip()) for field in line.split(",")])
            if l.seg == -1.0:
                nl = nec_line('Wire',cnt, segments, l.sx, l.sy, l.sz, l.ex, l.ey, l.ez, l.thickness)
            else:
                nl = nec_line('Wire', cnt, l.seg, l.sx, l.sy, l.sz, l.ex, l.ey, l.ez, l.thickness)
            self.LOGGER.debug(f"l is {l}")
            self.LOGGER.debug(f"nl is {nl}")
            cnt+=1
            converted += self.nec_tuple_to_str(nl)+"\n"
        return converted
