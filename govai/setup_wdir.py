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
                  'original_data',
                  'feature',
                  'model',
                  'nb']
    binary_classifcation = ['submission',
                            'original_data',
                            'feature',
                            'model'
                            'nb']

ALLOWED_CONF_TYPES = [ConfType.regression,]

conf_type = sys.argv[1]
if conf_type not in ALLOWED_CONF_TYPES:
    raise KeyError(f'{conf_type} not allowed')

wdir = Path(sys.argv[2])
if not wdir.exists():
    wdir.mkdir(exist_ok=True, parents=True)

configs_path = pr.resource_filename("govai.store", f"configs/{conf_type}")
assert configs_path is not None, f"configs/{conf_type} missing in govai/store/"

wdir_conf_path = wdir/'configs'
shutil.copytree(configs_path, str(wdir_conf_path))

wdir_conf_paths = wdir_conf_path.rglob('**/*.yaml')
wdir_conf_paths = [*wdir_conf_paths]
for wdir_conf_path in wdir_conf_paths:
    conf = OmegaConf.load(str(wdir_conf_path))
    conf.wdir = str(wdir.absolute())
    with open(wdir_conf_path, 'w') as fp:
        s = OmegaConf.to_yaml(conf)
        fp.write(s)

if conf_type == ConfType.regression:
    for structure in WorkingDirStructure.regression:
        subir = wdir / structure
        subir.mkdir(exist_ok=True, parents=True)