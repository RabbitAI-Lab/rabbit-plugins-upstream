## Description: <br>
Persistent user-owned memory for agents with standalone runtime execution. Use when an agent should remember, recall, search memory, save or restore handoff state, manage TODOs, record expenses, diagnose XMemo auth, or operate XMemo even when MCP tools are not configured. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xmemo](https://clawhub.ai/user/xmemo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use XMemo Memory to preserve durable, user-owned memory across sessions, including remembered facts, handoff state, TODOs, expenses, and troubleshooting context. The skill supports both a bundled Node.js runtime and XMemo MCP tools when available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores and retrieves durable memory, so users could save secrets or sensitive personal or customer data unintentionally. <br>
Mitigation: Avoid saving secrets, tokens, private keys, or sensitive personal/customer data unless the user explicitly intends to and the applicable privacy requirements are met. <br>
Risk: Using --allow-plaintext may store an unencrypted local token readable by processes running as the same operating-system user. <br>
Mitigation: Prefer XMEMO_KEY or a managed secret store; use --allow-plaintext only after explicit consent and keep local credential files out of repositories and shared logs. <br>
Risk: Authenticated custom service origins receive credentials when commands run against them. <br>
Mitigation: Use only trusted HTTPS origins for remote services; reserve plain HTTP for localhost or loopback development. <br>


## Reference(s): <br>
- [XMemo Skill Operations](references/operations.md) <br>
- [XMemo Skill Troubleshooting](references/troubleshooting.md) <br>
- [XMemo Service](https://xmemo.dev) <br>
- [XMemo Memory on ClawHub](https://clawhub.ai/xmemo/skills/xmemo) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional redacted JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The bundled runtime supports compact terminal output, --json responses, command-specific help, and bounded network requests.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
