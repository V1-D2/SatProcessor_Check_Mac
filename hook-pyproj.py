import os
import sys
if hasattr(sys, '_MEIPASS'):
    os.environ['PROJ_LIB'] = os.path.join(sys._MEIPASS, 'pyproj', 'proj_dir', 'share', 'proj')