## Description:

宝塔面板 Skill，让 AI Agent 调用宝塔面板能力，管理网站、文件、数据库、Docker、计划任务及服务器环境，完成状态查询、故障排查和安全检查等日常运维操作；支持自动部署宝塔面板与 MCP 服务，并接入 Claude Code、Codex、Cursor、WorkBuddy 等 AI Agent。

This skill is ready for commercial/non-commercial use.

## Publisher:

[aapanel](https://clawhub.ai/user/aapanel)

### License/Terms of Use:

MIT

## Use Case:

Developers, operators, and external server administrators use this skill to let an AI agent query, troubleshoot, and manage BT Panel or aaPanel servers. It also guides reviewed deployment of the BT MCP service and connection to agent clients such as Claude Code, Codex, Cursor, and WorkBuddy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide high-impact server administration, including installation, firewall or domain publishing changes, permission changes, service restarts, web-root probes, and database credential checks.

Mitigation: Require explicit review before those actions, keep the default posture read-only, and install only when the user intends to let the agent administer BT Panel servers.

Risk: Some bundled troubleshooting or deployment flows may allow broad or disruptive remediation when the user's prompt is vague.

Mitigation: Avoid broad outage prompts unless server-side troubleshooting is intended, confirm exact resources before changes, and report actual verified outcomes rather than assuming success.

Risk: MCP setup may involve root access, API tokens, TLS certificates, and network allowlists.

Mitigation: Prefer SSH keys or secure secret storage, do not echo or persist secrets, require trusted TLS for public MCP access, and use the smallest practical IP or CIDR allowlist.

## Reference(s):

- [Vendor source manifest](references/vendor-sources.md)
- [BT MCP trusted IP certificate guide](https://docs.bt.cn/user-guide/ai/mcp-installation#申请可信-ip-证书)
- [ClawHub skill page](https://clawhub.ai/aapanel/skills/btpanel)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline shell commands, configuration snippets, and operational checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should redact secrets and separate observed facts, inferences, proposed changes, and completion status.]

## Skill Version(s):

1.0.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
