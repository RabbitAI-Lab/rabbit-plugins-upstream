---
name: kpa-pegasus-setup
slug: kpa-pegasus-setup
displayName: "KPA掌机天马安装与优化助手"
version: 2.3.2
platforms: [macos, linux, windows]
author: lis
description: KPA 掌机天马/RA/PPSSPP 安装与排障优化；不含 ROM/BIOS。
trigger:
  - KPA / KONKR Pocket ADVANCE / 天马 / Pegasus / RetroArch
  - 竖版方向键反了 / 核心装不上 / NDS 双屏变形
  - 封面不对 / 没有简介 / 缓存清理 / 一键安装
locale: zh-CN
---

# KPA掌机天马安装与优化助手

面向 **KONKR Pocket ADVANCE**（KPA，AYANEO 旗下，Android 12 / arm64-v8a / 960×640）：把新机或半配置机整理成天马(Pegasus)前端 + RetroArch + PPSSPP 可用状态 —— 平台分组建齐、27 个核心可执行、竖版方向正确、封面与简介完整、每平台热门 10 款置顶、图库不被素材刷屏、可一键重跑。

本包是**实机工程沉淀**，路径、按键码、旋转值均来自该机型验证，脚本幂等。ROM / BIOS / APK / 遮罩 PNG 不随包分发：主题二进制在 GitHub `assets-heavy/`，`step2_theme.sh` 缺失时打印指引并跳过，不影响其余步骤。

## 前置条件

1. `platform-tools`（macOS 实测 r34.0.5），或设 `KPA_ADB=/path/to/adb`。
2. USB 调试已授权，或 `adb connect <ip>:5555`；`adb devices` 必须显示 `device`。
3. TF 卡默认 `/storage/6AF3-384F`（不同卡设 `KPA_TF`）；ROM 按 `<TF>/Roms/<平台>/` 组织。
4. BIOS 自备（清单 `assets/data/bios_list.txt`）：PS / DC / SATURN / PCE-CD / MDCD / MSX / NAOMI 必需，卡带与街机不需要。

## 一键入口（推荐）

```bash
bash scripts/kpa_oneclick.sh --dry-run   # 只读体检 + 计划，设备离线也能预览
bash scripts/kpa_oneclick.sh             # 体检 → 双回滚点 → 7 步幂等 → 清缓存 → 校验 → report.md
```

其他模式：`--verify-only`（只出校验报告）、`--steps 3,4`（只跑指定步骤）、`--no-backup`（不建议）。产物在 `~/WorkBuddy/kpa-oneclick/<时间戳>/`：`oneclick.log` / `backup/` / `health.txt` / `report.md`（含「必须人手实机确认」清单）。

只跑 7 步用 `bash scripts/run_all.sh`。专项脚本（竖版修正 / MSX 核心 / ANDROID 收录 / `.nomedia` / 详情页 / 主题增强 / 五类实机修复 / 健康校验 / 简介回填 / 设备同步）清单与用法见 `references/PLAYBOOK.md` §20 与各脚本头注释。

⚠️ 针对特定机器数据的一次性修复 —— 热门 10 款置顶、DOS 同名 `.conf`、GBA 真盒绘回填、土星坏 CHD 删除、CPS1/CPS3 键位、N64 摇杆绑定 —— **不进一键脚本**，按需查 `references/PLAYBOOK.md` §18–§19。

## 硬性禁令（Top 10；全文 57 条见 `references/HARD_RULES.md`）

1. **禁止 `am force-stop com.ayaneo.home`** —— 会杀掉 AYAWindow 的按键服务，KPA/Android 层按键全部失灵，只能关机重启。系统按键不属于 RetroArch。
2. **禁止把核心 `.so` 推到 public 路径** —— SELinux `avc: denied { execute }`；只认 `/data/data/com.retroarch.aarch64/cores/`。`run-as` / `adb root` / `su` / `adb backup` 在 Android 12 均无效。
3. **禁止改 metadata / 加目录后不清 `dataCache.json` 就判断生效** —— 必须 force-stop → 删缓存 → 重启天马，否则仍显示旧条目与旧简介。
4. **禁止靠改 `game_dirs.txt` 排除目录** —— 天马启动会重写回原样；幽灵条目只能删源目录根治。
5. **禁止整份覆盖 `metadata.pegasus.txt`** —— 只就地 patch launch/字段，云端与设备 ROM 数不匹配会丢游戏。
6. **禁止未单点确认就批量推广按键/配置改动，也禁止批量「更新已安装核心」** —— 核心源慢、nightly 不稳，与 219 个竖版 cfg / 遮罩 / CRT 有回归风险。用户说「回轮」= 回滚到指定时间点。
7. **禁止整文件覆盖竖版 cfg** —— 只精确替换 4 行方向，保留 `a/b/start/select/rotation`；禁止新建或污染核心级 `config/remaps/*.rmp`。
8. **禁止照搬 `video_rotation` 数值差异推导方向** —— MAME `rot=1` 与 FBNEO `rot=3` 最终呈现一致，动手前先查历史。
9. **禁止用 3.2 秒截图或单一亮度阈值判黑屏/坏封面** —— 冷启动 8–26 秒；先查前台窗口与 `ANR in com.retroarch.aarch64`；封面按图像内容分类，不按尺寸一刀切。
10. **禁止假设 adb 能操作 RetroArch / 核心菜单** —— RA 直接 poll evdev 设备节点，`input keyevent` / `input tap` 全部无效，`sendevent` 无权限；只有 BACK(4) 能呼出 RA 菜单。核心选项、DOSBox-pure 启动菜单只能人手完成。

## 按需读取

| 想做什么 | 读哪个 |
|---|---|
| 新机一键安装 / 最短路径 / 不走弯路 10 条 | `INSTALL.md` |
| 关键技术事实速查（按键 / 竖版 / MSX / 主题 / PPSSPP / 缓存） | `references/PLAYBOOK.md` §21 |
| 分项实操手册（metadata / RA 分层 / 竖版 / 封面 / 详情页 / 清理 / DOS / 按键） | `references/PLAYBOOK.md` |
| 57 条禁令全文与正确做法 | `references/HARD_RULES.md` |
| 健康校验 SOP、已知遗留、清理清单与回滚点 | `references/VERIFICATION.md` |
| 优化全过程复盘 + 机能体检 / 是否发挥到极致 / 分级优化候选 | `references/OPTIMIZATION_JOURNEY.md` |
| 完整工程复盘（7 阶段、踩坑、三次用户纠正） | `references/PROCESS_REVIEW.md` |
| 逐版变更、根因与更正 | `CHANGELOG.md` |
| 直接执行 | `scripts/kpa_oneclick.sh`；只跑 7 步用 `scripts/run_all.sh` |

图示属于 `@user_43faedd6` 账号统一的**蓝标（Blueprint Badge）系列**（`assets/blueprints/`），`python3 scripts/blueprint_icons.py` 重新生成、`--check` 校验。

## 健康基线（两个口径，别混用）

| 口径 | 数字 | 说明 |
|---|---|---|
| 设备实测（2026-11-15） | **35 平台 / 3706 条** | 删除 VB 与土星《钟表骑士》两作后的实机基线；ROM / 封面引用缺失 0、重复 file 0、无 launch 0、无简介 0 |
| 资产模板（`kpa_health_check.sh --local`） | **36 平台 / 3773 条** | 包内 `assets/meta_latest/` 仍含 VB 模板；离线自检用这个口径 |

- 竖版 cfg **219 个**（MAME 2003+ 140 / FBNeo 72 / CPS1 3 / CPS2 2 / NEOGEO 2），方向映射 219/219 正确；早期文档写 216 属口径漂移（少算 3 个 FBNeo 系）。
- 27/27 libretro 核心可执行、8/8 独立 APP 前台正常、`lastrun.log` 零 error；简介模板句 0 条（3,736 条快照已全有真实简介）。
- 历史快照 **3769 / 3736 / 3770 / 3773** 是不同时点的数，引用时必须带日期，不当当前值用。
- 遗留：`WS/恐怖传说.zip` 真坏 ROM；`Roms/_quarantine/VR运动会.bin`（移走不删、可逆）；`savestate_auto_save=true` 会再生 `.state.auto`；街机 CPS1/CPS3、ATOMOSWAVE 竖版、PPSSPP / PS ABXY、N64 方向键的**实体键手感仍需用户实测**（adb 注入对 RA 无效）。

## 清理与回滚

- 设备侧默认零备份；确需保留的最小回滚点（QML 原版、`firmware.bin.bak` 等）在清理清单里单列。
- 本机工作区产物与报告归档在 GitHub 仓库 `archive/`；本机只保留上架版 skill + adb 工具。
- 回滚用 `sync_from_device.sh` 从好机器同步，或重跑对应 step。**值级还原优先**：`.bak` 可能是「改完后」才建的副本，覆盖前先比对内容。
- **任何删除前先出只读清单、说明影响、获确认，分批 ≤10 项逐批校验**；设备删除无废纸篓，`Roms/_quarantine/` 移走不删。

## 版本与来源

- 当前版本 **2.3.1**；逐版变更、根因与自我更正以 `CHANGELOG.md` 为唯一版本历史来源（本文件不再重复版本流水账）。
- 发布：SkillHub `@user_43faedd6/kpa-pegasus-setup` · GitHub `lisong2003-lgtm/kpa-pegasus-setup`；ClawHub `kpa-pegasus-setup`（入口可用性以当次回查为准）。
- 资源版权归各自所有者；本包只分发配置文本、脚本与自建主题修改，不含 ROM / BIOS / APK。
