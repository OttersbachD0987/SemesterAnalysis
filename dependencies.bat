@echo off
set arg1=%1
echo Installing dependencies via pip...
setlocal
set fail=1
(pip install -r "requirements.txt" > %arg1% 2>&1 && set fail=0)

if %fail% equ 0 (
    echo All dependencies have been installed.
) else (
    echo There was an error during the installation process, goto %arg1% for more details.
)
endlocal