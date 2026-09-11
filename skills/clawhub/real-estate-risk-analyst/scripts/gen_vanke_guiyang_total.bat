@echo off
rem ============================================================
rem 生成「万科在筑 53 个官方项目总表」
rem 依赖：本地全量证级 dump（已落盘，无需联网）
rem 用法：双击或在命令行执行本文件
rem 产物：output_cross/贵阳/万科在筑_官方项目总表_20260812.xlsx
rem   - Sheet1 项目汇总（53 个项目 + 证级数 + 申请主体 + 首末证日）
rem   - Sheet2 全部证级清单（167 本含万科）
rem   - Sheet3 来源说明
rem 注：批准套数/面积需 details_json 补；本启动器仅用 list 级数据出项目总表。
rem ============================================================
rem 路径自动定位（发布版已移除硬编码私人路径）
set SKILL=%~dp0..
if "%PY%"=="" set PY=python
if "%OUT%"=="" set OUT=%CD%\output_cross\贵阳
if "%GW_JSON%"=="" set GW_JSON=%OUT%ll_guiyang_permits_2026.json

"%PY%" "%SKILL%\scripts\by_developer.py" ^
  --mode project-summary ^
  --city guiyang ^
  --brand 万科 ^
  --brand-key 万科 ^
  --from-json "%GW_JSON%" ^
  --out "%OUT%\万科在筑_官方项目总表_20260812.xlsx"

echo.
echo done. 产物: %OUT%\万科在筑_官方项目总表_20260812.xlsx
pause
