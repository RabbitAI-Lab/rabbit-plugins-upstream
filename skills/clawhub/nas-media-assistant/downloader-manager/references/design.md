# downloader-manager · 技术设计

> **受众**：人 / Codex / 开发者。本文解释技术方案、架构决策、维护指南。
> Agent 调用说明见 [`SKILL.md`](./SKILL.md)。

---

## 一、技术方案

### 1.1 总体定位

下载分发、监控与失败重试闭环。接收下载链接，按规则选择下载器，监控至完成/失败，
输出结构化事件。两种下载器通过适配器模式完全解耦，互不影响。

### 1.2 架构原则：适配器解耦

```
                 路由器（与下载器无关）              适配器（各自独立，互不影响）
        ┌──────────────────────────────┐   ┌──────────────────────────────┐
链接 ──▶ │  router.py                   │──▶│  xunlei_cloud_adapter         │
       │   ① classify_link 链接分类   │   │   ed2k/thunder/magnet/http   │
       │   ② select_adapter 选择      │   │   全协议 · 迅雷会员高速       │
       │   ③ dedup 去重               │   ├──────────────────────────────┤
       │   ④ add_task 提交            │──▶│  qbittorrent_adapter          │
       │   ⑤ monitor 监控+自动切换    │   │   magnet/http .torrent       │
       │   ⑥ event 完成事件/失败回报  │   │   WebUI REST API · BT 生态    │
       └──────────────────────────────┘   └──────────────────────────────┘
```

**核心洞察**：下载器的差异（API 协议、认证方式、路径映射、状态定义）全部封装在各自适配器内。
路由器只调用 `BaseAdapter` 抽象接口（`add_task` / `query_task` / `get_file_path`），不感知具体实现。
新增下载器只需实现 `BaseAdapter` 并在 `_get_adapters()` 注册，路由器逻辑零改动。

### 1.3 下载器与路径

| 下载器 | 协议 | 容器路径 | 宿主路径 |
|--------|------|---------|---------|
| **迅雷 Cloud MCP** | ed2k / thunder / magnet / http(s) | `/media/xunlei-inbox/` | `/volume1/迅雷下载` |
| **qBittorrent** | magnet / http(s) .torrent | `/media/downloads/qBittorrent下载/` | `/volume1/Downloads/qBittorrent下载` |

> 两个适配器各自持有 `download_dir` + `get_file_path()`，路由器不硬编码路径，互不影响。
> 路径映射在 `get_file_path()` 内完成，将下载器内部路径转换为容器内路径供下游使用。
> 以下为默认路径，首次使用时需向用户确认可读写。路径由 NAS 挂载决定，如需变更需调整挂载配置。

**环境变量**：

| 变量 | 用途 | 默认值 | 别名 |
|---------|------|--------|------|
| `XUNLEI_SSE_URL` | 迅雷 MCP SSE 地址 | 无（首次使用时由用户提供） | - |
| `QB_URL` | qBittorrent WebUI | 无（首次使用时由用户提供） | `DOWNLOADER_URL` |
| `QB_USER` / `QB_PASS` | qB 凭据 | `admin` / `adminadmin`（首次使用时由用户提供） | `DOWNLOADER_USER` / `DOWNLOADER_PASS` |
| `QB_SAVE_PATH` | qB 保存路径（容器内） | `/downloads` | - |

> 迅雷 MCP SSE URL 格式：`https://api-xmodels.xunlei.com/models/sse/<token>`
> token 由用户从 NAS 迅雷 Web 界面获取，编排器组装为完整 SSE URL 注入 `XUNLEI_SSE_URL`（详见 §1.7）。

### 1.4 适配器选择与自动切换

#### 选择规则：迅雷会员优先

| 链接类型 | 首选 | 回退 |
|---------|------|------|
| `ed2k://` / `thunder://` | 迅雷 | 无（qB 不支持） |
| `magnet://` / `http(s)://` | 迅雷 | qBittorrent |
| 本地 `.torrent` 文件 | qBittorrent | 无（迅雷不支持文件上传） |

`select_adapter()` 逻辑：

1. 调用方显式指定 `--adapter` 且适配器支持该链接类型 -> 使用指定适配器
2. 迅雷可用且支持该链接类型 -> 迅雷（会员高速，全协议）
3. qBittorrent 可用且支持该链接类型 -> qBittorrent
4. 均不匹配 -> 返回 None（报错「无适配器支持链接类型」）

#### 自动切换（迅雷 -> qBittorrent）

监控中检测到迅雷慢速或卡死时，自动删除迅雷任务并切换 qBittorrent（仅 magnet/http，仅一次）：

| 触发条件 | 阈值 | 动作 |
|---------|------|------|
| 卡死 | 20 × 30s = 10 分钟进度无变化 | 删迅雷任务 -> 创建 qB 任务 |
| 慢速 | 10 × 30s = 5 分钟平均速度 < 50KB/s | 同上 |
| 已切换仍失败 | - | 输出 `DL_DEAD`，建议换链 |

> ed2k/thunder 无法切换到 qB（不支持），直接输出 `DL_DEAD`。
> 阈值常量 `STALL_THRESHOLD` / `SLOW_THRESHOLD` / `SLOW_POLL_COUNT` 可在 `router.py` 的 `cmd_monitor()` 调整。

#### 换链闭环设计

采用事件驱动架构，downloader-manager 只输出结构化事件，不关心下游如何消费：

```
add(url, name)
  │
  ├─ monitor -> completed -> download_completed 事件（含 file_path）
  │                                    Agent 据此决定后续编排
  │
  └─ monitor -> failed -> download_failed 事件（含 code + suggested_action）
                                    Agent 据 suggested_action 决定：换链 / 重试 / 回报用户
```

**失败处理策略**：

| 失败类型 | 策略 | 说明 |
|---------|------|------|
| `DL_DEAD` / `DL_HASH` / `DL_BLOCKED` | 建议换链 | 链接本身有问题，换一个链接重试 |
| `DL_NET` | 重试同链（≤2 次） | 网络波动，同链可能恢复 |
| `DL_AUTH` / `DL_DISK` / `DL_UNKNOWN` | 回报用户 | 配置/环境问题，需人工介入 |

> 终止条件：成功 / `retry_count >= 3` / 用户主动停止（不碰下载目录源文件）。

### 1.5 去重策略

提交新任务前依次检查，命中任一则跳过（`_find_duplicate()`）：

1. **JobManager 活跃任务**：URL 完全匹配 -> 返回已有 job_id
2. **适配器任务列表**：同名任务且未完成 -> 返回已有 task_id

> 双重检查避免同一资源在两个下载器或同一下载器内重复下载。

### 1.6 健壮性机制

| 机制 | 实现 | 说明 |
|------|------|------|
| 适配器完全解耦 | 每个适配器独立初始化、独立健康检查 | 一方失败不影响另一方 |
| 健康检查缓存 | `health_check.py` 60s TTL | 避免高频请求下载器 API |
| 自动切换兜底 | 迅雷慢速/卡死自动切 qB（仅一次） | ed2k/thunder 无法切换时直接回报 |
| 去重防重复 | 提交前双重检查（JobManager + 适配器） | 避免同一资源重复下载 |
| Job 持久化 | `JobManager` JSON 文件持久化 | 进程重启不丢失记录，支持事后追问 |

### 1.7 配置生命周期

**首次注入约定**：所有配置由编排器/Agent 在用户首次调用下载功能时获取并注入环境变量，
后续会话复用，不逐次索取。技能只读环境变量，不关心来源。

**迅雷 MCP token 获取流程**：

1. 用户登录 NAS 迅雷 Web 界面
2. 获取 MCP 连接 token
3. 编排器组装 SSE URL（`https://api-xmodels.xunlei.com/models/sse/<token>`）并注入 `XUNLEI_SSE_URL`

| 迅雷版本 | 需用户提供 | 地址获取 |
|---------|-----------|---------|
| NAS专用版 | token | skill 自动发现 |
| Docker版 | token + 服务地址 | 用户提供 |

> 未配置则迅雷适配器不可用，仅 qBittorrent 可用。

**qBittorrent 配置**：用户提供 WebUI 地址 + 账号 + 密码，注入 `QB_URL` / `QB_USER` / `QB_PASS`
（兼容 `DOWNLOADER_*` 别名）。默认值仅限内网，投产前需替换。

**下载路径确认**：首次使用时需向用户确认以下路径可读写：

| 下载器 | 容器路径 | 宿主路径 |
|--------|---------|---------|
| 迅雷 | `/media/xunlei-inbox/` | `/volume1/迅雷下载` |
| qBittorrent | `/media/downloads/qBittorrent下载/` | `/volume1/Downloads/qBittorrent下载` |

> 路径由 NAS 挂载决定，skill 只使用已挂载的路径。如需变更，需调整 NAS 挂载配置并同步更新适配器的 `download_dir`。

### 1.8 元数据携带链路（media-search -> downloader -> media-organizer）

下载器不解析、不依赖元数据内容，只做**透明携带**：把 `add --metadata` 收到的 media-lookup 归一化结果原样存入 `Job.meta["media_metadata"]`，完成/失败事件原样回传，供编排器在下载结束后转交 `media-organizer --metadata`。

```
media-lookup(归一化JSON)
   |
media-search ----(选定链路 + 元数据)----> router.py add --metadata/--metadata-file
                                              |  _load_metadata(): 单对象/数组统一为 list
                                              v
                                        JobManager.create(meta={"media_metadata":[...]})
                                              |  持久化到 /tmp/downloader_jobs.json
                                              v
                                        monitor -> download_completed 事件
                                              |  "metadata": _job_metadata(job)  (回传 list)
                                              v
                                  编排器 --metadata-file <写回的文件> --> media-organizer
```

| 环节 | 实现 | 位置 |
| --- | --- | --- |
| 接收 | `_load_metadata(args)`：`--metadata`(JSON 串) 或 `--metadata-file`；单对象/数组统一为 list | router.py |
| 沉淀 | `jm.create(..., meta={"media_metadata":[...]})`；`Job.meta` 已是预留 dict 字段 | job_manager.py |
| 回传 | `download_completed` / `download_failed` 事件 `"metadata": _job_metadata(job)`；无则 `[]` | router.py |
| 透传 | downloader 不校验 schema、不读字段；编排器负责写回文件喂给 media-organizer | - |

> 设计上 downloader 对元数据"零理解"：即便 media-organizer 契约演进，downloader 也无需改动，只要能 JSON 序列化即可。

---

## 二、核心规则（设计决策）

### 为何使用适配器模式完全解耦

两种下载器 API 协议差异极大（迅雷 MCP SSE vs qBittorrent REST API），认证方式、路径映射、
状态定义各不相同。将差异封装在适配器内，路由器只调 `BaseAdapter` 抽象接口，互不影响。
一方不可用不影响另一方，新增下载器只需实现 `BaseAdapter` 并注册，路由器逻辑零改动。

### 为何迅雷会员优先

用户已开通迅雷会员，享有高速下载通道与全协议支持（ed2k/thunder/magnet/http）。
默认优先迅雷最大化下载速度；迅雷不可用或慢速时自动回退/切换 qBittorrent（BT 生态更稳定）。

### 为何自动切换仅一次

避免两个下载器之间无限切换循环（迅雷慢 -> 切 qB -> qB 也慢 -> 切回迅雷）。
切换一次后如果 qB 仍慢速/卡死，直接输出 `DL_DEAD` 建议换链，不再重试。

### 为何 Job 持久化

下载任务可能耗时数小时，监控进程可能中断。`JobManager` 以 JSON 文件持久化任务状态，
进程重启后可恢复查询。`job_id` 贯穿全流程，支持用户事后追问。

### 为何 .torrent 文件强制 qBittorrent

迅雷 Cloud MCP 不支持本地文件上传，只能接收 URL/链接。
本地 `.torrent` 文件自动走 qBittorrent（支持文件上传 + BT 种子管理）。

### 为何元数据"透明携带"而非 downloader 解析

元数据的语义（movie/tv、collection、seasons）只对归档器有意义，对下载器是噪声。若 downloader 解析元数据，会把 media-lookup 的契约变化耦合进下载链路，违反适配器解耦原则。改为"收-存-传"三步透明携带：downloader 只保证 JSON 不丢、不解释，编排器在 `download_completed` 后把 `metadata` 写回文件喂给 `media-organizer --metadata`。这样下载链路保持纯粹，元数据契约演进只影响两端（media-lookup 出 / media-organizer 入）。

### 为何事件驱动而非回调

downloader-manager 作为独立插件，只对自己能力负责。输出结构化事件（`download_completed` /
`download_failed`），由 Agent/编排器决定后续编排（归档、换链、回报用户等）。
这种松耦合让插件可独立测试、独立演进，不依赖下游实现。

---

## 三、维护指南

- **新增下载器**：实现 `BaseAdapter` 抽象接口（`add_task` / `query_task` / `list_tasks` /
  `cancel_task` / `health_check` / `supports_link_type` / `get_file_path`），在 `router.py`
  的 `_get_adapters()` 注册即可，路由器逻辑零改动。
- **迅雷 SSE 地址变更**：更新环境变量 `XUNLEI_SSE_URL`，无需改代码。
- **qBittorrent 凭据变更**：更新环境变量 `QB_URL` / `QB_USER` / `QB_PASS`，无需改代码。
- **切换阈值调整**：编辑 `router.py` 的 `cmd_monitor()` 中 `STALL_THRESHOLD`（卡死轮次）和
  `SLOW_THRESHOLD`（慢速阈值）。
- **失败码扩展**：在 `_emit_failure()` 新增 code，在换链闭环逻辑中补充对应动作。
- **路径变更**：下载目录路径变更时，只需修改对应适配器的 `download_dir` 类属性，
  路由器不硬编码路径。

---

## 四、资源索引

| 文件 | 用途 |
|------|------|
| `scripts/router.py` | **下载路由器**：链接分类、适配器选择、去重、监控、自动切换、完成/失败事件输出 |
| `scripts/base.py` | 核心类型定义（`LinkType` / `TaskState` / `TaskStatus`）+ `BaseAdapter` 抽象接口 + 链接分类器 |
| `scripts/job_manager.py` | JSON 持久化的 Job 状态机管理（queued -> downloading -> completed/error） |
| `scripts/health_check.py` | 适配器健康检查（60s 缓存，避免高频探测） |
| `scripts/adapters/qbittorrent_adapter.py` | qBittorrent WebUI REST API 适配器（SID 认证 + .torrent 上传） |
| `scripts/adapters/xunlei_cloud_adapter.py` | 迅雷 Cloud MCP SSE 适配器（全协议，会员高速） |
| `scripts/utils/mcp_sse_client.py` | MCP-over-SSE JSON-RPC 客户端（会话复用 + 自动重连） |
| `scripts/utils/thunderlink.py` | thunder:// ed2k:// 专用链接编解码（纯本地，零依赖） |
