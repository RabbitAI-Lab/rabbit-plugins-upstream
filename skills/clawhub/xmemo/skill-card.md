## Description:

Persistent user-owned memory for agents with standalone runtime execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to give agents durable XMemo-backed memory, recall, search, restart continuity, TODO tracking, expense recording, and authentication diagnostics. It supports standalone Node.js execution and XMemo MCP/native integrations when available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The standalone runtime can store an XMemo credential in a local plaintext user file when --allow-plaintext is used.

Mitigation: Prefer XMEMO_KEY or a managed secret store; if local plaintext storage is used, treat the credential file as sensitive and use logout or token rotation when access should end.

Risk: Authenticated commands send credentials to the configured XMemo service origin.

Mitigation: Use the default hosted origin or only trusted HTTPS custom origins before running authenticated commands.

Risk: The installer downloads and unpacks a remote Skill archive.

Mitigation: Install only from trusted HTTPS origins; the bundled installers enforce HTTPS paths, reject non-HTTPS redirects, and verify that the archive contains the runtime entrypoint.

## Reference(s):

- [XMemo Skill Operations](references/operations.md)
- [XMemo Skill Troubleshooting](references/troubleshooting.md)
- [XMemo Memory on ClawHub](https://clawhub.ai/xmemo/skills/xmemo)
- [XMemo service](https://xmemo.dev)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Terminal text and optional JSON responses with Markdown documentation examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recall and search support compact terminal output; JSON output is available for trusted callers.]

## Skill Version(s):

1.1.5 (source: server evidence and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
