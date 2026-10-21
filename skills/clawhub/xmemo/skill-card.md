## Description:

Persistent, user-owned memory for agents. Use the standalone runtime to remember, recall, search, preserve restart continuity, manage TODOs and expenses, inspect account overview, activity and stats diagnostics, or diagnose XMemo when MCP tools are unavailable. Not for codebase search, web search, or short-lived in-session notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use XMemo Memory to preserve and retrieve user-owned context across sessions, projects, and tools. It supports recall and search, task continuity, TODOs, expenses, account activity, and diagnostics when the corresponding runtime and account access are available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-run sign-in may store an access key in an unencrypted local file without clear prior approval.

Mitigation: Prefer managed credential storage; use the local unencrypted token file only after explicitly accepting that storage.

Risk: Project summaries may be sent to and retained by the XMemo service when automatic memory is enabled.

Mitigation: Decide which summaries may be sent and retained before enabling automatic project memory.

## Reference(s):

- [XMemo Memory on ClawHub](https://clawhub.ai/xmemo/skills/xmemo)
- [XMemo service](https://xmemo.dev)
- [Authentication and credential setup](references/auth-setup.md)
- [Memory operations](references/memory-operations.md)
- [Runtime operations](references/runtime-operations.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text or Markdown guidance and command output; optional JSON output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command output depends on the selected memory or account operation and available runtime permissions.]

## Skill Version(s):

1.1.45 (source: CHANGELOG and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
