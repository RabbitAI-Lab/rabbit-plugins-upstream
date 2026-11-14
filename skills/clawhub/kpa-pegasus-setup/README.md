# KPA掌机天马安装与优化助手

面向 **KONKR Pocket ADVANCE**（KPA，AYANEO 旗下，Android 12 / arm64-v8a / 960×640）的 Pegasus 天马前端 + RetroArch + PPSSPP 全流程安装、排障与优化 Skill。

整套方案来自一次真实机器的完整搭建工程：36 平台约 3769 游戏、27 个可用 libretro 核心、8 个独立 APP、219 个竖版游戏方向映射，全部经过实机验证。仓库里既有可重复执行的幂等脚本，也有踩坑复盘与 26 条硬性禁令。

## 安装

```bash
# SkillHub
skillhub install "@user_43faedd6/kpa-pegasus-setup"

# ClawHub
clawhub install kpa-pegasus-setup

# GitHub（手动）
git clone https://github.com/lisong2003-lgtm/kpa-pegasus-setup.git
cp -R kpa-pegasus-setup/skill ~/.workbuddy/skills/kpa-pegasus-setup
```

> SkillHub / ClawHub 的安装命令会自动多套一层 `@handle/` 目录，若手动安装请注意把内容移到 `<skills>/<slug>/SKILL.md` 这一层级才会被识别。

## 快速开始

```bash
adb devices                         # 必须先看到 device
bash scripts/run_all.sh             # 7 步幂等安装，可重复运行修复
bash scripts/kpa_health_check.sh    # 只读全库静态校验
```

专项工具（默认 dry-run 或只读）：

| 脚本 | 用途 |
|---|---|
| `kpa_vertical.sh` | 把已有竖版 cfg 的 4 行方向改成实机正确版（`--apply` 才写） |
| `kpa_msx_core.sh` | MSX blueMSX 核心本地镜像：`prepare` 搭源 / `restore` 改回官方源 |
| `kpa_android_apps.sh` | ANDROID 移植游戏 `.app` 占位 + per-game launch |
| `kpa_nomedia.sh` | 4 处 `.nomedia` + MediaStore 重扫 |
| `kpa_gamedetails.sh` | 详情页 QML 增强 + 清缓存 |
| `kpa_theme_tweak.py` | 主题增强：平台名字号 24→36 并高亮、平台条常显、记住上次游戏（`--apply` / `--revert`） |
| `kpa_gamefix.sh` | 修复四类实机问题：DOS 存档弹窗 / NDS 双屏变形 / Flycast 雪花 / Atomiswave OSD 弹窗（`dos\|nds\|flycast\|aw-osd\|all`） |
| `kpa_health_check.sh` | 全库静态校验 / 离线自检 `--local` |
| `bangumi_desc.py` | 空壳简介升级为真简介并回填 publisher/genre |
| `sync_from_device.sh` | 从已配置好的机型拉回重资产（个人离线用） |

## 目录

```
SKILL.md                    主入口：禁令速查、流程、关键技术事实
references/
  PROCESS_REVIEW.md         完整工程复盘（7 阶段、踩坑、三次用户纠正）
  HARD_RULES.md             26 条硬性禁令与正确做法
  PLAYBOOK.md               分项实操手册
  VERIFICATION.md           健康校验 SOP、遗留项、清理清单、回滚点
scripts/                    幂等安装脚本 + 专项工具
assets/golden/              配置文本、QML 增强版与原版（无二进制）
assets/data/                平台→核心映射、竖版方向库、BIOS 清单
assets/meta_latest/         36 平台 metadata 模板
assets-heavy/               （仅本仓库）prosperoOS 主题包与背景图，文本版发行包不含
archive/                    （仅本仓库）工程报告、校验数据与回滚点
```

## v2.0.1 修复（实机反馈）

六类体验问题，逐条实机复现 → 定根因 → 改完复测：

| 现象 | 处理 |
|---|---|
| DOS 左下角反复刷 `Save State Error` | 只在 DOSBox-pure 关 `rewind_enable` / `savestate_auto_save`（游戏未运行时存状态必然失败） |
| NDS 双屏被纵向拉长、画面被裁 | 改 `Top/Bottom` + `aspect_ratio_index=21`（21/22 才是核心原始比例） |
| Atomiswave 背景满屏雪花噪点 | 关 flycast 多线程渲染 |
| Atomiswave 的 `Please upgrade to MAME romsets` 提示 | 逐游戏 **per-game** cfg 关 OSD 文字（per-playlist 层不生效） |
| 平台名字太小、切平台看不出当前在哪 | 字号 24→36、选中纯白/未选压暗、平台条常显；顶部游戏条 10→16 |
| 退出游戏回到平台第一个 | 记 `Last Game` 自动定位回原游戏 + 天马/RA 电池白名单 |

同时纠正一个会误导排查的认知：**adb 注入的输入事件 RA 完全收不到** —— `input keyevent`（含 gamepad / keyboard 等 source）与 `input tap` 注入后截图逐像素相同，`sendevent` 报 `Permission denied`，只有 BACK 有效。所以 **RA 核心菜单、DOSBox-pure 启动菜单只能人手操作**，不要反复试注入。详见 `references/PLAYBOOK.md` 第 10 节。

坏 ROM `VR运动会.bin`（40 秒仍全黑）已隔离到 `Roms/_quarantine/` 并从 metadata 移除，天马条目 3770 → 3769。

## v2.0.0 关键修正

旧版有三处会直接导致故障的错误，本版已全部纠正：

1. **竖版方向映射写反**：旧版 `up=h0left / down=h0right / left=h0down / right=h0up` 是厂商原版基线；实机验证的正确值是 `up=h0right / down=h0left / left=h0up / right=h0down`。`SKILL.md` 与 `step4_metadata.sh` 均已改，并新增 `kpa_vertical.sh` 修存量 cfg。
2. **ANDROID 集合 `file:` 写成组件名**：Pegasus 会丢弃，表现为整个集合不显示。改为 `extensions: app` + `.app` 占位真实文件 + per-game `launch:`，`assets/meta_latest/ANDROID.txt` 已重写。
3. **机型名与 MSX 安装方式过时**：正式名是 KONKR Pocket ADVANCE；MSX 核心不能靠 push（SELinux 拒绝执行），改为本地 HTTP 最小核心源让 RA 自己装。

另补充：禁止强杀 `com.ayaneo.home`（会杀掉系统按键服务）、`.nomedia`、详情页增强、健康校验、清理盘点、22 条禁令与全流程复盘。

## 已知遗留

`WS/恐怖传说.zip` 坏 ROM、`Roms/_quarantine/VR运动会.bin` 待换可用 ROM、1142 条空壳简介、详情页观感待实机确认。详见 `references/VERIFICATION.md`。

已解决（v2.0.1）：TF 卡幽灵备份目录与 555 条缺文件警告已归零；设备侧 17 项 / 17.40MB 备份已清理；主题与双屏观感已修。

## 说明

- **不含 ROM / BIOS / APK / 遮罩素材**，需自备（清单见 `assets/data/bios_list.txt`）。SkillHub / ClawHub 只允许文本类文件，故 prosperoOS 主题包与背景图放在本仓库 `assets-heavy/`；从 GitHub 克隆完整版后把它们拷进 `skill/assets/golden/` 即可，`step2_theme.sh` 检测到缺失会打印获取指引并跳过，其余步骤不受影响。
- 归档报告已对设备序列号、局域网 IP 与本机用户名脱敏。
- 所有路径与按键码针对该机型实测；换机型请重新核对 TF 卡挂载点、分辨率与按键码。
- 清理与回滚有严格纪律：先出只读清单、说明影响、获确认，分批 ≤10 项、每批校验。设备删除无废纸篓。
