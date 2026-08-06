# references/lifecycle.md · 5 阶段生命周期长版

> **受众**：编排器 / Agent。根 `SKILL.md` 只列精简主线，本文件承载异常分支、重试链路与状态机细节。
> 设计依据：v2 决策 #4（流程图）——根 SKILL.md 留主线，长版进 references。

---

## 一、5 阶段全流程（带异常分支）

```
用户需求（任意对话端点）
  │
  ▼
① 查询归一化 + 按需识别
  │
  │  路由子链路:
  │   - 链路0 media-lookup（按需）: 片名+年份清晰 / 结果文件名信息充分 -> 直进 ②
  │   - 链路0（模糊·同名多义·需合集/季集/简介）-> media-lookup identify
  │   - 链路0（TMDB 不可达）-> 自动豆瓣兜底（`source=douban_fallback`）
  │   - 链路0（仍同名多义）-> 列候选让用户消歧
  │
  ▼
② 多链路检索（并行扇出 + 合并）
  │
  │  主链路:
  │   - 链路1 media-search: 分层检索（tier1 优先，不足回退 tier2）
  │   - title_parser 从结果文件名提取 年份/清晰度/编码/音轨/字幕/大小
  │   - aggregator 去重 + 评分 + 过滤（枪版/低相关度/低质）
  │   - 排序：HD 优先（同分按 credibility）
  │
  │  异常分支:
  │   - 候选稀薄/仍同名多义 -> 回调 media-lookup 补全/消歧 → 重新跑 ②
  │   - 全部源失败 -> 报告「未检索到《XX》磁力资源」,引导换关键词/放宽清晰度
  │   - 用户原话「换一批」-> 调整 `top_n` 或换关键词重检索
  │
  ▼
③ 下载任务（downloader-manager）
  │
  │  协议路由（迅雷会员优先）:
  │   - ed2k / thunder -> 迅雷（无回退）
  │   - magnet / http   -> 迅雷首选;迅雷不可用/慢速回退 qBittorrent（仅一次）
  │   - 本地 .torrent   -> 强制 qBittorrent（迅雷不支持文件上传）
  │   - `--adapter` 显式指定时覆盖默认
  │
  │  任务管理:
  │   - dedup 去重（URL + 名称双重检查）-> 命中则跳过并返回已有 job_id
  │   - JobManager 持久化（JSON 文件）-> 进程重启可恢复查询
  │   - 元数据透明携带（`--metadata`）-> 完成后原样回传编排器
  │
  │  监控事件:
  │   - 完成 -> `download_completed` 事件（含 `file_path` + `metadata`）-> 调 ④
  │   - 失败 -> `download_failed` 事件（含 `code` + `suggested_action`）-> 决策
  │
  │  失败决策:
  │   - `DL_DEAD` / `DL_HASH` / `DL_BLOCKED` -> 换链（回 ② 取下一候选）,最多 3 次
  │   - `DL_NET` -> 重试同链（≤ 2 次）
  │   - `DL_AUTH` / `DL_DISK` / `DL_UNKNOWN` -> 回报用户,不换链
  │
  ▼
④ 文件整理（media-organizer）
  │
  │  流程:
  │   - 解析文件名 -> 分类（电影/剧集/动漫）-> 系列检测 -> 规范命名
  │   - [信息] 标签三级回退（原始文件名 -> ffprobe/mediainfo -> [未标注]）
  │   - 原子搬家（同 FS mv / 跨 FS cp->校验->rm）
  │   - 整理确认: 预演（无 --commit）→ 用户确认 → --commit 执行
  │
  │  异常分支:
  │   - 衍生剧疑似未确认 -> `pending_lookup` -> 调 media-lookup 补全 -> 带 --metadata 重试
  │   - 缺元数据（系列/年份/动画）-> 启发式/占位/默认处理（**不** pending,避免噪声）
  │   - 目标已存在 -> 默认跳过;`--overwrite` 覆盖
  │   - 主文件识别失败 -> 报告「未找到可归档视频，疑似假资源」
  │
  │  附加动作:
  │   - `--purge-junk` 清理广告图/伪装视频/站点 nfo/推广 txt/sample（需 `--commit`）
  │   - 触发 Emby / Plex / Jellyfin / Radarr + Sonarr 刷新
  │
  ▼
⑤ 回报对话端点
  │
  │  成功: 「✅ 已入库：功夫 (2004) -> /media/movies/电影/功夫 (2004)/功夫 (2004)[国英多音轨+简繁英双语].mkv」
  │  失败: 「❌ 下载失败 (DL_DEAD)，已自动换链 2/3 次，仍未成功，建议手动提供链接」
  │  待确认: 「⚠️ 整理计划有 N 项需要确认 (--report 见附件)」
  │
  └─→ 结束（或回到 ② 换链 / 回到 ④ 整理）
```

---

## 二、状态机（Job / Plan / 候选）

### 2.1 任务 Job 状态（downloader-manager）

```
queued ──(add)──> downloading ──(完成)──> completed
                     │                       (or)
                     │                  already_organized
                     │                       (media-organizer 判定)
                     │
                     ├─(失败)──> error ──(retry ≤ 3)──> queued (换链)
                     │
                     └─(用户停止)──> cancelled
```

| 状态 | 含义 | 下一步 |
|---|---|---|
| `queued` | 已加入 JobManager,等待提交到下载器 | 提交 → `downloading` |
| `downloading` | 下载器已接受任务,监控中 | 完成 → `completed` / 失败 → `error` |
| `completed` | 下载完成,产出文件可整理 | 调 `media-organizer` 整理 |
| `error` | 下载失败,`failure.code` 标记 | 按 `suggested_action` 决策 |
| `cancelled` | 用户主动停止 | 不碰下载目录源文件 |

### 2.2 整理 Plan 状态（media-organizer）

| status | 含义 | 是否移动 |
|---|---|---|
| `resolved` | 元数据齐全,可归档 | ✅（待 `--commit`） |
| `pending_lookup` | 衍生剧疑似未确认,需补元数据 | ❌ 等 `--metadata` 重试 |
| `already_organized` | 已在正确分类目录 + 规范文件名 | ❌ 跳过（`--rescan` 可重扫） |

> pending_lookup 闭环: 预演无 `--metadata` → 输出 `need_lookup` → Agent 调 media-lookup 取回 → 带 `--metadata` 重试 → `resolved` → 确认 → `--commit`。

### 2.3 候选 candidates 状态（media-search）

返回 JSON 中 `candidates[]` 是"通过过滤+排序"的结果,`excluded[]` 是"被过滤掉"的结果（每项含 `url` + `reason`）。
- 选号续派时回查会话上下文里的 `candidates` 列表,按编号派发
- 换链时从 `candidates` 顺序取下一条（已被 excluded 的跳过）
- 用户「换一批」-> 调 `media-search` 重跑（可调 `top_n` 或换关键词）

---

## 三、异常路径速查表

| 阶段 | 异常 | 处置 | 失败兜底 |
|---|---|---|---|
| ① 识别 | TMDB 不可达 | 自动豆瓣兜底（`source=douban_fallback`） | 仍无 → 报告错误,让用户消歧 |
| ① 识别 | 同名多义 | 列出候选让用户选 | 用户放弃 → 终止 |
| ② 检索 | 全部源失败 | 报告「未检索到《XX》磁力资源」 | 引导换关键词/放宽清晰度 |
| ② 检索 | 候选稀薄 | 仍返回,提示「换一批?」 | 用户接受稀薄结果 → 派发 |
| ③ 下载 | 死链/卡死/慢速 | 自动切换 qB（仅一次）| 仍失败 → 换链（最多 3 次） |
| ③ 下载 | ed2k/thunder 不可用 | 无回退,直接 `DL_DEAD` | 换链 / 报告用户 |
| ③ 下载 | 凭据/磁盘错误 | 不换链,报告用户 | 等待用户修复 |
| ③ 下载 | 全部候选耗尽 | 报告「已尝试 X 链均失败」 | 引导用户手动提供链接 |
| ④ 整理 | 衍生剧疑似 | `pending_lookup` 等补元数据 | 用户放弃 → `--fast` 降级 |
| ④ 整理 | 目标已存在 | 默认跳过 | `--overwrite` 覆盖 |
| ④ 整理 | 主文件识别失败 | 报告「疑似假资源」 | 跳过该文件 |
| ④ 整理 | ffprobe 不可用 | `[信息]` 降级 `[未标注]` | 提示用户手动补充 |
| ⑤ 回报 | 端点不可达 | 保留状态,下次会话同步 | 等待端点恢复 |

---

## 四、重试与退避策略

### 4.1 检索重试
- 单源失败: 重试 2 次,指数退避（1s / 2s / 4s）
- tier-1 全挂: 自动回退 tier-2
- 全部源全挂: 报告「全源失败」,检查 `references/search-strategy.md`

### 4.2 下载重试
- 迅雷慢速: 5 分钟平均速度 < 50KB/s 触发切换
- 迅雷卡死: 20 × 30s = 10 分钟进度无变化触发切换
- 自动切换仅一次: qB 仍失败 → `DL_DEAD` 不再切回
- 换链: 最多 3 次（`retry_count >= 3` 终止）

### 4.3 整理重试
- pending_lookup: Agent 调 media-lookup 补全后带 `--metadata` 重试（**同一根目录**）
- `--rescan`: 强制重扫已就位文件
- `--commit` 失败: 报告原因,下次会话可继续（幂等）
