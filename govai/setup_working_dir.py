import sys
import shutil

from pathlib import Path
import pkg_resources as pr


wdir = Path(sys.argv[1])
if not wdir.exists():
    wdir.mkdir(exist_ok=True, parents=True)

configs_path = pr.resource_filename("govai.store", "configs")
shutil.copytree(configs_path, str(wdir/'configs'))

data_dir = wdir / 'original_data'
sub_dir = wdir / 'submission'
ft_dir = wdir / 'feature'
models_dir = wdir / 'model'

data_dir.mkdir(exist_ok=True)
sub_dir.mkdir(exist_ok=True)
ft_dir.mkdir(exist_ok=True)
models_dir.mkdir(exist_ok=True)