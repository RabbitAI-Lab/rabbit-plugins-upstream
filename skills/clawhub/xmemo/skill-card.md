## Description:

Persistent user-owned memory for agents with standalone runtime execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to give agents durable, account-backed memory for recall, search, handoffs, TODOs, expenses, and authentication diagnostics across sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials may be stored unencrypted when plaintext storage is explicitly enabled.

Mitigation: Prefer XMEMO_KEY or a managed secret store; use --allow-plaintext only after accepting same-user local process access to the token file.

Risk: Durable memory can retain secrets or sensitive personal/customer data if users save it.

Mitigation: Do not save secrets or sensitive personal/customer data unless the user has explicitly approved it and the applicable privacy requirements are satisfied.

Risk: Authenticated custom service origins receive the credential used by XMemo commands.

Mitigation: Use the default XMemo service or only trusted HTTPS custom origins; reserve localhost HTTP for local development.

## Reference(s):

- [XMemo Skill Operations](references/operations.md)
- [XMemo Skill Troubleshooting](references/troubleshooting.md)
- [XMemo service](https://xmemo.dev)
- [ClawHub skill page](https://clawhub.ai/xmemo/skills/xmemo)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Standalone commands require Node.js 20 or newer, network access to XMemo, and a valid credential for authenticated operations.]

## Skill Version(s):

1.1.1 (source: ClawHub server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
