import os, sys
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)

import unittest
import ConfigEnv

class TestConfigEnv(unittest.TestCase):

    def getCurrentPath(self):
        return os.path.dirname(os.path.abspath(__file__))+"/"

    def test_addFileJson(self):
        config = ConfigEnv.ConfigEnv(self.getCurrentPath()+"data/config.json")
        self.assertEqual( config._config['DEFAULT']['SECRET_KEY'], "secret-key-of-myapp" )

    def test_addFileIni(self):
        config = ConfigEnv.ConfigEnv(self.getCurrentPath()+"data/config.ini")
        self.assertEqual( config._config['DEFAULT']['SECRET_KEY'], "secret-key-of-myapp" )
