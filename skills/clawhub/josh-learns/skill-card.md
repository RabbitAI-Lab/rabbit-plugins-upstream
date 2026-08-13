## Description:

Mesh Publish provides a multi-layer local memory system for agents, including fresh daily notes, mesh graph indexing, interaction logging, cross-layer search, compliance checks, PDF archival, and vault sync.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mozz0](https://clawhub.ai/user/mozz0)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to persist, search, summarize, and recover local agent memory across sessions, resets, and workspace rebuilds. It is intended for workflows where local logs, mesh records, and PDF archives are acceptable memory stores.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent conversation logging and PDF archiving may capture secrets, tokens, personal data, private keys, or regulated information.

Mitigation: Define explicit controls for logging scope, redaction, retention, deletion, and archive access before using it with sensitive information.

Risk: Vault sync can push archives to a hardcoded NAS destination using embedded credentials and weakened SSH host verification.

Mitigation: Remove hardcoded credentials and destinations, use managed secrets, and restore SSH host verification before installing or running vault sync.

Risk: Long-lived local and PDF memory stores may retain more data than intended.

Mitigation: Set retention limits and review archived content before syncing or sharing the vault.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mozz0/skills/josh-learns)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and generated local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces or updates local memory logs, JSON mesh records, checkpoint files, PDF vault archives, and optional NAS sync output.]

## Skill Version(s):

3.3.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
