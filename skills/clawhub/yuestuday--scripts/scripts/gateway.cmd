@echo off
rem OpenClaw Gateway launcher (auto-generated, adapts to installed version)
set "OPENCLAW_SERVICE_MANAGED_ENV_KEYS=OPENCLAW_AUTH_QWEN"
set "TMPDIR=%LOCALAPPDATA%\Temp"
set "OPENCLAW_GATEWAY_PORT=18789"
set "OPENCLAW_WINDOWS_TASK_NAME=OpenClaw Gateway"
set "OPENCLAW_WINDOWS_TASK_HIDDEN_LAUNCHER=1"
set "OPENCLAW_SERVICE_MARKER=openclaw"
set "OPENCLAW_SERVICE_KIND=gateway"

rem Resolve node: prefer npm's bundled node, fall back to PATH
set "NODE_EXE=%APPDATA%\npm\node.exe"
if not exist "%NODE_EXE%" set "NODE_EXE=C:\Program Files\nodejs\node.exe"
if not exist "%NODE_EXE%" set "NODE_EXE=node"

rem Resolve openclaw entrypoint dynamically
set "OPENCLAW_ENTRY=%APPDATA%\npm\node_modules\openclaw\dist\index.js"

"%NODE_EXE%" "%OPENCLAW_ENTRY%" gateway --port 18789
