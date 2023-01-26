import os
import sys

from pipecapacity.common.ymlInput import ymlInput
from pipecapacity.common.update_deep import AttributeDict
from pipecapacity.common.ApplicationManager import ConfigureApplicationInputs
from pipecapacity.vertical_riser import vertical_riser

ymlfile = 'src/pipecapacity/tests/test_data/pipecapacity.yml'
sys.argv.append(ymlfile)
print(os.path.isfile(ymlfile))
cfg = ymlInput(ymlfile, updateYml=None)
cfg = AttributeDict(cfg)

basename = 'pipecapacity'
application_manager = ConfigureApplicationInputs(basename)
application_manager.configure(run_dict=None)

cfg_base = vertical_riser(application_manager.cfg)
