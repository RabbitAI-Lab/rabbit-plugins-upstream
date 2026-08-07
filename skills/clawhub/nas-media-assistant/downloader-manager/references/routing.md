# downloader-manager/references/routing.md · 迅雷 vs qBittorrent 协议路由

> **受众**：编排器 / Agent / 开发者。本文件承载下载器选择规则与自动切换策略。
> 完整技术方案与适配器细节见 `downloader-manager/references/design.md`。

---

## 一、选择规则：迅雷会员优先

| 链接类型 | 首选 | 回退 | 说明 |
| --- | --- | --- | --- |
| `ed2k://` / `thunder://` | 迅雷 | **无**（qB 不支持） | 迅雷 Cloud MCP 全协议 + 会员高速 |
| `magnet://` / `http(s)://` | 迅雷 | qBittorrent | 迅雷不可用/慢速时回退（仅一次） |
| 本地 `.torrent` 文件 | qBittorrent | **无** | 迅雷不支持文件上传,强制 qB |

`select_adapter()` 判定顺序：
1. 调用方显式指定 `--adapter` 且适配器支持该链接类型 → 使用指定适配器
2. 迅雷可用且支持该链接类型 → 迅雷（会员高速，全协议）
3. qBittorrent 可用且支持该链接类型 → qBittorrent
4. 均不匹配 → 返回 `None`（报错「无适配器支持链接类型」）

## 二、自动切换（迅雷 → qBittorrent）

监控中检测到迅雷慢速或卡死时，**自动删除迅雷任务并切换 qBittorrent**（仅 magnet/http，仅一次）：

| 触发条件 | 阈值 | 动作 |
| --- | --- | --- |
| **卡死** | 20 × 30s = 10 分钟进度无变化 | 删迅雷任务 → 创建 qB 任务 |
| **慢速** | 10 × 30s = 5 分钟平均速度 < 50KB/s | 同上 |
| **已切换仍失败** | - | 输出 `DL_DEAD`,建议换链 |

> ed2k/thunder 无法切换到 qB（不支持），直接输出 `DL_DEAD`。
> 阈值常量 `STALL_THRESHOLD` / `SLOW_THRESHOLD` / `SLOW_POLL_COUNT` 在 `router.py` 的 `cmd_monitor()` 可调。

## 三、去重策略（双重检查）

提交新任务前依次检查，命中任一则跳过（`_find_duplicate()`）：

1. **JobManager 活跃任务**：URL 完全匹配 → 返回已有 `job_id`
2. **适配器任务列表**：同名任务且未完成 → 返回已有 `task_id`

> 双重检查避免同一资源在两个下载器或同一下载器内重复下载。
