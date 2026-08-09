## Description:

Persistent user-owned memory for agents with standalone runtime execution. Use when an agent should remember, recall, search memory, preserve restart continuity, manage TODOs, record expenses, diagnose XMemo auth, or operate XMemo even when MCP tools are not configured.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to store, recall, search, and restore user-owned memory across sessions, including task state, TODOs, expenses, and troubleshooting context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores user-directed memory and authentication data with an external persistent memory service.

Mitigation: Install only when external persistent memory is intended, avoid saving secrets or sensitive personal/customer data, and prefer XMEMO_KEY or a managed secret store over plaintext credential files.

Risk: Authenticated commands can send credentials to a custom service origin.

Mitigation: Use custom service origins only when they are trusted, and keep the default HTTPS service unless a reviewed deployment requires otherwise.

Risk: Temporary access is limited and may expire.

Mitigation: Use formal account login for the full command set and restart continuity; reserve temporary registration for unattended use or when the user explicitly declines registration.

## Reference(s):

- [XMemo Memory on ClawHub](https://clawhub.ai/xmemo/skills/xmemo)
- [XMemo publisher profile](https://clawhub.ai/user/xmemo)
- [XMemo service](https://xmemo.dev)
- [XMemo Skill Operations](artifact/references/operations.md)
- [XMemo Skill Troubleshooting](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Plain text or Markdown with command examples; JSON is available when requested by the bundled script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include compact recall/search output, state handoff content, TODO or expense confirmations, and diagnostic results.]

## Skill Version(s):

1.1.3 (source: server evidence release.version and CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
