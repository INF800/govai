import sys
import shutil

from pathlib import Path
import pkg_resources as pr


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
shutil.copytree(configs_path, str(wdir/'configs'))

if conf_type == ConfType.regression:
    for structure in WorkingDirStructure.regression:
        subir = wdir / structure
        subir.mkdir(exist_ok=True, parents=True)