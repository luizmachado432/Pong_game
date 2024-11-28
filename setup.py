import sys
from cx_Freeze import setup, Executable

#essa parte do codigo é para criar um .exe dele
include_files = ['sons_imagens']


build_exe_options = {
    "packages": ["pygame", "os"],
    "include_files": include_files,
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Pong_Luiz_Felipe",
    version="1.0",
    description="Meu jogo Pong usando pygame",
    options={"build_exe": build_exe_options},
    executables=[Executable("Pong_Luiz_Felipe.py", base=base)],
)