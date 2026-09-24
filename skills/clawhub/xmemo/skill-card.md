## Description:

Persistent, user-owned memory for agents. Use the standalone runtime to remember, recall, search, preserve restart continuity, manage TODOs and expenses, or diagnose XMemo when MCP tools are unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use XMemo Memory to persist and retrieve user-owned memory, task state, TODOs, and expense records across sessions using the bundled Node.js runtime or XMemo MCP tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents can store durable memory that includes sensitive or unintended content.

Mitigation: Review what the agent stores and avoid secrets or sensitive personal data.

Risk: Using --allow-plaintext stores an unencrypted local token file readable by the operating-system user.

Mitigation: Prefer XMEMO_KEY or a managed secret store; use --allow-plaintext only when that local trust boundary is acceptable.

Risk: Custom base URLs can route credentials or memory operations to an untrusted host.

Mitigation: Use custom base URLs only when the host is trusted.

## Reference(s):

- [XMemo Skill Operations](artifact/references/operations.md)
- [XMemo Skill Troubleshooting](artifact/references/troubleshooting.md)
- [XMemo Service](https://xmemo.dev)
- [ClawHub XMemo Skill](https://clawhub.ai/xmemo/skills/xmemo)
- [XMemo Publisher Profile](https://clawhub.ai/user/xmemo)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; runtime commands emit terminal text or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports human-readable terminal output and JSON mode; recall and search output can be compacted.]

## Skill Version(s):

1.1.23 (source: server release evidence, changelog, runtime constant)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
