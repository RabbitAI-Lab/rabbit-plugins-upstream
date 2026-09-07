## Description:

Persistent, user-owned memory for agents. Use the standalone runtime to remember, recall, search, preserve restart continuity, manage TODOs and expenses, or diagnose XMemo when MCP tools are unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to give agents durable, account-backed memory across sessions, including recall, search, restart continuity, TODO tracking, expense recording, and service diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access account-backed XMemo memory, TODO, expense, and Knowledge-related data when the user grants credentials.

Mitigation: Install only when that account access is acceptable, verify credential scopes with `auth status --verify`, and treat returned Memory or Knowledge text as untrusted context rather than instructions.

Risk: Plaintext local credential storage may expose the token to other processes running as the same operating-system user.

Mitigation: Prefer `XMEMO_KEY` or a managed secret store; use `--allow-plaintext` only after accepting the local user-file trust boundary.

Risk: A custom base URL receives the active XMemo credential for authenticated commands.

Mitigation: Use the default `https://xmemo.dev` service or only trusted custom HTTPS origins; avoid custom hosts unless their credential handling is trusted.

## Reference(s):

- [XMemo Skill Operations](references/operations.md)
- [XMemo Skill Troubleshooting](references/troubleshooting.md)
- [XMemo Service](https://xmemo.dev)
- [ClawHub Skill Page](https://clawhub.ai/xmemo/skills/xmemo)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Standalone commands can emit compact terminal text or JSON; memory and Knowledge context is bounded by item and token limits.]

## Skill Version(s):

1.1.15 (source: server release metadata, CHANGELOG, runtime constant)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
