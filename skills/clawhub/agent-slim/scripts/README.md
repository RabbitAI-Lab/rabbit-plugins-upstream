# 脚本区

## 入口

```sh
python3 scripts/agent_slim.py host --home <codex-home> --output host.json
python3 scripts/agent_slim.py audit --json
python3 scripts/agent_slim.py plan --audit audit.json --output plan.json
python3 scripts/agent_slim.py apply --plan plan.json
python3 scripts/agent_slim.py apply --plan plan.json --apply
python3 scripts/agent_slim.py verify --plan plan.json --test-prompts prompts.json
python3 scripts/agent_slim.py restore --manifest <transaction>/manifest.json --apply
```

- `agent_slim.py`：CLI、只读 audit 和安全工作流调度。
- `agent_slim_adapter.py`：只读探测 Codex Home 能力，输出 `supported / unknown / unsupported` 三态；不执行插件管理或正文读取。
- `agent_slim_workflow.py`：plan/apply/verify/restore、事务 manifest、SHA-256、恢复脚本和冲突保护。

## 约束

- 纯标准库优先，兼容 Python 3.9+。
- 默认 dry-run；apply/restore 需要显式 `--apply`。
- 只允许三种移动动作；不提供删除、VACUUM、密钥/provider/认证或系统配置改动。
- 实际改动前写 manifest、manifest SHA-256、`restore.py` 和 `restore.sh`。
- 目标或隔离目标已存在时停止，不覆盖。
- 会话正文不进入报告或审计日志；只用于本地 SHA-256 和移动。
- 缺少 test-prompts 时，路由回归只能 PARTIAL，不伪造 PASS。

完整契约见 `docs/execution-contract.md`。
