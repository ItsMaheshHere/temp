@echo off
REM Force kill Tuxler VPN process
C:\Windows\System32\taskkill.exe /F /IM tuxlerVPN.exe

REM Optional: wait a little before exit
timeout /t 2 >nul
exit /b 0
