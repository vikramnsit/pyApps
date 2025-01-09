import yaml
from projects import ROOT_DIR
import os


class Config:
    @staticmethod
    def load_config(file_name='config.yaml'):
        with open(os.path.join(ROOT_DIR, file_name), 'rt') as o:
            content = yaml.safe_load(o)
        return content



