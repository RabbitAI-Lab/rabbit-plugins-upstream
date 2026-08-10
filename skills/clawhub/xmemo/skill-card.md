## Description:

Persistent user-owned memory for agents with standalone runtime execution. Use when an agent should remember, recall, search memory, preserve restart continuity, manage TODOs, record expenses, diagnose XMemo auth, or operate XMemo even when MCP tools are not configured.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to give agents durable, user-owned memory across sessions, including recall/search, handoff state, restart continuity, TODOs, expenses, and XMemo authentication diagnostics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The XMemo service stores agent memories, TODOs, restart state, and optional expense records outside the local workspace.

Mitigation: Install only when external XMemo storage is intended, and do not save secrets or sensitive personal data unless the user explicitly requests it and the required privacy policy is supported.

Risk: Using --allow-plaintext stores an XMemo token unencrypted under the current user's home directory.

Mitigation: Prefer XMEMO_KEY or a managed secret store; use --allow-plaintext only after accepting that same-user local processes may read the credential file.

Risk: Authenticated commands sent to a custom service origin can disclose credentials to that origin.

Mitigation: Use the default https://xmemo.dev service or only trusted HTTPS origins; plain HTTP is limited to localhost or loopback development.

## Reference(s):

- [XMemo Skill Operations](references/operations.md)
- [XMemo Skill Troubleshooting](references/troubleshooting.md)
- [XMemo Service](https://xmemo.dev)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text, compact terminal output, or JSON from CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores and retrieves user-directed memories, TODOs, restart state, and optional expense records through XMemo.]

## Skill Version(s):

1.1.4 (source: server evidence and changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
