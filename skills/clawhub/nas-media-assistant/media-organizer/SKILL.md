---
name: media-organizer
description: |
  独立闭环的本地媒体库归档、迁移与文件治理技能。从文件名 / 注入元数据 / ffprobe 提取名称·年份·分辨率·音轨·语言等信息，完成分类（电影/剧集/动漫）+ 系列检测 + 规范命名 + 原子搬家，幂等可重跑。零网络依赖（离线优先）：自身策略无法确诊（如衍生剧疑似未确认）时返回 pending_lookup，由 Agent 调 media-lookup 取回归一化元数据后带 --metadata 重试；从不自行查 TMDB。
metadata:
  openclaw:
    emoji: 🗂️
    requires:
      binaries: [python3]
    primaryEnv: MOVIES_DIR
  security:
    credentials_usage: |
      1. 文件操作仅发生在授权的 NAS 影音根区（MOVIES_DIR）及下载暂存区（XUNLEI_INBOX）。
      2. 迁移采用原子化移动（同文件系统 mv；跨文件系统 cp->校验->rm）；清理仅删本次任务产生的空目录。
      3. 根目录安全保护：严禁影视库下分类根目录（电影/动漫/剧集等）的重命名、移动、删除。
---


# media-organizer · 媒体库归档分类与迁移

> **Agent 总规则**见 [`../../AGENT.md`](../../AGENT.md)。
> 架构 / 处理流程 / 系列检测 / [信息] 回退 / 衍生剧 / 维护指南见 [`references/design.md`](./references/design.md)。
> **命名规则权威定义**（电影 / 剧集 / 动漫 / [信息] 标签）见 [`references/naming.md`](./references/naming.md)。

## 1. 职责

下载后（或全库整理）的本地媒体归档：解析文件名 → 分类（电影/剧集/动漫）→ 系列检测 → 规范命名 → 原子搬家到影音库。
**离线优先、零网络依赖**：能解决的直接 `resolved`；无法确诊时返回 `pending_lookup`，**从不自行查 TMDB**。

## 2. 触发

```
下载完成需归档入库        -> 预演（无 --commit）确认计划 -> --commit 执行
全库/某目录需规范整理     -> 同上；已就位规范文件自动跳过（--rescan 可重扫）
清理广告图/伪装视频       -> --purge-junk 预演确认清单 -> --purge-junk --commit 删除
返回 pending_lookup      -> 调 media-lookup 取回元数据后带 --metadata 重试
```

## 3. CLI

```bash
python3 media-organizer/scripts/organize_media.py <根目录> [选项]
```

| 参数 | 说明 |
| --- | --- |
| `<根目录>` | 待整理路径（文件或文件夹） |
| `--base <路径>` | 影音库根（默认 `/media/movies`，对应 `MOVIES_DIR`） |
| `--commit` | 实际执行移动（**默认只预演**） |
| `--metadata '<JSON>'` / `--metadata-file <路径>` | 注入 media-lookup 归一化元数据（数组） |
| `--tv-format season\|year` | 多季文件夹格式（`season`=第N季 / `year`=按年份） |
| `--overwrite` / `--rescan` / `--no-ffprobe` / `--fast` | 覆盖 / 强制重扫 / 跳 ffprobe / 离线不 pending |
| `--purge-junk` | 删广告图/伪装视频/nfo/推广 txt/sample（配 `--commit` 才删） |
| `--report <路径>` | 完整计划 + 汇总写入 JSON |

### 元数据注入契约

`pending_lookup` 后，Agent 调 `media-lookup` 取回归一化 JSON，组成数组经 `--metadata` / `--metadata-file` 传回：

```json
[
  {"media_type":"movie","title":"功夫","year":"2004","tmdb_id":9470,
   "collection":"合集名或null","genres":["动作","喜剧"],"source":"tmdb"}
]
```

> 索引按 `title`（中文）+ `original_title`（英文）建立，文件名解析的英文标题也能匹配。

## 4. 输出（`--report` JSON）

```jsonc
{
  "plans": [{
    "src": "/abs/source.mkv", "title": "片名", "year": "2024",
    "kind": "movie|tv|anime",
    "info_str": "[国语配音 中文字幕]",
    "status": "resolved",                // resolved | pending_lookup | already_organized
    "need_lookup": null,                 // 仅 pending_lookup 时非空
    "target": "/abs/target/片名 (2024)/片名 (2024) [信息].mkv"
  }],
  "summary": {"total":N,"moved":N,"skipped":N,"pending_lookup":N,"already_organized":N}
}
```

> `status=pending_lookup` 不被移动，等 Agent 补元数据重试；`status=already_organized` 跳过（`--rescan` 可重扫）。


## 5. 能力边界

- **✅ 离线独立**：文件名解析 / 分类 / 系列四级检测 / 衍生剧 / `[信息]` 标签 / 已就位跳过 / 无用文件清理
- **❌ 需 media-lookup**：衍生剧疑似但母剧未在注册表/未注入元数据（`need:["spinoff_check"]`）
- **⚠️ 可降级不 pending**：缺元数据时用启发式/占位处理

## 6. 注意事项

- **先预演后执行**：首次调用不带 `--commit`，确认 `--report` 计划无误后再 `--commit`
