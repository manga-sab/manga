import tempfile

"""
Torrc information.

::

  >>> import stem.torrc
  >>> torrc = stem.torrc.Torrc()
  >>> torrc['controlport'] = 9051
  >>> write_torrc(torrc)
  '/var/folders/8r/0cd26s_d7dqgqkf5sbsgf4vh0000gn/T/torrc-D_I79n'

  >>> torrc = parse_torrc('/var/folders/8r/0cd26s_d7dqgqkf5sbsgf4vh0000gn/T/torrc-D_I79n')
  >>> torrc
  {'controlport': '9051'}
  >>> print torrc
  controlport 9051

**Module Overview:**

::

  parse_torrc - parses a torrc file and returns a Torrc instance
  write_torrc - writes the Torrc into a file

  Torrc - Torrc information
    +- __str__ - string representation
"""

def parse_torrc(torrc_path=None):
  """
  Returns a Torrc instance with all the key value mappings in a torrc
  
  :param str msg: path to torrc file
  
  :returns: **Torcc** key value mappings of torrc
  """
  
  torrc = Torrc()
  
  if not torrc_path:
    raise ValueError("Require Torrc")
  
  with open(torrc_path) as torrc_fh:
    for line in torrc_fh.readlines():
      line = line.strip()
      if line.startswith('#'):
        continue
      else:
        key, val = line.split(' ')
        torrc[key] = val
  
  return torrc

def write_torrc(config, torrc_path=None):
  """
  Creates a torrc file.

  :param Torrc config: config options for torrc
  :param str torrc_path: path to make new torrc file
  
  :returns: **str** path to the new torrc
  """
  
  if not torrc_path:
      torrc_path = tempfile.mkstemp(prefix = "torrc-", text = True)[1]
  
  with open(torrc_path, "w") as torrc_file:
    for key, value in config.items():
      torrc_file.write("%s %s\n" % (key, value))
  
  return torrc_path

class Torrc(dict):
  def __init__(self):
    super(Torrc, self).__init__()
  
  def __str__(self):
    return '\n'.join(["%s %s" % (key, value) for key, value in self.items()])
  

