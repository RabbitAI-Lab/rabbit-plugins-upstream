# 分项实操手册

## 1. Pegasus metadata 规范

文件位置 `<TF>/Roms/<平台>/metadata.pegasus.txt`（UTF-8）。头部与游戏块：

```txt
collection: CPS1
shortname: cps1
extensions: zip
launch: am start --user 0 -n com.retroarch.aarch64/com.retroarch.browser.retroactivity.RetroActivityFuture -e ROM "{file.path}" -e LIBRETRO /data/data/com.retroarch.aarch64/cores/fbalpha2012_cps1_libretro_android.so -e CONFIGFILE /storage/emulated/0/Android/data/com.retroarch.aarch64/files/retroarch.cfg

game: 1941 反击战
file: 1941.zip
assets.box_front: Imgs/1941 反击战.png
description: 《1941 反击战》，CPS1 平台街机射击游戏。
  第二行起缩进两空格可续写长简介。
publisher: CAPCOM
release: 1990
genre: 射击
players: 1-2
```

要点：
- `description:` 支持多行，后续行缩进两空格；留空则主题显示 `No description available`。
- `publisher / developer / release / genre / players` 影响 prosperoOS 详情页「More by 厂商」区块；16 个平台原本缺这些字段。
- per-game `launch:` 覆盖集合级 `launch:`，用于换核心（例：`mercsj / samuraia / sonicwi` 换 `fbneo_libretro_android.so`）或独立 APP（PSP 用 PPSSPP intent）。
- **改完必做**：`rm /sdcard/pegasus-frontend/dataCache.json` → 重启天马。

### ANDROID 移植游戏（关键）

`file:` 必须是真实文件，组件名会被丢弃：

```txt
collection: ANDROID
shortname: android
extensions: app

game: 忍者神龟：施莱德的复仇
file: tmnt.app
launch: am start --user 0 -n com.netflix.NGP.TMNTShreddersRevenge/crc64ce797c93931d6e91.MainActivity
assets.box_front: Imgs/忍者神龟：施莱德的复仇.png
```

用 `scripts/kpa_android_apps.sh` 创建占位文件并推送。已整合 7 个：忍者神龟 / 星露谷物语 / 泰拉瑞亚 / 像素足球19 / 小丑牌 / 海之号角 / 口袋博物馆。封面用 `adb exec-out screencap` 截启动画面生成。

## 2. RetroArch 配置分层（优先级从低到高）

| 层 | 路径 | 说明 |
|---|---|---|
| 全局 | `/storage/emulated/0/Android/data/com.retroarch.aarch64/files/retroarch.cfg` | 黑黄 ozone / vulkan / CRT / 96ms / 存档迁 TF / 官方核心源；**设备上存在两份，改要一起改** |
| 核心级 | `/sdcard/RetroArch/config/<核心名>/<核心名>.cfg` | 该核心全部游戏生效 |
| 全局着色器 | `/sdcard/RetroArch/config/global_*.slangp` | 改这一处可覆盖上百个逐游戏预设 |
| per-game | `/sdcard/RetroArch/config/<核心名>/<ROM名>.cfg` | 竖版旋转 / 方向映射写这里 |
| remaps | `/sdcard/RetroArch/config/remaps/<核心>/<核心>.rmp` | **厂商基线，禁止污染**（会作用于该核心全部游戏） |

`libretro_directory` 指向 `/data/user/0/com.retroarch.aarch64/cores/`，RA 从不读 public `RetroArch/cores/`。显示核查基线：`video_filter=""`（滤镜关）、`video_shader_enable=true` 命中 crt-easymode、厂商 `overlays/*_B.cfg` 边框正常、竖版 cfg 统一 `input_overlay_enable=false`。

## 3. 竖版游戏（219 个 cfg）

**最终统一值**（用户实机「1941 测试正常」）：

```ini
video_rotation = "1"          # MAME 2003-Plus / VARCADE；FBNEO 系填 "3"
aspect_ratio_index = "0"
video_scale_integer = "false"
input_overlay_enable = "false"
input_player1_up_btn = "h0right"
input_player1_down_btn = "h0left"
input_player1_left_btn = "h0up"
input_player1_right_btn = "h0down"
input_player1_a_btn = "109"
input_player1_b_btn = "108"
input_player1_start_btn = "97"
input_player1_select_btn = "96"
```

- 厂商原版基线是反的：`up=h0left / down=h0right / left=h0down / right=h0up`（69 个 FBNEO cfg 字节级一致，md5 `44950e1a…`）。**翻转时只精确替换 4 行方向**，其余原样。
- 分布（2026-11-13 实测）：`MAME 2003-Plus` 140（rot=1）、`FinalBurn Neo` **72**（rot=3）、CPS1 3 / CPS2 2 / NEOGEO 2（rot=3），合计 **219**，方向映射 219/219 全部正确。早期文档写 216（FBNeo 69），差 3 个是后续补入，属口径漂移不是故障。
- 竖版判定用 `assets/data/mame_orient.json`（6055 条），DB 缺的 4 个补 `gekiridn / tengaij / p47mus / schmeisr`。
- 修已有 cfg 用 `bash scripts/kpa_vertical.sh`（默认 dry-run，`--apply` 才写）。

## 4. MSX blueMSX 核心（本地镜像法）

APK 未内置 bluemsx/fmsx；官方源约 17.5KB/s，手动下载会卡在 14%。步骤：

1. 拿到 `bluemsx_libretro_android.so`（可从已安装设备的私有目录或 RA 官方 zip 解出）。
2. 建最小核心源目录：`zip -j bluemsx_libretro_android.so.zip <.so>`，并造 `.index-extended`（**不是 `.index`**）：
   ```txt
   2026-11-10 3f68b86d bluemsx_libretro_android.so.zip
   ```
   格式每行 `日期 哈希 文件名`。只有 `.index` 时 RA 列表显示「没有可显示的条目」。
3. Mac 起 `python3 -m http.server 8765 --bind 0.0.0.0`（目录即核心源目录）。
4. 临时把**两份** `retroarch.cfg` 的 `core_updater_buildbot_cores_url` 改成 `http://<Mac 局域网 IP>:8765/`。
5. RA 菜单：在线更新 → 核心下载 → BlueMSX —— **必须人手在掌机上点**。实测 adb 注入的 `input` 事件 RA 完全收不到（`sendevent` 亦无权限），详见 HARD_RULES 第 23 条。RA 自己下载并解压到私有 cores 目录。
6. 验证 logcat `avc: granted { execute } .../cores/bluemsx_libretro_android.so`；**装完把两份 cfg 改回官方源 `http://buildbot.libretro.com/nightly/android/latest/arm64-v8a/` 并关掉 HTTP 服务**。
7. MSX metadata 加 launch 行指向该核心；BIOS 在 `/storage/emulated/0/RetroArch/system/`（MSX.rom / MSX2.rom + Machines / Databases）。

MSX 冷启动约 15–18 秒出日文字符界面，不是黑屏。脚本见 `scripts/kpa_msx_core.sh`。

## 5. `.nomedia`（图库隐藏）

加 4 个目录，不删文件、不影响天马按路径读封面：

```txt
/storage/6AF3-384F/Roms/
/storage/emulated/0/RetroArch/
/storage/emulated/0/pegasus-frontend/
/storage/emulated/0/Android/data/com.pocketmuseum.app/
```

重扫：`content call --uri content://media --method scan_volume --arg external_primary`。内部存储立即生效（RetroArch 1105→1、pocketmuseum 20002→1），TF 卡卷 `public:179,129` 重扫不生效，**需重启一次**。脚本见 `scripts/kpa_nomedia.sh`。

## 6. 详情页 `GameDetails.qml` 增强

视觉根因：`gamedetails` 是 mainList 第 2 页（需按 ↓），未选中 `opacity: selected ? 1 : 0.5`、标题 `vpx(24)`、简介 `vpx(18)`、`elide: Text.ElideRight` 截断长文、无背景卡片。

增强版 `assets/golden/GameDetails.improved.qml.txt`：opacity 0.5→0.85、加半透明卡片 + 橙色强调条、标题 24→30、简介 18→25、去掉 elide、`lineHeight: 1.3`、左右 margin。固定色写法（不要用 `theme.highlight || ...`，该主题未定义会回退失败）。

原版回滚点 `assets/golden/GameDetails.before.qml.txt`（设备侧 `.bak20261113`）。推送后清 `dataCache.json` 重启，检查 logcat 无 QML/QQml 报错。**RA 完全不接收 adb 注入的输入**（见 HARD_RULES 23），所以详情页观感只能在掌机上目视确认。脚本见 `scripts/kpa_gamedetails.sh`。

内容侧：3772 条 description 平均 46.3 字，约 30%（1142 条）是「《X》，X 平台。」空壳句；用 `scripts/bangumi_desc.py` 升级为真简介并回填 16 个平台的 publisher/genre/release。

## 7. 封面修复链路

坏封面三来源：黑屏图（抓图失败）、小图（<8KB）、缺图。按顺序：

1. zip 内部文件名（汉化 ROM 的原版英文名）→ `https://thumbnails.libretro.com/<系统>/Named_Boxarts/<名>.png` 匹配；系统名形如 `MAME`、`SNK - Neo Geo`、`Bandai - WonderSwan`、`Sega - Game Gear`、`Nintendo - Game Boy Color`。
2. 匹配不到 → RA 实机截图：`am start` 带核心参数 → 等 15–40s → `screencap` → PIL 裁掉 RA 边框缩放 480×320。
3. 三核心全黑 → 标题文字占位图。
4. EASYRPG 特例：从游戏目录 `.xyz` 标题画面按 `xyzpal_first / xyzpal_last` 调色板解码，重做 13 张真封面（Mogeko城堡 / 威伦诺尔 / 寂静岭 / 废都物语 / 怪异症候群1-2 / 恐怖美术馆 / 梦幻重装机兵 / 灰色庭院 / 野比大雄系列 4 作），部署到 `Roms/EASYRPG/Imgs/` 并 md5 校验。

## 8. 冷启动等待基准（冒烟判定）

| 平台 / 游戏 | 出画面时间 |
|---|---|
| PS / SATURN / N64 / MD / SFC / NDS | 8–20s |
| `PS/射雕英雄传.chd`（368MB） | 15s |
| ATOMISWAVE | 20–30s（首屏 NOTICE 版权屏，不是不兼容） |
| MSX | 15–18s |
| 泰拉瑞亚 / 星露谷物语 | 15s |

3.2 秒截图会得出大量假黑屏。判定顺序：前台窗口 → `ANR in com.retroarch.aarch64` → 非黑像素 + 外接矩形 → 再下结论。

## 9. 网络与传输实测

- 可用：`api.github.com`、gh-proxy 镜像、libretro thumbnails。thumbnails 目录索引走 `git/trees?recursive=1`，`contents` 分页无效。
- 不可假设可达：GitHub raw、bgm.tv、wikipedia、thegamesdb、screenscraper。
- macOS adb r34.0.5；大传输分块 55MB / 300 文件；`tar -T` 清单只放文件；校验用 `md5sum "路径"`（中文路径必须带双引号）。

## 10. 实机体验类修复（v2.0.1）

用户实测反馈的六类问题，全部已定位根因并修复。脚本：`scripts/kpa_gamefix.sh`（配置类）+ `scripts/kpa_theme_tweak.py`（主题类），都幂等、支持 `--revert`。

| 现象 | 根因 | 修法 |
|---|---|---|
| DOS 左下角反复刷 `Save State Error` | 全局 `rewind_enable=true` + `savestate_auto_save=true`，而 DOSBox-pure 进来先停在 START MENU、游戏尚未运行 | 只在 `DOSBox-pure.cfg` 关这两项（不影响其它平台倒带） |
| NDS 双屏被纵向拉长、画面被裁 | `melonds_screen_layout="Left/Right"` + `aspect_ratio_index="23"`，两屏并排后又被拉满屏 | 改 `Top/Bottom` + index **21** |
| Atomiswave 背景满屏雪花噪点 | flycast 多线程渲染在 Atomiswave 下有 bug | `reicast_threaded_rendering="disabled"` |
| Atomiswave 左下角 `Please upgrade to MAME romsets` | 核心对旧格式 romset 发 `SET_MESSAGE`，RA 以 OSD 显示数秒 | 每个 **per-game** cfg 写 `video_font_enable="false"` |
| 顶部平台名太小、看不出当前平台 | 字号 24 且选中/未选同色 | delegate 字号 36、选中 `#ffffff` / 未选 `#6affffff` |
| 退出游戏回到平台第一个而非刚才那个 | 2.96GB RAM 下天马被 LMK 回收，重启后只记 `Last Collection` | 记 `Last Game` + `restoreLastGame()` + 电池白名单 |

### 10.1 主题平台条为什么"一直存在却看不见"

`theme.qml` 里 `collectionNav` 写的是 `visible: false`，但它被 `OpacityMask` 的 `ShaderEffectSource` 当作纹理源渲染 —— **平台条其实一直在显示**，只是 `font.pixelSize: vpx(24)` 且所有项同为 `white`（选中项只换字体族，差别极小）。

所以正确改法是只动 delegate 的 `font.pixelSize` 与 `color`（外加 `opacity: gameBar.active ? 1 : 0` → `1` 让它常显）。

⚠️ **不要新造一个"平台名大标题"控件** —— 实测会与遮罩渲染出的那层重叠，出现双层错位文字。

### 10.2 NDS 双屏比例怎么客观定

不要靠肉眼。用截图数"亮像素外接矩形宽度"：

```python
# 960×640 截图，隔点采样后取非黑区域的 x/y 范围
```

实测同一标题画面：`aspect_ratio_index` 为 **21 / 22** 时亮像素宽约 **408px**（核心原始比例，左右留黑边，文字不变形）；为 **23 / 24** 时拉到 **918px**（满屏，纵向变形）。`Hybrid` 布局该核心不支持 —— 设了与 `Top/Bottom` 截图逐像素相同。

### 10.3 一条走不通的路：DOS 自动跳过启动菜单

想省掉每次进 DOS 都要在 `DOSBOX PURE START MENU` 里选程序，试过全部常规路线，**均无效**：

1. `dosbox_pure_conf` 改 `"true"` / `"1"` / `"2"` / 完整 label 四种值 —— 都仍停在菜单；
2. 在 `.dosz` 旁放同名 `.conf`（`[autoexec]` + `PLAY.BAT`） —— 无效；
3. 用 Python 往 `.dosz` 内追加 `DOSBOX.CONF`（CRC 自检通过） —— 无效；
4. 用 `input keyevent` 在菜单里按「→ Set Auto Start」 —— RA 收不到事件（HARD_RULES 23）；
5. `sendevent` 直写 evdev —— `Permission denied`。

**结论：这一步只能人手做。** 操作路径：进游戏 → 菜单出现 → 用 ↓ 移到 `PLAY.BAT` → 按 **→**（`Set Auto Start`）→ 该项出现标记，下次跳过菜单。想恢复菜单：在核心菜单选 Restart 时按住 L2/R2。

15 个 DOS 包的启动项（已逐个解包确认，全部含 `PLAY.BAT`）：

| 游戏 | 启动项 | 实际执行 |
|---|---|---|
| 仙剑奇侠传 | PLAY.BAT | PAL |
| 轩辕剑外传-枫之舞 | PLAY.BAT | SWDA |
| 高校魔影 | PLAY.BAT | g_map |
| 大唐英雄传 / 明星志愿 / 毁灭战士2 | PLAY.BAT | — |
| 炎龙骑士团 / 炎龙骑士团2 | PLAY.BAT | FD / FD2 |
| 英雄传说3-白发魔女 | PLAY.BAT | ED3 |
| 金庸群侠传 | play.bat | — |
| 魔影哈雷 / 魔神战纪2 / 魔胎 / 鹿鼎记 / 龙骑士4 | PLAY.BAT | — |
