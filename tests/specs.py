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
        config = ConfigEnv.ConfigEnv()
        config.addFile(self.getCurrentPath()+"data/config.json")
        self.assertEqual( config._config['DEFAULT']['SECRET_KEY'], "secret-key-of-myapp" )

    def test_addFileIni(self):
        config = ConfigEnv.ConfigEnv()
        config.addFile(self.getCurrentPath()+"data/config.ini")
        self.assertEqual( config._config['TEST']['TEST_TMP_DIR'], "tests" )

    def test_overideFile(self):
        config = ConfigEnv.ConfigEnv()
        config.addFile(self.getCurrentPath()+"data/config.json")
        self.assertEqual( config._config['CI']['SERVICE'], "travis-ci" )
        config.addFile(self.getCurrentPath()+"data/config.ini")
        self.assertEqual( config._config['CI']['SERVICE'], "plus-travis-ci" )

    def test__recursiveRoute(self):
        config = ConfigEnv.ConfigEnv()
        fakeContext = {
            "a" : {
                "b_c" : "yep yap"
            },
            "d" : "yap yep"
        }
        yapyep = config._recursiveRoute(fakeContext,["d"])
        yepyap = config._recursiveRoute(fakeContext,["a","b","c"])

        self.assertEqual( yepyap , "yep yap" )
        self.assertEqual( yapyep , "yap yep" )
