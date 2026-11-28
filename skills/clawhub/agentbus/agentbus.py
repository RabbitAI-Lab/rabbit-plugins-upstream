#!/usr/bin/env python3
"""agentbus — 让多个 AI agent 靠一个共享文件夹交接工作，每一步都留痕。

设计约束（v0.2）：

- **零依赖、单文件。** 除标准库外不 import 任何东西，`curl` 下来就能跑。
- **不认识任何具体产品。** 代码里不出现任何 agent 名称；谁是主、谁干什么，
  全部来自总线根目录的 `CONTRACT.md`。
- **文件即协议。** 没有 broker、没有 socket、没有数据库、没有常驻进程。
  拷走这个文件夹，整个系统就搬走了。
- **可靠性靠三件事：** `flock` 跨进程互斥、`tmp + fsync + os.replace` 原子写、
  结论码必须独占一行（防止"未达到 PASS"被读成通过）。

结果词表是封闭的：`COMPLETED` / `FAIL` / `PARTIAL`。`PASS` 作为
`COMPLETED` 的别名被接受，其余任何词一律拒收，不会写进台账。
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import shlex
import subprocess
import sys
import tempfile
import time
from pathlib import Path

try:  # POSIX
    import fcntl
except ImportError:  # pragma: no cover - Windows
    fcntl = None  # type: ignore[assignment]
try:  # Windows
    import msvcrt
except ImportError:  # pragma: no cover - POSIX
    msvcrt = None  # type: ignore[assignment]

VERSION = "0.2.0"
SCRIPT = Path(__file__).resolve()

# 编号只要求"大写前缀 + 日期 + 序号"，不绑定任何产品缩写。
# 前缀可以是 T、TASK、JOB 之类；不允许 / . 空格，防止路径穿越。
ID_RE = re.compile(r"^[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*-\d{8}-\d{3}$")

TASK_RESULTS = ("COMPLETED", "FAIL", "PARTIAL")
# 契约里写的是 PASS/FAIL/PARTIAL；写 PASS 的人不该被判错。
RESULT_ALIASES = {
    "PASS": "COMPLETED",
    "DONE": "COMPLETED",
    "OK": "COMPLETED",
    "SUCCESS": "COMPLETED",
    "FAILED": "FAIL",
    "INCOMPLETE": "PARTIAL",
}

DEFAULT_LEASE_SECONDS = 1800

LEDGER_HEADER = (
    "# agentbus 任务台账\n\n"
    "| 日期 | 编号 | 任务 | 负责 | 状态 | 证据 | 复盘 |\n"
    "|---|---|---|---|---|---|---|\n"
)

# 只有"整行就是一个结论码"才算结论。正文里顺嘴提到的词不算，
# 这是"未达到 PASS"永远不能被读成 PASS 的唯一保证。
VERDICT_RE = re.compile(
    r"^[ \t]*(?:[-*][ \t]+)?(?:最终结论|验收结论|执行结论|结论|RESULT|VERDICT)"
    r"[ \t]*[：:][ \t]*`?([A-Za-z][A-Za-z_]*)`?[ \t]*[。.]?[ \t]*$",
    re.MULTILINE | re.IGNORECASE,
)


# ---------------------------------------------------------------- 文本模板

TASK_TEMPLATE = """# 任务包 {{ID}}

| 项 | 值 |
|---|---|
| 标题 | {{TITLE}} |
| 创建 | {{CREATED}} |
| 派单方 | {{DISPATCHER}} |
| 总线 | `{{ROOT}}` |
| 结果词表 | `COMPLETED` / `FAIL` / `PARTIAL` |

## 目标

{{GOAL}}

## 范围

{{SCOPE}}

## 输入

{{INPUTS}}

## 交付物

{{DELIVERABLES}}

## 验收标准

{{ACCEPTANCE}}

## 约束

{{CONSTRAINTS}}

## 怎么领、怎么交

```bash
{{CLAIM_COMMAND}}

# 干活，把结果写进同目录的 回执包.md，然后：
{{COMPLETE_COMMAND}}
```

回执里必须有一行且只有一行结论，形如：

```
结论：COMPLETED
```

`PASS` 会被当作 `COMPLETED` 接受；其余词一律拒收，不会进台账。
"""

RECEIPT_TEMPLATE = """# 回执包 {{ID}}

| 项 | 值 |
|---|---|
| 执行者 | {{WORKER}} |
| 完成时间 | {{COMPLETED_AT}} |

## 做了什么

{{SUMMARY}}

## 证据

{{EVIDENCE}}

## 未完成 / 风险

{{RISKS}}

结论：{{RESULT}}
"""

CONTRACT_TEMPLATE = """# CONTRACT

- 总线：`{{ROOT}}`
- 生成：{{CREATED}}
- 版本：agentbus {{VERSION}}

这份文件是**唯一的路径来源**。所有 agent 的接入片段只需要一句话：
开工前先读这份契约，按里面的角色执行。

## 参与者

{{PARTICIPANTS}}

## 归属

{{OWNERSHIP}}

## 规则

- worker 不自判 `PASS`，只写自己执行的那一半记录。
- 结论码只有三个：`COMPLETED` / `FAIL` / `PARTIAL`（`PASS` 视作 `COMPLETED`）。
- 回执里结论码必须**独占一行**，例如 `结论：COMPLETED`。写在句子里的不算。
- 冲突顺序：用户当场指令 > 派单方 > worker 自选。
- 共享台账只允许 `complete` / `requeue` 更新，不手工改。
"""

# 接入片段的落盘位置。这里出现产品名是必要的：它说的是"把这段文字放到哪"，
# 不是"协议依赖某个产品"。协议层（队列、租约、台账、结论码）不认识任何名字。
ADAPTERS = {
    "codex": (
        "~/.codex/AGENTS.md（追加到协作段）",
        "改完需要**重启 App 或另开对话**才生效，运行中的会话用的是启动时快照。",
    ),
    "claude-code": (
        "项目根部 CLAUDE.md，或 ~/.claude/CLAUDE.md（全局）",
        "新开会话即生效；已有会话需要 `/clear` 或重启。",
    ),
    "cursor": (
        ".cursor/rules/agentbus.mdc",
        "保存后新开对话生效；已在跑的对话不会重新读规则。",
    ),
    "generic": (
        "任意 agent 的系统提示词 / 项目说明文件",
        "具体生效时机取决于该 agent 何时读取这份文件。",
    ),
}

ADAPTER_BODY = """## agentbus 交接

- **开工前先读** `{{CONTRACT}}`，按里面写的角色办事。
- 领任务：`{{CLAIM}}`
- 交任务：把结果写进任务包同目录的 `回执包.md`，结论码独占一行，然后运行：
  `{{COMPLETE}}`
- 不要动别人领走的任务；不要手工改共享台账 `{{LEDGER}}`。
"""


# ---------------------------------------------------------------- 基础工具


def user_config_path() -> Path:
    base = os.environ.get("XDG_CONFIG_HOME") or (Path.home() / ".config")
    return Path(base).expanduser() / "agentbus" / "config.json"


def read_user_config() -> dict:
    path = user_config_path()
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise ValueError(f"本机默认总线配置无法解析: {path}（{exc}）") from exc
    if not isinstance(data, dict):
        raise ValueError(f"本机默认总线配置应是 JSON 对象: {path}")
    return data


def resolve_root(cli_root):
    """--root > AGENTBUS_HOME > 本机默认配置 > ./.agentbus

    只靠环境变量是不够的：非交互 shell 不读 `.zshrc`，定时任务里
    `AGENTBUS_HOME` 往往不存在，于是脚本悄悄在别处新建一个空总线。
    所以本机默认值写进配置文件，由脚本自己读。
    """
    if cli_root:
        return cli_root, "cli"
    env_root = os.environ.get("AGENTBUS_HOME")
    if env_root:
        return env_root, "env"
    configured = read_user_config().get("root")
    if isinstance(configured, str) and configured.strip():
        return configured, "user-config"
    return ".agentbus", "fallback"


def now_iso() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def today() -> str:
    return dt.datetime.now().astimezone().date().isoformat()


def month_key() -> str:
    return today()[:7]


def day_key() -> str:
    return today().replace("-", "")


def one_line(value) -> str:
    return " ".join(str(value).split())


def cell(value) -> str:
    return one_line(value).replace("|", "/")


def bullet(values, empty: str) -> str:
    return "\n".join(f"- {one_line(item)}" for item in values) if values else empty


def numbered(values) -> str:
    return "\n".join(f"{index}. `{one_line(item)}`" for index, item in enumerate(values, 1))


def atomic_text(path: Path, text: str) -> None:
    """先写临时文件再 replace：任何时刻读到的都是完整文件。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=str(path.parent))
    tmp = Path(temporary)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp, path)
    finally:
        if tmp.exists():
            tmp.unlink()


def atomic_json(path: Path, payload: dict) -> None:
    atomic_text(path, json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n")


def read_json(path: Path) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"JSON 对象无效: {path}")
    return payload


def render(text: str, values: dict) -> str:
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", str(value))
    missing = sorted(set(re.findall(r"\{\{([A-Z0-9_]+)\}\}", text)))
    if missing:
        raise ValueError(f"模板存在未替换字段: {', '.join(missing)}")
    return text


def validate_id(task_id: str) -> str:
    if not ID_RE.match(task_id):
        raise ValueError(
            f"无效编号: {task_id!r}（应形如 T-20261128-001：大写前缀 + -日期 + -三位序号）"
        )
    return task_id


def normalize_result(code: str) -> str:
    return RESULT_ALIASES.get(str(code).strip().strip("`").upper(), str(code).strip().strip("`").upper())


def strict_verdicts(text: str):
    return [match.group(1) for match in VERDICT_RE.finditer(text)]


def resolve_result(text: str, requested):
    """从回执里取出唯一结论；不做全文模糊匹配。"""
    found = [normalize_result(code) for code in strict_verdicts(text)]
    unknown = sorted({code for code in found if code not in TASK_RESULTS})
    if unknown:
        raise ValueError(
            f"回执结论码不在允许集: {', '.join(unknown)}"
            f"（允许：{' / '.join(TASK_RESULTS)}；PASS 视为 COMPLETED）"
        )
    distinct = sorted(set(found))
    if len(distinct) > 1:
        raise ValueError(f"回执包含多个不同结论: {', '.join(distinct)}；请只保留一行")

    if requested:
        want = normalize_result(requested)
        if want not in TASK_RESULTS:
            raise ValueError(f"--result 无效: {requested}（允许：{' / '.join(TASK_RESULTS)}）")
        if not found:
            raise ValueError(
                f"回执没有独占一行的结论；必须是单独一行 `结论：{want}`，"
                "写进正文句子里不算"
            )
        if distinct[0] != want:
            raise ValueError(f"--result {want} 与回执中的 {distinct[0]} 不一致")
        return want

    if not found:
        raise ValueError(
            "回执缺少结论：需要单独一行 "
            + " / ".join(f"`结论：{code}`" for code in TASK_RESULTS)
        )
    return distinct[0]


class QueueLock:
    """跨进程互斥，锁由操作系统持有，不靠文件 mtime 猜。

    早期实现会删掉"两分钟前的锁文件"，如果持锁方正在哈希一个大文件，
    锁就被抢走了。OS 锁在进程退出时自动释放，不需要猜年龄。
    """

    def __init__(self, path: Path, timeout: float = 10.0):
        self.path = path
        self.timeout = timeout
        self._handle = None

    def __enter__(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        handle = self.path.open("a+", encoding="utf-8")
        deadline = time.monotonic() + self.timeout
        while True:
            try:
                if fcntl is not None:
                    fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                elif msvcrt is not None:  # pragma: no cover - Windows
                    handle.seek(0)
                    msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
                break
            except OSError:
                if time.monotonic() >= deadline:
                    handle.close()
                    raise TimeoutError(f"等待队列锁超时: {self.path}")
                time.sleep(0.05)
        handle.seek(0)
        handle.truncate()
        handle.write(f"{os.getpid()} {now_iso()}\n")
        handle.flush()
        self._handle = handle
        return self

    def __exit__(self, *exc_info):
        handle = self._handle
        self._handle = None
        if handle is None:
            return False
        try:
            if fcntl is not None:
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
            elif msvcrt is not None:  # pragma: no cover - Windows
                handle.seek(0)
                try:
                    msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
                except OSError:
                    pass
        finally:
            handle.close()
        return False


# ---------------------------------------------------------------- 总线


class Bus:
    def __init__(self, root, root_source: str = "cli"):
        self.root = Path(root).expanduser().resolve()
        self.root_source = root_source
        self.tasks = self.root / "tasks"
        self.queue = self.root / "queue"
        self.pending = self.queue / "pending"
        self.claimed = self.queue / "claimed"
        self.completed = self.queue / "completed"
        self.failed = self.queue / "failed"
        self.corrupt = self.queue / "corrupt"
        self.shared = self.root / "shared"
        self.contract = self.root / "CONTRACT.md"
        self.config = self.root / "bus.json"

        config: dict = {}
        if self.config.is_file():
            # 配置坏了就停：静默退回默认台账会把审计记录劈成两半。
            try:
                config = read_json(self.config)
            except (OSError, ValueError) as exc:
                raise ValueError(f"bus.json 无法解析，拒绝静默回退默认台账: {self.config}（{exc}）") from exc
        self.ledger = Path(
            os.environ.get("AGENTBUS_LEDGER") or config.get("ledger") or self.shared / "ledger.md"
        ).expanduser().resolve()
        self.review_dir = Path(
            os.environ.get("AGENTBUS_REVIEW_DIR") or config.get("review_dir") or self.shared / "review"
        ).expanduser().resolve()
        self.lock_path = self.queue / ".lock"

    # -- 目录与初始文件

    def ensure(self) -> None:
        self.root.mkdir(parents=True, exist_ok=True)
        for directory in (
            self.tasks,
            self.pending,
            self.claimed,
            self.completed,
            self.failed,
            self.corrupt,
            self.review_dir,
            self.ledger.parent,
        ):
            directory.mkdir(parents=True, exist_ok=True)
        if not self.ledger.is_file():
            atomic_text(self.ledger, LEDGER_HEADER)
        review = self.review_dir / f"{month_key()}.md"
        if not review.is_file():
            atomic_text(review, f"# agentbus 复盘 {month_key()}\n\n")
        if not self.config.is_file():
            atomic_json(
                self.config,
                {
                    "schema": 1,
                    "version": VERSION,
                    "created_at": now_iso(),
                    "ledger": str(self.ledger),
                    "review_dir": str(self.review_dir),
                },
            )

    def lock(self) -> QueueLock:
        return QueueLock(self.lock_path)

    # -- 查询

    def exists(self, task_id: str) -> bool:
        names = (f"{task_id}.json", task_id)
        for directory in (self.pending, self.claimed, self.completed, self.failed, self.corrupt, self.tasks):
            if any((directory / name).exists() for name in names):
                return True
        if self.ledger.is_file() and f"`{task_id}`" in self.ledger.read_text(encoding="utf-8"):
            return True
        return False

    # -- 台账与复盘

    def append_ledger(self, task_id: str, title: str, owner: str, status: str, evidence: str) -> None:
        if self.ledger.is_file() and f"`{task_id}`" in self.ledger.read_text(encoding="utf-8"):
            return
        row = (
            f"| {today()} | `{task_id}` | {cell(title)} | {cell(owner)} | `{cell(status)}` | "
            f"{cell(evidence)} | - |\n"
        )
        self.ledger.parent.mkdir(parents=True, exist_ok=True)
        with self.ledger.open("a", encoding="utf-8") as handle:
            handle.write(row)

    def update_ledger(self, task_id: str, status: str, evidence: str, title: str = "", owner: str = "-") -> str:
        """写台账：有行就改，没行就补。

        任务可能从未登记就走到 complete（队列是手工建的、或从备份恢复的）。
        只改不补会让这些完成记录在共享台账里彻底消失——恰恰是最难重建的那部分。
        """
        text = self.ledger.read_text(encoding="utf-8") if self.ledger.is_file() else ""
        lines = text.splitlines()
        for index, line in enumerate(lines):
            if not line.startswith("|") or f"`{task_id}`" not in line:
                continue
            cells = line.split("|")
            if len(cells) >= 8:
                if owner and owner != "-":
                    # 派单时写的是"待领取"或占位名，真正负责的人是领取的那个人，
                    # 不更新这一列，台账就永远记不住是谁干的。
                    cells[4] = f" {cell(owner)} "
                cells[5] = f" `{cell(status)}` "
                cells[6] = f" {cell(evidence)} "
                cells[7] = f" {month_key()} "
                lines[index] = "|".join(cells)
                atomic_text(self.ledger, "\n".join(lines) + "\n")
                return "updated"
        self.ledger.parent.mkdir(parents=True, exist_ok=True)
        header = "" if lines else LEDGER_HEADER
        row = (
            f"| {today()} | `{task_id}` | {cell(title or '未登记任务（完成时补记）')} | "
            f"{cell(owner)} | `{cell(status)}` | {cell(evidence)} | {month_key()} |\n"
        )
        with self.ledger.open("a", encoding="utf-8") as handle:
            handle.write(header + row)
        print(f"WARN: 台账缺少 `{task_id}`，已补记一行：{self.ledger}", file=sys.stderr)
        return "appended"

    def append_review(self, task_id: str, title: str, result: str, evidence: str) -> Path:
        path = self.review_dir / f"{month_key()}.md"
        current = path.read_text(encoding="utf-8") if path.is_file() else f"# agentbus 复盘 {month_key()}\n\n"
        heading = f"## {today()} `{task_id}` {one_line(title)}"
        if heading not in current:
            current = current.rstrip() + (
                f"\n\n{heading}\n\n"
                f"- 结果：`{one_line(result)}`\n"
                f"- 证据：{one_line(evidence)}\n"
                "- 未完成项：以回执中的「未完成 / 风险」为准。\n"
            )
            atomic_text(path, current.rstrip() + "\n")
        return path

    # -- 契约

    def participants(self):
        """从 CONTRACT.md 的「参与者」段取角色名；取不到就返回空列表。"""
        if not self.contract.is_file():
            return []
        names = []
        inside = False
        for line in self.contract.read_text(encoding="utf-8").splitlines():
            stripped = line.strip()
            if stripped.startswith("## "):
                inside = stripped.lstrip("# ").strip().startswith("参与者")
                continue
            if inside and stripped.startswith(("-", "*")):
                token = stripped.lstrip("-* ").split()
                if token:
                    names.append(token[0].strip("*`"))
        return names


def make_bus(cli_root) -> Bus:
    root, source = resolve_root(cli_root)
    return Bus(root, root_source=source)


def next_id(bus: Bus, prefix: str) -> str:
    pattern = re.compile(rf"^{re.escape(prefix)}-{day_key()}-(\d{{3}})$")
    used = []
    candidates = list(bus.tasks.glob(f"{prefix}-{day_key()}-*"))
    for directory in (bus.pending, bus.claimed, bus.completed, bus.failed):
        candidates.extend(directory.glob(f"{prefix}-{day_key()}-*.json"))
    for path in candidates:
        name = path.stem if path.suffix == ".json" else path.name
        match = pattern.match(name)
        if match:
            used.append(int(match.group(1)))
    return f"{prefix}-{day_key()}-{max(used) + 1 if used else 1:03d}"


def claim_command(bus: Bus, worker: str = "") -> str:
    base = (
        f"{shlex.quote(sys.executable)} {shlex.quote(str(SCRIPT))} "
        f"--root {shlex.quote(str(bus.root))} claim"
    )
    if worker:
        return f"{base} --worker {shlex.quote(worker)}"
    return f"{base} --worker <你的名字>"


def complete_command(bus: Bus, task_id: str = "") -> str:
    tail = f" --id {shlex.quote(task_id)}" if task_id else " --id <编号>"
    return (
        f"{shlex.quote(sys.executable)} {shlex.quote(str(SCRIPT))} "
        f"--root {shlex.quote(str(bus.root))} complete{tail}"
    )


# ---------------------------------------------------------------- 命令：init


def build_contract_values(bus: Bus, participants, ownership) -> dict:
    return {
        "ROOT": str(bus.root),
        "CREATED": now_iso(),
        "VERSION": VERSION,
        "PARTICIPANTS": "\n".join(f"- {one_line(item)}" for item in participants),
        "OWNERSHIP": "\n".join(f"- {one_line(item)}" for item in ownership),
    }


def wizard_answers(defaults):
    """三个问题；非交互环境直接用默认值，绝不挂住。"""
    if not sys.stdin.isatty():
        print("非交互环境，使用默认契约（要自定义请手工编辑 CONTRACT.md）。", file=sys.stderr)
        return defaults

    def ask(prompt: str, default: str) -> str:
        try:
            answer = input(f"{prompt} [{default}]: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return default
        return answer or default

    print("三个问题，直接回车用默认值。\n")
    names = ask("参与者，逗号分隔，第一个是派单/终审方", "main, worker-a, worker-b")
    parsed = [item.strip() for item in names.replace("，", ",").split(",") if item.strip()]
    if not parsed:
        parsed = ["main"]
    dispatcher = parsed[0]
    exec_owner = parsed[1] if len(parsed) > 1 else dispatcher
    doc_owner = parsed[2] if len(parsed) > 2 else exec_owner
    exec_role = ask(f"{exec_owner} 负责什么", "可执行物（代码、脚本、配置、构建）")
    doc_role = ask(f"{doc_owner} 负责什么", "可读物（报告、表格、清单、图示）")
    return {
        "participants": [
            f"{dispatcher} — 派单、排优先级、终审、出结论码",
            f"{exec_owner} — {exec_role}",
            f"{doc_owner} — {doc_role}",
        ],
        "ownership": [
            f"可执行物 → {exec_owner}",
            f"可读物 → {doc_owner}",
            f"验证 → {dispatcher}，即使对象是 {doc_owner} 的产出",
        ],
    }


def write_contract(bus: Bus, wizard: bool, overwrite: bool = False) -> Path:
    if bus.contract.is_file() and not overwrite:
        return bus.contract
    defaults = {
        "participants": [
            "main — 派单、排优先级、终审、出结论码",
            "worker-a — 可执行物（代码、脚本、配置、构建）",
            "worker-b — 可读物（报告、表格、清单、图示）",
        ],
        "ownership": [
            "可执行物 → worker-a",
            "可读物 → worker-b",
            "验证 → main，即使对象是 worker-b 的产出",
        ],
    }
    answers = wizard_answers(defaults) if wizard else defaults
    content = render(
        CONTRACT_TEMPLATE,
        build_contract_values(bus, answers["participants"], answers["ownership"]),
    )
    atomic_text(bus.contract, content)
    return bus.contract


def cmd_init(bus: Bus, args) -> int:
    """幂等：新目录就建，已有总线就挂上去补齐缺件，绝不因为"已存在"拒绝。

    接管一条旧总线（对话记录、老台账、老队列都在）时，用户要的是"接上"，
    不是"已存在，拒绝"。拒绝会把人逼去用 --force，而 --force 听起来像会清数据。
    """
    existed = bus.config.is_file()
    bus.ensure()
    contract = write_contract(bus, args.wizard, overwrite=args.force and existed)
    payload = {
        "status": "ATTACHED" if existed else "INITIALIZED",
        "version": VERSION,
        "root": str(bus.root),
        "root_source": bus.root_source,
        "contract": str(contract),
        "ledger": str(bus.ledger),
        "review_dir": str(bus.review_dir),
    }
    if existed:
        payload["reused"] = "总线已存在：复用原有台账与队列，未改动任何历史记录"
        payload["counts"] = {
            "pending": len(list(bus.pending.glob("*.json"))),
            "claimed": len(list(bus.claimed.glob("*.json"))),
            "completed": len(list(bus.completed.glob("*.json"))),
        }
    if args.set_default:
        path = user_config_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        atomic_json(path, {"schema": 1, "root": str(bus.root), "set_at": now_iso()})
        payload["default_config"] = str(path)
        payload["next"] = "已记为本机默认总线：之后在任何目录、任何 shell 都不用再带 --root"
    else:
        payload["next"] = "建议加 --set-default 记为本机默认，否则每条命令都要带 --root"
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


# ---------------------------------------------------------------- 命令：dispatch


def cmd_dispatch(bus: Bus, args) -> int:
    bus.ensure()
    task_id = validate_id(args.id or next_id(bus, args.prefix))
    with bus.lock():
        if bus.exists(task_id):
            raise FileExistsError(f"编号已存在，禁止重复派发: {task_id}")
        task_dir = bus.tasks / task_id
        task_dir.mkdir(parents=True, exist_ok=False)
        package = task_dir / "任务包.md"
        receipt = task_dir / "回执包.md"
        content = render(
            TASK_TEMPLATE,
            {
                "ID": task_id,
                "TITLE": args.title,
                "CREATED": now_iso(),
                "DISPATCHER": args.dispatcher,
                "ROOT": str(bus.root),
                "GOAL": args.goal,
                "SCOPE": bullet(args.scope, "- 只做达成目标所必需的部分。"),
                "INPUTS": bullet(args.input, "- 无额外输入。"),
                "DELIVERABLES": bullet(args.deliverable, "- 按目标交付可读文件，并写回执。"),
                "ACCEPTANCE": bullet(
                    args.acceptance, "- 交付物可打开；来源、未知项、风险和数据边界如实记录。"
                ),
                "CONSTRAINTS": bullet(
                    args.constraint,
                    "- 不改任务包；共享台账只能由 `complete` 更新，不手工改。",
                ),
                "CLAIM_COMMAND": claim_command(bus, args.assignee),
                "COMPLETE_COMMAND": complete_command(bus, task_id),
            },
        )
        atomic_text(package, content)
        payload = {
            "schema": 1,
            "task_id": task_id,
            "title": args.title,
            "kind": "task",
            "status": "QUEUED",
            "dispatcher": args.dispatcher,
            "assignee": args.assignee,
            "package_path": str(package),
            "receipt_path": str(receipt),
            "result_vocabulary": list(TASK_RESULTS),
            "created_at": now_iso(),
            "lease_seconds": int(args.lease_seconds),
        }
        atomic_json(bus.pending / f"{task_id}.json", payload)
        bus.append_ledger(
            task_id, args.title, args.assignee or "待领取", "QUEUED", f"任务包：{package}"
        )
    print(
        json.dumps(
            {"status": "QUEUED", "id": task_id, "package": str(package), "assignee": args.assignee},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


# ---------------------------------------------------------------- 命令：claim


def lease_state(payload: dict) -> str:
    raw = payload.get("lease_expires_at")
    if not raw:
        return "NO_LEASE"
    try:
        expires = dt.datetime.fromisoformat(str(raw))
    except ValueError:
        return "INVALID_LEASE"
    return "EXPIRED" if dt.datetime.now().astimezone() >= expires else "ACTIVE"


def cmd_claim(bus: Bus, args) -> int:
    bus.ensure()
    worker = one_line(args.worker)
    if not worker:
        raise ValueError("--worker 不能为空")
    known = bus.participants()
    if known and worker not in known:
        print(
            f"WARN: {worker!r} 不在 CONTRACT.md 的参与者列表里（{', '.join(known)}）。"
            "能继续，但记录会对不上人。",
            file=sys.stderr,
        )
    with bus.lock():
        candidates = []
        for path in bus.pending.glob("*.json"):
            try:
                payload = read_json(path)
            except (OSError, ValueError):
                # 隔离而不是跳过：坏掉的 pending 文件会让队列永远看起来是空的。
                bus.corrupt.mkdir(parents=True, exist_ok=True)
                target = bus.corrupt / path.name
                os.replace(path, target)
                atomic_json(
                    bus.corrupt / f"{path.name}.reason",
                    {"quarantined_at": now_iso(), "reason": "pending JSON 无法解析"},
                )
                print(
                    json.dumps({"status": "QUARANTINED", "queue_file": str(target)}, ensure_ascii=False),
                    file=sys.stderr,
                )
                continue
            candidates.append((str(payload.get("created_at", "")), path.name, path, payload))

        for _, _, path, payload in sorted(candidates):
            task_id = validate_id(str(payload.get("task_id", "")))
            package = Path(str(payload.get("package_path", ""))).expanduser()
            receipt = Path(str(payload.get("receipt_path", ""))).expanduser()

            if not package.is_file():
                error = f"任务包缺失: {package}"
                payload.update(status="FAILED", failed_at=now_iso(), error=error)
                target = bus.failed / path.name
                os.replace(path, target)
                atomic_json(target, payload)
                evidence = f"失败记录：{target}"
                bus.update_ledger(task_id, "FAILED", evidence, str(payload.get("title", "")), worker)
                bus.append_review(task_id, str(payload.get("title", "")), "FAILED", evidence)
                continue

            if receipt.is_file() and receipt.stat().st_size > 0:
                # 回执已经写好了，说明上一个人干完了但没提交。
                payload.update(status="RECEIPT_EXISTS", receipt_path=str(receipt))
                target = bus.claimed / path.name
                os.replace(path, target)
                atomic_json(target, payload)
                payload["queue_file"] = str(target)
                payload["hint"] = "回执已存在，直接运行 complete 提交结果"
                print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
                return 0

            lease_seconds = int(payload.get("lease_seconds") or args.lease_seconds or DEFAULT_LEASE_SECONDS)
            expires = dt.datetime.now().astimezone() + dt.timedelta(seconds=lease_seconds)
            payload.update(
                status="IN_PROGRESS",
                claimed_at=now_iso(),
                claimed_by=worker,
                attempt=int(payload.get("attempt", 0)) + 1,
                lease_seconds=lease_seconds,
                lease_expires_at=expires.isoformat(timespec="seconds"),
            )
            payload.setdefault("history", []).append(
                {"at": now_iso(), "event": "claim", "worker": worker, "attempt": payload["attempt"]}
            )
            target = bus.claimed / path.name
            os.replace(path, target)
            atomic_json(target, payload)
            payload["queue_file"] = str(target)
            print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
            return 0

    print(json.dumps({"status": "EMPTY", "root": str(bus.root)}, ensure_ascii=False, indent=2))
    return 0


# ---------------------------------------------------------------- 命令：complete


def cmd_complete(bus: Bus, args) -> int:
    bus.ensure()
    task_id = validate_id(args.id)
    with bus.lock():
        claimed = bus.claimed / f"{task_id}.json"
        if not claimed.is_file():
            if (bus.pending / f"{task_id}.json").is_file():
                raise FileNotFoundError(f"任务 {task_id} 还在 pending，先 claim 再 complete")
            raise FileNotFoundError(f"领取队列里没有任务: {task_id}")

        payload = read_json(claimed)
        receipt = Path(args.receipt).expanduser().resolve() if args.receipt else Path(
            str(payload["receipt_path"])
        ).expanduser()
        if not receipt.is_file() or receipt.stat().st_size == 0:
            raise FileNotFoundError(f"回执不存在或为空，禁止完成: {receipt}")

        result = resolve_result(receipt.read_text(encoding="utf-8", errors="ignore"), args.result)
        worker = one_line(payload.get("claimed_by", "")) or "-"
        destination = bus.failed if result == "FAIL" else bus.completed
        payload.update(
            status=result,
            completed_at=now_iso(),
            receipt_path=str(receipt),
            receipt_sha256=hashlib_sha256(receipt),
        )
        target = destination / claimed.name
        os.replace(claimed, target)
        atomic_json(target, payload)

        evidence = f"回执：{receipt}"
        ledger = bus.update_ledger(task_id, result, evidence, str(payload.get("title", "")), worker)
        review = bus.append_review(task_id, str(payload.get("title", "")), result, evidence)
        print(
            json.dumps(
                {
                    "status": "FAILED" if result == "FAIL" else "COMPLETED",
                    "id": task_id,
                    "result": result,
                    "worker": worker,
                    "receipt": str(receipt),
                    "receipt_sha256": payload["receipt_sha256"],
                    "queue_file": str(target),
                    "ledger": ledger,
                    "review": str(review),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0


def hashlib_sha256(path: Path) -> str:
    import hashlib

    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


# ---------------------------------------------------------------- 命令：运维


def cmd_requeue(bus: Bus, args) -> int:
    bus.ensure()
    with bus.lock():
        targets = []
        if args.id:
            targets = [bus.claimed / f"{validate_id(args.id)}.json"]
        else:
            for path in sorted(bus.claimed.glob("*.json")):
                try:
                    if lease_state(read_json(path)) == "EXPIRED":
                        targets.append(path)
                except (OSError, ValueError):
                    continue
        moved = []
        for source in targets:
            if not source.is_file():
                continue
            payload = read_json(source)
            payload.update(status="QUEUED")
            payload.pop("lease_expires_at", None)
            payload.pop("claimed_by", None)
            payload.pop("claimed_at", None)
            payload.setdefault("history", []).append({"at": now_iso(), "event": "requeue"})
            target = bus.pending / source.name
            os.replace(source, target)
            atomic_json(target, payload)
            bus.update_ledger(
                str(payload.get("task_id", "")), "QUEUED", "已放回队列", str(payload.get("title", ""))
            )
            moved.append(str(payload.get("task_id", "")))
    print(json.dumps({"status": "REQUEUED", "ids": moved}, ensure_ascii=False, indent=2))
    return 0


def cmd_heartbeat(bus: Bus, args) -> int:
    bus.ensure()
    task_id = validate_id(args.id)
    with bus.lock():
        source = bus.claimed / f"{task_id}.json"
        if not source.is_file():
            raise FileNotFoundError(f"领取队列里没有任务: {task_id}")
        payload = read_json(source)
        seconds = int(args.seconds or payload.get("lease_seconds") or DEFAULT_LEASE_SECONDS)
        expires = dt.datetime.now().astimezone() + dt.timedelta(seconds=seconds)
        payload.update(lease_seconds=seconds, lease_expires_at=expires.isoformat(timespec="seconds"))
        payload.setdefault("history", []).append({"at": now_iso(), "event": "heartbeat", "seconds": seconds})
        atomic_json(source, payload)
    print(
        json.dumps(
            {"status": "RENEWED", "id": task_id, "lease_expires_at": payload["lease_expires_at"]},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


# ---------------------------------------------------------------- 命令：只读


def cmd_status(bus: Bus, args) -> int:
    if not bus.root.is_dir():
        raise FileNotFoundError(f"总线根不存在，先 init: {bus.root}")

    def entries(directory: Path):
        rows = []
        for path in sorted(directory.glob("*.json")):
            try:
                payload = read_json(path)
                row = {
                    "id": payload.get("task_id", path.stem),
                    "status": payload.get("status", "UNKNOWN"),
                    "title": payload.get("title", ""),
                }
                if directory == bus.claimed:
                    row["lease"] = lease_state(payload)
                    row["claimed_by"] = payload.get("claimed_by")
                rows.append(row)
            except (OSError, ValueError):
                rows.append({"id": path.stem, "status": "INVALID"})
        return rows

    payload = {
        "version": VERSION,
        "root": str(bus.root),
        "root_source": bus.root_source,
        "contract": str(bus.contract) if bus.contract.is_file() else None,
        "pending": entries(bus.pending),
        "claimed": entries(bus.claimed),
        "completed_recent": entries(bus.completed)[-10:],
        "failed_recent": entries(bus.failed)[-10:],
        "corrupt": entries(bus.corrupt),
    }
    payload["counts"] = {
        key: len(payload[key]) for key in ("pending", "claimed", "completed_recent", "failed_recent", "corrupt")
    }
    payload["lease_expired"] = [row["id"] for row in payload["claimed"] if row.get("lease") == "EXPIRED"]
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


def scan_queue(bus: Bus):
    problems = []
    expired = []
    for directory in (bus.pending, bus.claimed, bus.completed, bus.failed, bus.corrupt):
        for path in sorted(directory.glob("*.json")):
            try:
                payload = read_json(path)
            except (OSError, ValueError) as exc:
                problems.append({"file": str(path), "reason": f"JSON 无法解析: {exc}"})
                continue
            task_id = payload.get("task_id")
            if not task_id or not isinstance(task_id, str):
                problems.append({"file": str(path), "reason": "缺少 task_id"})
                continue
            package = Path(str(payload.get("package_path", ""))).expanduser()
            if not package.is_file():
                problems.append({"file": str(path), "reason": f"任务包缺失: {package}"})
            if directory == bus.claimed and lease_state(payload) == "EXPIRED":
                expired.append(
                    {
                        "id": task_id,
                        "claimed_by": payload.get("claimed_by"),
                        "lease_expires_at": payload.get("lease_expires_at"),
                        "fix": f"requeue --id {task_id}",
                    }
                )
    return problems, expired


def cmd_doctor(bus: Bus, args) -> int:
    if not bus.root.is_dir():
        raise FileNotFoundError(f"总线根不存在，先 init: {bus.root}")
    problems, expired = scan_queue(bus)
    notes = []

    if bus.root_source == "fallback":
        notes.append(
            {
                "level": "warn",
                "item": "root",
                "detail": "既没有 --root、AGENTBUS_HOME，也没有本机默认总线：本次退回相对路径 "
                ".agentbus，可能在当前目录新建一个空总线。建议 init --set-default。",
            }
        )
    elif bus.root_source == "user-config":
        notes.append(
            {"level": "info", "item": "root", "detail": f"使用本机默认总线 {user_config_path()}"}
        )
    env_root = os.environ.get("AGENTBUS_HOME")
    if env_root and Path(env_root).expanduser().resolve() != bus.root:
        notes.append(
            {
                "level": "warn",
                "item": "root",
                "detail": f"AGENTBUS_HOME 指向 {Path(env_root).expanduser().resolve()}，本次实际使用 {bus.root}",
            }
        )
    if not bus.contract.is_file():
        notes.append({"level": "warn", "item": "contract", "detail": f"缺少 CONTRACT.md: {bus.contract}"})
    if not os.access(bus.ledger.parent if bus.ledger.parent.exists() else bus.root, os.W_OK):
        notes.append({"level": "error", "item": "ledger", "detail": f"台账目录不可写: {bus.ledger.parent}"})

    quarantined = []
    if args.fix:
        with bus.lock():
            for item in problems:
                path = Path(item["file"])
                if not path.is_file():
                    continue
                target = bus.corrupt / path.name
                os.replace(path, target)
                atomic_json(
                    bus.corrupt / f"{path.name}.reason",
                    {"quarantined_at": now_iso(), "reason": item["reason"]},
                )
                quarantined.append({"from": str(path), "to": str(target), "reason": item["reason"]})
        # 隔离掉的问题不再算"还没修好"，否则修完仍然报 ATTENTION。
        moved = {item["from"] for item in quarantined}
        problems = [item for item in problems if item["file"] not in moved]

    counts = {
        "pending": len(list(bus.pending.glob("*.json"))),
        "claimed": len(list(bus.claimed.glob("*.json"))),
        "completed": len(list(bus.completed.glob("*.json"))),
        "failed": len(list(bus.failed.glob("*.json"))),
        "corrupt": len(list(bus.corrupt.glob("*.json"))),
    }
    healthy = not problems and not expired and not [n for n in notes if n["level"] == "error"]
    print(
        json.dumps(
            {
                "status": "OK" if healthy else "ATTENTION",
                "version": VERSION,
                "root": str(bus.root),
                "root_source": bus.root_source,
                "counts": counts,
                "problems": problems,
                "expired_leases": expired,
                "notes": notes,
                "quarantined": quarantined,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0 if healthy else 1


# ---------------------------------------------------------------- 命令：adapter


def adapter_text(bus: Bus, name: str, worker: str) -> str:
    body = render(
        ADAPTER_BODY,
        {
            "CONTRACT": str(bus.contract),
            "CLAIM": claim_command(bus, worker),
            "COMPLETE": complete_command(bus),
            "LEDGER": str(bus.ledger),
        },
    )
    where, when = ADAPTERS[name]
    header = f"<!-- 放到：{where} -->\n<!-- 生效：{when} -->\n\n"
    return header + body


def cmd_adapter(bus: Bus, args) -> int:
    text = adapter_text(bus, args.name, args.worker)
    if args.write:
        target = Path(args.write).expanduser()
        if target.exists() and not args.force:
            raise FileExistsError(f"目标已存在，未覆盖: {target}（确认要写请加 --force）")
        existing = target.read_text(encoding="utf-8") if target.is_file() else ""
        atomic_text(target, (existing.rstrip() + "\n\n" + text) if existing.strip() else text)
        print(json.dumps({"status": "WRITTEN", "path": str(target)}, ensure_ascii=False, indent=2))
        return 0
    print(text)
    print(f"\n<!-- 这条片段要放到：{ADAPTERS[args.name][0]} -->")
    return 0


# ---------------------------------------------------------------- 命令：demo


def cmd_demo(bus: Bus, args) -> int:
    """在临时目录里真跑一遍完整闭环，不碰任何真实数据。

    每一步都是真的 subprocess 调用，输出不是编的。
    """
    base = Path(tempfile.mkdtemp(prefix="agentbus-demo-"))
    root = base / "bus"
    script = str(SCRIPT)

    def run(*argv):
        proc = subprocess.run(
            [sys.executable, script, "--root", str(root), *argv],
            capture_output=True,
            text=True,
        )
        cmd = " ".join(["agentbus", *argv])
        print(f"$ {cmd}")
        out = (proc.stdout or "").strip()
        err = (proc.stderr or "").strip()
        if out:
            print(out)
        if err:
            print(err, file=sys.stderr)
        if proc.returncode != 0:
            raise RuntimeError(f"demo 第 {cmd!r} 步失败（exit {proc.returncode}）")
        return out

    started = time.time()
    print(f"临时总线：{root}\n" + "-" * 60)
    try:
        run("init")
        print()
        task_id = json.loads(
            run(
                "dispatch",
                "--title",
                "示例：核对一份清单",
                "--assignee",
                "worker-a",
                "--goal",
                "把清单里的每一项核对一遍，给出差异；无法判定的标为待确认。",
                "--deliverable",
                "核对报告.md",
            )
        )["id"]
        print()
        run("claim", "--worker", "worker-a")
        print()

        (root / "tasks" / task_id / "回执包.md").write_text(
            render(
                RECEIPT_TEMPLATE,
                {
                    "ID": task_id,
                    "WORKER": "worker-a",
                    "COMPLETED_AT": now_iso(),
                    "SUMMARY": "1. 读取清单，逐项核对；2. 记录 2 项差异，1 项待确认。",
                    "EVIDENCE": "核对报告.md（示例中由执行方产出）",
                    "RISKS": "1 项因缺少原始凭据无法判定，标为待确认。",
                    "RESULT": "COMPLETED",
                },
            ),
            encoding="utf-8",
        )
        print("（执行方写下 回执包.md，结论码独占一行）\n")
        run("complete", "--id", task_id)
        print()
        run("status")
        print("-" * 60)
        ledger_lines = [line for line in (root / "shared" / "ledger.md").read_text(encoding="utf-8").splitlines() if line.startswith("| 2")]
        print("台账新增的行：")
        print("\n".join(ledger_lines) or "（空，说明台账没写进去）")
        elapsed = time.time() - started
        print(f"\n完整闭环 {elapsed:.1f} 秒，全部是本地文件操作，没有网络、没有常驻进程。")
    finally:
        if args.keep:
            print(f"\n数据保留在：{root}")
        else:
            import shutil

            shutil.rmtree(base, ignore_errors=True)
            print("\n临时目录已清理（要保留请加 --keep）。")
    return 0


# ---------------------------------------------------------------- 入口


def build_parser() -> argparse.ArgumentParser:
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument(
        "--root",
        default=argparse.SUPPRESS,
        help="总线根目录；不传则按 AGENTBUS_HOME → 本机默认 → ./.agentbus 解析",
    )

    parser = argparse.ArgumentParser(
        prog="agentbus",
        description="让多个 AI agent 靠一个共享文件夹交接工作，每一步都留痕。",
        epilog="先跑 `agentbus demo` 看它是什么样，再 `agentbus init --wizard`。",
    )
    parser.add_argument("--root", help="总线根目录")
    parser.add_argument("--version", action="version", version=f"agentbus {VERSION}")
    sub = parser.add_subparsers(dest="command")

    p = sub.add_parser("init", parents=[common], help="初始化总线并生成 CONTRACT.md")
    p.add_argument("--wizard", action="store_true", help="交互回答三个问题生成契约")
    p.add_argument("--set-default", action="store_true", help="记为本机默认总线，之后不用再带 --root")
    p.add_argument("--force", action="store_true", help="已有 CONTRACT.md 也重写（不动台账与队列）")
    p.set_defaults(func=cmd_init)

    p = sub.add_parser("dispatch", parents=[common], help="派一个任务")
    p.add_argument("--id", help="任务编号；不填按 T-YYYYMMDD-NNN 自动生成")
    p.add_argument("--prefix", default="T", help="自动编号的前缀（默认 T）")
    p.add_argument("--title", required=True, help="一句话标题")
    p.add_argument("--goal", required=True, help="要达成什么")
    p.add_argument("--dispatcher", default="main", help="派单方名字（默认 main）")
    p.add_argument("--assignee", default="", help="指定谁做；不填则队列里标为待领取")
    p.add_argument("--scope", action="append", default=[], help="范围，可重复")
    p.add_argument("--input", action="append", default=[], help="输入，可重复")
    p.add_argument("--deliverable", action="append", default=[], help="交付物，可重复")
    p.add_argument("--acceptance", action="append", default=[], help="验收标准，可重复")
    p.add_argument("--constraint", action="append", default=[], help="约束，可重复")
    p.add_argument("--lease-seconds", type=int, default=DEFAULT_LEASE_SECONDS, help="租约秒数")
    p.set_defaults(func=cmd_dispatch)

    p = sub.add_parser("claim", parents=[common], help="领一个任务，拿租约")
    p.add_argument("--worker", required=True, help="领取人名字（任意字符串）")
    p.add_argument("--lease-seconds", type=int, default=DEFAULT_LEASE_SECONDS, help="租约秒数")
    p.set_defaults(func=cmd_claim)

    p = sub.add_parser("complete", parents=[common], help="提交回执，记台账")
    p.add_argument("--id", required=True, help="任务编号")
    p.add_argument("--receipt", help="回执路径；默认用任务包里记的那个")
    p.add_argument("--result", help="结论码；不填从回执独占行读取")
    p.set_defaults(func=cmd_complete)

    p = sub.add_parser("status", parents=[common], help="看队列（JSON）")
    p.set_defaults(func=cmd_status)

    p = sub.add_parser("doctor", parents=[common], help="体检：缺包、坏文件、过期租约")
    p.add_argument("--fix", action="store_true", help="把坏掉的队列文件挪进 corrupt/")
    p.set_defaults(func=cmd_doctor)

    p = sub.add_parser("requeue", parents=[common], help="把过期任务放回队列")
    p.add_argument("--id", help="只处理这个编号；不填处理所有过期租约")
    p.set_defaults(func=cmd_requeue)

    p = sub.add_parser("heartbeat", parents=[common], help="续租")
    p.add_argument("--id", required=True, help="任务编号")
    p.add_argument("--seconds", type=int, default=DEFAULT_LEASE_SECONDS, help="续多少秒")
    p.set_defaults(func=cmd_heartbeat)

    p = sub.add_parser("adapter", parents=[common], help="打印某个 agent 的接入片段")
    p.add_argument("name", choices=sorted(ADAPTERS), help="agent 类型")
    p.add_argument("--worker", default="worker", help="片段里示例用的 worker 名字")
    p.add_argument("--write", help="直接写入这个路径（默认只打印）")
    p.add_argument("--force", action="store_true", help="目标已存在也追加写入")
    p.set_defaults(func=cmd_adapter)

    p = sub.add_parser("demo", parents=[common], help="临时目录真跑一遍完整闭环")
    p.add_argument("--keep", action="store_true", help="保留临时目录路径方便翻看")
    p.set_defaults(func=cmd_demo)

    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not getattr(args, "command", None):
        parser.print_help()
        return 0
    try:
        bus = make_bus(getattr(args, "root", None))
        return args.func(bus, args)
    except (ValueError, FileNotFoundError, FileExistsError, TimeoutError, OSError) as exc:
        print(json.dumps({"status": "ERROR", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
