@echo off

echo Checking the Virtual Environment...
if exist ".\venv" (
    echo The Virtual Environment already exists.
) else (
    echo The Virtual Environment does not exist, creating now.
    py -m venv venv
    echo The Virtual Environment has been created.
)

echo:

echo Activating the Virtual Environment...
call venv/Scripts/activate.bat
echo The Virtual Environment has been activated.
echo:
call dependencies.bat install_log.balrog
echo:
echo Activation has been completed.