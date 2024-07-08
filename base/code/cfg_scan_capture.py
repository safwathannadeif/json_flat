# start run
import configparser
from pathlib import Path

################################
p_path = Path(__file__).parent.parent
relative = "cfg/INI/scan_capture.ini"
cfg_file = (p_path / relative).resolve()
config = configparser.ConfigParser()
config.read(cfg_file)
