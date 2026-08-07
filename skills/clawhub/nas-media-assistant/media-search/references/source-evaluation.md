# 数据源实测评估 (source_evaluation.md)

> 评估对象：`assets/config.json` 中**当前启用**的 5 个网页源（`souxunlei / yilu / nyaa / dongmanhuayuan / xl720`）。
> 评估时间：2026-08-02（同期下线 btsearch 与 heimacili，本文件保留其结论作为历史记录）。
> 评估方法：3 个真实查询（中文电影/中文剧集/日文剧集），本地直接 `python3 -c` 调用各 parser，记录耗时、命中数与评分前 3 质量。

---

## 1. 整体数据

| id | 优先级 | 平均耗时 | 中文电影 | 中文剧集 | 日文剧集 | 平均命中 | 最高 q | 推荐度 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **souxunlei** | 2 | **2.6s** | 10 | 10 | 10 | **10.0** | **77.7** | ⭐⭐⭐⭐⭐ |
| **yilu (1lou)** | 3 | 6.7s | 5 | 5 | 5 | 5.0 | 76.6 | ⭐⭐⭐⭐ |
| **dongmanhuayuan** | 5 | 4.9s | 10 | 10 | 10 | 10.0 | 10.5* | ⭐⭐（仅动漫）|
| **nyaa** | 6 | 2.1s | 9 | 1 | 10 | 6.7 | 70.0 | ⭐⭐⭐（国际）|
| **xl720** | 4 | 9.2s | 3 | 2 | 2 | 2.3 | 35.0 | ⭐（弱）|

> `*` dongmanhuayuan 命中文剧查询时返回大量"海贼王/舰娘"无关结果，是列表前 N 命中，命中数高≠相关度高。

---

## 2. 逐源结论

### 2.1 ⭐⭐⭐⭐⭐ souxunlei（搜迅雷）— 主力源
- **链接形态**：`magnet:?xt=urn:btih:...`（hash 直接由 URL 解析，无需详情页）
- **耗时**：1.6~3.6s（**全源最快**）
- **命中数**：每次稳定 10 条
- **质量**：质量分数 64~77，几乎全是 4K/1080p + 完整季
- **元数据**：搜索页带文件大小 + 文件数，无需进详情页
- **结论**：**中文内容主力源，建议留在 tier-1**

### 2.2 ⭐⭐⭐⭐ yilu（1lou）— 高质量种子
- **链接形态**：`.torrent` 种子（无 magnet，需 downloader 拉种子后喂 qBittorrent）
- **耗时**：5.4~7.6s
- **命中数**：恒为 `TARGET_RESULTS=5`（parser 主动截断，减少详情页请求）
- **质量**：质量分数 62~76，标题信息最丰（含帧率/集数/字幕/编码/大小）
- **failover**：7 镜像（me/one/icu/xyz/info/vip/pro），parser 内自动切
- **推荐下载器**：qBittorrent（站方提示不支持迅雷）
- **结论**：**高质量种子主源，建议留在 tier-1**
- **NAS 内网可达性**：用户报告 1lou 在外网可能不可达（failover 多镜像能覆盖部分场景；最终方案：部署 sing-box）

### 2.3 ⭐⭐⭐ nyaa — 国际向补充
- **链接形态**：`magnet:?xt=urn:btih:...`
- **耗时**：1.5~2.4s
- **命中数**：中文 0~1 条；日文/英文 10 条
- **质量**：质量分数 70（命中时），格式规范
- **结论**：**国际内容（动漫/日剧/美剧）补位；中文检索贡献极低，可留 tier-2**
- **副作用**：日文检索时与 dongmanhuayuan 重叠度高

### 2.4 ⭐⭐ dongmanhuayuan（动漫花园）— 动漫专项
- **链接形态**：`magnet:?xt=urn:btih:...` + 部分 playpage
- **耗时**：3.5~7.5s
- **命中数**：恒 10 条，但**匹配中文剧查询时返回大量无关动漫**（海贼王/舰娘）
- **质量**：质量分数 10.5（基础分，无 4K/1080p 标识），是因为"标题里没匹配关键词就降权"
- **结论**：**仅在 type=anime 时作为高质量源；中文影视查询基本是噪声**
- **建议**：把 `type=anime` 路由到它，`type=movie/tv` 自动排除（aggregator 阶段用 `query_type` 过滤）

### 2.5 ⭐ xl720（迅雷电影天堂）— 待观察/可能下线
- **链接形态**：`magnet`（从详情页抽）
- **耗时**：**9.0s（最慢）**
- **命中数**：2~3 条
- **质量**：质量分数 10.5~35.0，**质量最低**
- **结论**：**耗时高、命中少、质量低。建议降级到 tier-2 末尾或临时 `enabled: false`**

### 已下线源（2026-08 移除，结论保留）

#### btsearch — Playwright 缺，沙箱/普通环境不可用
- parser 内 `from playwright.sync_api import sync_playwright` 直接 `ImportError`，返回 `[]`（静默失败）
- 启用需 `pip install playwright + playwright install chromium`（~150MB），多数环境不装
- 2026-08 已移除 parser 文件 + config 条目

#### heimacili（黑马磁力）— Cloudflare 拒
- Cloudflare 高级反爬，自动化访问均返回首页空结果；需要 `cf_clearance` cookie + 仍可能失效
- 2026-08 已移除 parser 文件 + config 条目

---

## 3. 建议的 tier 调整

### 3.1 当前 priority（保持现状）
```
tier-1 (priority 1~3): souxunlei / yilu / nyaa
tier-2 (priority 4~5): dongmanhuayuan / xl720
```
**问题**：tier-2 含 xl720（弱）+ dongmanhuayuan（对中文查询噪声大）；tier-1 三源都是稳定主力

### 3.2 建议：调整 priority 与 enabled

| id | priority / enabled | 理由 |
| --- | --- | --- |
| souxunlei | 1 / ✅ | 中文主力，tier-1 第一位 |
| yilu | 2 / ✅ | 高质量种子，tier-1 |
| nyaa | 3 / ✅ | 国际内容补位，tier-1 |
| dongmanhuayuan | 4 / ✅ | 动漫专项，tier-2 |
| xl720 | 5 / ✅ | 弱源，tier-2 兜底 |

调整后：
- **tier-1**（最常用 3 源）：souxunlei → yilu → nyaa
  - 中文查询：souxunlei 主供 + yilu 高质量
  - 国际查询：nyaa 主供 + souxunlei 兜底
- **tier-2**（按需回退 2 源）：dongmanhuayuan → xl720
  - dongmanhuayuan 命中动漫专项
  - xl720 弱但留作兜底

### 3.3 验证

调整后在用户已部署的 NAS 上跑：

```bash
# 看 tier-1 健康度
python3 scripts/health_check.py status
# 看单次 dispatch 命中的 tier 与 skipped
python3 scripts/search_dispatcher.py '{"title":"流浪地球","type":"movie","year":"2023"}' 2>&1 | grep -E 'tier|skip'
```

---

## 4. 反爬与维护成本

| id | 反爬强度 | cookie 需求 | 维护成本 | 备注 |
| --- | --- | --- | --- | --- |
| souxunlei | 🟢 弱 | 无 | 🟢 低 | 纯 hex 编码 + requests |
| yilu | 🟢 弱 | 无 | 🟡 中 | 7 镜像 + 解析附件链接（结构变化时改） |
| nyaa | 🟢 弱 | 无 | 🟢 低 | requests + bs4 |
| dongmanhuayuan | 🟢 弱 | 无 | 🟢 低 | requests + bs4 |
| xl720 | 🟡 中 | 无 | 🟡 中 | 详情页抽 magnet，结构变化要改 |

> "反爬强度"指 parser 实现时遇到的难度，不完全等同于站点对人类的难度。

---

## 5. 与 media-organizer 衔接

| source 链接形态 | 落地文件名 | 走哪条下载链路 |
| --- | --- | --- |
| `magnet:?xt=urn:btih:...` | `<原名>.torrent` 或 qBittorrent 自动命名 | qBittorrent / 迅雷 |
| `https://.../attach-download-*.htm`（1lou） | `<原名>.torrent` | qBittorrent |
| `playpage` URL | - | **当前 downloader-manager 不支持**，aggregator 已过滤 |
| `direct` URL | 原文件名 | qBittorrent |

> 1lou 的 `.torrent` 链接需要 downloader 主动下载后**导入** qBittorrent（不是直接喂给 qBittorrent），这点已在 downloader-manager 设计文档说明。

