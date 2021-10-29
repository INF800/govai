import sys
import shutil

from pathlib import Path
import pkg_resources as pr


wdir = Path(sys.argv[1])
assert wdir.exists(), "working dir doesnot exist"

configs_path = pr.resource_filename("govai.store", "configs")
shutil.copytree(configs_path, str(wdir/'configs'))