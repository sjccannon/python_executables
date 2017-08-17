import sys, os
import cx_Freeze

os.environ['TCL_LIBRARY'] = "C:\\Program Files\\Python36-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Program Files\\Python36-32\\tcl\\tcl8.6"

base = None

if sys.platform =='win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("tkinter_test.py", base = base)]

cx_Freeze.setup(
    name = "SJC_ENST_converter",
    options = {"build_exe": {"packages":["tkinter"], "include_files": ["tcl86t.dll", "tk86t.dll"]}},
    version = "1.0",
    description = "converts enseml transcript to NM transcript",
    executables = executables
    )
