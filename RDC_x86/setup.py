from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')
includes = ['encodings','encodings.utf_8', 'sip']
options = {
    'bundle_files': 1,
    'compressed': 1,
    'optimize': 2,
    'includes': includes,
    'dll_excludes': ["MSVCP90.dll"]
}
images = [("images", ["23Bde.png", "23Bde.ico"])]

setup(
    windows = [{
        "script": "RDC_x86.py",
        "icon_resources": [(1, "23Bde.ico")]
        }
    ],
    options = {"py2exe": options},
    data_files = images,
    zipfile = None,
)
# python setup.py py2exe --includes sip
# pyinstaller --onefile --noconsole --icon="23Bde.ico" "RDC_x86.py"
