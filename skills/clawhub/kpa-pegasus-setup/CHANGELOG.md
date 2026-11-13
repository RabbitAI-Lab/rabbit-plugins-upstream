# Changelog

## 2.0.2 — 2026-11-13

### 修复

- `scripts/kpa_gamefix.sh` 的 `--revert` 改为**值级还原**，不再依赖 `.bak` 文件。原因：同一份 cfg 会被多轮改动，`.bak` 很容易在某次「改完之后」才被创建，于是变成「已改版」备份 —— `cp` 回去等于没回滚（本轮实测在 Flycast 的 10 个 per-game cfg 上踩到了）。
  现在的还原语义：DOS → `rewind_enable`/`savestate_auto_save` 回 `true`；NDS → 布局回 `Left/Right`、触屏回 `Mouse`、`aspect_ratio_index` 回 `23`；Flycast → `reicast_threaded_rendering` 回 `enabled`；Atomiswave → 删除 `video_font_enable` 行。
- 设备上双向验证通过：回滚后 `video_font_enable` 计数归 0、`rewind_enable=true`；再 `--apply` 恢复 16 处写入，值回到 `false`。

## 2.0.1 — 2026-11-13

按实机反馈修六类体验问题，并推翻一处会误导排查的错误认知。

### 修复

- **DOS 左下角 `Save State Error` 弹窗**：全局 `rewind_enable=true` + `savestate_auto_save=true`，而 DOSBox-pure 进来先停在 `DOSBOX PURE START MENU`、游戏尚未运行 → 存状态必然失败。只在 `DOSBox-pure.cfg` 关这两项，不影响其它平台倒带。
- **NDS 双屏被纵向拉长、画面被裁**：`melonds_screen_layout="Left/Right"` + `aspect_ratio_index="23"`，两屏并排后又被拉满屏 → 改 `Top/Bottom` + index **21**（实测 21/22 才是核心原始比例，亮像素宽约 408px；23/24 拉到 918px）。`Hybrid` 该核心不支持。
- **Atomiswave 背景满屏雪花噪点**：`reicast_threaded_rendering` 改 `disabled`。
- **Atomiswave 的 `Please upgrade to MAME romsets` 提示**：逐游戏 per-game cfg 写 `video_font_enable="false"`（**per-playlist 层实测不生效**）。
- **平台名字太小、切平台看不出当前在哪**：delegate 字号 24→36、选中 `#ffffff` / 未选 `#6affffff`、平台条常显；顶部游戏条 10→16。
- **退出游戏回到平台第一个而非刚才那个**：记 `Last Game` + `restoreLastGame()` 定位回原游戏；天马 / RA 加入电池优化白名单（RAM 仅 2.96GB，天马易被 LMK 回收）。
- **坏 ROM `VR运动会.bin`**：实测 40 秒仍全黑（同平台罪恶装备X 20 秒进画面），移入 `Roms/_quarantine/` 并从 metadata 移除条目，天马 3770→3769。**移走不删，可逆。**

### 新增

- `scripts/kpa_gamefix.sh`：`dos` / `nds` / `flycast` / `aw-osd` / `all`，默认 dry-run，`--apply` 写入、`--revert` 回滚，全部幂等。**回滚用值级还原而非文件恢复** —— 同一份 cfg 可能被多轮改动，`.bak` 很容易在某次"改完之后"被创建而变成"已改版"备份，此时 `cp` 回去等于没回滚（本次实测就踩到了）。
- `scripts/kpa_theme_tweak.py`：主题 6 处增强，锚点失配会明确报告而不是写半成品；`--apply --restart` 一步到位。
- `references/PLAYBOOK.md` 第 10 节：六类问题根因对照表、主题遮罩机制、NDS 比例客观定法、以及「一条走不通的路」（DOS 自动跳过启动菜单，含 15 个包启动项清单）。

### 修正

- **推翻错误认知**：原文写「`input motionevent` 可点 RA 菜单、方向键 19–22 有效」。实测 RA **完全不接收** adb 注入的事件 —— `input keyevent`（keyboard / gamepad / joystick / dpad 四种 source 全试）与 `input tap` 注入后截图**逐像素相同**；`sendevent /dev/input/event3` 报 `Permission denied`（shell 不在 input 组）。只有 **BACK(4)** 走 Activity 回调有效。天马是普通 Qt 应用、走 InputManager，注入对它有校 —— 两者不能混为一谈。
- 新增禁令 12–15：RA 输入注入边界 / per-playlist 覆盖 OSD 开关不生效 / 往 `Roms/<平台>/` 放非 ROM 文件前必须先收紧 `extensions` / 禁止用设备端 `unzip` 改 `.dosz`。

### 基线

- 天马条目 **3770 → 3769**（隔离坏 ROM），`is_missing = 0`。
- 竖版 cfg 实测 **219**（MAME 2003+ 140 / FBNeo 72 / CPS1 3 / CPS2 2 / NEOGEO 2），方向映射 **219/219** 全量校验通过；早期文档写 216 属口径漂移。
- 设备侧 17 项 / 17.40MB 备份已清理完毕，幽灵目录与 555 条缺文件警告归零，平台数 37→36。

## 2.0.0 — 2026-11-13

名称定为「KPA掌机天马安装与优化助手」，slug 统一为 `kpa-pegasus-setup`，发布到 SkillHub / ClawHub / GitHub。

### 修正（会导致实机故障的错误）

- 竖版方向映射：`up=h0left / down=h0right / left=h0down / right=h0up`（厂商基线）→ `up=h0right / down=h0left / left=h0up / right=h0down`（实机验证值）。同步修正 `SKILL.md` 与 `scripts/step4_metadata.sh` 两处。
- ANDROID 集合 `file:` 由 Android 组件名改为 `.app` 占位真实文件 + `extensions: app` + per-game `launch:`；重写 `assets/meta_latest/ANDROID.txt`，并补 `assets/golden/game_dirs.txt` 的 ANDROID 行。
- 机型名由误写的 "AYANEO Pocket Advance" 改为正式名 KONKR Pocket ADVANCE（AYANEO 旗下）。
- MSX 核心安装方式由「下载 .so 到 public 路径」改为「本地 HTTP 最小核心源 + `.index-extended`，让 RA 自己装进私有 cores 目录」。
- `scripts/bangumi_desc.py` 移除硬编码的 adb 绝对路径，改为 `KPA_ADB` / PATH / 自动发现；TF 卡路径支持 `KPA_TF`。
- `scripts/step6_cleanup.sh` 移除两处通配 `rm -rf`，改为只盘点、不自动删。

### 新增

- `scripts/kpa_vertical.sh`：修存量竖版 cfg，默认 dry-run，只精确替换 4 行方向。
- `scripts/kpa_msx_core.sh`：MSX 本地镜像 prepare / restore。
- `scripts/kpa_android_apps.sh`：ANDROID 占位文件与 metadata 部署。
- `scripts/kpa_nomedia.sh`：4 处 `.nomedia` + MediaStore 重扫。
- `scripts/kpa_gamedetails.sh`：详情页 QML 增强与回滚点。
- `scripts/kpa_health_check.sh`：全库静态校验 + 离线自检 `--local`。
- `references/PROCESS_REVIEW.md`：7 阶段完整工程复盘。
- `references/HARD_RULES.md`：22 条硬性禁令与正确做法。
- `references/PLAYBOOK.md`：9 个分项实操手册。
- `references/VERIFICATION.md`：健康校验 SOP、达标基线、遗留项、清理清单、回滚点。
- `assets/golden/GameDetails.improved.qml.txt` 与 `.before20261113`。
- `README.md`、`.gitignore`、本文件；GitHub 仓库 `archive/` 归档工程报告与回滚点（已脱敏）。

### 记录

- 补充「禁止 `am force-stop com.ayaneo.home`」等系统按键层禁令。
- 补充核心批量更新风险评估（3% 中断无影响，不建议更新 nightly）。
- 补充冷启动等待基准（8–26 秒）与 toybox `unzip` 中文条目 CRC 误报说明。
- 明确遗留项：`WS/恐怖传说.zip` 坏 ROM、`_backup_20261112_2347` 幽灵目录、1142 条空壳简介、详情页观感待实机确认、设备侧 17 项待清理。

## 1.0.0 — 2026-11-12

上架版：7 步幂等安装脚本（APP / 主题 / RA 主配置 / metadata + 竖版 cfg / PPSSPP / 清理 / 验证）、`sync_from_device.sh`、`bangumi_desc.py`、36 平台 metadata 与方向库、prosperoOS 主题包。约 3.4MB，不含 ROM / BIOS / APK。
