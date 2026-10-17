## Description:

Provides persistent, user-owned cloud memory for agents to recall context, preserve task continuity, and manage action items and expenses across sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

Agent users and developers use XMemo to save and retrieve approved long-lived project context, resume work after interruptions, and track tasks or expenses when a persistent memory service is needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud memory and search queries can expose private or sensitive information to the XMemo service.

Mitigation: Save only user-approved, non-sensitive memories; exclude secrets, tokens, private keys, cookies, and sensitive personal or customer data from memories and queries.

Risk: A plaintext local credential file may be readable by processes running as the same user.

Mitigation: Prefer XMEMO_KEY from a managed secret store, OpenClaw Secret Egress, or a managed vault over local plaintext credential storage.

Risk: A custom service URL receives the credential used for XMemo requests.

Mitigation: Use custom base URLs only for trusted hosts.

## Reference(s):

- [XMemo Memory on ClawHub](https://clawhub.ai/xmemo/skills/xmemo)
- [Memory operations](references/memory-operations.md)
- [Authentication and credential setup](references/auth-setup.md)
- [Runtime operations](references/runtime-operations.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration guidance]

**Output Format:** [Text or JSON command responses; optional Markdown agent instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Persistent cloud-backed memory; account authorization is needed for full functionality.]

## Skill Version(s):

1.1.43 (source: ClawHub release evidence and artifact CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
