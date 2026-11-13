---
name: kpa-pegasus-setup
slug: kpa-pegasus-setup
displayName: "KPA掌机天马安装与优化助手"
version: 2.0.2
platforms: [macos, linux, windows]
author: lis
description: KONKR Pocket ADVANCE（KPA，Android 12 / 960×640）掌机的 Pegasus 天马前端 + RetroArch + PPSSPP 全流程安装、排障与优化。覆盖 metadata / dataCache 缓存、ANDROID 移植游戏收录、竖版游戏方向映射、libretro 核心安装（含 MSX 本地镜像法）、BIOS / 遮罩 / 着色器 / 滤镜、.nomedia 图库隐藏、详情页增强、主题平台条增强、双屏布局、全库健康校验与可逆清理。含 7 步幂等脚本、9 个专项工具与 26 条硬性禁令。触发词：KPA、KONKR Pocket ADVANCE、AYANEO 掌机、天马、Pegasus、RetroArch、竖版方向键反了、核心装不上、掌机优化、模拟器安装、NDS 双屏变形、退出游戏回不到原位、ATOMOSWAVE 雪花、DOS 弹窗。
trigger:
  - KPA 掌机安装 / 优化
  - 天马不显示游戏 / 封面不对 / 简介不显示
  - 竖版游戏方向键反了
  - RetroArch 核心装不上 / MSX 黑屏
  - KPA 体检与清理
locale: zh-CN
---

# KPA掌机天马安装与优化助手

面向 **KONKR Pocket ADVANCE**（KPA，AYANEO 旗下，Android 12 / arm64-v8a / 960×640），把一台新机或半配置机整理成：天马(Pegasus) 前端 36 平台约 3769 游戏、RetroArch 27 个可用核心、PPSSPP 直启、竖版方向正确、封面与简介完整、图库不被素材刷屏、主题与双屏观感可用。

本包是**实机工程沉淀**，不是通用模拟器教程：所有路径、按键码、旋转值均来自该机型验证。脚本幂等，可重复运行修复。

> **不携带版权与大文件**：APK、BIOS、遮罩 PNG、ROM 均不随包分发。SkillHub / ClawHub 只允许文本类文件，因此 **prosperoOS 主题包与背景图放在 GitHub 仓库 `assets-heavy/`**（`step2_theme.sh` 检测到缺失会打印获取指引并跳过，不影响其余步骤）；`assets/golden/` 只放配置文本与 QML 修改。如需离线完整版，克隆 GitHub 仓库，或用 `scripts/sync_from_device.sh` 从已配置好的机器拉取（仅供个人使用，勿再发布）。

## 必须遵守：硬性禁令

违反以下任一条都曾导致实机故障，完整 26 条见 `references/HARD_RULES.md`。

1. **禁止 `am force-stop com.ayaneo.home`** —— 会杀掉 AYAWindow 的 `WindowKeyEventService`，KPA / Android 层系统按键全部失灵，只能关机重启恢复。**系统按键属于 KPA / Android / AYASetting / AYAWindow 层，不是 RetroArch 按键**，不要在 RA 配置里找它。
2. **禁止把 libretro 核心 `.so` 推到 public 路径**（`/sdcard`、`Android/data`、`/data/local/tmp`）后指望加载 —— SELinux `avc: denied { execute }`；只有 `/data/data/com.retroarch.aarch64/cores/` 可用。`run-as` / `adb root` / `su` / `adb backup` 全部无效（Android 12 备份产出 0 字节）。
3. **禁止改 metadata / 新增目录后不清 `dataCache.json` 就判断生效** —— 必须 `rm /sdcard/pegasus-frontend/dataCache.json` 再重启天马；缓存会保留已删除游戏。
4. **禁止靠改 `game_dirs.txt` 排除目录** —— 天马启动会重写回原样；幽灵条目只能删备份目录根治。
5. **禁止整份覆盖 `metadata.pegasus.txt`** —— 只就地 patch 启动命令/字段，云端与设备 ROM 数不匹配会丢游戏。
6. **禁止未经单点确认就批量推广按键/配置改动**。用户说「回轮」= 回滚到指定时间点。正确节奏：查历史结论 → 只改一个 → 实机确认 → 再推广。
7. **禁止对竖版 cfg 整文件覆盖式改按键** —— 只精确替换 4 行方向，保留 a/b/start/select/rotation；禁止新建或污染核心级 `config/remaps/*.rmp`（会作用于该核心全部游戏）。
8. **禁止照搬 `video_rotation` 数值差异推导方向映射**（MAME `rot=1` 与 FBNEO `rot=3` 最终呈现一致）；动手前先查历史。
9. **禁止用 3.2 秒截图或单一亮度阈值判黑屏 / 坏封面** —— 冷启动 8–26 秒；先查前台窗口与 `ANR in com.retroarch.aarch64`（ANR 弹窗造成非黑像素假阳性）。
10. **禁止批量「更新已安装核心」** —— 官方源约 17.5KB/s、nightly 非稳定版，且与 216 个竖版 cfg / 遮罩 / CRT 配套有回归风险；要更新单独点某一个。
11. **清理前必须先出只读清单 + 影响说明并获确认**；设备删除无废纸篓，分批 ≤10 项、每批校验。
12. **禁止假设 adb 能操作 RetroArch / 核心菜单** —— `input keyevent`（含 `gamepad` / `keyboard` 源）、`input tap` 对 RA **全部无效**（RA 直接 poll evdev 设备节点），`sendevent` 报 `Permission denied`（shell 不在 input 组）。只有 BACK(4) 能呼出 RA 菜单（走 Activity 回调）。**核心选项、DOSBox-pure 启动菜单的 auto start 这类操作只能由人手完成**，不要反复试注入。
13. **禁止用 per-playlist cfg 覆盖 `video_font_enable`** —— 实测 `config/Flycast/ATOMOSWAVE.cfg` 不生效，必须写进该平台**每个 per-game** cfg（`config/Flycast/<游戏名>.cfg`）。
14. **禁止在 `Roms/<平台>/` 放非 ROM 文件而不先收紧 `extensions`** —— metadata 无 `extensions` 时 Pegasus 按目录扫全部文件，多一个 `.conf` 就立刻多一个幽灵条目。
15. **禁止用设备端 `unzip` 改 `.dosz`** —— 含中文条目名会报 `Invalid entry name`；改包一律在本机用 Python `zipfile` 以 append 模式追加（只写新条目，不重压几百 MB）。

## 按需读取

| 想做什么 | 读哪个 |
|---|---|
| 完整工程复盘（7 阶段、踩坑、三次用户纠正） | `references/PROCESS_REVIEW.md` |
| 22 条禁令全文与正确做法 | `references/HARD_RULES.md` |
| 分项实操手册（metadata / RA 分层 / 竖版 / MSX / 封面 / 详情页 / .nomedia） | `references/PLAYBOOK.md` |
| 健康校验 SOP、已知遗留问题、清理清单 | `references/VERIFICATION.md` |
| 直接执行 | `scripts/run_all.sh` 或下方专项脚本 |

## 前置条件

1. `platform-tools`（macOS 实测 r34.0.5）解压到 `~/WorkBuddy/*/tools/platform-tools/`，或设 `KPA_ADB=/path/to/adb`。
2. KPA USB 连接并授权调试，或 `adb connect <ip>:5555`；`adb devices` 必须显示 `device`。
3. TF 卡默认 `/storage/6AF3-384F`（不同卡设 `KPA_TF`）；ROM / 封面按 `<TF>/Roms/<平台>/` 组织。
4. BIOS 自备（清单 `assets/data/bios_list.txt`）：PS / DC / SATURN / PCE-CD / MDCD / MSX / NAOMI 必需，卡带与街机平台不需要。

## 执行流程

```bash
bash scripts/run_all.sh     # step1..step7，幂等，可重跑
```

| 步骤 | 内容 | 关键判定 |
|---|---|---|
| step1 | 安装 RetroArch / Pegasus / PPSSPP（官方渠道下载，大 APK 先 push 到 `/data/local/tmp` 再 `pm install -r`） | `pm list packages -3` |
| step2 | prosperoOS 主题（**master 分支**）+ `assets.logo \|\| assets.boxFront` 回退 + 放大封面 + 背景 | `lastrun.log` 中 `Cannot open` = 0 |
| step3 | RA 主配置（黑黄 ozone / vulkan / CRT / 96ms / 存档迁 TF）+ 目录 + BIOS 检查 | 单独开 RA 呈黑黄 |
| step4 | 各平台 metadata 补 launch；按 `mame_orient.json` 生成竖版 cfg | 216 个竖版 cfg，方向统一 |
| step5 | PPSSPP 满屏 ini + PSP ROM 双份 + 逐游戏 launch | intent 直启 `Booted` |
| step6 | AppleDouble / `.DS_Store` 清理；可选项**只报告不自动删** | 用户确认后分批 |
| step7 | 清缓存 → 重启天马 → 截图 + `lastrun.log` 错误检查 | `N games found`、零 ANR |

**专项脚本**（按需单独调用，默认只读 / dry-run）：

| 脚本 | 用途 |
|---|---|
| `scripts/kpa_vertical.sh` | 把已有竖版 cfg 的 4 行方向修正为实机正确版（默认 dry-run，`--apply` 才写） |
| `scripts/kpa_msx_core.sh` | MSX blueMSX：搭本地 HTTP 最小核心源，让 RA 自己装进私有目录 |
| `scripts/kpa_android_apps.sh` | ANDROID 移植游戏：`.app` 占位 + per-game launch + 推 metadata |
| `scripts/kpa_nomedia.sh` | 4 个 `.nomedia` + MediaStore 重扫 |
| `scripts/kpa_gamedetails.sh` | 详情页 QML 增强（字号 / 卡片 / 去截断）+ 清缓存 |
| `scripts/kpa_theme_tweak.py` | 主题增强：平台名字号 24→36 并高亮、平台条常显、记录 Last Game 退出后回原位（默认只检查，`--apply` 才写） |
| `scripts/kpa_gamefix.sh` | 四类实机问题修复：DOS 存档弹窗 / NDS 双屏变形 / Flycast 雪花 / Atomiswave OSD 弹窗（默认 dry-run，`--apply` 写、`--revert` 回滚） |
| `scripts/kpa_health_check.sh` | 全库静态校验（ROM / 封面 / launch / 简介 / 竖版 cfg）+ 清理盘点 |
| `scripts/bangumi_desc.py` | 把模板式空壳简介升级为真简介并回填 publisher/genre（需 bgm.tv 可达） |
| `scripts/sync_from_device.sh` | 从已配置好的机型拉回重资产（个人离线用） |

**仍需人工**：① RA 首启解包内置核心 ② 自备 BIOS ③ MSX 核心需在 RA 菜单点一次下载（脚本只搭好本地源） ④ 系统桌面壁纸（AYA 桌面只认内置壁纸） ⑤ 详情页观感实机确认 ⑥ **RA / 核心菜单内的任何操作**（改核心选项、DOSBox-pure 启动菜单里按「→ Set Auto Start」设默认程序），因为 adb 注入的事件 RA 收不到。

## 关键技术事实（速查）

- **竖版方向最终值（216 个 cfg 统一）**：`up=h0right / down=h0left / left=h0up / right=h0down`；按键 `a=109 / b=108 / start=97 / select=96`。厂商原版基线是反的（`up=h0left …`），**不要照抄**。MAME 2003-Plus（MAME/VARCADE）`video_rotation="1"`；FBAlpha/FBNeo 系（FBNEO/CPS1/2/3/NEOGEO）`video_rotation="3"`；两者最终呈现一致（文字顶部朝右、满屏横躺）。竖版判定用 `assets/data/mame_orient.json`（6055 条）+ 4 个补漏 `gekiridn / tengaij / p47mus / schmeisr`。
- **ANDROID 集合**：`file:` 必须是**真实存在的文件**。写 `<包名>/<Activity>` 会被 Pegasus 丢弃，表现为整个集合不显示。正确写法：`extensions: app` + `file: <游戏名>.app`（占位空文件）+ 每个游戏一条 `launch: am start --user 0 -n <包名>/<Activity>`。封面用 `adb exec-out screencap` 截启动画面。
- **核心安装**：RA APK 内置约 83 核心，覆盖全部平台唯缺 MSX。MSX 官方源慢（约 17.5KB/s）会卡在 14%；本地镜像法：把已有 `.so` 打成 zip + 造 `.index-extended`（每行 `日期 哈希 文件名`，**不是 `.index`**）+ 临时改**两份** `retroarch.cfg` 的 `core_updater_buildbot_cores_url` 指向 Mac 的 HTTP 服务，让 RA 自己下载解压到私有 cores 目录；装完改回官方源并关服务。MSX 冷启动约 15–18 秒，不是黑屏。
- **输入注入的真实边界（2026-11-13 二次实测修正）**：RA **完全不接收** adb 注入的事件 —— `input keyevent 19/20/21/22`、`input gamepad|joystick|dpad|keyboard keyevent`、`input tap` 对 RA 全部无效（RA 直接 poll `/dev/input/event*`，绕过 InputManager），`sendevent /dev/input/event3` 报 `Permission denied`（shell 不在 input 组，`getevent` 也读不到）。**唯一有效的是 BACK(4)**，走 Activity 回调能呼出 RA 菜单。天马(Pegasus) 是普通 Qt 应用、走 InputManager，`input tap` / `input motionevent DOWN x y` + 0.3s + `UP x y` 对它有效。**因此 RA 核心选项、DOSBox-pure 启动菜单这类操作只能人手完成。**
- **实机体验类配置（v2.0.1 新增，逐条实机验证）**：
  - **主题平台条**：`collectionNav` 虽写了 `visible: false`，但被 `OpacityMask` 的 `ShaderEffectSource` 渲染出来 —— **平台条其实一直显示**，只是字号 24 且同色看不出当前平台。改 delegate 的 `font.pixelSize`（24→36）与 `color`（选中 `#ffffff` / 未选中 `#6affffff`）即可，**不需要新造标题控件**（新造会与遮罩重复渲染成双层字）。
  - **退出游戏回不到原位**：任务栈正常（RA 独立 task、天马在下层），真因是 **RAM 仅 2.96GB，天马(196MB) 被 LMK 回收**，重启后只记得 `Last Collection`、不记得具体游戏。修法：`theme.qml` 记 `Last Game` + `restoreLastGame()` 定位回列表；并把天马/RA 加白名单 `cmd deviceidle whitelist +<pkg>`。
  - **NDS 双屏**：`melonds_screen_layout="Left/Right"` + `aspect_ratio_index="23"` 会把两屏并排后再拉满屏 → 纵向变形、画面被裁。改 `Top/Bottom` + index **21**（实测 21/22 才是核心原始比例，亮像素宽约 408px；23/24 会拉到 918px）。`Hybrid` 该核心不支持（设了与 Top/Bottom 画面逐像素相同）。
  - **Flycast 雪花噪点**：`reicast_threaded_rendering="enabled"` 会让 Atomiswave 背景满屏随机雪花，改 `disabled` 即净（GGX 对比截图已验证）。
  - **DOS 存档弹窗**：全局 `rewind_enable=true` + `savestate_auto_save=true`，而 DOSBox-pure 进来先停在 `DOSBOX PURE START MENU`、游戏尚未运行 → 存状态必然失败，左下角刷 `Save State Error: Unable to save state while game is not running.`。只在 `DOSBox-pure.cfg` 关这两项，不影响其它平台倒带。
  - **Atomiswave 的 MAME romset 提示**：flycast 对旧格式 romset 发 `SET_MESSAGE`，RA 以 OSD 显示数秒不散。`video_font_enable="false"` 可关，但**必须写进 per-game cfg**（per-playlist 的 `ATOMOSWAVE.cfg` 实测不生效）；副作用是该平台不再显示存档/快进/截图提示。
- **metadata / 详情页**：`description:` 支持，多行值后续行缩进两空格；详情页 `GameDetails.qml` 原版未选中 `opacity=0.5`、简介 `vpx(18)` + `elide` 截断，观感弱。增强版在 `assets/golden/GameDetails.improved.qml.txt`，原版回滚点 `GameDetails.before.qml.txt`。空壳模板句约 1142 条，用 `bangumi_desc.py` 升级。
- **`.nomedia`**：Roms / RetroArch / pegasus-frontend / pocketmuseum 四处；隐藏图库素材但不删文件、不影响天马按路径读封面。内部存储 `scan_volume` 立即生效，TF 卡需重启。
- **PPSSPP**：targetSdk 35 无 `MANAGE_EXTERNAL_STORAGE`，读不到 TF 卡 ROM，必须把 PSP ROM 拷一份到 app 私有 `files/` 并 chmod 666，**双份均为必需勿删**；RetroArch 无 PPSSPP 核心（加载即崩）。
- **其他**：ATOMOSWAVE 裸 `.bin` 可直接玩（首屏 NOTICE 约 20–30 秒，曾被误判不兼容）；但 `VR运动会.bin`（117MB）实测 40 秒仍全黑、同平台罪恶装备X 20 秒即进画面 —— 判定为坏 ROM，已隔离到 `Roms/_quarantine/` 并移除 metadata 条目（**移走不删，可逆**）；GBA 不要加遮罩（240×160 = 原生满屏 960×640）；封面修复优先 libretro thumbnails，其次实机截图裁 480×320，再不行做标题占位图；中文 zip 条目名会让 toybox `unzip` 误报 CRC BAD 或 `Invalid entry name`，本机 Python `zipfile` 复核为准。

## 健康状态基线（实测）

- 全量静态校验 **3769 条**：ROM 缺失 0、封面缺失 0、无 launch 0、无简介 0、重复 file 引用 0、重复游戏名 0；`dataCache.json` 重建后 `is_missing = 0`。
- 竖版 cfg 实测 **219 个**（MAME 2003+ 140 / FBNeo 72 / CPS1 3 / CPS2 2 / NEOGEO 2），方向映射 **219/219 全部正确**。文档早期基线写 216，差 3 个 FBNeo 系后续补入，属口径漂移而非故障。
- 27/27 libretro 核心可执行（`avc: granted { execute }`）、8/8 独立 APP 前台正常；`lastrun.log` 零 error。
- 已消除：`Roms/_backup_*/` 幽灵目录造成的虚增平台与 555 条缺文件警告（2026-11-13 清理）、设备侧 17 项备份（17.40MB）已删、本机 9 项 377MB 已移入废纸篓。
- 遗留项：`WS/恐怖传说.zip` 真坏 ROM（TorrentZip）；1142 条空壳简介（需 bgm.tv 可达）；详情页观感待实机确认；`Roms/_quarantine/VR运动会.bin` 待补好 ROM。详见 `references/VERIFICATION.md`。

## 清理与回滚

- 设备侧默认零备份；确需保留的最小回滚点（QML 原版、`firmware.bin.bak` 等）在清理清单里单列。
- 本机工作区产物与报告 HTML 归档在 GitHub 仓库 `archive/`；本机按「只保留上架版 skill + adb 工具」清理。
- 回滚用 `sync_from_device.sh` 从好机器同步，或重跑对应 step；**任何删除前先出清单、说明影响、获确认，分批 ≤10 项逐批校验**。

## 版本与来源

- **v2.0.2（2026-11-13）**：`kpa_gamefix.sh` 的回滚改为**值级还原**。原因：同一份 cfg 会被多轮改动，`.bak` 很容易在某次"改完之后"才创建，变成"已改版"备份 —— `cp` 回去等于没回滚（本轮实测踩到）。现按原值还原并在设备上双向验证（回滚删行/改回 `true`，再应用恢 16 处写入）。其余同 2.0.1。
- **v2.0.1（2026-11-13）**：按实机反馈修 6 类体验问题 —— ①主题平台名字号 24→36 且选中高亮 ②退出后恢复上次游戏（`Last Game` + 白名单）③NDS 双屏改上下排列 + 原始比例 ④Flycast 关多线程渲染修雪花 ⑤DOS 关倒带修存档弹窗 ⑥Atomiswave 逐游戏关 OSD 修 MAME romset 提示。新增 `kpa_theme_tweak.py` 与 `kpa_gamefix.sh`（均幂等、`--revert` 可回滚）。**修正一个错误认知**：adb 注入的事件 RA 全部不接收（`input` 各源无效、`sendevent` 无权限），只有 BACK 有效。新增禁令 12–15。隔离坏 ROM `VR运动会.bin`，健康基线 3770→3769。
- **v2.0.0（2026-11-13）**：纠正竖版方向映射、ANDROID `.app` 占位写法、机型名；新增 MSX 本地镜像、`.nomedia`、详情页增强、健康校验、清理盘点专项脚本；补 22 条硬性禁令、全流程复盘与遗留项清单。
- 发布：SkillHub `@user_43faedd6/kpa-pegasus-setup` · ClawHub `kpa-pegasus-setup` · GitHub `lisong2003-lgtm/kpa-pegasus-setup`
- 资源版权归各自所有者；本包只分发配置文本、脚本与自建主题修改，不含 ROM / BIOS / APK。
