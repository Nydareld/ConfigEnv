import os, sys
modulePath = os.path.abspath("../ConfigEnv")
if modulePath not in sys.path:
    sys.path.insert(0, modulePath)

import unittest
from ConfigEnv import Config

# print(ConfigEnv.__dict__.keys() )
 # print(ConfigEnv)

class TestConfig(unittest.TestCase):

    def getCurrentPath(self):
        return os.path.dirname(os.path.abspath(__file__))+"/"

    def test_addFileJson(self):
        config = Config()
        config.addFile(self.getCurrentPath()+"data/config.json")
        self.assertEqual( config._config['DEFAULT']['SECRET_KEY'], "secret-key-of-myapp" )

    def test_addFileIni(self):
        config = Config()
        config.addFile(self.getCurrentPath()+"data/config.ini")
        self.assertEqual( config._config['TEST']['TEST_TMP_DIR'], "tests" )

    def test_overideFile(self):
        config = Config()
        config.addFile(self.getCurrentPath()+"data/config.json")
        self.assertEqual( config._config['CI']['SERVICE'], "travis-ci" )
        config.addFile(self.getCurrentPath()+"data/config.ini")
        self.assertEqual( config._config['CI']['SERVICE'], "plus-travis-ci" )

    def test__recursiveRoute(self):
        config = Config()
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

    def test__findConfig(self):
        config = Config(self.getCurrentPath()+"data/config.json")
        self.assertEqual( config._findConfig('DEFAULT_SECRET_KEY'), "secret-key-of-myapp" )

    def test__setCache(self):
        config = Config(self.getCurrentPath()+"data/config.json")
        config._setCache("toto","tata")
        self.assertEqual( config._configCache['toto'], "tata" )

    def test__findConfig_andCache(self):
        config = Config(self.getCurrentPath()+"data/config.json")
        config._findConfig('DEFAULT_SECRET_KEY')
        self.assertEqual( config._configCache['DEFAULT_SECRET_KEY'], "secret-key-of-myapp" )
