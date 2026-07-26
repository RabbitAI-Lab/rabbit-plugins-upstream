---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: 041680e517c313fbd9efd67f2de7c4dd_e30bbf07774a11f1a7da5254006c9bbf
    ReservedCode1: xGef11LMz8nYzpomqM7PwaDcF9sBnel90iAVuQ3mvsBXGCyi/cNnYYk04zGtDqWZNETya3JEla8kTHv6dHwne/xpqRvpFXCtOfDULjDdLIu+MCso1RF68e+eNL+0RGjV8cs6S9tS/T6r6lzWahskX1xugynxH9NtksxpXyKhlA6qVYUUMa0bcAfF6C0=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: 041680e517c313fbd9efd67f2de7c4dd_e30bbf07774a11f1a7da5254006c9bbf
    ReservedCode2: xGef11LMz8nYzpomqM7PwaDcF9sBnel90iAVuQ3mvsBXGCyi/cNnYYk04zGtDqWZNETya3JEla8kTHv6dHwne/xpqRvpFXCtOfDULjDdLIu+MCso1RF68e+eNL+0RGjV8cs6S9tS/T6r6lzWahskX1xugynxH9NtksxpXyKhlA6qVYUUMa0bcAfF6C0=
---

# Smart Memory v3 — General Best Practices 复核报告

> 审查日期：2026-07-04  
> 项目路径：`D:\.agents\memory\smart-memory\v3`  
> 审查框架：general-best-practices (8 维度)  
> 源代码范围：全部 `.py` + `schema.sql` + 测试文件

---

## 一、各维度评分总览

| 维度 | 评分 | 简要 |
|------|------|------|
| 代码质量 | 7/10 | 命名清晰、docstring 完备，但部分函数超长、存在时区不一致 |
| 架构 | 7/10 | 三层分离明确，但缺乏依赖注入和接口抽象 |
| 测试 | 6/10 | 覆盖全面，但混用自定义框架、缺少纯单元测试 |
| 安全 | 9/10 | 全覆盖参数化 SQL + CHECK 约束，无硬编码凭据 |
| 性能 | 6/10 | 有缓存策略，但无连接池和性能基准 |
| 可观测性 | 4/10 | 仅 migrate.py 使用 logging，无结构化日志和 metrics |
| 文档 | 4/10 | 代码内 docstring 良好，但缺少 README 和架构文档 |
| 版本控制/工具链 | 2/10 | 无依赖声明、linting 配置和 CI 流水线 |

---

## 二、已有改进说明

以下改进已在 B1-B11 优化批次中完成，本报告不再重复建议：

| 编号 | 内容 | 涉及文件 |
|------|------|----------|
| B1 | schema.sql 表/字段级中文注释 | `schema.sql` |
| B2 | 7 个核心类统一 `ClassName(field=value)` 格式 `__repr__` | `cues.py`, `signals.py`, `gc.py`, `manifest.py`, `recall.py`, `decide.py`, `precondition.py` |
| B3 | `migrate.py` 中 7 处 `print()` 改为 `logging` | `migrate.py` |
| B4 | 边界测试：空 DB recall、重复插入幂等性、importance/retention 0/1 | `test_data_layer.py` |
| B5 | 全项目 docstring 扫描，确认公开方法已完整 | — |
| B6 | stdlib import 按字母序重排 | `cues.py` |
| B7 | recall.py 提取 10 个模块级常量 | `recall.py` |
| B8 | `search_by_tags` 的 `keywords LIKE` 改为 `json_each()` | `cues.py` |
| B9 | 触发器 `WHEN` 子句补充到 schema.sql | `schema.sql`, `db.py` |
| B10 | 新增 `idx_signals_cue_type` 和 `idx_cues_status_retention` 复合索引 | `schema.sql`, `db.py` |
| B11 | `datetime.utcnow()` → `datetime.now(timezone.utc)` 3.13 兼容 | `signals.py` 等 |

---

## 三、尚存问题与改进建议

### [P0] 核心缺陷 — 缺少基础工程化配置

#### 3.1 缺少 README

**文件**: 项目根目录 `D:\.agents\memory\smart-memory\v3\`

**问题**: 项目无 `README.md` 文件。新开发者无法了解项目用途、安装方式、目录结构和使用方法。

**建议**: 新增 README.md，至少包含：
- 项目简介（线索驱动的渐进式记忆系统）
- 环境依赖（Python ≥ 3.10, jieba, pyyaml）
- 快速开始（初始化、记录、召回三个最小步骤）
- 目录结构说明
- CLI 命令速览表

---

#### 3.2 缺少依赖声明文件

**问题**: 项目无 `requirements.txt` 或 `pyproject.toml`。外部依赖（`jieba`, `pyyaml`）未显式声明，安装完全依赖隐式环境。

**建议**: 在项目根目录创建 `requirements.txt`：

```
jieba>=0.42.1
pyyaml>=6.0
```

或创建 `pyproject.toml` 并声明 `[project] dependencies`。

---

#### 3.3 缺少 linting / formatting 配置

**问题**: 无 `.flake8`、`.pylintrc`、`pyproject.toml [tool.ruff]` 或 `pre-commit` 配置。代码风格一致性依赖人工维护。

**建议**: 在项目根目录创建 `.flake8`：

```ini
[flake8]
max-line-length = 100
ignore = E501, W503
exclude = .git,__pycache__,docs
```

或创建 `pyproject.toml` 配置 ruff：

```toml
[tool.ruff]
line-length = 100

[tool.ruff.lint]
select = ["E", "F", "I", "N", "W"]
ignore = ["E501"]
```

---

#### 3.4 缺少 CI 流水线配置

**问题**: 无 CI 配置文件（如 `.github/workflows/test.yml`）。测试仅可通过手动运行 `python test_all.py` 触发。

**建议**: 新增 CI 配置，至少运行 `python test_all.py`。

---

### [P1] 重要问题 — 影响一致性与可维护性

#### 3.5 时间戳时区不一致：`_now_iso()` 使用本地时间

**文件**: 下列位置使用 `datetime.now()` 产生本地时间，而项目其余部分统一使用 UTC：

| 文件 | 行号 | 代码 |
|------|------|------|
| `precondition.py` | 21-22 | `return datetime.now().strftime(...)` |
| `manifest.py` | 17-18 | `return datetime.now().strftime(...)` |
| `migrate.py` | 110 | `now = datetime.now().strftime(...)` |

**问题**: `signals.py` 的 `record` 方法写入 UTC 时间戳（通过 SQLite `datetime('now')`），但 `precondition_cache.evaluated_at` 和 `manifest.updated` 却写入本地时间。这导致：
- 跨时区部署时 `precondition_cache` TTL 计算错误
- `decay-report` 中 `hours_since_update` 计算偏移

**修复优先级**: P1。对每个文件：
1. `from datetime import datetime, timezone`
2. `_now_iso()` 改为 `return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")`

---

#### 3.6 CLI 命令处理函数严重超长

**文件**: `memory.py`

| 函数 | 行数 | 超出 30 行 |
|------|------|------------|
| `main()` | ~130 行 | **+100** |
| `cmd_recall()` | ~110 行 | **+80** |
| `cmd_scan_round()` | ~80 行 | **+50** |
| `cmd_stale_detect()` | ~60 行 | **+30** |
| `cmd_decay_report()` | ~55 行 | **+25** |

**问题**: 超出 GB 规范"函数通常不超过 30 行"的建议。CLI 函数混合了参数解析、业务逻辑和输出格式化。

**建议**: 将每个命令拆分为：
- 一个薄的 `cmd_*()` 适配器（仅处理 args → 调用核心逻辑 → 格式化输出）
- 核心逻辑下沉到对应模块（如 `recall.py` 的 `RecallEngine` 已有，但很多格式化代码仍在 `memory.py`）

---

#### 3.7 缺少依赖注入，所有类在构造函数中硬编码 `get_connection()`

**文件**: `cues.py`, `signals.py`, `recall.py`, `gc.py`, `manifest.py`, `precondition.py`, `decide.py`

**模式**（以 `CueStore` 为例）：
```python
class CueStore:
    def __init__(self):
        self._conn = get_connection()  # 全局单例
```

**问题**: 
- 所有单元测试必须通过 monkey-patch `v3.db.get_connection` 才能替换连接
- 无法同时操作多个数据库实例
- 违反"依赖注入"原则（Program to interfaces, not implementations）

**建议**（渐进式）：
```python
class CueStore:
    def __init__(self, conn: sqlite3.Connection | None = None):
        self._conn = conn if conn is not None else get_connection()
```
这样测试时可直接注入 SQLite `:memory:` 连接，无需 patch。

---

#### 3.8 `test_db.py` 和 `test_data_layer.py` 使用自定义 `check()` 而非 `unittest.TestCase`

**文件**: `test_db.py`（218 行）、`test_data_layer.py`（424 行）

**问题**: 自定义检查函数跳过了标准 unittest 框架的 test discovery、setUp/tearDown、assert* 方法和 CI 兼容报告。

**建议**: 重构这两个文件为标准 `unittest.TestCase` 子类：

```python
class TestDBInit(unittest.TestCase):
    def setUp(self):
        if os.path.exists(DB_PATH):
            os.remove(DB_PATH)

    def test_init_db_returns_connection(self):
        conn = init_db()
        self.assertIsNotNone(conn)

    def test_init_db_is_idempotent(self):
        init_db()
        init_db()  # 不应抛异常
```

同时调整 `test_all.py` 中 `_run_standalone_test` 的分支逻辑，将这两个文件改走 `unittest discover`。

---

### [P2] 次要改进 — 长期工程化方向

#### 3.9 测试未区分快慢

**问题**: `test_all.py` 将单元测试和 CLI 集成测试混在同一轮。CLI 集成测试（`run_cli_tests`）每次启动子进程、操作真实数据库和文件系统，耗时远长于单元测试。规范建议"分离快速单元测试与较慢的集成测试"。

**建议**: 在 `test_all.py` 中添加 `--skip-cli` / `--fast` 参数，或拆分为两个独立测试入口。

---

#### 3.10 缺少结构化日志

**文件**: 除 `migrate.py` 外的所有核心模块

**问题**: 
- `migrate.py` 是唯一使用 `logging.getLogger(__name__)` 的模块
- 其余模块通过返回值 + CLI print 传递信息，核心逻辑层无任何日志
- 规范建议"使用结构化日志（生产环境 JSON 格式）"

**建议**: 为核心模块（`cues.py`, `recall.py`, `decide.py`, `gc.py`）添加 logger，在关键路径记录 INFO/WARNING：

```python
import logging
logger = logging.getLogger(__name__)
```

最低限度在 SQL 写操作和数据状态变更（`mark_stale`, `gc`, `restore`）处添加 `logger.info`。

---

#### 3.11 无连接池

**文件**: `db.py`

**问题**: `get_connection()` 返回全局单例连接。在 CLI 场景足够了，但一旦有多线程并发访问需求（如 web 服务包装），单连接会成为瓶颈。规范建议"为数据库和网络连接使用连接池"。

**建议**: 如果未来扩展为服务化，考虑引入 `sqlite3` 的 `check_same_thread=False` + `threading.local()` 或专用连接池。

---

#### 3.12 `checkpoint_db` 未导出

**文件**: `__init__.py`

**问题**: `db.py` 中定义了 `checkpoint_db()` 函数（用于 WAL checkpoint），但 `__init__.py` 的 `__all__` 仅导出 `init_db`, `get_connection`, `close_db`，排除了 `checkpoint_db`。

**建议**: 在 `__init__.py` 第 8 行添加：

```python
from .db import init_db, get_connection, close_db, checkpoint_db
```

---

#### 3.13 `memory.py` 中脆弱的 import 路径操作

**文件**: `memory.py` 第 33-36 行

```python
_PKG_DIR = str(Path(__file__).resolve().parent)
_PARENT_DIR = str(Path(__file__).resolve().parent.parent)
if _PARENT_DIR not in sys.path:
    sys.path.insert(0, _PARENT_DIR)
```

**问题**: 依赖 `sys.path.insert` 是脆弱的方式。如果 `memory.py` 被作为模块导入而非脚本运行，路径操作可能失效。

**建议**: 在 `v3` 目录下创建 `__main__.py`，将 `memory.py` 的 `main()` 移到其中，通过 `python -m v3` 运行。这样 Python 自动将 `_PARENT_DIR` 加入 `sys.path`。

---

#### 3.14 缺少变更日志

**问题**: 项目无 `CHANGELOG.md`。B1-B11 优化批次、架构演进等重要变更无记录。

**建议**: 创建 `CHANGELOG.md`，记录版本号和关键变更摘要。

---

## 四、优先级执行路线图

| 阶段 | 优先级 | 改进项 | 预计工作量 |
|------|--------|--------|-----------|
| 立刻 | P0 | 创建 README.md | 30 min |
| 立刻 | P0 | 创建 requirements.txt | 5 min |
| 立刻 | P0 | 创建 .flake8 或 ruff 配置 | 10 min |
| 本周 | P1 | 修复 `_now_iso()` 时区不一致 (3 处) | 15 min |
| 本周 | P1 | 拆分 `memory.py` 超长函数 | 60 min |
| 本周 | P1 | 添加构造函数依赖注入 (`conn=None`) | 45 min |
| 本周 | P1 | 重构 test_db.py + test_data_layer.py 为 unittest.TestCase | 60 min |
| 本月 | P2 | 拆分快/慢测试 | 30 min |
| 本月 | P2 | 核心模块添加 logging | 20 min |
| 本月 | P2 | `__init__.py` 导出 `checkpoint_db` | 2 min |
| 按需 | P2 | 连接池、CI、CHANGELOG、`__main__.py` | — |

---

## 五、总结

v3 项目在 **代码质量**（命名、docstring、参数化 SQL）和 **安全**（CHECK 约束全覆盖）方面达到较高水准。B1-B11 优化批次已修复了大量细节问题。当前最大短板集中在 **工程化基础设施**（无 README、无依赖声明、无 linting/CI）和 **架构耦合**（硬编码连接、缺少依赖注入）。P0 三项是新增项目的基础配置，可立刻补齐；P1 四项是影响可维护性和一致性的核心问题，建议本周内完成。
*（内容由AI生成，仅供参考）*
