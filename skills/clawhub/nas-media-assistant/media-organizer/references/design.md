# media-organizer · 技术设计

> **受众**：人 / Codex / 开发者。本文承载架构、命名规则权威定义、技术细节。
> Agent 调用说明见 [`SKILL.md`](./SKILL.md)。

---

## 一、架构与解耦设计

### 1.1 总体定位

下载后/全库整理时的**本地离线归档器**：解析文件名 + 注入元数据 + ffprobe -> 分类 -> 系列检测 -> 规范命名 -> 原子搬家。**不内嵌任何 TMDB 查询**，零网络依赖，幂等可重跑。

### 1.2 与 media-lookup 的解耦协作（两个契约）

media-organizer 只对自身归档能力负责，**不与 media-lookup 耦合**。两者经两个单向契约协作：

```
                      ┌── 契约①: 元数据注入(--metadata) ──┐
media-lookup ─────────┤  归一化 JSON 数组                 ├──> media-organizer
(归一化元数据)         └──────────────────────────────────┘
                                                        │
                      ┌── 契约②: pending_lookup 回报 ────┐
media-organizer ──────┤  need_lookup: 告诉编排器要查什么  ├──> Agent -> media-lookup -> 重试
                      └──────────────────────────────────┘
```

**契约①·元数据注入（方案 B）**：Agent 把 media-lookup 产出的**归一化 JSON**（不碰原始 dict）组成数组，经 `--metadata` / `--metadata-file` 传入。`_build_meta_index()` 按各条目 `title`（中文标题）**和 `original_title`（英文原名）** 建索引（精确 + 大小写模糊），使文件名解析出的英文标题也能匹配到元数据。归一化形态：

```
movie: {media_type:"movie", title, year, tmdb_id, collection:"合集名"或null, genres:[...], source}
tv:    {media_type:"tv", title, year, tmdb_id, collection:null,
        seasons:[{season:"S01", name:"第一季", year:"2014", episode_count:n}], genres:[...], source}
```

**契约②·pending_lookup 回报**：自身策略无法确诊时，对应 plan 置 `status="pending_lookup"` + `need_lookup`，**不被移动**。`need_lookup` 含 `title/year/media_type_hint/need/reason/extra_queries`，Agent 据此调 media-lookup，取回后带 `--metadata` 重试即转为 `resolved`。

> 设计意图：把"查元数据"完全外移给 media-lookup，归档器保持纯离线、可单测、可幂等重跑。衍生剧疑似未确认是**唯一**会触发 pending 的场景；系列/年份/动画类型缺元数据时用启发式/占位/默认处理，**不**pending（避免噪声）。

### 1.3 已归档文件跳过（库索引消解）

不再维护逐文件库索引（`library_index.json` 概念已删除）。已就位的规范文件靠**路径规范检测**跳过：`_already_organized()` 判定文件已在正确分类目录且文件名含规范标记（电影含 `(年份)`、剧集/动漫含 `SxxExx`）即跳过解析；`--rescan` 强制重扫整库。这样既幂等又避免全盘逐文件比对的开销。

---

## 二、处理流程

```
1. 扫描      scan_videos(): 遍历根目录视频文件(忽略 Sample/花絮/.nfo/字幕/图片；图片冒充视频扩展名者也跳过)
2. 跳过判断  _already_organized(): 规范路径文件跳过(--rescan 可重扫) -> status=already_organized
3. 解析分类  classify(): parse_media()->title/year/[信息]/sea/ep -> 判 kind(movie/tv/anime)+系列检测
4. 归组      finalize_tv_shows(): 剧集按剧名分组 -> 单季独立 / 多季格式2(第N季)/格式3(主题)
5. 降级      单成员系列自动降级为独立电影(避免单部误入系列文件夹)
6. 迁移      finalize_target()+_move_file(): 同FS用mv原子移动; 跨FS用cp->校验->rm; 已存在询问覆盖/跳过
   (附) 自扩充 _save_learned_series(): 本次经元数据解析出的系列沉淀回 .cache/media_cache.json known 段
7. 清垃圾    cleanup_junk_files(): --purge-junk 启用时,移动视频后扫描残留并删广告图/伪装视频/nfo/txt等
   (附) 清空目录 cleanup_empty_dirs(): --commit 后删除本次产生的空目录
```

分类优先级（`classify` 内）：①剧场版/OVA/OAD/SP/番外->强制电影 ②衍生剧(·标题)->特别篇路径 ③有集号(SxxExx)->剧集/动漫 ④无集号->电影(含系列检测)。

---

## 三、命名规则（权威定义）

> 根 `SKILL.md` 与本文件均引用此处为命名唯一权威。

### 3.1 电影
```
独立电影(无元数据)：  电影名 (年份)/电影名 (年份) [信息].扩展名
独立电影(有元数据)：  中文标题 (年份)/中文标题.原始英文信息.扩展名
系列电影：            系列名（系列）/中文标题.原始英文信息.扩展名
```
- 独立电影每部独立文件夹；系列电影同系列并入系列文件夹、**不建子文件夹**、与已有成员并列。
- 文件夹名与文件名必须含**英文括号**包围的年份。
- **元数据中文标题优先**：当注入元数据含中文 `title` 且与文件名解析出的英文标题不同时，文件夹用中文标题，文件名组合为「中文标题.原始英文文件名（去广告前缀和中文标题后）.扩展名」，保留全部质量/分辨率/编码信息。
  - 示例：`Vanishing.Point.2026.2160p.WEB-DL.H.265.HDR.DTS5.1-PandaQT.mkv` + 元数据 `title="消失的人"` → `消失的人 (2026)/消失的人.Vanishing.Point.2026.2160p.WEB-DL.H.265.HDR.DTS5.1-PandaQT.mkv`
  - 无 `original_title` 或标题相同时回退标准格式 `电影名 (年份) [信息].扩展名`。
- 文件名追加 `[信息]` 标签（见 §六），仅在标准格式时使用。
- **副标题完整保留**：冒号/中点分隔的副标题不截断（`电锯惊魂8：竖锯 (2017)`、`灵魂摆渡·黄泉 (2018)`）。

### 3.2 剧集
```
独立剧集(单季)：  剧名 (年份)/剧名 - SXXEYY [信息].扩展名
多季 - 主题季：   剧名/剧名·主题(年份)/剧名·主题 - SXXEYY [信息].扩展名
多季 - 第N季：     剧名/剧名·第N季/剧名 - SXXEYY [信息].扩展名
衍生剧/特别篇：   剧名/剧名·特别篇/完整标题 - S00EYY [信息].扩展名
```
- 衍生剧/主题剧归入母剧文件夹的 `剧名·特别篇`（与 `·第N季` 格式统一，文件名用 `S00EYY` 保留集号）。
- `--tv-format season`（默认）= `第N季` 格式；`--tv-format year` = 按年份标注（需注入季年份，缺则回退 season）。

### 3.3 动漫
```
动漫名 (年份)/Season XX/动漫名 - SXXEYY [信息].扩展名
```

### 3.4 通用规范化
- 标题去首尾空格；`/ \ : * ? " < > |` 替换为下划线（`safe_name()`）。
- 季集号用 `SxxEyy` 两位零填充；扩展名保留原文件扩展名。
- 花絮/特典单独放 `Extras/`。

---

## 四、路径规范

Agent 调用前必须 `ls` 确认物理目录真实存在，严禁臆断。

| 容器内路径 | 宿主机路径 | 说明 |
| --- | --- | --- |
| `/media/movies/` | `/volume1/影视库/` | 影视库根（`--base` 默认，对应 `MOVIES_DIR`） |
| `/media/downloads/` | 下载暂存根区 | 下载入口（`XUNLEI_INBOX`） |

- 影视库下分类子目录：目前仅 `电影/` `动漫/` `剧集/`。
- `folder_kind()` 按路径含 `剧集/电视剧/tv/shows/剧` -> tv；`动画/动漫/anime/番` -> anime；`电影/movie` -> movie；其余 None。
- 新增分类（如综艺、纪录片）须用户明确确认名称与路径后方可创建。

---

## 五、电影系列归类（四级检测）

`detect_movie_series()` 返回 `(series_folder, source)`，独立电影返回 `(None,"独立电影")`：

| 级别 | 方法 | 来源标记 | 说明 |
| --- | --- | --- | --- |
| 0 | 文件夹路径 | `文件夹(系列)` | 文件已在 `XX（系列）` 文件夹内，优先命中、免查询 |
| 1a | curated 系列名册 | `本地注册表` | `data/series_registry.json` 模式匹配(read-only) |
| 1b | known 缓存段 | `本地缓存(known)` | 自扩充沉淀的 `title->series_folder`（见 §八） |
| 2 | 注入元数据 collection | `元数据(合集)` | media-lookup 归一化的 `collection` 字段经 `series_from_collection()` 归一 |
| 3 | 启发式 | `启发式(中点)` / `启发式(冒号)` | 中点(·)基名>=3字 / 冒号分隔剥尾部续集编号 |

> 单成员系列在阶段二自动降级为独立电影（`独立电影(单成员降级)`），避免单部电影误入系列文件夹。

---

## 六、`[信息]` 标签回退

`build_info_tag()` 三级回退构造 `[信息]` 标签：

| 级别 | 来源 | 标记 | 说明 |
| --- | --- | --- | --- |
| 1 | 原始文件名 | `原始文件名` | 文件名已含信息段（如 `[国语配音 中文字幕]`）直接用 |
| 2 | ffprobe / mediainfo | `ffprobe` | 调 `ffprobe_info.py` 分析文件流：分辨率(2160p/1080p…)·视频编码(x264/x265)·音频编码(DTS/AC3/TrueHD)·声道·Atmos·音轨语言·字幕；国内压制组常把语言写在轨道 title，故同时解析 language 标签与 title 文本、优先 title |
| 3 | 占位 | `占位(未标注)` | 上述均不可得时标 `[未标注]`；`--no-ffprobe` 直接跳到本级 |

输出形如 `[国英多音轨+简繁中字幕].[1080p.x264.AC3.5.1]`。双引擎：优先 ffprobe，不可用回退 mediainfo。

---

## 七、衍生剧 / 主题剧检测

场景：同一 IP 同时含电影和剧集（如灵魂摆渡：电影《灵魂摆渡·黄泉》+ 剧集三季 + 衍生微剧《灵魂摆渡·十年》）。

`detect_spinoff()`（在 `series_detect.py`，纯决策不查网络）按以下判定：

1. **必须 tv**：`full_entry` 注入且 `media_type != "tv"` -> 非衍生（电影·副标题不算）。
2. **中点(·)分隔**：标题含 `·`，基名（· 左侧）>= 3 字符（< 3 多为译名中点如「哈利·波特」，非系列分隔）。
3. **母剧确认**：有 `base_entry` 且为 tv，且衍生年 >= 母剧首播年 -> `is_spinoff=True`（归 `剧名·特别篇`，`S00EYY`）。
4. **缺母剧元数据**：疑似但无 `base_entry` -> 返回 `need:"base_show_lookup"`，`classify` 据此置 `pending_lookup`，`need_lookup.extra_queries` 指明要查的母剧。
5. **注册表兜底**：元数据未确认时退查 `_registry_member()`，命中已登记 tv 成员（如「灵魂摆渡·十年」）-> 离线确认衍生剧。

分流规则（media_type + 文件夹上下文）：文件在 `电影/` 下 -> 跳过 TV 衍生检测保持电影属性；文件在 `剧集/` 下且确认为 tv -> 走衍生剧检测归母剧 `剧名·特别篇/`。

---

## 八、本地知识缓存（双文件）

为避免单文件 `series`(curated) + `known`(运行时) 双段混装导致 git 噪声/职责不清，拆成两个文件，**职责单一、互不污染**：

| 文件 | 段 | 维护方 | 提交 | 用途 |
| --- | --- | --- | --- | --- |
| `data/series_registry.json` | `series` | 人工 curated（随项目发布） | ✅ 提交 | Level 1a 系列名册：模式匹配 + 成员列表 |
| `.cache/media_cache.json` | `known` | 运行时自扩充（`--commit` 触发） | ❌ gitignore | Level 1b title -> 已解析元数据 离线沉淀 |

**`data/series_registry.json`**（committed，read-only）：

```jsonc
{
  "_comment": "curated 系列名册，随项目发布；运行时不会写此文件。",
  "series": [
    {"name":"疯狂动物城","folder":"疯狂动物城（系列）",
     "match_patterns":["疯狂动物城","Zootopia"],
     "members":[{"title":"疯狂动物城","year":2016}, ...]}
  ]
}
```

- `_load_series_registry()` -> `data/series_registry.json` -> `series` 段
- `_check_registry()` / `_registry_member()` 走此段

**`.cache/media_cache.json`**（gitignored，本机状态）：

```jsonc
{
  "_comment": "运行时自扩充。--commit 时把经注入元数据成功解析的系列沉淀回这里；下次同类文件离线命中 Level 1b，从不查 TMDB。",
  "known": {
    "电影A": {"year":"2020","kind":"movie","series_folder":"测试（系列）","source":"learned"}
  }
}
```

- `_load_media_cache()` -> `.cache/media_cache.json` -> `known` 段
- `_load_known()` 取 known 段做 Level 1b 匹配
- `_save_learned_series()` 在 `--commit` 时把本次 `info_source` 含 `元数据` 且 `resolved` 的系列 title 写入；删掉文件下次会重新学习，不破坏主流程

---

## 九、函数职责与依赖图

```
main()
 ├─ _build_meta_index(args)            # --metadata / --metadata-file -> title+original_title 双索引
 ├─ scan_videos(root)                  # 遍历视频文件
 ├─ _already_organized(abspath, stem) # 规范路径跳过(--rescan 可重扫)
 ├─ classify(abspath, stem, ext, meta, no_ffprobe)   # 阶段一：解析+分类+系列检测
 │    ├─ parse_media(stem)             #   title/year/[信息]/sea/ep (清洗【】广告前缀)
 │    ├─ folder_kind(abspath)          #   路径推断分类
 │    ├─ build_info_tag(...)           #   [信息]三级回退 -> _ffprobe_info -> ffprobe_info.extract_info
 │    ├─ detect_spinoff(...) [series_detect]  #   衍生剧判定(纯决策)
 │    ├─ _registry_member / _check_registry   #   注册表 series 段
 │    ├─ detect_movie_series(...)     #   电影系列四级
 │    │    ├─ _series_from_path       #   L0 路径
 │    │    ├─ _load_series_registry   #   L1a
 │    │    ├─ _load_known / _match_known  #  L1b
 │    │    ├─ _meta_lookup + series_from_collection  #  L2 注入 collection
 │    │    └─ 启发式(中点/冒号)        #   L3
 │    └─ _resolve_tv_kind(...)        #   tv/anime 判定(注入元数据 > 文件夹上下文)
 ├─ finalize_tv_shows(plans, tv_format, meta)  # 阶段1.5: 剧集归组
 │    ├─ _get_season_names(show, meta)  #   注入 seasons[].name
 │    └─ _get_season_year(show, sea, meta)  # 注入 seasons[].year
 ├─ [降级] 单成员系列 -> 独立电影
 ├─ finalize_target(p, base)           # 阶段三: 定最终目标路径
 ├─ _move_file(src, tgt)              # mv / cp->校验->rm
 ├─ _save_learned_series(plans)       # 自扩充写回 .cache/media_cache.json known 段
 └─ cleanup_empty_dirs(root)          # 清理空目录

series_detect.py (纯决策，不查网络):
 ├─ series_from_collection(coll)  # 合集名 -> 系列文件夹名(剥后缀归一)
 ├─ is_animated(genres)           # genres 是否含动画 -> True/False/None
 └─ detect_spinoff(title, year, full_entry, base_entry)  # 衍生剧判定
```

---

## 十、命令行参数全表

| 参数 | 默认 | 说明 |
| --- | --- | --- |
| `root`（位置） | - | 待整理根目录（文件或文件夹） |
| `--base` | `/media/movies` | 影音库根（宿主 `MOVIES_DIR`） |
| `--commit` | False | 实际执行移动（默认只预演） |
| `--overwrite` | False | 目标已存在时覆盖（默认跳过） |
| `--report` | - | 写计划 + 汇总 JSON 到此路径 |
| `--no-ffprobe` | False | 跳过 ffprobe，`[信息]` 用 `[未标注]` |
| `--tv-format` | `season` | `season`=第N季 ｜ `year`=按年份标注（需注入季年份） |
| `--metadata` | - | 注入元数据（JSON 数组，media-lookup 归一化结果） |
| `--metadata-file` | - | 同 `--metadata`，从文件读 |
| `--fast` | False | 离线尽力而为，不输出 pending_lookup（快速预演；会清空 meta 并把 pending 降级为 resolved） |
| `--rescan` | False | 不跳过已就位规范文件，强制重扫整库 |
| `--purge-junk` | False | 删除无用残留（广告图/伪装视频/nfo/推广txt/sample）；预演只报告，配合 `--commit` 实际删除 |

典型用法：

```bash
# 预演（默认）
python3 media-organizer/scripts/organize_media.py /media/downloads/inbox --no-ffprobe
# 带 media-lookup 元数据注入（pending 恢复后）
python3 media-organizer/scripts/organize_media.py /media/downloads/inbox --metadata-file /tmp/meta.json
# 确认无误后执行
python3 media-organizer/scripts/organize_media.py /media/downloads/inbox --commit --metadata-file /tmp/meta.json
# 全库整理（已就位自动跳过）
python3 media-organizer/scripts/organize_media.py /media/movies --commit --rescan
# 入库同时清理下载残留广告图/伪装视频（先预演确认，再 --commit 删除）
python3 media-organizer/scripts/organize_media.py /media/downloads/inbox --purge-junk --no-ffprobe
python3 media-organizer/scripts/organize_media.py /media/downloads/inbox --purge-junk --commit
```

---

## 十一、核心规则

### 为何与 media-lookup 解耦

归档是离线、确定性、可幂等重跑的动作；元数据查询是带网络/限流/降级的不确定性动作。两者耦合会让归档器不可单测、不可离线预演、受 TMDB 可用性牵连。解耦后：归档器纯离线；需要元数据时经 `--metadata` 注入或 `pending_lookup` 外移给 media-lookup，职责单一、链路清晰。

### 为何 `series_registry` / `media_cache` 分两个文件

- `series_registry.json` 是 curated 的稳定快路径（常见大系列的模式匹配 + 衍生剧成员登记），随项目发布，受众是所有用户——必须 commit。
- `media_cache.json` 的 `known` 段是运行时自扩充的沉淀（注入元数据解析成功后自动写回），让"查过一次的系列"下次离线即命中，逐步降低对 media-lookup 的依赖，无需人工维护逐文件索引。
- **合并到单文件**会让 `known` 每次运行都涨，git diff 噪声爆炸（违反 A1：结构清晰）。**彻底分离**让 curated 段独立演进（随项目升级，PR review 友好），known 段纯本机状态，gitignore 后零噪声。
- 删掉 `.cache/media_cache.json` 不影响 curated 段，下次运行会重新自学习。


### 为何以"路径规范检测"跳过已归档文件

逐文件库索引（library_index）需要全盘扫描维护、易与真实文件系统不一致。改用"规范命名 + 正确分类目录"的路径检测：已就位文件名自带规范标记（电影含 `(年份)`、剧集含 `SxxExx`），命中即跳过，既幂等又零索引开销；`--rescan` 提供强制重扫出口。

### 为何 pending_lookup 仅限衍生剧疑似未确认

系列/年份/动画类型缺元数据时，可用启发式（中点/冒号）、占位（`(未知年份)`）、文件夹上下文（动画判定）兜底，不影响归档主流程且可后续 `--rescan` 修正。唯独衍生剧疑似但母剧未确认时，乱归会破坏母剧文件夹结构，故外移给 media-lookup 确认；其余降级不阻塞、不噪声。

---

## 十二、错误处理

| 情形 | 处理 |
| --- | --- |
| 目标已存在同名文件 | 默认跳过；`--overwrite` 覆盖 |
| 主文件识别失败 | 回报「未找到可归档视频，疑似假资源」 |
| 迁移失败（权限/只读） | 一句话回报原因，**不删源文件** |
| 父目录不存在 | `ls` 确认；无法创建则回报检查挂载 |
| 衍生剧疑似未确认 | `pending_lookup`，等 Agent 调 media-lookup 补全后重试 |
| ffprobe 不可用 | `[信息]` 降级 `[未标注]`，提示用户手动补充 |
| 剧集误入电影目录 | 检测到 `SxxExx` 归到 `剧集/` 或 `动漫/` |
| 元数据注入缺失某条 | 该条走离线启发式/占位；不影响其余文件归档 |

> TMDB 限流 / 429 / DNS 修复等机制属于 `media-lookup`，见 `media-lookup/references/design.md`，本工具不涉及网络。

---

## 十三、无用文件清理（`--purge-junk`）

下载资源包常夹带推广物料，整理入库后这些残留需清除。`--purge-junk` 在「视频迁移后、清空目录前」统一扫描并删除，预演只报告、`--commit` 才删。

### 13.1 识别规则（`_classify_junk`）

| 类别 | 判定 | 示例 |
| --- | --- | --- |
| 广告图片 | 扩展名为图片(png/jpg/jpeg/webp/bmp/gif) **且** 文件名含推广特征(网址或广告词) | `【更多无水印高清电影请访问 www.BBQDDQ.com】.png` |
| 站点/推广文件 | `.nfo`/`.url`/`.htm`/`.html`（媒体包中恒为发布信息/网页快捷方式，无条件删） | `site.nfo` |
| 推广文本 | `.txt` **且** 内容含明确广告词（仅网址不删，防误删笔记/索引） | `更多高清电影请访问…` |
| 伪装视频 | 视频扩展名 **但** 文件头是图片 magic(`_looks_like_image`: PNG/JPEG/GIF/BMP) | 把 png 改名 `.mkv` |
| sample/预告/花絮 | 视频扩展名 **且** 文件名匹配 `sample/trailer/预告/花絮/bonus/extra/特典/promo` | `Sample.trailer.mkv` |

**保留**：字幕(`.srt`/`.ass`/`.ssa`) 与正片视频一律不动。合法封面图(无推广特征)、非广告 txt 也保留。

### 13.2 伪装视频的双重防线

伪装图片（图片内容冒充 `.mkv`）有两个陷阱：① 会被 `scan_videos()` 当作视频归档入库，污染影音库；② 即使残留也需识别删除。故设两道防线：

1. **扫描期拦截**（`scan_videos`）：枚举视频时读文件头，`_looks_like_image()` 命中即跳过——**绝不当作视频归档**。真正的 mkv/mp4/ts 文件头(EBML/ftyp/0x47)不与图片 magic 冲突，零误判。
2. **清理期删除**（`cleanup_junk_files`）：残留的伪装文件按 `_classify_junk` 识别为「伪装图片(视频扩展名)」删除。

### 13.3 调用顺序与安全

```
迁移视频 -> cleanup_junk_files(扫描 root, 报告或删除) -> cleanup_empty_dirs(删空目录)
```

- 默认**只预演**：`--purge-junk`（不带 `--commit`）仅打印「将删(预演)」清单，不改动文件。
- 删除需显式 `--purge-junk --commit` 双重确认；删除数计入 `--report` 的 `summary.junk_purged`。
- 仅在传入 `root` 范围内扫描，不触及影音库(`--base`) 已归档内容。
- `--purge-junk` 可独立于归档使用：对纯下载暂存目录只清垃圾不整理（不带视频则迁移步骤无操作）。

