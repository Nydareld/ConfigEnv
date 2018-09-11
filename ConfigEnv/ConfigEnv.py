import json
import configparser

class ConfigEnv():
    """docstring for ConfigJsonEnv."""

    def __init__(self, file = None):
        self._config = dict()
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
