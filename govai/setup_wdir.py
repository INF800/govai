# This module has only two purposes
# 1. Copy configs into working directory (based on task type)
# 2. Generate folder structure for each task type
# 
# Simply add new task inside `ConfType` and using the same
# name create list of folder structures that must be created
# inside working directory in `WorkingDirStructure`

import sys
import shutil
from dataclasses import dataclass

from pathlib import Path
import pkg_resources as pr
from omegaconf import OmegaConf

class ConfType:
    regression = 'regression'
    binary_classification = 'binary_classifcation'
    instance_segmentation = 'instance_segmentation'

class WorkingDirStructure:
    regression = ['submission',
                  'original_data/kfold',
                  'feature',
                  'model']
    binary_classifcation = ['submission',
                            'original_data/kfold',
                            'feature',
                            'model']

ALLOWED_CONF_TYPES = [ConfType.regression,]

conf_type = sys.argv[1]
if conf_type not in ALLOWED_CONF_TYPES:
    raise KeyError(f'{conf_type} not allowed')

wdir = Path(sys.argv[2])
if not wdir.exists():
    wdir.mkdir(exist_ok=True, parents=True)

configs_path = pr.resource_filename("govai.store", f"configs/{conf_type}")
assert configs_path is not None, f"configs/{conf_type} missing in govai/store/"

wdir_conf_path = str(wdir/'configs')
shutil.copytree(configs_path, wdir_conf_path)
conf = OmegaConf.load(wdir_conf_path+'/default.yaml')
conf.wdir = str(wdir.absolute())
with open(wdir_conf_path+'/default.yaml', 'w') as fp:
    s = OmegaConf.to_yaml(conf)
    fp.write(s)

if conf_type == ConfType.regression:
    for structure in WorkingDirStructure.regression:
        subir = wdir / structure
        subir.mkdir(exist_ok=True, parents=True)