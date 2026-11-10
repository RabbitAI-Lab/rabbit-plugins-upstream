## Description:

对使用中的 Agent 做跨维度、只读优先、可逆的整体瘦身：盘点常驻与按需上下文，量化 Token 与磁盘影响，分级执行并用回归与回滚保证能力不回退；默认 dry-run。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT

## Use Case:

开发者和 Agent 管理者可用它盘点常驻上下文、技能、备份与旧会话，评估 Token 和磁盘占用，并审阅可回滚的减负计划。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The standalone recovery script can restore files outside the selected Agent folder.

Mitigation: Correct and verify the recovery script's path checks before use, keep an independent backup, and do not rely on checksums alone to prevent symlink redirection.

Risk: Regression command files run with the user's account and environment access.

Mitigation: Supply only regression command files that you trust.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lisong2003-lgtm/skills/agent-slim)
- [GitHub release page](https://github.com/lisong2003-lgtm/agent-slim/releases/tag/v0.1.2)
- [Usage guide](docs/usage.md)
- [Safety boundaries](docs/safety.md)
- [Execution contract](docs/execution-contract.md)
- [Audit JSON contract](docs/audit-json-contract.md)
- [Adapter contract](references/adapter-contract.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Guidance]

**Output Format:** [Structured JSON reports and plans with human-readable summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dry-run by default; executable changes are limited to allowlisted file moves; Token estimates are identified separately from measured usage.]

## Skill Version(s):

0.1.2 (source: frontmatter, changelog, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
