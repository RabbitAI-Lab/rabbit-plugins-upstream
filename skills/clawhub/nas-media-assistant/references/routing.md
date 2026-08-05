# references/routing.md · 模式判定与路由子技能传参

> **受众**：编排器 / Agent。根 `SKILL.md` 只列 5 模式速查表，本文件承载完整判定逻辑与路由子技能时的传参约定。
> 设计依据：v2 决策 #3（路由表）——根 SKILL.md 留速查，详情进 references。

---

## 一、模式判定决策表（长版）

### 1.1 5 模式定义

| 模式 | 触发短语（典型） | 工作模式 | 后续动作 |
|---|---|---|---|
| **下载模式** | `下/下载/搞个/帮我下 + 片名[+质量]` | 检索+下载一气呵成；顶层候选命中即下 | 调 `media-search` 跑出候选，**顶层命中直接派发**到 `downloader-manager`，不列列表 |
| **检索模式** | `查/检索/找下 + 片名` / 纯片名 | 仅检索，呈现带号列表等用户选号 | 调 `media-search` 跑出候选 → 渲染带号列表 → 用户选号后由编排器派发 |
| **选号续派** | `下 1` / `下 2` / `第一个` / `三` / `都要` | 从上轮会话 `candidates` 中按编号派发 | 回查会话上下文 `candidates[N]` → 派发到 `downloader-manager` |
| **整库/单文件整理** | `整理/归类/入库/归档` | 离线预演 → 用户确认 → `--commit` | 调 `media-organizer` |
| **重整/失败换链** | `重新整理/换链/失败` | 换链重试或重扫 | 按上下文重派或 `media-organizer --rescan` |

> 「纯片名」（如"流浪地球"、"乡村爱情 18"）按"检索模式"处理——判定为**想看有什么资源**。

### 1.2 判定流程（自上而下匹配，命中即停）

```
用户原话
  │
  ▼
① 含「下/下载/搞个/帮我下」?       ─是─→ 下载模式
  │ 否
  ▼
② 含「查/检索/找/搜」?              ─是─→ 检索模式
  │ 否
  ▼
③ 纯片名（无动词）?                  ─是─→ 检索模式
  │ 否
  ▼
④ 含数字编号（1/2/3 / 第一个/三）?   ─是─→ 选号续派
  │ 否
  ▼
⑤ 含「整理/归类/入库/归档/规范」?    ─是─→ 整理模式
  │ 否
  ▼
⑥ 其它 / 不明                       → 引导用户明确意图
```

> **判定辅助**：判定前先看会话上下文是否含最近的 `candidates` 列表（含则优先选号续派判定）；
> 多个判定分支同时满足时按"下载 > 检索 > 选号 > 整理"优先级。

---

## 二、路由子技能传参约定

### 2.1 → media-lookup（链路0·按需）

调用方：编排器（识别/消歧/补全场景）。

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `title` | str | ✅ | 中文/英文片名 |
| `year` | str | ❌ | 消歧用，未知则不传 |
| `subcommand` | enum | ✅ | `identify`（主入口） / `movie` / `tv` / `douban` |
| `force_douban` | bool | ❌ | 强制走 `douban` 子命令（TMDB 不可达时兜底） |

返回：标准 JSON 媒体条目（schema 见 `media-lookup/SKILL.md` §5）。
失败：未命中返回 `{"error":...}`，Agent 应透传给编排器，不得自行编造元数据。

### 2.2 → media-search（链路1·检索）

调用方：编排器（下载模式 / 检索模式 / 选号续派的取号环节）。

```json
{
  "title": "消失的人",
  "type": "movie",
  "year": "2026",
  "quality": "1080p",
  "codec": "x265",
  "language": "双语"
}
```

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `title` | str | ✅ | 归一化后的片名（建议先经 media-lookup） |
| `type` | enum | ✅ | `movie` / `tv` / `anime` |
| `year` | str | ❌ | 同名消歧，未知不传 |
| `quality` / `codec` / `language` | str | ❌ | 覆盖默认偏好（`DEFAULT_QUALITY`/`PREFERRED_CODEC`/`PREFERRED_LANG`） |

返回：`{ candidates:[...], excluded:[...], stats:{...}, link:"web", from_cache:bool }`（schema 见 `media-search/SKILL.md` §5）。

### 2.3 → downloader-manager（链路3·派发）

调用方：编排器（顶层候选命中即下 / 选号续派）。

```bash
python3 downloader-manager/scripts/router.py add "<url>" \
  --name "<电影名 (年份)>" \
  --metadata '[{...media-lookup 归一化 JSON...}]'
```

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `url` | str | ✅ | magnet / ed2k / thunder / http(s) / 本地 .torrent 路径 |
| `--name` | str | ✅ | 任务显示名（建议"片名 (年份)"格式） |
| `--metadata` / `--metadata-file` | JSON | ❌ | media-lookup 归一化元数据，**透明携带**到 downloader 完成事件，喂给 `media-organizer --metadata` |
| `--adapter` | enum | ❌ | `xunlei` / `qbittorrent`，覆盖默认选择规则 |

返回：CLI 立即输出 `job_id`（如 `dl_20260804_abc123`），完整事件由 `monitor` 命令输出。

### 2.4 → media-organizer（链路4·归档）

调用方：编排器（下载完成事件触发 / 用户手动整理）。

```bash
python3 media-organizer/scripts/organize_media.py <根目录> [选项]
```

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| 位置参数 | path | ✅ | 待整理路径（文件或文件夹） |
| `--base` | path | ❌ | 影音库根（默认 `/media/movies`） |
| `--metadata` / `--metadata-file` | JSON | ❌ | media-lookup 归一化元数据（数组） |
| `--commit` | flag | ❌ | 实际执行移动（默认只预演） |
| `--overwrite` | flag | ❌ | 目标存在时覆盖 |
| `--rescan` | flag | ❌ | 不跳过已就位文件 |
| `--purge-junk` | flag | ❌ | 清理无用残留（需 `--commit` 才真删） |
| `--report` | path | ❌ | 把完整计划 + 汇总写入 JSON |

**契约**：
- 预演（无 `--commit`）→ 返回 `--report` JSON + 控制台计划，**不改文件**
- 收到 `pending_lookup` → Agent 调 media-lookup 取回元数据后带 `--metadata` 重试
- `--commit` → 按计划执行移动 + 可选清理

### 2.5 → 跨链路衔接

| 上游 | 触发 | 携带 | 喂给下游 |
|---|---|---|---|
| media-lookup | 归一化 JSON | `title/year/tmdb_id/collection/seasons/genres` | media-search（type 判定）/ media-organizer（`--metadata`） |
| media-search | 选定 `candidates[N]` | `url/name/link_type/credibility/quality_score` | downloader-manager（`add --metadata`） |
| downloader-manager | `download_completed` 事件 | `file_path + metadata` | media-organizer（`--metadata-file`） |
| downloader-manager | `download_failed` 事件 | `failure.code + metadata` | 编排器按 `suggested_action` 决定：换链 / 重试 / 回报用户 |

---

## 三、边界 case 与异常路径

### 3.1 同名多义
- 「功夫」电影 vs 剧集：先调 `media-lookup identify` → 拿到 `media_type` 消歧
- 「乡村爱情 18」：年份 + 季集号足以消歧（`title_parser` 可从结果文件名补全年份）
- 仍歧义：列出候选让用户选（不要 Agent 自行猜）

### 3.2 检索失败 / 候选稀薄
- 全部源无结果 → 报告「未检索到《XX》磁力资源」，建议换关键词/放宽清晰度
- 候选稀薄（< top_n）→ 仍返回，不强制补足；用户在带号列表可"换一批"
- 引擎不可达 / 403 → 记录链路失败继续其它源；全失败回报检查 `docs/README.md` 配置

### 3.3 下载失败
- 死链（0 seeders / 卡死 / 慢速）→ `DL_DEAD` → 编排器调 media-search 取下一候选换链
- 网络波动（`DL_NET`）→ 重试同链（≤ 2 次）
- 配置问题（`DL_AUTH` / `DL_DISK` / `DL_UNKNOWN`）→ 回报用户，不换链

### 3.4 整理失败
- 衍生剧疑似未确认 → `pending_lookup` → 调 media-lookup 取回母剧元数据后带 `--metadata` 重试
- 缺元数据（系列/年份/动画类型）→ 启发式/占位/默认处理，**不**pending（避免噪声）
- 目标已存在 → 默认跳过；`--overwrite` 覆盖
