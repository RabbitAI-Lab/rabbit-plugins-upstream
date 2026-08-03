## Description: <br>
Persistent user-owned memory for agents with standalone runtime execution. Use when an agent should remember, recall, search memory, preserve restart continuity, manage TODOs, record expenses, diagnose XMemo auth, or operate XMemo even when MCP tools are not configured. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xmemo](https://clawhub.ai/user/xmemo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to give agents durable XMemo-backed memory, recall, search, task handoff, restart continuity, TODO, expense, and diagnostic workflows across sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can store an XMemo credential in an unencrypted user file when plaintext storage is explicitly allowed. <br>
Mitigation: Prefer XMEMO_KEY or a managed secret store; use --allow-plaintext only after accepting the local user-file trust boundary. <br>
Risk: Authenticated commands send memory operations and credentials to the configured XMemo service origin. <br>
Mitigation: Use the default XMemo service or only trusted custom HTTPS origins; plain HTTP should be limited to localhost development. <br>
Risk: Agents may persist secrets, private customer data, or sensitive personal data as durable memory. <br>
Mitigation: Do not save secrets or sensitive data unless the user intentionally chooses to store it and the applicable privacy policy supports that use. <br>


## Reference(s): <br>
- [XMemo Skill Operations](references/operations.md) <br>
- [XMemo Skill Troubleshooting](references/troubleshooting.md) <br>
- [XMemo service](https://xmemo.dev) <br>
- [ClawHub skill listing](https://clawhub.ai/xmemo/skills/xmemo) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Standalone Node.js commands can emit compact human-readable output or redacted JSON with --json.] <br>

## Skill Version(s): <br>
1.1.0 (source: changelog, release evidence, and runtime constant) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
