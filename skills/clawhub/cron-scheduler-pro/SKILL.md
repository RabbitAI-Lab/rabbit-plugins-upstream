---
slug: cron-scheduler-pro
name: cron-scheduler-pro
version: "1.0.0"
displayName: 定时调度专家
summary: 本地优先的周期任务引擎，时区锁定、一次性任务自清理、并发安全，告别漏跑与堆积。
license: MIT
description: |-
  定时调度专家为 AI Agent 提供本地优先、无云依赖的周期任务调度能力。它把"每隔X做Y"的意图固化为可信任的执行契约，支持每日/每周/每月/自定义间隔四种调度类型，并内置时区锁定、一次性任务自动清理、并发写安全、下次运行预览与失败重试。

  核心能力：周期任务捕获（add_job）、下次运行预览（next_run）、暂停/恢复/归档、运行历史与统计、一次性任务自清理、时区锁定与校验、并发文件锁、失败自动重试与熔断。

  适用场景：Agent 定期巡检、日报生成、数据同步、健康检查、个人提醒、一人公司自动化流水线。

  差异化：相比只提供脚本入口的原始方案，本技能新增时区锁定（调度前强制确认时区，杜绝"9点到底是哪个9点"）、一次性任务自清理（run-once 任务成功后自动归档，避免堆积）、并发写安全（文件锁防止 add/update 死锁）、失败重试与熔断（连续失败超阈值自动暂停）、以及运行可视化时间线（一眼看到接下来 24 小时跑什么）。

  触发关键词：定时, 调度, 周期任务, cron, 提醒, schedule, recurring, job, timer, interval
tags:
- 自动化
- 定时调度
- 任务管理
tools:
- read
- exec
---

# 定时调度专家

把"每两小时检查一次收件箱"这种模糊意图，变成可信任、可审计、可预览的执行契约。本技能解决五个核心痛点：**时区漂移**（"9点"到底是哪个时区）、**任务漏跑**（调度器没跑或跑了不知道）、**一次性任务堆积**（提醒完了任务不清理）、**并发死锁**（add 后立刻 update 导致锁冲突）、**失败无感知**（任务挂了没人知道）。

## 核心设计哲学

1. **重复只捕获一次，然后信任**：调度一旦建立，Agent 不必每次心跳都重新判断"该不该跑"。
2. **调度是契约**：不只是提醒，而是对时间的执行承诺。
3. **可见性优先**：用户随时能知道"接下来跑什么、上次跑了什么"。
4. **本地优先**：所有数据存本地，无云同步、无第三方服务。

## 存储结构

所有数据本地存储，按职责分文件：

```
~/.skill-platform/workspace/memory/cron/
├── jobs.json      # 任务定义（active/paused/archived）
├── runs.json      # 运行历史（最近100条）
├── stats.json     # 统计数据（成功率、平均耗时）
└── .lock          # 文件锁（并发写保护）
```

无外部同步，无云存储，无第三方 cron 服务。

## 任务状态机

```
active ──pause──→ paused ──resume──→ active
   │                                   │
   └──────────archive──────────────────→ archived
```

| 状态 | 含义 | 是否触发 |
|:-----|:-----|:---------|
| `active` | 调度生效中 | 是 |
| `paused` | 临时暂停 | 否 |
| `archived` | 不再活跃，保留历史 | 否 |

## 调度类型

| 类型 | 示例 | 说明 |
|:-----|:-----|:-----|
| `daily` | 每天 09:00 | 固定每日时刻 |
| `weekly` | 每周一 10:00 | 固定每周时刻 |
| `monthly` | 每月1号 08:00 | 固定每月时刻 |
| `interval` | 每 2 小时 | 固定间隔 |
| `once` | 2026-07-18 15:30 | 一次性（成功后自动归档） |

## 时区锁定（核心差异化）

"每天 9 点提醒我喝水"——9 点是东京还是纽约？这是漏跑最高频的原因。

### 强制时区确认

首次创建任务前，必须确认时区并写入记忆：

```bash
python3 tools/cron/set_timezone.py --timezone "Asia/Shanghai"
```

写入 `MEMORY.md`：
```
Timezone: Asia/Shanghai (UTC+8)
```

### 创建任务时时区校验

```python
# add_job.py 内部逻辑
def validate_timezone(job):
    tz = get_stored_timezone()
    if not tz:
        raise SchedulerError(
            "时区未锁定。请先运行 set_timezone.py 设置时区。\n"
            "否则 '9点' 的含义将不确定，导致漏跑。"
        )
    if job.schedule_type == 'daily':
        # 确认: "9点 Shanghai 时间?" 
        confirm = f"将按 {tz} 时区调度：每天 {job.time}。确认？"
        if not user_confirm(confirm):
            return None
```

### 跨时区任务

对于跨时区团队，任务可指定独立时区：

```bash
python3 tools/cron/add_job.py \
  --name "daily-standup" \
  --type daily \
  --time "09:00" \
  --timezone "Asia/Tokyo" \
  --task "发起每日站会提醒"
```

## 核心工作流

### 1. 捕获周期任务

```bash
python3 tools/cron/add_job.py \
  --name "inbox-check" \
  --type interval \
  --every "2h" \
  --task "检查收件箱并汇总未读邮件"
```

### 2. 预览下次运行

```bash
python3 tools/cron/next_run.py
```

输出可视化时间线：

```
未来 24 小时调度时间线 (Asia/Shanghai)
═══════════════════════════════════════════════════
现在  10:00 ●
      12:00 │ inbox-check (interval 2h)
      14:00 │ inbox-check
      16:00 │ inbox-check
      18:00 │ inbox-check
      09:00 │ daily-briefing (daily) [次日]
═══════════════════════════════════════════════════
下一次运行: inbox-check, 距今 2 小时 (12:00 CST)
```

### 3. 暂停与恢复

```bash
python3 tools/cron/pause_job.py --name "inbox-check"
python3 tools/cron/resume_job.py --name "inbox-check"
```

### 4. 查看单个任务

```bash
python3 tools/cron/show_job.py --name "inbox-check"
```

```
任务: inbox-check
状态: active
类型: interval (每 2 小时)
时区: Asia/Shanghai
创建: 2026-07-18 10:00
上次运行: 2026-07-18 10:00 (成功, 耗时 3.2s)
下次运行: 2026-07-18 12:00
重试次数: 0/3
任务内容: 检查收件箱并汇总未读邮件
```

### 5. 查看全部任务

```bash
python3 tools/cron/list_jobs.py
```

```
活跃任务 (3):
  inbox-check    [interval 2h]  下次: 12:00  成功率: 100%
  daily-briefing [daily 09:00]  下次: 明日   成功率: 98%
  weekly-report  [weekly Mon]   下次: 周一   成功率: 100%
已暂停 (1):
  monitor-api    [interval 5m]  已暂停 2 小时
已归档 (5): 使用 --archived 查看
```

## 一次性任务自清理（核心差异化）

原始方案中一次性提醒跑完后仍留在 jobs.json，时间一长堆积成垃圾。本技能强制：

```python
# 一次性任务定义
job = {
    "name": "remind-water",
    "type": "once",
    "at": "2026-07-18T15:30:00+08:00",
    "task": "提醒喝水",
    "delete_after_run": True   # 强制 True，不可关闭
}
```

运行成功后：
1. 从 `active` 移到 `archived`
2. 保留 7 天后自动物理删除
3. 运行记录保留在 `runs.json`

```bash
# 手动清理过期归档
python3 tools/cron/cleanup.py --older-than 7d
```

## 并发写安全（核心差异化）

原始方案的 add-then-update 模式在并发时会死锁。本技能用文件锁解决：

```python
import fcntl

def write_jobs(jobs_data):
    lock_path = CRON_DIR / ".lock"
    with open(lock_path, "w") as lock_file:
        # 阻塞式获取排他锁
        fcntl.flock(lock_file, fcntl.LOCK_EX)
        try:
            # 原子写入：写临时文件 → rename
            tmp = CRON_DIR / "jobs.json.tmp"
            tmp.write_text(json.dumps(jobs_data, indent=2))
            tmp.replace(CRON_DIR / "jobs.json")
        finally:
            fcntl.flock(lock_file, fcntl.LOCK_UN)
```

**单步创建原则**：所有属性在 `add_job` 时一次传入，禁止"先 add 再 update"两步操作。

## 失败重试与熔断

```python
# 运行失败时的重试策略
RETRY_CONFIG = {
    "max_retries": 3,
    "backoff": [60, 300, 900],   # 1分钟、5分钟、15分钟
    "circuit_breaker": {
        "threshold": 5,           # 连续失败5次
        "action": "pause",        # 自动暂停任务
        "notify": True            # 通知用户
    }
}
```

熔断触发后：
1. 任务自动转为 `paused`
2. 记录熔断原因到 `runs.json`
3. 下次 Agent 交互时通知用户："任务 X 因连续失败 5 次已自动暂停，请检查"

## 运行历史与统计

`runs.json` 保留最近 100 条运行记录：

```json
{
  "job_name": "inbox-check",
  "started_at": "2026-07-18T10:00:00+08:00",
  "finished_at": "2026-07-18T10:00:03+08:00",
  "duration_ms": 3200,
  "status": "success",
  "retries": 0,
  "error": null
}
```

```bash
# 查看统计
python3 tools/cron/stats.py
```

```
调度统计 (最近 7 天)
═══════════════════════════════════════
总运行: 84 次
成功:   81 次 (96.4%)
失败:    3 次
平均耗时: 4.2s

失败详情:
  inbox-check  2026-07-16 14:00  网络超时 (已重试2次后成功)
  daily-briefing 2026-07-15 09:00  LLM 调用失败 (已熔断暂停)
```

## 场景化指南

### 场景 A：Agent 心跳优化

不要在心跳里做昂贵检查，改为调度任务：

```bash
# 替代每 30 分钟心跳检查收件箱
python3 tools/cron/add_job.py \
  --name "inbox-check" --type interval --every "2h" \
  --task "检查收件箱并汇总"

# 心跳只做轻量的"该跑什么了"
python3 tools/cron/next_run.py --due-only
```

### 场景 B：精确一次性提醒

```bash
python3 tools/cron/add_job.py \
  --name "meeting-reminder" \
  --type once \
  --at "2026-07-18T15:25:00+08:00" \
  --task "5 分钟后开始项目评审会议，会议室 A"
# 提醒后自动归档，无需手动清理
```

### 场景 C：日报生成

```bash
python3 tools/cron/add_job.py \
  --name "daily-report" \
  --type daily \
  --time "18:00" \
  --timezone "Asia/Shanghai" \
  --task "生成今日工作日报并保存到 reports/目录"
```

### 场景 D：健康检查带熔断

```bash
python3 tools/cron/add_job.py \
  --name "api-health" \
  --type interval \
  --every "5m" \
  --task "探测 API 健康端点，失败则告警" \
  --max-retries 3 \
  --circuit-breaker 5
```

## FAQ

**Q：任务到时间了没跑？**
A：检查四点：① 任务是否 `active`；② 时区是否正确（`next_run.py` 显示的下次时间对吗）；③ Agent 心跳是否在运行（本引擎依赖 Agent 唤醒）；④ 是否被熔断暂停（看 `stats.py`）。

**Q：一次性任务能取消吗？**
A：能。`pause_job.py` 或 `archive_job.py` 在触发前取消。若已触发但任务还在执行，无法中断。

**Q：jobs.json 损坏怎么办？**
A：本技能写入用临时文件+rename 原子操作，正常不会损坏。若意外损坏，`runs.json` 可部分重建任务历史。建议定期 `cleanup.py --backup`。

**Q：多个 Agent 共享调度吗？**
A：默认按用户隔离（每人一份 jobs.json）。共享需挂载共享目录并依赖文件锁，但心跳驱动仍是各 Agent 独立。

**Q：interval 任务的起始点怎么算？**
A：从创建时刻起算。如 10:00 创建"每 2 小时"，则 12:00、14:00... 触发。若需对齐到整点，用 `--align` 参数。

**Q：如何迁移到新机器？**
A：复制整个 `cron/` 目录即可。时区信息在 `MEMORY.md`，一并复制。

## 故障排查

| 症状 | 可能原因 | 处置 |
|:-----|:---------|:-----|
| 任务不触发 | 时区未锁定 | 运行 `set_timezone.py`，检查 `next_run.py` |
| 任务触发但没执行 | Agent 心跳未运行 | 确认 Agent 在线，本引擎需 Agent 唤醒 |
| `next_run` 时间不对 | 时区或夏令时问题 | 确认时区，检查是否 DST 切换 |
| jobs.json 写入失败 | 文件锁未释放 | 删除 `.lock` 文件（确认无进程占用） |
| 一次性任务堆积 | `delete_after_run` 被关闭 | 本技能强制开启，检查是否用了旧版 |
| 连续失败无告警 | 熔断阈值过高 | 调整 `--circuit-breaker` 阈值 |

## 性能优化

1. **心跳轻量化**：心跳只调 `next_run.py --due-only`（只查到期任务），不做全量扫描。
2. **历史裁剪**：`runs.json` 默认保留 100 条，超出自动裁剪最旧。
3. **统计延迟计算**：`stats.py` 不实时计算，用缓存结果，每 10 次运行刷新一次。
4. **批量预览**：`next_run.py` 一次计算所有任务的下次运行，避免逐个查询。

## 与其他技能协作

- 配合安全情报雷达：把 `scan.sh` 注册为 interval 任务。
- 配合定时守护技能：本技能管"调度"，守护技能管"被调度的脚本如何写得可靠"。
- 配合定时大师技能：本技能是本地引擎，大师技能是平台级 cron 的使用指南。

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（需能运行 Python 脚本）
- **操作系统**：Linux / macOS / Windows（文件锁在 Windows 上用 msvcrt 替代 fcntl）
- **Python**：3.8+（仅标准库，无外部包）

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Python 3 | 运行时 | 必需 | 系统自带或 python.org |
| fcntl | 标准库 | Linux/Mac 必需 | Python 自带 |
| msvcrt | 标准库 | Windows 必需 | Python 自带 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 本技能为纯本地调度引擎，无需任何外部 API Key。
- 被调度的任务内容由 Agent 执行，任务本身可能调用其他 API（由具体任务决定）。

### 可用性分类
- **分类**：MD+EXEC（Markdown 指令 + Python 脚本执行）
- **说明**：Agent 通过调用 Python 脚本管理调度，本引擎负责时区、并发、清理与统计。
