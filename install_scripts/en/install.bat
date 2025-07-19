@echo off
setlocal

:: Target dir
set "APPDIR=%USERPROFILE%\.pyapps\cryptr"

:: Set ENTRY to launcher.py
set "ENTRY=launcher.py"

:: Batch-Alias for command
set "WRAPPER=%APPDIR%\cryptr.bat"

:: Create dir
if not exist "%APPDIR%" (
    mkdir "%APPDIR%"
)

:: Copy files to dir
xcopy /E /Y * "%APPDIR%"

:: Create cryptr.bat (CLI-Wrapper)
echo @echo off > "%WRAPPER%"
echo python "%APPDIR%\%ENTRY%" %%* >> "%WRAPPER%"

:: Add dir to PATH-Variable
set KEY="HKCU\Environment"
for /f "tokens=3*" %%a in ('reg query %KEY% /v PATH 2^>nul') do set OLD_PATH=%%a %%b

echo %OLD_PATH% | find /I "%APPDIR%" >nul
if errorlevel 1 (
    setx PATH "%OLD_PATH%;%APPDIR%"
    echo 🔧 %APPDIR% was added to the PATH-Variable.
) else (
    echo ℹ️ %APPDIR% is already in the PATH-Variable.
)

echo ✅ Installation completed
echo 👉 Now you can just use ^"cryptr^" in the terminal to start Cryptr.

endlocal
pause
