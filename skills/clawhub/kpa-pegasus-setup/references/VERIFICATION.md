# 健康校验 SOP、遗留项与清理清单

## 1. 三层校验

| 层 | 做法 | 通过线 |
|---|---|---|
| 静态（全量，非抽样） | 解析 36 平台 `metadata.pegasus.txt`，逐条核对 ROM 存在、封面存在、`launch:`、简介、`file:` 唯一性、游戏名重复、`dataCache.json` 的 `is_missing` | 各项均为 0；竖版 cfg 精确 219 |
| 核心 / APP 冒烟 | 按 metadata 原始 `launch:` 冷启动 → force-stop → 截图 → 量化非黑像素与外接矩形 → 查 logcat `ANR in com.retroarch.aarch64` / SELinux / dlopen | 核心 `avc: granted { execute }`；APP 前台窗口正确 |
| 抽样功能 | 每平台随机 2–3 个游戏（有竖版再加 2–3 个），验证核心、启动、滤镜、着色器、遮罩、满屏/满高、按键 | 113 样本记录留痕 |

用 `bash scripts/kpa_health_check.sh` 跑静态层（只读）。冒烟层需设备在线，等待基准见 `PLAYBOOK.md` 第 8 节。

## 2. 达标基线（2026-11-13 实测）

- `assets/meta_latest/` 是 3773 条全量模板（含少数已按实机结果从天马移除、但 ROM/封面仍保留的条目），离线自检 `kpa_health_check.sh --local` 报 36 平台 / 3773 游戏 / ISSUES none；**设备最终态是 3769 条**（2026-11-13 隔离坏 ROM 后）。部署以设备现状为准，只就地 patch，禁止整份覆盖。
- 全量静态校验 3769 条：ROM 缺失 **0**、封面缺失 **0**、无 launch **0**、无简介 **0**、重复 file 引用 **0**、重复游戏名 **0**、缓存 `is_missing` **0**；孤儿封面 2 张（保留的 `dynwarjr` 与 `超级炸弹人4` ROM/封面，便于换同名 ROM 后加回）；竖版 cfg **219**（方向映射 219/219 全量校验正确）。
- 缓存 144 个「重名」全是跨平台同名（如泡泡龙跨 7 平台），同平台内重名 0，不是重复条目。
- **27/27 唯一 libretro 核心可执行**、**8/8 独立 APP 前台正常**（7 个安卓移植游戏 + PPSSPP）；`pm list packages -3` 只有 12 个第三方应用，全部已整合，无遗漏模拟器。
- 冒烟首轮判 35 OK / 3 DARK / 1 BLACK；长等待复核后 DARK 全部出画面，唯一真黑屏 = `WS/恐怖传说.zip`。
- 219 个竖版方向已全量校验：`up=h0right` 命中 219/219，用户实机「1941 测试正常」；显示 / 遮罩 / 滤镜 / 按键核查通过。
- `lastrun.log` 零 error（除幽灵备份目录警告）；设备已恢复天马前台；两份 `retroarch.cfg` 已改回官方核心源、本地 HTTP 服务已停。
- 「更新已安装核心」被 3% 强制中断：仅生成 1 个 `fbalpha2012_cps1 .lcbk`，无 zip 残留，5 个核心冒烟正常 → **无影响，不需要更新**。

## 3. 已知遗留项（发布时仍未处理）

| 项 | 现状 | 建议 |
|---|---|---|
| `WS/恐怖传说.zip` 坏 ROM | TorrentZip，本机标准库报 `invalid code lengths set`，实机 20 秒纯黑；同平台《恐怖传说2》正常 | 换 ROM 或按前例从天马移除（保留 ROM + 封面） |
| ~~`Roms/_backup_20261112_2347/` 幽灵 metadata~~ | **已解决（2026-11-13）**：备份目录已删、`game_dirs.txt` 失效行已清、缓存重建后 455+ 条警告归零、平台数 37→36 | 无需处理 |
| 空壳简介 1142 条（约 30.3%） | 「《X》，X 平台。」模板句，详情页信息量低；16 个平台缺 publisher/genre/release | `bash scripts/bangumi_desc.py --push`（需 bgm.tv 可达网络，带缓存/限速/断点续跑） |
| 详情页观感待实机确认 | QML 增强版已推送、清缓存无报错、主界面正常；远程输入无法稳定停在详情页那一屏 | 实机目视；不满意用 `GameDetails.before.qml.txt` 回滚 |
| `.nomedia` TF 卡卷 | 内部存储重扫立即生效；TF 卡 `public:179,129` 重扫无效 | 重启一次后确认图库素材消失 |
| 系统桌面壁纸 | AYA 桌面只认内置壁纸；系统层（锁屏/系统）戴夫日落图已设置 | 桌面壁纸需手动在「掌机设置 → 个性化 → 系统壁纸」选内置图 |
| ~~设备侧清理清单未执行~~ | **已完成（2026-11-13 18:43）**：17 项分两批删除并逐项校验，17/17 GONE | 无需处理 |
| `Roms/_quarantine/VR运动会.bin` | 117MB，实测 40 秒仍全黑（同平台罪恶装备X 20 秒进画面），判定坏 ROM；已移出平台目录并从 metadata 移除条目，天马条目 3770→3769 | 换到可用 ROM 后移回 `Roms/ATOMISWAVE/` 并重新加回 metadata |

已移除 / 换核心项（已验证，无需再动）：`galaga`、`古惑狼赛车`、GG 雅士达 3 个坏 ROM、`CPS1/dynwarjr`、`SFC/超级炸弹人4` 已从天马移除；`mercsj / samuraia / sonicwi` 已换 `fbneo` 并补竖版 cfg。

## 4. 回滚点清单（清理时不得误删）

| 路径 | 用途 |
|---|---|
| `theme/GameDetails.before.qml.txt`（设备侧 `.bak20261113`） | 详情页增强的唯一原版回滚点，9KB |
| `assets/golden/GameDetails.improved.qml.txt` | 增强版 |
| `msx_cfg_backup/retroarch.cfg.ORIGINAL_URL` | 唯一有效的 cfg 官方源原版（另一份 `.bak_msx_url` 指向已关闭的本地镜像，是无效备份） |
| `edit/*.before.txt`、`edit/game_dirs/game_dirs.before.txt` | metadata / game_dirs 改动 diff 依据 |
| `RetroArch/system/firmware.bin.bak` | BIOS/固件备份，牵涉核心启动 |
| `/sdcard/pegasus-frontend/dataCache.json` | 运行时缓存，删了要重启重建，不算垃圾 |
| `/sdcard/pegasus-frontend/lastrun.log` | 前端运行日志，自动覆盖 |

## 5. 清理清单与执行纪律

**设备侧（17 项 / 17.40MB，已于 2026-11-13 全部执行完毕，保留记录供复核）**：`Roms/_backup_20261112_2347` 目录、`EASYRPG/_backup_covers_20261113`（与 Imgs 重复的新封面）、`RetroArch/config/_backup_20261112_2335` 与 `_2245`、`downloads/core_backups`、4 份 public 路径的 `bluemsx_libretro_android.so`、2 份无效 `retroarch.cfg.bak_msx_url`、`Download/dataCache.json.bak`、`game_dirs.txt.bak20261113`、4 个平台的 `metadata.pegasus.txt.bak20261113`。完整清单（含每条删除理由与回滚点）在 GitHub 仓库 `archive/inventory/cleanup_inventory.json` 与 `archive/reports/KPA_cleanup_plan.html`。

**本机侧**：缓存快照（`kpa-deploy/tm/dc*.json` 9 个 / 47MB）、ROM zip 复核样本（`health/zipsample/` 13 个 / 65MB）、`tools/platform-tools.zip`、56 组 md5 重复文件的冗余副本、未使用的 APK / 字体 / 验证截图。

**纪律**：
1. 先只读盘点，列出路径 / 大小 / 删除理由 / 影响 / 回滚点。
2. 用户明确确认范围后才动手；设备删除无废纸篓，本机用可恢复方式（废纸篓或隔离区）。
3. 分批 ≤10 项，每批校验；保留删除记录。
4. 不删 ROM、封面、BIOS、shader、遮罩、竖版 cfg、主题资源、运行时 `dataCache.json`、第 4 节回滚点。

## 6. 归档报告

工程期间产出的 4 份报告与校验数据已归档在 GitHub 仓库 `archive/`，本机工作区清理后仍可回溯：

- `archive/reports/KPA_verification_report.html` — 36 平台抽样表 + 内嵌截图（113 样本）
- `archive/reports/KPA_changes_2026-11-13.html` — 变更报告
- `archive/reports/KPA_health_check.html` — 16 项达标判定 / 27 核心表 / 8 APP 表 / 遗留问题
- `archive/reports/KPA_cleanup_plan.html` — 只读清理清单 + 风险警告
- `archive/inventory/` — 静态校验、核心冒烟、盘点与重复文件清单
- `archive/rollback/` — metadata / QML / cfg 回滚点

归档时已对设备序列号、局域网 IP 与本机用户名做脱敏。
