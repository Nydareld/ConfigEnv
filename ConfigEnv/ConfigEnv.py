import json
import configparser

class ConfigEnv():
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

    def _recursiveRoute(self,context,left):
        search = ""
        for index in range(len(left)):
            search += left.pop(0) if len(search) == 0 else "_"+left.pop(0)
            if search in context and isinstance(context[search],dict):
                return self._recursiveRoute(context[search],left)
            elif search in context:
                return context[search]
