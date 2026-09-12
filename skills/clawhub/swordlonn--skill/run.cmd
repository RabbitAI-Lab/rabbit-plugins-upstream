@echo off
REM ============================================================
REM WatchItAI Skill - Cross-platform entry point (no Node.js needed)
REM
REM Auto-detects architecture and launches the correct Go binary.
REM
REM Usage:
REM   run.cmd share              REM Start screen sharing
REM   run.cmd link               REM Create session & return viewer link
REM   run.cmd start              REM Start bridge server only
REM   run.cmd status             REM Check bridge server status
REM   run.cmd permissions        REM Check system permissions
REM   run.cmd preflight          REM Run permission pre-check
REM   run.cmd authorize <CODE>   REM Bind skill to account (one-time code)
REM   run.cmd authorize --request REM Auto Device Flow (recommended)
REM   run.cmd info               REM Show system info
REM   run.cmd version            REM Show version
REM   run.cmd help               REM Show help
REM ============================================================

setlocal

set "SCRIPT_DIR=%~dp0"

REM Detect architecture (Windows only ships amd64 binary)
set "ARCH=amd64"
set "BINARY_NAME=watchitai-windows-%ARCH%.exe"
set "BINARY_PATH=%SCRIPT_DIR%bin\%BINARY_NAME%"
set "GZ_PATH=%SCRIPT_DIR%bin\%BINARY_NAME%.gz"
set "DOWNLOAD_URL=https://watchitai.net/downloads/%BINARY_NAME%"

if not exist "%BINARY_PATH%" (
    if not exist "%SCRIPT_DIR%bin" mkdir "%SCRIPT_DIR%bin"
    REM Try decompressing shipped .gz file first
    if exist "%GZ_PATH%" (
        echo 🗜️  Decompressing %BINARY_NAME%.gz...
        powershell -NoProfile -Command "try { [System.IO.Compression.GzipStream]::new([System.IO.File]::OpenRead('%GZ_PATH%'), [System.IO.Compression.CompressionMode]::Decompress) | CopyTo([System.IO.File]::Create('%BINARY_PATH%')) } catch { exit 1 }"
        if errorlevel 1 (
            echo ❌ Decompression failed.
            exit /b 1
        )
        echo ✅ Decompressed %BINARY_NAME%
    ) else (
        REM No .gz — try network download as fallback
        echo 🔧 Binary not found locally, attempting download...
        echo    %DOWNLOAD_URL%
        powershell -NoProfile -Command "try { [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri '%DOWNLOAD_URL%' -OutFile '%BINARY_PATH%' -UseBasicParsing -TimeoutSec 60 } catch { Write-Host '❌ Download failed: ' $_.Exception.Message; exit 1 }"
        if errorlevel 1 (
            echo ❌ Download failed. Please download manually:
            echo    %DOWNLOAD_URL%
            echo    Then place it at: %BINARY_PATH%
            exit /b 1
        )
        echo ✅ Downloaded %BINARY_NAME%
    )
)

REM Ensure config.json exists (create minimal skeleton with correct perms if missing)
REM so the Go binary can write accessKey without ENOENT.
if not exist "%SCRIPT_DIR%config.json" (
    (
        echo {
        echo   "domain": "watchitai.net",
        echo   "bridgePort": 8765,
        echo   "mode": "server"
        echo }
    ) > "%SCRIPT_DIR%config.json"
)

REM --- Special handling for authorize command with friendly help ---------------
set "FIRST_ARG=%~1"
if /i "%FIRST_ARG%"=="authorize" (
    set "SECOND_ARG=%~2"
    if "%SECOND_ARG%"=="" (
        echo Usage:
        echo   run.cmd authorize ^<XXXX-XXXX^>     Bind using one-time auth code
        echo   run.cmd authorize --request          Auto Device Flow (recommended^)
        echo.
        echo Bind this skill to your watchitai.net account to unlock:
        echo   - Longer sessions (no 15-min single-session anonymous cap^)
        echo   - Higher daily quota (no 30-min/day anonymous cap^)
        echo   - Session ownership and audit history
        echo.
        echo Recommended - one-click Device Flow:
        echo   1. Run:  run.cmd authorize --request
        echo   2. Browser opens automatically; log in if needed
        echo   3. Click "Confirm authorize" on the web page
        echo   4. Skill auto-receives credentials (no copy/paste required^)
        echo.
        echo Legacy auth code path:
        echo   1. Log in at https://watchitai.net
        echo   2. Go to Profile -^> Access Keys
        echo   3. Click "Generate Code" and copy the 8-character code
        echo   4. Run:  run.cmd authorize XXXX-XXXX
        exit /b 1
    )
)

REM Run from SCRIPT_DIR so config.json (including accessKey) lives next to
REM the skill install dir regardless of the user's shell working directory.
cd /d "%SCRIPT_DIR%"
"%BINARY_PATH%" %*

endlocal
