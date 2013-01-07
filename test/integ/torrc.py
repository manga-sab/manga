import stem.torrc
import unittest
import os

VALID_TORRC = """Softsport 9020
#Flasaport 7839\n\n
redsport 1203\n\n\n
dffport 1302\n\n\n\n\n"""


class TestTorrcparser(unittest.TestCase):
  def test_torrc_parser(self):
     torrc_file=open("textfile",'w')
     torrc_file.write(VALID_TORRC)
     torrc_file.close()
     torrc_file=open("textfile")
     parsed_torrc=stem.torrc.parse_torrc("textfile")
     torrc_file.close()
     #os.chdir("/home/sabyashiv/stem/test/integ")
     os.remove("textfile")
     torrc_ori={
         "Softsport": "9020",
         "redsport": "1203",
         "dffport": "1302",
               }
     for key in parsed_torrc :
       self.assertEqual(parsed_torrc[key],torrc_ori[key])


