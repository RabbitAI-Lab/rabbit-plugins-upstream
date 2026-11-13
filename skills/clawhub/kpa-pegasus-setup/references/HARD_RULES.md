# 硬性禁令（22 条）

每一条都来自实机故障或用户纠正。`SKILL.md` 收录前 11 条，本文是全文与正确做法。

## A. 系统层与权限

**1. 禁止 `am force-stop com.ayaneo.home`**
- ❌ 为了刷新 AYA 桌面而强杀 → 杀掉 AYAWindow 的 `WindowKeyEventService`，KPA / Android 层系统按键全部失灵，只能关机重启恢复。
- ✅ 刷新用重启或等待；系统按键属于 KPA / Android / AYASetting / AYAWindow 层，**不要在 RetroArch 配置里找它**。排查按键问题先分清是「系统按键」还是「RA 游戏内按键」。

**2. 禁止把 libretro 核心 `.so` 推到 public 路径后指望加载**
- ❌ `adb push xxx.so /sdcard/RetroArch/cores/` → SELinux `avc: denied { execute }`，linker 报 `not accessible for the namespace`。
- ✅ 只有 `/data/data/com.retroarch.aarch64/cores/` 是 `avc: granted { execute }`；靠 APK 内置解包，或让 RA 核心下载器自己装。

**3. 禁止用 `run-as` / `adb root` / `su` / `adb backup` 操作 RA 私有数据**
- `package not debuggable` / production 拒绝 / 无 root / Android 12 `adb backup` 产出 0 字节。
- ✅ 迁移用 `scripts/sync_from_device.sh`（APK 从 `pm path` 拉）+ BIOS 单独拷。

**4. 禁止 `input tap` / 大部分 `input keyevent` 操作 RA ozone 菜单**
- 固件走内核 evdev 直读；`keyevent 66/23/96/97/20` 基本无效。
- ✅ `input motionevent DOWN x y` + 0.3s + `UP x y`（单击=移高亮，再单击=确认）；BACK(4)、方向键 19/20/21/22 有效。

## B. Pegasus 天马

**5. 禁止改 metadata / 新增目录后不清 `dataCache.json` 就判断生效**
- ✅ `rm /sdcard/pegasus-frontend/dataCache.json` → force-stop 重启 `org.pegasus_frontend.android` → 日志 `N games found` 才是准数。缓存会保留已删除游戏（幽灵条目）。

**6. 禁止靠改 `game_dirs.txt` 排除目录**
- 天马启动会重写回原样。
- ✅ 根治幽灵条目只能删掉那个被递归扫描的备份目录。

**7. 禁止整份覆盖 `metadata.pegasus.txt`**
- 云端与设备 ROM 数不匹配会丢游戏。
- ✅ 只就地 patch 启动命令 / 字段；改前留 `.before` 快照，改后清点条目数。

**8. 禁止 ANDROID 集合 `file:` 写 Android 组件名**
- ❌ `file: com.xxx/.MainActivity` → Pegasus 丢弃，表现为整个集合不显示。
- ✅ `extensions: app` + `file: <短名>.app`（真实占位空文件）+ 每个游戏一条 `launch: am start --user 0 -n <包名>/<Activity>`。

**9. 禁止改 `media-pack.bytes` / 往口袋博物馆 media-pack 加文件**
- 触发包校验失败并重下。ANDROID 集合缺图用第 8 条的占位法解决。

## C. RetroArch 配置与按键

**10. 禁止对竖版 cfg 整文件覆盖式改按键**
- ✅ 只精确替换 4 行方向：`up=h0right / down=h0left / left=h0up / right=h0down`；保留 `a=109 / b=108 / start=97 / select=96`、`video_rotation`、x/y 行。
- ✅ 禁止新建或污染核心级 `config/remaps/<核心>/<核心>.rmp`（会作用于该核心全部游戏）。历史上 21:14 的 rmp 污染了 A/B/X/Y，21:53 的 cfg 方向错误，都靠回轮解决。

**11. 禁止未经用户单点确认就批量推广按键/配置改动**
- ✅ 节奏：查历史结论 → 只改一个游戏 → 用户实机确认 → 再推广。「回轮」= 回滚到用户指定的时间点，不是重新生成一份。

**12. 禁止照搬 `video_rotation` 数值差异推导方向映射**
- MAME 2003-Plus `rot=1` 与 FBNEO `rot=3` 最终呈现一致（FBNeo 核心自带旋转叠加）。动手前先查历史结论，别用数值差异反推按键。

**13. 禁止手工在核心 cfg 写 `video_shader` 键**
- 会破坏 RA 自动预设加载链；改 `config/global_*.slangp` 一处即可覆盖上百个逐游戏预设。

**14. 禁止不带 `-e CONFIGFILE` 启动 RA 判断配置成败**
- 不带会读默认配置（中文变 `?`、菜单黑白），容易误判。GBA 启动命令禁止带 `--activity-clear-top`。

**15. 禁止批量「更新已安装核心」**
- 官方源约 17.5KB/s（手动下载卡在 14%）、nightly 非稳定版、与 219 个竖版 cfg / 遮罩 / CRT 配套有回归风险。
- ✅ 中断后的核查：看 `RetroArch/downloads/` 有无 zip 残留、`core_backups/` 有无 `.lcbk`、对 5 个核心冒烟；实测未覆盖任何核心。要更新单独点某一个。

**16. 禁止给 GBA 加遮罩**
- KPA 专为 GBA 设计，240×160 = 1.5 倍原生满屏 960×640，遮罩只会破坏画面。

**17. 禁止把存档/截图放 `/storage/6AF3-384F/save/`**
- RA 进程无 `sdcard_rw` 权限；只能放 TF 卡 `Android/data/<pkg>/files/`。

## D. PSP / 显示 / 判定

**18. 禁止 PSP ROM 只放 TF 卡或删掉 app 私有目录那份**
- PPSSPP targetSdk 35 无 `MANAGE_EXTERNAL_STORAGE`，读不到 TF 卡；双份均为必需，拷到 `/storage/emulated/0/Android/data/org.ppsspp.ppsspp/files/` 并 chmod 666。

**19. 禁止用 3.2 秒截图 / 单一亮度阈值 / 文件大小推断黑屏或封面质量**
- 冷启动 8–26 秒（PS 20s、ATOMISWAVE 20s、`PS/射雕英雄传.chd` 368MB 需 15s、MSX 15–18s、泰拉瑞亚/星露谷 15s）；首轮 27 DARK / 11 BLACK，8 秒复查后 23 个恢复。
- ✅ 先查前台窗口与 `ANR in com.retroarch.aarch64`；ANR 弹窗会造成非黑像素假阳性。中文 zip 条目名还会让 toybox `unzip` 误报 CRC BAD，本机 Python `zipfile` 复核为准。

**20. 禁止并行冒烟任务互相污染截图、禁止强杀 TMNT/Oceanhorn 后直接截图**
- 会留 ANR 弹窗，需 `input tap` 点「等待」清除后再截图。ANR 检测只匹配 `ANR in com.retroarch.aarch64`，否则会串到后台 APP。

## E. 清理与工程纪律

**21. 禁止在设备上留 `.bak*` 备份**
- 用户要求零备份；改动为覆盖式 / 幂等增量，回滚用 `sync_from_device.sh` 或重跑对应 step。
- 实际工程中确需保留的最小回滚点（`GameDetails.qml.bak20261113`、`firmware.bin.bak`）必须在清理清单里单列、经确认后处理。

**22. 清理前必须先出只读清单 + 影响说明并获用户确认**
- ✅ 列出路径 / 大小 / 删除理由 / 回滚点；设备删除无废纸篓，分批 ≤10 项、每批校验。本机删除用可恢复方式（废纸篓或隔离区）。
- 网络受限时不要假设 GitHub raw / bgm.tv / wikipedia / thegamesdb / screenscraper 可达；实测仅 `api.github.com` + gh-proxy + libretro thumbnails 可用（thumbnails 索引走 `git/trees?recursive=1`，contents 分页无效）。macOS adb 用 r34.0.5；大传输分块 55MB / 300 文件，`tar -T` 清单只放文件，校验用 `md5sum "路径"`（带双引号）。

## F. RA 输入注入与配置层级（v2.0.1 新增）

**23. 禁止假设 adb 能操作 RetroArch / 核心菜单**
- ❌ 反复试 `input keyevent 19/20/21/22`、`input gamepad|joystick|dpad|keyboard keyevent`、`input tap`、`input motionevent` 去点 RA 菜单或 DOSBox-pure 启动菜单 —— **RA 完全不接收**。它直接 poll `/dev/input/event*`，绕过 InputManager，注入的事件根本不进它的输入队列（实测四种 source 注入后截图逐像素完全相同）。
- ❌ `sendevent /dev/input/event3 ...` → `Permission denied`（shell 不在 `input` 组；`getevent` 同样读不到，无输出）。
- ✅ 唯一有效的是 `input keyevent 4`(BACK)，走 Activity 回调能呼出 RA 菜单。
- ✅ **天马(Pegasus) 是普通 Qt 应用、走 InputManager**，`input tap` / `input motionevent DOWN x y` + 0.3s + `UP x y` 对它有效。别把天马和 RA 的输入路径混为一谈 —— 这是本条最容易被误推的地方。
- ✅ 结论：RA 核心选项、DOSBox-pure 启动菜单（`→ Set Auto Start`）这类操作**只能人手完成**。脚本负责把"该改哪个文件、改成什么值"准备好，但不要承诺自动点菜单。

**24. 禁止用 per-playlist cfg 覆盖 OSD 开关**
- ❌ 新建 `config/Flycast/ATOMOSWAVE.cfg` 写 `video_font_enable = "false"` —— 实测无效，弹窗照旧显示。
- ✅ 写进该平台**每个 per-game** cfg：`config/Flycast/<游戏名>.cfg`，逐游戏生效（`kpa_gamefix.sh aw-osd` 批量处理）。
- 层级实测：全局 → per-core → per-game 都生效；per-playlist 对 `video_font_enable` 不生效（但 `aspect_ratio_index` 这类显示键在 `NAOMI.cfg` 里是生效的，不能一概而论）。

**25. 禁止在 `Roms/<平台>/` 放非 ROM 文件而不先收紧 extensions**
- ❌ 直接往 `Roms/DOS/` 放 `游戏名.conf` 想让核心自动加载 —— metadata 没有 `extensions` 时 Pegasus 按目录扫全部文件，立刻多出幽灵条目。
- ✅ 要么先给 metadata 加 `extensions: dosz`，要么把辅助文件放到 `Roms/` 之外。

**26. 禁止用设备端 unzip 改 `.dosz`**
- ❌ toybox `unzip` 遇中文条目名报 `Invalid entry name` / `couldn't open`，`unzip -l` 直接无输出。
- ✅ 本机 Python：`zipfile.ZipFile(p, 'a')` 只追加新条目（不重压几百 MB），改完 `z.testzip()` 返回 `None` 才算成功；先 `cp` 一份 `.orig` 到设备同目录，验证通过再删。
