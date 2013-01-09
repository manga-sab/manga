import stem.torrc
import unittest
import os

from StringIO import StringIO

VALID_TORRC = """Softsport 9020
#Flasaport 7839\n\n
redsport 1203\n\n\n
dffport 1302\n\n\n\n\n"""

INVALID_TORRC = """Congosport"""
class TestTorrcparser(unittest.TestCase):
  def test_torrc_parser(self):
     """
     Checks the proper writing and accurate retrieval of the parser
     """
     parsed_torrc=stem.torrc.Torrc(StringIO(VALID_TORRC))
     torrc_ori={
         "Softsport": "9020",
         "redsport": "1203",
         "dffport": "1302",
               }
     for key in parsed_torrc :
       #To verify the parsed data matches the original data
       self.assertEqual(parsed_torrc[key],torrc_ori[key])
  
  def test_invalid_input(self):
    """
    Checks invalid inputs in the file to be parsed
    """
    test=stem.torrc.Torrc()
    self.assertRaises(stem.torrc.InvalidInput, test._parse, StringIO(INVALID_TORRC))
    
    
