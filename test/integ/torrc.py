import stem.torrc
import unittest
import os

VALID_TORRC = """Softsport 9020
#Flasaport 7839\n\n
redsport 1203\n\n\n
dffport 1302\n\n\n\n\n"""

INVALID_TORRC = """Congosport"""
class TestTorrcparser(unittest.TestCase):
  def test_torrc_parser(self):
     torrc_file=open("textfile",'w')
     torrc_file.write(VALID_TORRC)
     torrc_file.close()
     parsed_torrc=stem.torrc.parse_torrc("textfile")
     torrc_file.close()
     os.remove("textfile")
     torrc_ori={
         "Softsport": "9020",
         "redsport": "1203",
         "dffport": "1302",
               }
     for key in parsed_torrc :
       self.assertEqual(parsed_torrc[key],torrc_ori[key])

  def test_invalid_input(self):
    torrc_file=open("textfile",'w')
    torrc_file.write(INVALID_TORRC)
    torrc_file.close()
    torrc_file=open("textfile")
    self.assertRaises(stem.torrc.INVALID_INPUT, stem.torrc.parse_torrc, "textfile")
    torrc_file.close()
    os.remove("textfile")
    
    
