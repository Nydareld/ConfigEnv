import json
import configparser

class Config():
    """docstring for ConfigJsonEnv."""

    def __init__(self, file = None):
        self._config = dict()
        self._configCache = dict()
        if file is not None:
            self.addFile(file)

    def addFile(self,file):
        if file.endswith('.json') :
            with open(file, 'r') as f:
                fileContent = json.load(f)
        elif file.endswith('.ini') :
            fileContent = configparser.ConfigParser()
            fileContent.read(file)
        else :
            raise Exception('file format not suported')
        self._config = {**self._config, **fileContent}

    def get(self,path):
        if path in self._configCache:
            return self._configCache[path]
        else :
            return self._findConfig(path)

    def _findConfig(self,path):
        splited = path.split("_")
        self._recursiveRoute(self._configCache,splited)

    def _recursiveRoute(self,context,left):
        search = ""
        for index in range(len(left)):
            search += left.pop(0) if len(search) == 0 else "_"+left.pop(0)
            print(search)
            if search in context and isinstance(context[search],dict):
                print("in context Dict")
                return self._recursiveRoute(context[search],left)
            elif search in context:
                print("in context data")
                return context[search]
