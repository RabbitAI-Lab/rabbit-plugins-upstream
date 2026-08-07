---
name: media-lookup
description: 媒体元信息查询 skill（TMDB 为主源 + 豆瓣兜底）。涉及"片名查询/媒体识别/查电影/查剧集/查年份/查类型/查合集/查季集/TMDB 元信息"等需求时优先使用。输入片名[+年份]，返回一条消歧过的标准 JSON 媒体条目（标题/原名/年份/类型/TMDB ID/简介/合集/季集/海报）。支持能力：(1) 自动识别 movie/tv（identify）(2) 强制电影查询（movie）(3) 强制剧集查询（tv）(4) 豆瓣兜底直查免 Key（douban）。只读零副作用；TMDB 不可达自动降级豆瓣。本工具只读 TMDB_API_KEY 环境变量，不关心密钥来源（编排器/agent 首次注入并复用）。
homepage: https://openclaw.example.com/skills/media-lookup
metadata:
  openclaw:
    emoji: 🎬
    requires:
      binaries: [python3]
    primaryEnv: TMDB_API_KEY
  security:
    credentials_usage: |
      TMDB_API_KEY 仅发往 themoviedb.org 官方 API（或豆瓣公开 suggest 接口）。
      本工具只从环境变量读取密钥，不缓存密钥、不关心来源，不发往任何第三方检索站。
      密钥由编排器/agent 在用户首次调用时声明并注入环境变量，后续会话复用，不逐次索取。
    allowed_domains:
      - api.themoviedb.org
      - movie.douban.com
agent_created: true
---

# media-lookup · 媒体元信息查询工具

> **Agent 总规则**（路径 `ls` 校验 / 操作确认 / 凭证自检 / 错误处理 / 对话端点）见 [`../../AGENT.md`](../../AGENT.md)。
> 技术细节 / 健壮性机制（DNS 修复 / 限频 / 429 退避 / fail-fast / 缓存）见 [`references/design.md`](./references/design.md)。
> TMDB→豆瓣降级策略、缓存、输出约定见 [`references/fallback.md`](./references/fallback.md)。

## 1. 职责

影视元数据查询与识别工具（TMDB 为主源 + 豆瓣兜底）。输入片名[+年份]，返回一条消歧过的标准 JSON 媒体条目。
**只读、零副作用**：不写数据库、不发下载请求、不改用户文件（仅写自身缓存）。

## 2. 触发

```
├─ 片名+年份清晰、检索信息充分          -> 跳过本工具（无需查询）
├─ 模糊 / 同名多义 / 需合集·季集·简介·海报  -> identify（主入口）
├─ 已确知是电影 / 剧集、需强类型查询         -> movie / tv
└─ TMDB 不可达（网络/限流）                  -> douban（兜底）
```

## 3. 调用

**环境变量** `TMDB_API_KEY`：由编排器/agent 在用户首次调用时声明并注入，后续复用，本工具只读、不问来源。

**命令行**：

```bash
TMDB_API_KEY=*** python3 media-lookup/tmdb_lookup.py <子命令> <片名> [第3参数]
```

| 子命令 | Key 要求 | 第 3 参数 | 说明 |
|---|---|---|---|
| `identify` | 需 Key | `[年份]` 选填 | **主入口**：自动判定 movie/tv |
| `movie` | 需 Key | `[年份]` 选填 | 强制按电影查询 |
| `tv` | 需 Key | `[年份]` 选填 | 强制按剧集查询 |
| `douban` | 免 Key | `[movie\|tv]` 选填 | 豆瓣直查，不填自动判定 |

> `identify`/`movie`/`tv` 的第 3 参数是**年份**（消歧用）；`douban` 的第 3 参数是**类型过滤**（movie/tv）。

## 4. 输出（标准 JSON）

```json
{
  "media_type": "movie",
  "title": "功夫", "original_title": "Kung Fu Hustle",
  "year": "2004", "tmdb_id": 9470,
  "overview": "1940年代的上海……",
  "collection": null,
  "seasons": [],
  "genres": ["动作", "喜剧", "犯罪"],
  "poster_path": "/x7….jpg",
  "source": "tmdb"
}
```

- `source="douban_fallback"` 时 `tmdb_id=null`，无 `overview`/`genres`/`collection`（仅年份/季/标题）
- 未命中：`{"error":"未找到匹配媒体","query":...,"year":...}`

## 5. 能力边界

- ✅ 媒体识别 / 消歧 / 合集 / 季集 / 海报 / 类型 / 简介
- ❌ 下载 / 归档 / TMDB 之外的元数据源 / 分辨率（TMDB 无此字段）
- 仅写自身缓存（7 天 TTL）；不修改用户文件、不发下载请求
