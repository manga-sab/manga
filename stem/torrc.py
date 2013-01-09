from __future__ import with_statement
import tempfile

"""
Torrc information.

::

  >>> import stem.torrc
  >>> torrc = stem.torrc.Torrc()
  >>> torrc['controlport'] = 9051
  >>> torrc.write('/var/folders/8r/0cd26s_d7dqgqkf5sbsgf4vh0000gn/T/torrc-D_I79n')
  
  >>> torrc._parse('/var/folders/8r/0cd26s_d7dqgqkf5sbsgf4vh0000gn/T/torrc-D_I79n')
  >>> torrc
  {'controlport': '9051'}
  >>> print torrc
  controlport 9051

**Module Overview:**

::

  Torrc._parse - parses a torrc file and returns a Torrc instance
  Torrc.write - writes the Torrc into a file
  
  Torrc - Torrc information
    +- __str__ - string representation
"""
class InvalidInput(Exception): pass

class Torrc(dict):
  def __init__(self, torrc_file=None):
    super(Torrc, self).__init__()
    if torrc_file:
      self._parse(torrc_file)
  
  def __str__(self):
    return '\n'.join(["%s %s" % (key, value) for key, value in self.items()])
  
  def _parse(self, torrc_file):
    """
    Returns a Torrc instance with all the key value mappings in a torrc
    
    :param file :  torrc file
    
    :returns: **Torcc** key value mappings of torrc
    """
    
    for line in torrc_file:
      line = line.strip()
      if not (line.startswith('#') or line==""):
        try:
          key, val = line.split(None, 1)
        except:
          raise(InvalidInput())
        self[key] = val
  
  def write(self, path):
    """
    Creates a torrc file.
    
    :param Torrc config: config options for torrc
    :param str torrc_path: path to make new torrc file
    
    :returns: **str** path to the new torrc
    """
    
    with open(path, "w") as torrc_file:
      torrc_file.write(str(self))


