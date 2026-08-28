@echo off
REM ============================================================
REM 双色球V2.1.35智能预测 - 一键全自动
REM
REM 单入口: ssq_smart.py
REM 自动完成: 开奖日检测→Phase0.5永久自检→Phase0.6专家抓取→上期验证→数据下载→
REM           V1预测→V1.0增强→三方交叉验证→Phase6强化引擎→智能摘要
REM
REM 系统级任务(推荐): schtasks /create /tn "SSQ_V1_Smart" /tr "本bat路径"
REM                    /sc weekly /d TUE,THU,SUN /st 20:10 /ru SYSTEM /f
REM ============================================================

cd /d "%~dp0"

REM 关键: 任务计划程序/系统语境下 stdout 默认 GBK, 脚本打印 ✅❌ 等字符会 UnicodeEncodeError 崩溃并吞掉错误
REM 强制 UTF-8 代码页 + Python 输出编码, 确保完整日志
chcp 65001 >nul 2>&1
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1
set PYTHONDONTWRITEBYTECODE=1

REM 日志轮转: 保留最近 5 次运行 (避免只覆盖最后一次导致历史丢失, 也避免无限增长)
set LOGFILE=ssq_scheduler_run.log
if exist "%LOGFILE%" (
    for /l %%i in (4,-1,1) do (
        if exist "%LOGFILE%.%%i" move /y "%LOGFILE%.%%i" "%LOGFILE%.%%i+" >nul 2>&1
    )
    if exist "%LOGFILE%.1+" ren "%LOGFILE%.1+" "%LOGFILE%.2" >nul 2>&1
    if exist "%LOGFILE%.2+" ren "%LOGFILE%.2+" "%LOGFILE%.3" >nul 2>&1
    if exist "%LOGFILE%.3+" ren "%LOGFILE%.3+" "%LOGFILE%.4" >nul 2>&1
    if exist "%LOGFILE%.4+" ren "%LOGFILE%.4+" "%LOGFILE%.5" >nul 2>&1
    move /y "%LOGFILE%" "%LOGFILE%.1" >nul 2>&1
)
echo ============================================================ > "%LOGFILE%"
echo 双色球V2.1.35 智能预测 - %date% %time% >> "%LOGFILE%"
echo ============================================================ >> "%LOGFILE%"

REM 单命令全自动运行
REM 使用隔离运行时的绝对路径, 不依赖系统 PATH 是否含 python (任务计划程序环境常无 python)
REM 注意: ssq_smart.py 内部用 sys.executable 启动子进程, 子进程也会用同一隔离 python, 依赖完全一致
set PYRUN="C:\Users\www74\.workbuddy\binaries\python\versions\3.13.12\python.exe"
call %PYRUN% lib\ssq_smart.py --force >> "%LOGFILE%" 2>&1

REM 检查 python 退出码: ssq_smart.py 在关键步骤(预测/交叉验证)失败时会 exit(1)
REM 必须如实反映到日志与 bat 退出码, 否则"带病交付"会被系统任务误判为成功
set RC=%ERRORLEVEL%
echo. >> "%LOGFILE%"
echo ============================================================ >> "%LOGFILE%"
if "%RC%"=="0" goto BAT_OK
REM 失败告警: 落一个明确的可轮询告警文件, 用户无需天天翻日志也能发现运行失败
echo [BAT] 运行失败 (EXIT=%RC%) - %date% %time% > "ssq_run_alert.txt"
echo 请查看 ssq_scheduler_run.log 中的 [STDERR] 或 永久自检未通过 标记 >> "ssq_run_alert.txt"
echo [BAT] 运行失败 (EXIT=%RC%) - %date% %time% >> "%LOGFILE%"
echo [BAT] 请检查上方日志中的 [STDERR] 或 永久自检未通过 标记 >> "%LOGFILE%"
goto BAT_END
:BAT_OK
if exist "ssq_run_alert.txt" del /f /q "ssq_run_alert.txt" >nul 2>&1
echo [BAT] 全流程完成 (EXIT=0) - %date% %time% >> "%LOGFILE%"
:BAT_END
echo ============================================================ >> "%LOGFILE%"

REM ---- 开奖后自动核对(独立步骤, 不影响上方预测结果上报/告警) ----
REM 20:10 运行时, 上一期开奖结果早已上网, --auto 自动拉取并生成"开奖核对报告.html"到真实桌面
echo. >> "%LOGFILE%"
echo [核对] 开始上期开奖核对 - %date% %time% >> "%LOGFILE%"
call %PYRUN% lib\ssq_draw_check.py --auto >> "%LOGFILE%" 2>&1
echo [核对] 完成 - %date% %time% >> "%LOGFILE%"

exit /b %RC%
