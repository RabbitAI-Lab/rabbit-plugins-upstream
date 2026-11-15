# KPA 掌机 天马(Pegasus) + RetroArch 游戏库搭建与优化工程复盘

> 本文为**只读复盘**：基于会话记录、memory、工作区脚本/报告、现有 skill 归纳而成，**未修改任何设备或现有 skill**。
> 资料来源：
> - 会话 JSONL `~/.workbuddy/projects/Users-lis-WorkBuddy-2026-11-11-21-32-58/2d636885-33ed-4b6d-951c-c528ff0a845f.jsonl`（36MB / 9091 行；流式解析出 118 条 user 消息、941 条 assistant 结论、2229 条关键命令）
> - `.workbuddy/memory/2026-11-11.md`、`2026-11-12.md`、`2026-11-13.md`
> - 工作区 `kpa-deploy/`（执行记录 + 部署脚本）、`kpa-backup/2026-11-13/{audit,health,theme,edit,...}`（验证报告与回滚点）、`kpa-meta-work/`
> - 现有 skill `~/.workbuddy/skills/kpa-game-setup/SKILL.md` 及 `scripts/`、`assets/`

---

## 0. 工程概览

| 项 | 值 |
|---|---|
| 设备 | **KONKR Pocket ADVANCE**（KPA，说明书正式名；现有 skill 里误写为 "AYANEO Pocket Advance"），GT78_VN，Android 12，arm64-v8a，SN `[DEVICE_SN]` |
| 屏幕 | 960×640（3:2），无实体摇杆、无 L3/R3，约 17 个按键元件；自定义键由 AYASetting / AYAWindow 的 `WindowKeyEventService` 解释 |
| 存储 | TF 卡 `/storage/6AF3-384F`（62.5G exFAT）；内部 `/storage/emulated/0`；RA 私有 `/data/data/com.retroarch.aarch64/` |
| 前端 | 定制版 Pegasus（alpha16，包名 `org.pegasus_frontend.android`），最终主题 prosperoOS（PS5 风格） |
| 后端 | RetroArch `1.22.2_GIT`（`com.retroarch.aarch64`，783MB APK 内置 83 核心）+ PPSSPP 1.19.3 独立版 |
| 周期 | 2026-11-11 21:36 → 11-13 02:00（跨 3 天，约 28 小时；会话压缩记录延续至 06:40） |
| 规模 | 36 平台 / 约 3770–3773 游戏条目；36 份 `metadata.pegasus.txt`；216 个竖版 per-game cfg；27 个 libretro 核心 + 8 个独立 APP 全部冒烟通过 |

---

## 1. 阶段划分（按时间 / 主题）

### 阶段 P1 — 打通链路与首批定制包（11-11 21:36 → 23:56）

- **目标**：从零建立 adb 通道、取回两份百度网盘定制包、修掉「启动游戏中间横屏加载」、落地 RA 定制配置与主题设置。
- **执行动作**：下载 platform-tools 到 `tools/`；网盘通匿名探测→官方扫码登录拿 BDUSS 注入 CookieJar（`~/.kpa-baidu-cred.json`，0600）；下载 2.98GB 定制包并解出 3.6GB / 42982 文件，按需推送 `RetroArch/{system,config,overlays,cheats}`、`pegasus-frontend/themes`、`DraStic/PSP/M64PlusFZ`；就地 patch GBA 启动命令。
- **关键命令 / 路径**：
  - `am start --user 0 -n com.retroarch.aarch64/com.retroarch.browser.retroactivity.RetroActivityFuture -e ROM ... -e LIBRETRO /data/data/com.retroarch.aarch64/cores/mgba_libretro_android.so -e CONFIGFILE /storage/emulated/0/Android/data/com.retroarch.aarch64/files/retroarch.cfg`
  - 云端 `retroarch.cfg` → 两份路径；`MSYH.TTF`（macOS Arial Unicode 子集化 8.1MB）→ `/sdcard/RetroArch/`
  - `/sdcard/pegasus-frontend/settings.txt` 的 `general.theme` → `themes/pegasusG-Grid/`
  - 备份 `kpa-deploy/backup-20261111-215838/`、`backup2-20261111-222333/`
- **结果**：黑黄 ozone 菜单 + 中文正常；确认「横屏加载」根因 = `--activity-clear-top` 强制 RA 冷启；GBA 改 mGBA 且去掉该参数；**未整份覆盖**云端【3】游戏列表（458 条 vs 设备 429 ROM 仅 403 命中，整替会丢 26 个游戏）。产物 `KPA优化执行记录-20261111.md`、`-第二批-20261111.md`。

### 阶段 P2 — 全平台滤镜 / 遮罩 / 封面 / 核心体系（11-11 23:56 → 11-12 09:10，第 3~11 批）

- **目标**：逐平台「满屏/满高 + 主机主题遮罩 + 最佳滤镜」、关虚拟键、补入口、删冗余、补 GBA 封面、竖屏初探。
- **执行动作**：摸清 RA 自动预设链；修复多处「核心显示名 ≠ .so 名」错配；FC 换 B 方案（平铺 CRT + 整屏贴图遮罩）并推广到全平台；`pm path` + `grep -a 'assets/cores/'` 列出 APK 内置 100 核心，据此复活 DOS/GW/EASYRPG/PICO 入口；删 14 个空目录；卸载 DraStic/OpenBOR/GW/M64PlusFZ；补 GBA 426 张封面（libretro thumbnails + 口袋博物馆 `catalog.sqlite` 中英对照 + PIL 文字卡）；装 3 个安卓游戏。
- **关键命令 / 路径**：`kpa-deploy/gen_frames.py`、`gen_frames2.py`、`deploy_b.py`、`deploy_b2.py`、`scrape_covers.py`；`overlays/<平台>_B_frame.png` + `<平台>_B.cfg`；`config/global_<平台>.slangp` 改单行 `#reference ".../crt/crt-easymode.slangp"`；`config/<核心显示名>/<核心显示名>.slangp`。
- **结果**：`game_dirs.txt` 33→36；确认 `aspect_ratio_index` 语义（0=4:3 / 7=3:2 / 23=Core Provided / 24=Custom）；4:3 平台统一 853×640 满高；街机 MAME/VARCADE/FBNEO 用 23 原生比例不加遮罩（竖版游戏强制 4:3 会压扁）；GBA 3:2 原生满屏不遮罩；GW 因竖握外壳无法全屏按用户要求删除。产物 `KPA-第三批-全平台遮罩与封面-20261112.md`。

### 阶段 P3 — 主题 / 封面 / 详情页 / 简介 / PSP / MSX 专项（11-12 09:10 → 17:58）

- **目标**：解决世嘉「透明遮挡」、PSP 天马直启、prosperoOS 主题、MSX 黑屏、封面/详情页/简介、全平台核心实测。
- **执行动作**：清空 `global_MD/SATURN/DC*.slangp` 与 Gearsystem 滤镜链（crt-easymode 在 960×640 上网点雾感，用户选「无滤镜」）；PSP ROM 双份拷入 PPSSPP app 私有目录 + 逐游戏 launch；装 prosperoOS（master 分支）并修补 `assets.logo || assets.boxFront` 回退、封面放大、潜水员戴夫背景；MSX 根因定位为缺 bluemsx 核心（BIOS 齐全）；封面坏图三来源修复；详情页 description 字段 + dataCache 缓存机制；生成 3773 条模板中文简介。
- **关键命令 / 路径**：`rm /sdcard/pegasus-frontend/dataCache.json` 后重启；`/storage/emulated/0/Android/data/org.ppsspp.ppsspp/files/PSP/SYSTEM/ppsspp.ini`（`DisplayStretch=True` 带空格、`ShowTouchControls=False`）；`/sdcard/pegasus-frontend/themes/prosperoOS/`；`assets/meta_latest/*.txt`。
- **结果**：24 核心逐一实测可加载；ATOMISWAVE「不兼容」被纠正为误判（裸 .bin 可玩，NOTICE 屏 20-30s）；prosperoOS 实机验证通过；详情页与中文简介正常显示；模板简介元数据 +380KB。

### 阶段 P4 — KPA Skill 沉淀与上架瘦身（11-12 13:00 → 17:58）

- **目标**：把整套部署固化为幂等 skill，并瘦身为可分发的上架版。
- **执行动作**：建 `~/.workbuddy/skills/kpa-game-setup/`（初版 1.3G：三 APK + 修补主题 zip + RA config/overlays tar 140M + system BIOS tar 396M + `mame_orient.json` + `platform_cores.tsv` + 7 个 step 脚本 + `run_all.sh`）；两轮本机冒烟全 SKIP/OK；按用户决定删设备全部 `.bak*`、删 9 个旧主题（552M）、skill 瘦身到 3.4M（step1 改官方渠道下载 + gh-proxy 回退、BIOS 走 `assets/data/bios_list.txt` 清单、新增 `sync_from_device.sh`）。
- **结果**：产出上架版 `SKILL.md`（含 12+ 条实测关键技术事实）、`assets/golden/`（retroarch.cfg/settings.txt/ppsspp.ini/game_dirs.txt/戴夫壁纸/主题 zip）、`assets/meta_latest/` 36 平台最新元数据、`scripts/bangumi_desc.py`。

### 阶段 P5 — 系统按键溯源与竖版方向回轮 / 推广（11-12 21:23 → 23:56）★ 三次纠正集中区

- **目标**：修「系统按键被改」「EASYRPG 封面不对」「竖版按键不对」「MSX 核心」「移植游戏没进天马」；随后聚焦竖版方向。
- **执行动作**：读说明书 + 溯源全历史命令定位系统按键失灵；按用户要求回轮 21:23 那轮按键改动；23:03 代用户启游戏验证 → 23:06/23:08 试改 → 23:09 回轮 → 23:13 只改一个 → 23:20 推广 → 23:23 查历史纠正 rot 误判 → 23:28 跨平台 147 个翻转 → 23:47 移除 galaga。
- **关键命令 / 路径**：`kpa-backup/2026-11-12-2245/`（vendor 基线 `argus.cfg.vendor`、翻转模板 `airattck_flipped.cfg` / `mame_flipped.cfg`、`cfg_before_promote/`、`cfg_before_cross_platform/`、`galaga_removal/`）；`/storage/emulated/0/RetroArch/config/{FinalBurn Neo,MAME 2003-Plus,CPS1,CPS2,NEOGEO}/`；`config/remaps/FinalBurn Neo/FinalBurn Neo.rmp`。
- **结果**：**216 个竖版游戏方向统一为 `up=h0right / down=h0left / left=h0up / right=h0down`**，23:42 用户实测「1941 测试正常」收尾；系统按键经用户关机重启恢复。详见第 3 节。

### 阶段 P6 — 收尾四项决定与 MSX 本地镜像安装（11-13 00:00 → 01:35）

- **目标**：解决长期阻塞的 MSX 核心、`.nomedia`、QML 增强推送、坏 ROM/换核心、ANDROID 集合修复、EASYRPG 封面重做、抽样验证。
- **执行动作**：用户手动下载 blueMSX 卡在 14%（官方源 17.5KB/s）→ 用「方案 C 本地 HTTP 核心源」成功安装；加 4 个 `.nomedia` + `scan_volume`；推送 `GameDetails.improved.qml.txt`；移除 CPS1/dynwarjr、SFC/超级炸弹人4，mercsj/samuraia/sonicwi 换 fbneo 核心 + 补竖版 cfg；ANDROID 集合改 `.app` 占位；EASYRPG 13 张封面从 `.xyz` 标题画面解码重做；113 个样本全平台抽样验证。
- **关键命令 / 路径**：`python3 -m http.server 8765 --bind 0.0.0.0` + 临时改两份 `retroarch.cfg` 的 `core_updater_buildbot_cores_url` → `http://192.168.x.x:8765/`；`input motionevent DOWN x y` + 0.3s + `UP x y`；`audit/probe.py`、`KPA_verification_report.html`、`KPA_changes_2026-11-13.html`。
- **结果**：任务 #5/#25/#30–#33 全部 completed；`3771 games / 36 collections`；MSX 冷启动 ~15s 出日文界面；图库噪音内部存储消失。

### 阶段 P7 — 全量达标检查与清理只读盘点（11-13 01:39 → 02:00）

- **目标**：全量静态校验 + 逐核心/独立 APP 冒烟 + 清理清单（用户要求「清理前先确认目录及影响」）。
- **执行动作**：`health/static_check.py`（3770 条非抽样）、`health/core_probe.py`（39 测试点）、1443 个 zip CRC、`health/cleanup_inventory.py`。
- **结果**：**27/27 核心 `core_executed=yes` + 8/8 独立 APP 前台正常**；ROM/封面/简介零缺失；产出 `KPA_health_check.html`（342KB）、`KPA_cleanup_plan.html`；**按安全规则本轮只出清单 + 警告，未执行任何删除**，#38 保持 in_progress 等待确认。

---

## 2. 关键技术结论

### 2.1 Pegasus metadata / dataCache.json / game_dirs.txt / `.app` 占位 + per-game launch

- **metadata 格式**：头部 `collection / shortname / extensions / launch`，每游戏一个块：`game: / file: / launch: / assets.box_front: / description:`；`description:` 多行值后续行缩进两空格。支持 publisher / developer / release / genre / players 字段，prosperoOS 详情页「More by 厂商」区块依赖它们。
- **内容源**：libretro-database 的 31 个平台 `.rdb`（msgpack，magic `RARCHDB` + 16B 头）+ metadat CLRMAME dat（`publisher/releaseyear/genre/users` 字段，非 `comment`），命中 2906/3744（77%）；街机按 zip 名=romset、家用机按 local header 偏移 14 的 crc32 匹配；后补 3773 条模板中文简介。
- **dataCache.json（定制版 Pegasus alpha16 的元数据缓存）**：直接改 metadata 后重启**不生效**（日志 `Cache loaded successfully`）。**任何 metadata / 新增目录改动后必须 `rm /sdcard/pegasus-frontend/dataCache.json` 再 force-stop 重启 `org.pegasus_frontend.android`**。缓存会保留已删除游戏；游戏总数以清缓存后重建的 `N games found` 为准。
- **game_dirs.txt**：曾 33→36→39→36；**天马启动时会把它重写回原样**（01:56 实测恢复成 1096 字节），改它排除目录无效；根治幽灵条目必须删掉备份目录本身。
- **`.app` 占位 + per-game launch（ANDROID 移植游戏整合）**：Pegasus 需要一个真实存在的文件才会建游戏条目。做法 = `collection: ANDROID` + `extensions: app` + 创建 7 个真实占位文件（如 `tmnt.app`，内容 `android app launcher placeholder`）+ 每游戏 `file: <名>.app` + `launch: am start --user 0 -n <包名>/<Activity>` + `assets.box_front: Imgs/<名>.png` + `description:`。7 游戏：忍者神龟施莱德的复仇 / 星露谷物语 / 泰拉瑞亚 / 像素足球19 / 小丑牌 / 海之号角 / 口袋博物馆（Godot）。封面用 `adb exec-out screencap` 截启动画面生成 480×320。**之前「移植游戏没进天马」就是缺真实 `.app` 占位文件**。
- 详情页入口：顶栏 GameBar 选中游戏卡片即进入；`keys.details`（I/GamepadSelect/GamepadX）在 Explore 视图下不稳定。

### 2.2 RetroArch 配置分层

```
全局   /storage/emulated/0/Android/data/com.retroarch.aarch64/files/retroarch.cfg
       （+ /sdcard/RetroArch/ 副本，两份需一致）
       menu_driver=ozone / ozone_menu_color_theme=3(黑黄) / video_driver=vulkan
       video_shader_enable=true（且无 video_shader 键）/ video_filter="" / 音频延迟 96ms
       savefile/savestate/screenshot → TF 卡 app 专属 Android/data/<pkg>/files/{saves,states,screenshots}
  ↓
核心级 config/<核心显示名>/<核心显示名>.cfg   （aspect_ratio_index / custom_viewport / input_overlay）
       .opt    （core options，如 mame2003-plus_tate_mode="enabled"）
       .slangp （shader 预设，#reference "../global_<平台>.slangp"）
  ↓
per-game config/<核心显示名>/<游戏名>.cfg      （video_rotation / 四向 remap / ABXY+START/SELECT / input_overlay_enable=false）
  ↓
remaps config/remaps/<核心>/<核心>.rmp        （核心级 remap，作用于该核心【所有】游戏）
```

- **自动预设加载**：全局 `video_shader_enable=true` 且**无** `video_shader` 键时，RA 自动按 `config/<核心显示名>/<核心显示名>.slangp` → `config/<核心显示名>/<游戏名>.slangp` 套用；**不要手工写 `video_shader`**。预设内 `BORDER` 相对路径基准 = slangp 所在目录（`global_*` 用 `../overlays/`，核心目录内用 `../../overlays/`）。
- **核心显示名 ≠ .so 文件名**，错一个字母整条滤镜链静默失效：`mednafen_pce_fast→Beetle PCE Fast`、`mame2003_plus→MAME 2003-Plus`、`fbalpha2012_neogeo→FB Alpha 2012`（无 Neo Geo 后缀）、`stella2023→Stella 2023`。
- 遮罩两套：`input_overlay`（GB/GBC/GG/NGP 掌机外壳，`overlay0_descs=0` 纯贴图）与 shader `BORDER` / 整屏 `*_B.cfg` 贴图（FC/SFC/MD/PS1/DC/街机）；`aspect_ratio_index` 语义 0=4:3 / 7=3:2 / 23=Core Provided / 24=Custom。
- **优先级 per-game > 核心级 > 全局**。局部问题只改 per-game 的 4 行，**不要整文件覆盖**；核心级 `.rmp` 一旦污染会波及全部游戏（见 3.2）。
- **ROM 直启模板**（与天马 launch 一致，用于自动化验证）：
  ```
  am start --user 0 -n com.retroarch.aarch64/com.retroarch.browser.retroactivity.RetroActivityFuture \
    -e ROM '<TF>/Roms/<平台>/<游戏>.zip' \
    -e LIBRETRO /data/data/com.retroarch.aarch64/cores/<核心>_libretro_android.so \
    -e CONFIGFILE /storage/emulated/0/Android/data/com.retroarch.aarch64/files/retroarch.cfg
  ```
  不带 `-e CONFIGFILE` 会读默认配置（中文变 `?`、菜单黑白）——**不要用它判断配置成败**。GBA 定制版 = mGBA 核心 + 无 `--activity-clear-top`。

### 2.3 Android SELinux 拒绝 public 路径 `.so` 执行，只有 app 私有 cores/ 可用

- Android linker namespace 的 `permitted_paths` 实测仅 `/data:/mnt/expand:/data/user/0/com.retroarch.aarch64`；从 `/storage/emulated/0`（含 `Android/data/<pkg>`）、`/data/local/tmp` dlopen 全部被拒（"not accessible for the namespace"）；SELinux 对 public / shell 路径 `.so` 是 `avc: denied { execute }`，对 app 私有 `/data/data/com.retroarch.aarch64/cores/` 是 `avc: granted { execute }`（PS/swanstation 日志为证）。
- `run-as`（package not debuggable）/ `adb root`（production 拒绝）/ `su` 全不可用；直接写私有目录 Permission denied；`adb backup` 在 Android 12 产出 0 字节，不能迁移私有数据。
- **结论：核心 .so 不可推送、不可远程写，只能靠 APK 内置解包（RA APK 内置约 83 核心，覆盖全部平台唯缺 MSX）或让 RetroArch 自己下载/安装到私有 cores 目录。**
- 附带：PPSSPP targetSdk 35 无 `MANAGE_EXTERNAL_STORAGE`，读不到 TF 卡 ROM，**必须把 PSP ROM 拷一份到 `/storage/emulated/0/Android/data/org.ppsspp.ppsspp/files/` 并 chmod 666，与 TF 卡双份均为必需勿删**；RetroArch 无 PPSSPP 核心（加载即崩）。

### 2.4 竖版方向映射规则

- **最终全机 216 个竖版 per-game cfg 统一为**：
  ```
  up=h0right  down=h0left  left=h0up  right=h0down
  ```
  即「右→上、左→下、上→左、下→右」（用户最初描述的规则）。
- **厂商原版基线（69 个 FBNEO cfg 字节级一致，md5 `44950e1a…`）**：`up=h0left / down=h0right / left=h0down / right=h0up`；`a=109(SELECT→A) / b=108(START→B) / start=97(B→START) / select=96(A→SELECT)`；无 x/y 行（沿用全局 x=99/y=100）；`video_rotation=3`。翻转时**只精确替换 4 行方向**，a/b/start/select 与 rotation 全部原样。
- **216 个分布**：`MAME 2003-Plus` 140（rot=1）、`FinalBurn Neo` 69（rot=3）、CPS1 3 / CPS2 2 / NEOGEO 2（rot=3）。竖版判定用 `assets/data/mame_orient.json`（6055 条），DB 缺的 4 个补充 `gekiridn / tengaij / p47mus / schmeisr`。
- **MAME `rot=1` 与 FBNEO `rot=3` 呈现一致**：FBNeo/fbalpha 核心自带自动旋转叠加，RA 叠加用户旋转后与 MAME 2003-Plus 效果相同（文字顶部朝右、满屏横躺）。**不能照搬数值差异推导方向映射**（历史误判，见 3.3）。
- ⚠️ **现有 `SKILL.md` 第 52 行仍写厂商原版 `up=h0left …`，与设备最终状态（翻转版）不一致，需同步更新**。

### 2.5 MSX blueMSX 本地镜像 + `.index-extended` 安装

- 长期阻塞根因：APK 未内置 bluemsx/fmsx；用户手动下载卡在 14%（官方源实测 17.5KB/s，740KB zip 数分钟下不完）。
- **关键新知识**：RA 核心下载器读的是 `<cores_url>.index-extended`，**不是 `.index`**；格式每行 `日期 哈希 文件名`（例 `2026-11-10 3f68b86d bluemsx_libretro_android.so.zip`）。只有 `.index` 时列表显示「没有可显示的条目」。`core_updater_buildbot_cores_url` 正确值是 `.../nightly/android/latest/arm64-v8a/`（含 `latest/`）。
- **方案 C（已成功）**：把设备上已有 `.so`（md5 `32be4188…`）用 `zip -j` 打成 `bluemsx_libretro_android.so.zip`，造最小 `.index` + `.index-extended`；Mac 起 `python3 -m http.server 8765 --bind 0.0.0.0`；临时把**两份** `retroarch.cfg` 的 URL 改成 `http://192.168.x.x:8765/`；RA 在局域网秒下并自己解压到私有 cores 目录；装完把 cfg 改回官方源、关 HTTP 服务。
- **UI 导航**：`input tap` / `keyevent 66,23,96,97,20` 对 ozone 菜单基本无效，只有 `keyevent 4`(BACK) 有效；**`input motionevent DOWN x y` + 0.3s + `UP x y` 才可靠**（单击=移高亮，再单击=确认）。主菜单「在线更新」(430,334) → 子菜单「核心下载」(430,104)。
- 验证：logcat `avc: granted { execute } .../cores/bluemsx_libretro_android.so`；17 秒后出 MSX 日文字符界面（**MSX 冷启动约 15 秒，不是黑屏**）。备份 `kpa-backup/2026-11-13/msx_mirror/`、`msx_cfg_backup/retroarch.cfg.ORIGINAL_URL`。

### 2.6 `.nomedia`

- 全存储 30136 张图片，`Roms/` 与 `RetroArch/` 下原本没有 `.nomedia` → 封面/素材全被 MediaStore 扫进图库；20002 张来自 `com.pocketmuseum.app`（该目录原本也**没有** `.nomedia`，此前判断有误）。
- 加 4 个目录：`/storage/6AF3-384F/Roms/`、`/storage/emulated/0/RetroArch/`、`/storage/emulated/0/pegasus-frontend/`、`/storage/emulated/0/Android/data/com.pocketmuseum.app/`。**不删文件、不影响天马按路径读封面**。
- `content call --uri content://media --method scan_volume --arg external_primary` 有效：内部存储 RetroArch 1105→1、pocketmuseum 20002→1（约 2.1 万张立即从图库消失）；`/sdcard/Pictures` 9 张保持可见。**TF 卡卷 `public:179,129` 重扫不生效，需重启一次**才消失。

### 2.7 `GameDetails.qml` 详情页增强

- 视觉根因：`gamedetails` 是 mainList 第 2 页（需按 ↓），未选中时 `opacity: selected ? 1 : 0.5`，标题 `vpx(24)`、简介 `vpx(18)`，`elide: Text.ElideRight` 截断长文，无背景卡片/强调条。
- 内容根因：3772 条 description 平均 46.3 字，**约 30% 是「《X》，X 平台。」空壳模板句**；16 个平台完全没有 publisher/genre/release → 「More by 厂商」空白。
- `GameDetails.improved.qml.txt`（已推送）：opacity 0.5→0.85、加半透明卡片 + 强调条、标题 24→30、简介 18→25、去掉 elide、lineHeight 1.3。清 `dataCache.json` 重启天马后主界面正常、logcat 无 QML/QQml 报错。
- 备份 `theme/GameDetails.before.qml.txt` + 设备 `.bak20261113` 可回滚。**远程输入无法稳定停在详情页那一屏（方向键/滑动被解释成切换集合），观感待用户实机确认**。

### 2.8 EASYRPG 封面重做

- 用户两次提出「EASYRPG 平台的封面都不对」（#75 / #104）。原封面为错误/通用图。
- 做法：从各 RPG Maker 游戏目录内的 `.xyz` 标题画面文件按 `xyzpal_first / xyzpal_last` 调色板解码（`xyz_decoded/`），生成 13 张真封面存 `kpa-backup/2026-11-13/covers_new/`：Mogeko城堡、威伦诺尔、寂静岭、废都物语、怪异症候群1/2、恐怖美术馆、梦幻重装机兵、灰色庭院、野比大雄的双截龙 / 恶灵附身 / 死亡空间 / 生化危机；部署到 `Roms/EASYRPG/Imgs/` 并 md5 校验一致。
- 备份 `easyrpg_backup/metadata.pegasus.txt`、`easyrpg_sheet.png`、`covers_new_sheet.png`；设备侧 `EASYRPG/_backup_covers_20261113`（3.75M，与 Imgs 重复）列入待清理清单。

### 2.9 27 核心 + 8 独立 APP 冒烟校验

- 脚本 `kpa-backup/2026-11-13/health/core_probe.py`：按 metadata 原始 `launch:` 冷启动、force-stop、截图、量化非黑像素 + 外接矩形、查 logcat `ANR in com.retroarch.aarch64` / SELinux / dlopen。
- **27 个唯一 libretro 核心 27/27 `core_executed=yes`**（logcat `avc: granted { execute }`）+ **8 个独立 APP 8/8 前台正常**（7 个安卓移植游戏 + PPSSPP）。`pm list packages -3` 只有 12 个第三方应用，全部已整合，无遗漏模拟器。
- 判定 35 OK / 3 DARK / 1 BLACK；长等待复核后 DARK 全部出画面（PS 20s、ATOMISWAVE 20s、泰拉瑞亚 15s、星露谷 15s）；唯一真黑屏 = `WS/恐怖传说.zip` 坏 ROM。
- **关键教训：3.2 秒等待严重不足**（首轮 27 DARK / 11 BLACK，8 秒复查后 23 个恢复——PS/SATURN/N64/MD/SFC/NDS/ATOMISWAVE/EASYRPG 整平台只是冷启动慢；`PS/射雕英雄传.chd` 368MB 需 15 秒）。ANR 检测须只匹配 `ANR in com.retroarch.aarch64`（否则串到后台 TMNT/Oceanhorn 的 ANR）。截图全黑先查前台窗口 / ANR 弹窗，勿直接归因 ROM 不匹配（ANR 弹窗造成非黑像素假阳性）。
- 显示核查：`video_filter=""`（滤镜关）、`video_shader_enable=true` 命中 crt-easymode、厂商 `overlays/*_B.cfg` 边框正常、竖版 cfg 统一 `input_overlay_enable=false`；抽样 10 个竖版 cfg 方向 10/10 正确。

---

## 3. 踩过的坑与修复 / 回轮

### 3.1 通用坑清单（按类型）

| 坑 | 根因 | 修复 / 结论 |
|---|---|---|
| 启动游戏中间「横屏加载」 | `--activity-clear-top` 强制 RA 冷启 | 30 份 metadata 全清该参数；GBA 改 mGBA 核心 |
| RA 中文变 `?`、菜单黑白 | `am start` 不带 `-e CONFIGFILE` 读默认配置 | 验证必须带 CONFIGFILE；字体须 TrueType glyf（Noto Sans CFF/OTF 不行） |
| GBA 无封面 | 资源包唯独 GBA 缺 `Imgs/` 与 `assets.box_front` | libretro thumbnails + `catalog.sqlite` 中英对照 + PIL 文字卡，426/426 补齐；文件名匹配先剥 `.png` 后缀 |
| 封面「空白卡」 | prosperoOS 网格卡用 Steam 专用 `assets.logo` | `GridItem.qml` / `GameDetails.qml` 加 `\|\| assets.boxFront` 回退 |
| 「21 张低质封面」 | 用文件大小推断质量（误判）→ 复查发现是**大面积黑屏坏图**（二次误判） | 三来源修复：zip 内部名匹配 libretro → RA 实机截图 480×320 → 三核心全黑做文字占位图 |
| 世嘉「透明遮挡」 | crt-easymode 在 960×640 上密集网点雾感 | 清空 `global_MD/SATURN/DC*.slangp`，用户选「无滤镜」 |
| PSP 直启读成 0 字节 | PPSSPP targetSdk 35 分区存储 | ROM 双份拷到 app 私有 files/ + 逐游戏 launch；ini 正确路径在 `.../files/PSP/SYSTEM/` |
| ATOMISWAVE「不兼容」 | 被 NOTICE 版权屏 / 黑屏等待不足误导 | 裸 .bin 可玩，抽验 3 个满屏 60fps；无需换 MAME romset |
| 世嘉 core override 不生效 | Gambatte per-core override 在本机无效 | GB/GBC 改用 mGBA 核心（改 launch 行） |
| macOS adb ~22s 必崩 | 37.0.1 在 macOS `libunwind` 崩 | 换 r34.0.5 到 `/tmp/platform-tools/`，`/tmp/adbx.sh` 自动探测重连；块 55MB/300 文件 |
| `adb install` 报错为空 / fuse denied | 系统无 fuse 读权限 | 先 `adb push xxx.apk /data/local/tmp/` 再 `pm install -r` |
| 详情页简介不显示 | 双原因：无 `description` 字段 + dataCache 缓存 | 写 description + 删缓存重启 |
| 详情页 enrichment 写进游戏名 | CLRMAME dat 值字段是 `publisher/releaseyear/genre/users` 而非 `comment` | 重解析重推 |
| galaga 黑屏 | 初判「ROM 版本不匹配」→ 实为 **RA 主线程阻塞 ANR**；后确认是 1996-12-24 老 ROM 集与 mame2003_plus 版本代差 | 按用户选项「2 从天马移除」；教训：截图全黑先查 ANR/前台窗口 |
| `WS/恐怖传说.zip` | TorrentZip（`TORRENTZIPPED-…`），标准库报 `invalid code lengths set` | 未动，建议换 ROM 或移除 |
| 417 个 BAD zip | 设备 toybox `unzip` 对中文条目名报 `Invalid entry name` 的兼容性误报 | 本机 Python `zipfile.testzip()` 抽样全部完好，非损坏 |
| 幽灵 galaga 条目 | `Roms/_backup_20261112_2347/` 旧 metadata 被天马递归扫描 | 改 game_dirs.txt 无效（天马重写），根治须删备份目录 |

### 3.2 用户纠正 ① — 系统按键属于 KPA / Android / AYASetting / AYAWindow 层，不是 RetroArch

- **用户原话**：
  - #75（21:23）「系统按键还原，现在的系统按键都被改了」
  - #82（22:02）「**暂停**，第一我说的系统按键有的被改了，**是 kpa 的系统，安卓系统下，或者进入一些程序后不能像之前那样了**；第二、你能确认机器有多少个按键嘛，都是什么按键你知道吗，先说明」
  - #84（22:27）给说明书：「我中午 11:57 给的任务里有让你优化系统界面的，是不是这个时候更改过系统按键，**你找出系统按键更改的时间和原因**」「21:23 的任务你都改了哪些按键，**先回轮，不要去改**」
  - #86（22:39）「**我关机重启了机器，系统按键都回来了**，现在解决竖屏游戏按键的问题」
- **溯源结论（从原始 JSONL 核对，非凭印象）**：全历史唯一 `settings put` 是 11-11 22:52 的 `stay_on_while_plugged_in 7`；**从未写过** navigation_mode / keylayout / 按键映射，也从未进过「自由按键/自定义按键」设置页。11:57 那轮系统层动作只有：12:14:03 设系统壁纸、12:15:21 `wm density 264`→12:15:54 reset、12:20:17 清缓存、**12:14:32 `am force-stop com.ayaneo.home`**（Bash #1381，为刷新壁纸）。
- **根因**：强杀 `com.ayaneo.home` 会同时杀掉它承载的 AYAWindow **`WindowKeyEventService`**（无障碍按键服务），自定义键 / AYASpace / 进 App 后的按键解释失效。22:03 实测 `Crashed services={WindowKeyEventService}`、`Bound={}`；22:12 左右机器重启后恢复（`hasBound=true`）。**属运行时状态丢失，不是键位配置被改**（配置目录 mtime 仍是 11-10 19:11）。
- **机型按键澄清**：正确名 KONKR Pocket ADVANCE；说明书明确「K 键、手柄按键等功能及定义以 AYASetting / AYAWindow APP 版本更新为准」；`/system/usr/keylayout/Vendor_045e_Product_028e.kl` 408-411 行 `key 751 LC / 752 RC / 753 EQ / 754 AYA` → 厂商自定义键，须靠 WindowKeyEventService 解释；**无实体摇杆、无 L3/R3**（此前把 106/107 列进按键表是照搬 Xbox 键值，错了）。
- **硬性禁令**：**禁止 `am force-stop com.ayaneo.home`**；需要刷新 AYA 桌面时改用重启设备或等待。

### 3.3 用户纠正 ② — 竖版批量改错后「回轮到 23:03、只改一个、确认后再推广」

- **时间线**：
  - 23:03 代用户启 airattck 验证：注入 `keyevent 96`(投币)+`97`(开始) 成功进游戏 → 证明回滚后的 per-game cfg 已被 RA 正确加载。此时 = 69 个厂商模板 + 厂商核心 remap。
  - 23:06 只把 `airattck.cfg` 方向翻成用户规则；23:08 又把另外 68 个一起翻（69 个 md5 变 `25fb88a…`）。
  - #89（23:09）「**回轮到 23:03 分**」→ 用 `argus.cfg.vendor` 模板把 69 个全部覆盖回厂商原版（md5 `44950e1a…`），核心 rmp 未动，force-stop RA 后重开 airattck 让配置重载。
  - #90（23:13）「现在竖版游戏里其他其他按键都设置正确，**只需要改方向键，最初那条规则翻转（右→上、左→下、上→左、下→右）——这次只改一个**」→ 备份 `airattck.cfg.before_2313` → 只覆盖 `airattck.cfg` → 校验 = **68 个厂商原版 + 1 个翻转版**，其余一律未动。
  - #91（23:15）「**为什么都改错了，刚开始是改对了的**」→ 从原始 JSONL 复盘：21:36 推理已正确；21:42 用 python **只替换方向 4 行**、A/B/START/SELECT 保持厂商值、不写 x/y → 这版完全正确，与 23:13 当前版字节一致。之后 21:46 为回应「Y 键换 select」改用**整文件覆盖**写成 `a=108/b=100/x=99/y=109`，把已正确的 a/b 改错；21:53 再整文件覆盖成 `a=109/b=100/x=99/y=108`（实体 START 变游戏 Y）。
  - #93（23:20）「**对的，这次都对，现在推广**，比找出不同平台的竖向游戏进行测试」→ FBNEO 69 个全部翻转（推广前完整备份 `cfg_before_promote/` 153 文件）。
- **三个根因**：① 12:14 强杀 `com.ayaneo.home` 后，21:23~21:53 的实机反馈都在系统按键服务失效状态下产生，却被当成配置证据反复叠加修改；② 21:14 新建的核心级 `FinalBurn Neo.rmp` 多出 4 行 `btn_a/b/x/y` 污染**全部** FBNEO 游戏（"实体 START 变游戏 Y" 真正元凶），全程未被发现，只在单文件打补丁；③ 从「只改 4 行」退化成「整文件覆盖」，回滚时又把对的方向一起撤掉。
- **教训**：「回轮」= 回滚；局部问题只做局部替换；先确认全局 remap 与系统服务状态；实机反馈必须先确认基线可信；**未经用户单点确认不批量推广**。

### 3.4 用户纠正 ③ — MAME `rot=1` 与 FBNEO `rot=3` 呈现一致，不要照搬差异

- #94（23:23）：用户直接引用了 assistant 自己刚说的话「这里有个不能照搬的关键差异：MAME 2003-Plus 的 140 个竖版配置用的是 `video_rotation = "1"`，而 FBNEO / CPS1 / CPS2 / NeoGeo 用的是 `"3"` —— 旋转方向相反，方向映射很可能不能一起翻」，然后纠正：「**这个问题之前就处理过了，里先查看**」。
- 查历史日志确认误判：11-12 日志 25-31 / 46-49 行早已写明 —— FBNEO/fbalpha2012 的 `rot=3` 与 MAME 2003-Plus 的 `rot=1` **最终呈现一致（文字顶部朝右、满屏横躺）**，因为 FBNeo/fbalpha 核心自带自动旋转、RA 叠加后与 MAME 效果相同；「方向键 remap 与 MAME 一致保留」；216 个带 rotation 的 per-game cfg 模板统一；airattck / dogyuun / 1941 / batsugun / gekiridn 均实测确认。**「rot 数值不同 → 方向映射不能一起翻」是错误的多余担心，不要重复推导**。
- 后续：#96（23:28）用户确认「1941 方向是对的、其他按键正确，但方向键和之前 FBNeo 相反，需要翻转」→ 147 个（MAME 2003-Plus 140 + CPS1 3 + CPS2 2 + NEOGEO 2）按各自原版精确替换 4 行生成，全部翻转；全机 **216 个竖版统一**为 `up=h0right/down=h0left/left=h0up/right=h0down`；23:42 用户「1941 测试正常」→ 全部验证通过。
- 附带更正：23:25「MAME/galaga 黑屏 = ROM 版本不匹配」先被更正为 ANR 主线程阻塞（截图非黑像素是 ANR 弹窗假阳性），最终定性为老 ROM 集版本代差；23:56「已发现的问题只有 galaga 一个」也不成立（扩大抽测后又发现 3 个黑屏 ROM）。

---

## 4. 最终产物清单与当前健康状态

### 4.1 设备侧最终状态（目标态）

| 类别 | 内容 |
|---|---|
| 前端 | `/sdcard/pegasus-frontend/`：`settings.txt`（prosperoOS）、`themes/prosperoOS/`（含 `GameDetails.improved.qml.txt`、`davebg.jpg`、Logo 补齐）、`dataCache.json`（运行时缓存）、`game_dirs.txt` |
| RA 全局 | 两份 `retroarch.cfg`（黑黄 ozone / vulkan / CRT / 96ms / 存档迁 TF / 官方核心源） |
| RA 配置 | `config/<核心>/*.cfg/.opt/.slangp`、`config/global_*.slangp`、`config/remaps/`（厂商基线）、216 个竖版 per-game cfg |
| ROM / 封面 | `<TF>/Roms/` 36 平台 3770 条 metadata + 封面、216 竖版 cfg、ANDROID 7 个 `.app` 占位 + `Imgs/` |
| 核心 | `/data/data/com.retroarch.aarch64/cores/`（83 内置 + 已装 bluemsx） |
| PSP | `/storage/emulated/0/Android/data/org.ppsspp.ppsspp/files/`（4 个 ROM ~4.4G + `PSP/SYSTEM/ppsspp.ini`） |
| 图库 | 4 个 `.nomedia`（Roms / RetroArch / pegasus-frontend / pocketmuseum） |
| 第三方 APP | 12 个（RA / 天马 / PPSSPP / 7 移植游戏 / MT管理器 等），全部已整合 |

### 4.2 本机工作区产物

- **执行记录**：`kpa-deploy/KPA优化执行记录-20261111.md`、`-第二批-20261111.md`、`KPA-第三批-全平台遮罩与封面-20261112.md`
- **部署/工具脚本**：`kpa-deploy/{gen_frames,gen_frames2,deploy_b,deploy_b2,scrape_covers,transfer,verify,extract_pkg,download_big,baidu_login_kpa,baidu_mirror}.py`、`kpa-meta-work/bangumi_desc.py`
- **备份与回滚点**：`kpa-deploy/backup{,2,3,4}-*/`、`kpa-backup/2026-11-12-2245/`（vendor 基线、翻转模板、推广前 153/156 文件、`galaga_removal/`）、`kpa-backup/2026-11-13/`（audit / health / theme / edit / covers_new / xyz_decoded / msx_mirror / msx_cfg_backup / easyrpg_backup）
- **验证报告**：
  - `kpa-backup/2026-11-13/audit/KPA_verification_report.html`（36 平台表 + 内嵌截图，113 样本）
  - `kpa-backup/2026-11-13/audit/KPA_changes_2026-11-13.html`（变更报告）
  - `kpa-backup/2026-11-13/health/KPA_health_check.html`（342KB，16 项达标判定 / 27 核心表 / 8 APP 表 / 遗留问题）
  - `kpa-backup/2026-11-13/health/KPA_cleanup_plan.html`（14KB，只读清理清单 + 风险警告）
  - 数据：`audit/{all_metadata.txt,inventory.json,probe_final.json,sample_plan.json,shots/}`、`health/{static_result.json,core_result.json,cleanup_inventory.json,tf_files.txt,duplicate_list.txt}`
- **Skill**：`~/.workbuddy/skills/kpa-game-setup/`（上架版 3.4M）——`SKILL.md` + `scripts/{run_all,step1..step7,sync_from_device,kpa_env}.sh` + `bangumi_desc.py` + `assets/golden/`（retroarch.cfg / settings.txt / game_dirs.txt / ppsspp.ini / prosperoOS-kpa.zip / 两张戴夫图）+ `assets/data/`（bios_list.txt / mame_orient.json / platform_cores.tsv）+ `assets/meta_latest/`（36 平台元数据）

### 4.3 健康状态（已达标）

- 全量静态校验（3770 条，非抽样）：**ROM 缺失 0、封面缺失 0、无 launch 0、无简介 0、重复 file 引用 0、重复游戏名 0、缓存 `is_missing` 0**；孤儿封面 2 张（正是保留的 dynwarjr 与 超级炸弹人4 ROM/封面，便于换同名 ROM 后加回）；竖版 cfg 精确 216。
- 缓存 144 个「重名」全是跨平台同名（如泡泡龙 7 平台），同平台内重名 0，不是重复条目。
- **27/27 核心可执行 + 8/8 独立 APP 前台正常**；`lastrun.log` 零 error（除幽灵目录警告）。
- 216 个竖版方向 10/10 抽查正确、用户实机 1941 通过；显示/遮罩/滤镜/按键核查通过。
- 设备已恢复天马前台；两份 cfg 已改回官方核心源、本地 HTTP 服务已停。

### 4.4 已知未达标 / 待办项

| 项 | 现状 | 建议 |
|---|---|---|
| **`WS/恐怖传说.zip` 坏 ROM** | TorrentZip，本机标准库 `invalid code lengths set`，实机 20 秒纯黑；同平台《恐怖传说2》正常 | 换 ROM 或按前例从天马移除，**未动** |
| **`_backup_20261112_2347` 幽灵 metadata** | 备份目录被天马递归扫描，多算 1 条游戏（幽灵 galaga），`lastrun.log` 产生 455+ 条「文件不存在」警告；改 `game_dirs.txt` 无效（天马重写回原样） | 删除该备份目录；在清理确认后执行 |
| **空壳简介 1142 条**（#28 记 1143 / 30.3%） | 「《X》，X 平台。」模板句，详情页信息量低；16 平台（ANDROID/ATOMISWAVE/DOS/DREAMCAST/EASYRPG/FC/MDCD/MSX/NAOMI/NDS/PCECD/PICO/PS/PSP/SATURN/SFC）缺 publisher/genre/release | `scripts/bangumi_desc.py --push`（需 bgm.tv 可达网络，带缓存/限速/断点续跑，回家网络跑）升级为真简介并回填字段 |
| **详情页观感待实机确认** | QML 增强版已推送、清缓存无报错、主界面正常，但远程输入无法稳定停在详情页那一屏 | 用户实机确认；不满意用 `GameDetails.before.qml.txt` 回滚 |
| **清理清单未执行** | 设备侧 17 项 / 17.40MB、本机 136 文件 / 165.11MB、需用户决定 74.14MB；#38 in_progress | 按用户「清理前先确认目录及影响」偏好，**先备份、分批（≤10 项）执行、每批校验**；本轮只出清单未删 |
| **skill 与最终状态不一致** | `SKILL.md` 竖版 remap 仍写厂商原版 `up=h0left…`（设备已是 `up=h0right…`）；机型名误写 AYANEO Pocket Advance（应为 KONKR Pocket ADVANCE） | 同步更新 SKILL.md（本次复盘不改） |
| 已移除 / 换核心项 | galaga、古惑狼赛车、GG雅士达3、CPS1/dynwarjr、SFC/超级炸弹人4 已移除（部分保留 ROM+封面便于换回）；mercsj/samuraia/sonicwi 已换 fbneo + 补竖版 cfg | 已验证；无需再动 |
| 系统壁纸 | AYANEO 桌面只认内置壁纸；系统层（锁屏/系统）戴夫日落图已设置 | 桌面壁纸需用户手动在「掌机设置→个性化→系统壁纸」选内置图 |

---

## 5. 可沉淀为 skill 的 SOP 步骤与硬性禁令清单

### 5.1 SOP（幂等、可重复运行；对应 `scripts/run_all.sh`）

| 步骤 | 动作 | 关键判定 |
|---|---|---|
| step0 环境 | platform-tools 就绪、USB 授权（或 `adb connect <ip>:5555`）、`KPA_TF` 默认 `/storage/6AF3-384F`、ROM/封面/BIOS 随卡 | `adb devices` + `df` |
| step1 装 APP | RetroArch / Pegasus / PPSSPP（官方渠道下载，直连失败走 gh-proxy 镜像）；**大 APK 先 push 到 `/data/local/tmp/` 再 `pm install -r`** | `pm list packages -3` |
| step2 主题 | prosperoOS（**master 分支**）覆盖安装到 `themes/prosperoOS/`；`GridItem.qml`/`GameDetails.qml` 加 `assets.logo \|\| assets.boxFront` 回退；`settings.txt` 切主题 | `lastrun.log` 中 `Cannot open` 应为 0 |
| step3 RA 主配置 | 推 `retroarch.cfg`（黑黄 ozone / vulkan / CRT / 96ms / 存档 TF app 专属目录）、建 `{config,overlays,system}` 目录、BIOS 清单检查 | 单独开 RA 是黑黄即成功 |
| step4 metadata + 竖屏 | 各平台补 launch 行；按 `mame_orient.json` 生成竖版 cfg（MAME/VARCADE rot=1；FBNEO/CPS/NEOGEO rot=3；方向统一 `up=h0right…`）；description / 封面字段 | 216 个竖版 cfg，md5 分组一致 |
| step5 PSP | `ppsspp.ini` 满屏（`DisplayStretch=True` 带空格、`ShowTouchControls=False`）+ ROM 拷到 app 私有 files/ + 逐游戏 launch | intent 直启 logcat `Booted` |
| step6 清理 | AppleDouble / `.DS_Store` / 失效旧路径 / 缓存；出可选项报告（**不自动删**） | 用户确认后分批删 |
| step7 验证 | `rm dataCache.json` → force-stop 重启天马 → 截图 + `lastrun.log` 错误检查；核心/APP 冒烟脚本 | `N games found`、`avc: granted { execute }`、零 ANR |
| 手动（脚本会提示） | ① RA 首启解包内置核心 ② 自备 BIOS（PS/DC/SATURN/PCE-CD/MDCD/MSX/NAOMI）③ MSX 核心（本地镜像法或 Load Core→Install or Restore a Core）④ 系统桌面壁纸 | — |
| 补数据 | `bangumi_desc.py --push` 升级真简介 + 回填 16 平台字段；`assets/meta_latest/` 推最新元数据 | 清缓存重启生效 |

### 5.2 硬性禁令清单（写入 SKILL.md 的「必须遵守」）

1. **禁止 `am force-stop com.ayaneo.home`** —— 会杀掉 AYAWindow `WindowKeyEventService`，导致 KPA/Android 层系统按键全部失灵，只能重启恢复；刷新 AYA 桌面用重启或等待。
2. **禁止把核心 `.so` 推送到 public 路径**（`/sdcard/…`、`Android/data/…`、`/data/local/tmp`）后指望 dlopen —— SELinux `avc: denied { execute }`，只有 `/data/data/com.retroarch.aarch64/cores/` 可用。
3. **禁止用 `run-as` / `adb root` / `su` / `adb backup` 操作 RA 私有数据**（not debuggable / production / Android 12 备份 0 字节）。
4. **禁止 `input tap` / 大部分 `input keyevent` 操作 RA ozone 菜单**（固件走内核 evdev 直读）；只有 `input motionevent DOWN/UP`、BACK(4)、方向键 21/22/19/20 有效。
5. **禁止手工在核心 cfg 写 `video_shader` 键** —— 破坏 RA 自动预设加载链；改 `global_*.slangp` 一处即可覆盖上百逐游戏预设。
6. **禁止整份覆盖 `metadata.pegasus.txt`** —— 云端与设备 ROM 数不匹配会丢游戏；只就地 patch 启动命令/字段。
7. **禁止改 metadata / 新增目录后不删 `dataCache.json` 就重启判断生效** —— 必须 `rm /sdcard/pegasus-frontend/dataCache.json` 再 force-stop 重启 `org.pegasus_frontend.android`。
8. **禁止靠改 `game_dirs.txt` 排除目录** —— 天马启动会重写回原样；根治幽灵条目必须删备份目录。
9. **禁止 PSP ROM 只放 TF 卡或删除 app 私有目录那份** —— PPSSPP targetSdk 35 读不到；双份均为必需。
10. **禁止把存档/截图放 `/storage/6AF3-384F/save/`** —— RA 进程无 `sdcard_rw`，只能放 TF 卡 `Android/data/<pkg>/files/`。
11. **禁止对竖版 cfg 整文件覆盖式改按键** —— 只精确替换 4 行方向，保留 a/b/start/select/rotation/x/y；禁止新建或污染核心级 `config/remaps/<核心>/<核心>.rmp`（会作用于该核心全部游戏）。
12. **禁止未经用户单点确认就批量推广按键/配置改动**；「回轮」= 回滚到指定时间点，先单点验证再推广。
13. **禁止照搬 `video_rotation` 数值差异推导方向映射**（MAME rot=1 与 FBNEO rot=3 最终呈现一致）；动手前先查历史结论。
14. **禁止用文件大小 / 3.2 秒截图 / 单一亮度阈值推断封面质量或黑屏** —— 冷启动需 8–26 秒；先查前台窗口与 `ANR in com.retroarch.aarch64`（ANR 弹窗造成非黑像素假阳性）。
15. **禁止并行冒烟任务互相污染截图、禁止强杀 TMNT/Oceanhorn 后直接截图**（留 ANR 弹窗需点「等待」清除）。
16. **禁止在设备上留 `.bak*` 备份**（用户要求零备份；改动覆盖式/幂等，回滚用 `sync_from_device.sh` 或重跑 step）；清理前**必须先出清单 + 影响说明并获确认**。
17. **禁止批量「更新已安装核心」** —— 官方源 17.5KB/s、nightly 非稳定版、与 216 竖版 cfg/遮罩/CRT 配套有回归风险；要更新单独点某一个。
18. **禁止给 GBA 加遮罩**（KPA 专为 GBA 设计，240×160=1.5 原生满屏 960×640）。
19. **禁止改 `media-pack.bytes` / 往口袋博物馆 media-pack 加文件**（触发包校验失败/重下）；ANDROID 集合缺图用 `.app` 占位 + `extensions: app` + per-game launch 解决。
20. **禁止不带 `-e CONFIGFILE` 启动 RA 判断配置成败**；GBA 启动命令禁止带 `--activity-clear-top`。
21. 网络受限时**不要假设 GitHub raw / bgm.tv / wikipedia / thegamesdb / screenscraper 可达**；实测仅 `api.github.com` + gh-proxy + libretro thumbnails 可用（thumbnails 索引走 `git/trees?recursive=1`，contents 分页无效）。
22. macOS adb 用 r34.0.5 + `/tmp/adbx.sh` 重连包装；大传输分块 55MB / 300 文件，`tar -T` 清单只放文件，校验用抽样 `md5sum "路径"`（双引号）。

> 复核提示：本次复盘发现的 **SKILL.md 两处待同步**（竖版 remap 值、机型名）应作为 skill 下一版修订项，但按任务要求本次**未修改现有 skill**。
