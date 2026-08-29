## Description:

Persistent, user-owned memory for agents. Use the standalone runtime to remember, recall, search, preserve restart continuity, manage TODOs and expenses, or diagnose XMemo when MCP tools are unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use XMemo Memory to persist and retrieve project context, decisions, TODOs, restart handoff state, and lightweight expense records across sessions. The skill is most useful when an agent needs hosted memory through the bundled standalone runtime or an available XMemo MCP integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses XMemo as a hosted persistent memory service, so stored memories can outlive the current session.

Mitigation: Store only information that is appropriate for persistent hosted memory, and avoid secrets, authentication material, and sensitive personal or customer data unless explicitly approved.

Risk: Credential-writing commands can store a token in a local plaintext user file when --allow-plaintext is used.

Mitigation: Prefer XMEMO_KEY or a managed secret store; use --allow-plaintext only after accepting the local user-file trust boundary.

Risk: Authenticated commands send credentials to the configured XMemo service origin.

Mitigation: Use the default https://xmemo.dev service or another trusted HTTPS origin; plain HTTP should be limited to localhost or loopback development.

## Reference(s):

- [XMemo Skill Operations](references/operations.md)
- [XMemo Skill Troubleshooting](references/troubleshooting.md)
- [XMemo service](https://xmemo.dev)
- [ClawHub skill page](https://clawhub.ai/xmemo/skills/xmemo)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands support compact text output, bounded JSON output, credential-status checks, and per-request timeout options.]

## Skill Version(s):

1.1.13 (source: server release evidence, CHANGELOG, and runtime script)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
