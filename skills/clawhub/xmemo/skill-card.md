## Description:

Provides agents with persistent, user-owned memory for recall, task continuity, TODOs, and expense tracking across sessions; it is not intended for codebase or web search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use XMemo Memory to save and retrieve durable project context, preserve task continuity, and manage TODOs and expense records across agent sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan could not fully inspect many bundled scripts, leaving persistence-related behavior uncertain.

Mitigation: Review the declared tool scope and understand the host's environment, file-reading, and shell permissions before installing or running the skill.

## Reference(s):

- [XMemo Memory on ClawHub](https://clawhub.ai/xmemo/skills/xmemo)
- [Memory operations](references/memory-operations.md)
- [Ledger operations](references/ledger-operations.md)
- [Authentication setup](references/auth-setup.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Text or JSON memory results with concise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bounded memory context, TODOs, ledger summaries, or diagnostic results.]

## Skill Version(s):

1.1.50 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
