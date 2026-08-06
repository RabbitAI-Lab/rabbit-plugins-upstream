---
name: downloader-manager
description: |
  下载分发、监控与失败重试闭环。接收下载链接与元数据，按「迅雷优先」规则派发至
  迅雷 Cloud MCP 或 qBittorrent，慢速/卡死自动切换，去重防重复，完成输出结构化事件，
  失败结构化回报并换链重试。两种下载器通过适配器模式完全解耦：一方不可用不影响另一方。
  本技能是独立下载管理插件，只对自己能力负责。
homepage: https://openclaw.example.com/skills/downloader-manager
metadata:
  openclaw:
    emoji: ⬇️
    requires:
      binaries: [python3]
    primaryEnv: QB_URL
  security:
    credentials_usage: |
      1. 下载请求仅发往用户自有 NAS 下载器（qBittorrent WebUI / 迅雷 Cloud MCP），不涉及第三方。
      2. 迅雷 MCP token 由用户从 NAS 迅雷 Web 界面获取，编排器注入环境变量，不落盘、不上传。
      3. qBittorrent 凭据用于本地局域网 WebUI 认证，默认值仅限内网。
    allowed_domains:
      - '*.local'
      - '*.lan'
      - '192.168.0.0/16'
      - '*.xunlei.com'
agent_created: true
---

# downloader-manager · 下载分发与监控闭环

> **Agent 总规则**见 [`../../AGENT.md`](../../AGENT.md)。
> 架构 / 适配器解耦 / 元数据透明携带 / 维护指南见 [`references/design.md`](./references/design.md)。
> 协议路由（迅雷 vs qB / 自动切换）见 [`references/routing.md`](./references/routing.md)。
> 失败码（DL_DEAD/AUTH/DISK 等）与处置策略见 [`references/failure-handling.md`](./references/failure-handling.md)。

## 1. 职责

下载分发、监控与失败重试闭环。接收下载链接（磁力/直链/ed2k/thunder/本地 .torrent），
按规则选择下载器派发任务，监控至完成或失败，输出结构化事件供下游消费。
两种下载器**完全解耦**：迅雷 Cloud MCP（全协议，会员高速）与 qBittorrent（BT 生态），一方不可用不影响另一方。

## 2. 触发

```
├─ 有磁力/直链/ed2k/thunder 链接需要下载   -> add（自动选择下载器）
├─ 有本地 .torrent 文件需要下载           -> add（自动走 qBittorrent）
├─ 调用方指定了特定下载器                  -> add --adapter <xunlei|qbittorrent>
├─ 需要查询下载状态                       -> status / list
└─ 需要监控任务至完成（输出事件）          -> monitor
```

## 3. 工作流

```
add(url, name, metadata?) -> classify_link -> select_adapter
  -> dedup -> add_task（返回 job_id，metadata 存入 Job.meta）

monitor(job_id) -> 轮询（30s 间隔）
  ├─ 完成 -> download_completed 事件（含 file_path + metadata）
  ├─ 迅雷慢速/卡死 -> 自动切换 qBittorrent（仅一次）
  └─ 失败/超时 -> download_failed 事件（含 code + suggested_action）
```

## 4. 调用

**环境变量**：

| 变量 | 用途 | 必填 |
|---|---|---|
| `XUNLEI_SSE_URL` | 迅雷 MCP SSE 地址 | 至少其一 |
| `QB_URL` / `QB_USER` / `QB_PASS` | qBittorrent WebUI 地址+凭据 | 至少其一 |
| `QB_SAVE_PATH` | qB 保存路径（容器内，默认 `/downloads`） | 否 |

> 协议路由 / 自动切换阈值 / 凭据获取流程见 [`references/routing.md`](./references/routing.md)。

**命令行**：

```bash
# 添加任务（自动选择 + 去重 + 创建 Job）
python3 downloader-manager/scripts/router.py add "magnet:?xt=urn:btih:..." --name "电影名 (2024)"

# 携带 media-lookup 元数据（完成时回传给 media-organizer --metadata）
python3 downloader-manager/scripts/router.py add "magnet:..." --name "电影名 (2024)" \
  --metadata '[{"media_type":"movie","title":"电影名","year":"2024","source":"tmdb"}]'

# 其他命令：--adapter 覆盖 / .torrent 强制 qB / status / list / monitor / health
python3 downloader-manager/scripts/router.py {add ...|status <job_id>|list|monitor <job_id> --timeout 3600|health}
```

## 5. 输出事件

**完成事件** `download_completed`：

```json
{
  "event": "download_completed",
  "job_id": "dl_20260804_abc123",
  "client": "qbittorrent",
  "file_path": "/media/downloads/qBittorrent下载/电影名 (2024)/电影名 (2024).mkv",
  "name": "电影名 (2024)", "size": 8053063680,
  "metadata": [{"media_type":"movie","title":"电影名","year":"2024","source":"tmdb"}]
}
```

> `file_path` 为容器内绝对路径。`metadata` 为 `add` 时携带的 media-lookup 归一化元数据（数组，回传给 `media-organizer --metadata`）；未携带时为 `[]`。

**失败事件** `download_failed` 详见 [`references/failure-handling.md`](./references/failure-handling.md)。

## 6. Agent 约束

1. **迅雷会员优先** / **`--adapter` 可覆盖** / **.torrent 强制 qB**（迅雷不支持文件上传）
2. **去重自动**（URL + 名称双重检查） / **自动切换仅一次**（避免无限循环）
3. **job_id 串联全程** / **根目录保护**（不创建/移动/删除根目录）

## 7. 能力边界

- ✅ 链接分类 / 适配器路由 / 去重 / 监控 / 自动切换 / 失败码输出
- ❌ 媒体识别（上游）/ 检索（上游）/ 归档（下游）
- **元数据透明携带**：`--metadata` 原样存入 Job、完成/失败事件原样回传，downloader 不解析不依赖
- **不碰源文件**：失败或用户停止时不删除已下载的文件
