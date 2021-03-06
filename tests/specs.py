import os, sys
modulePath = os.path.abspath("../ConfigEnv")
if modulePath not in sys.path:
    sys.path.insert(0, modulePath)

import unittest
from ConfigEnv import Config
from ConfigEnv import FileFormatException

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
            "A" : {
                "B_C" : "yep yap"
            },
            "D" : "yap yep"
        }
        yapyep = config._recursiveRoute(fakeContext,["D"])
        yepyap = config._recursiveRoute(fakeContext,["A","B","C"])

        self.assertEqual( yapyep , "yap yep" )
        self.assertEqual( yepyap , "yep yap" )

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

    def test__get(self):
        config = Config(self.getCurrentPath()+"data/config.json")
        self.assertEqual( config.get('DEFAULT_SECRET_KEY'), "secret-key-of-myapp" )
        self.assertEqual( config._configCache['DEFAULT_SECRET_KEY'], "secret-key-of-myapp" )

    def test__badFile(self):
        with self.assertRaises(FileFormatException):
            Config(self.getCurrentPath()+"data/config.toto")

    def test__getCache(self):
        config = Config(self.getCurrentPath()+"data/config.json")
        self.assertEqual( 'DEFAULT_SECRET_KEY' in config._configCache, False )
        self.assertEqual( config.get('DEFAULT_SECRET_KEY'), "secret-key-of-myapp" )
        self.assertEqual( 'DEFAULT_SECRET_KEY' in config._configCache, True )
        self.assertEqual( config.get('DEFAULT_SECRET_KEY'), "secret-key-of-myapp" )

    def test__getEnvOveride(self):
        os.environ['DEFAULT_SECRET_KEY'] = "superSecret"
        config = Config(self.getCurrentPath()+"data/config.json")
        self.assertEqual( config.get('DEFAULT_SECRET_KEY'), "superSecret" )

    def test_clearCache(self):
        config = Config(self.getCurrentPath()+"data/config.json")
        self.assertEqual( config.get('CI_SERVICE'), "travis-ci" )
        config.addFile(self.getCurrentPath()+"data/config.ini")
        self.assertEqual( config.get('CI_SERVICE'), "travis-ci" )
        config.clearCache()
        print(config.get('CI_SERVICE'))
        self.assertEqual( config.get('CI_SERVICE'), "plus-travis-ci" )
