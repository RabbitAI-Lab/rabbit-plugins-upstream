## Description:

Guides an agent to use the ClawVault plugin for persistent local memory, verified recall, and lessons learned across sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[davidtkeane](https://clawhub.ai/user/davidtkeane)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to make an assistant search existing ClawVault memories before answering, save verified durable facts and lessons, and avoid storing guesses as long-term memory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent memory may retain sensitive information if users share secrets while memory is active.

Mitigation: Avoid saving secrets, credentials, or personal data unless the user explicitly asks, and periodically review or clear stored memories when plugin controls are available.

Risk: Fact verification may use the agent's own web-search or fetch tools, which can send queried information outside local storage.

Mitigation: Use local ground truth where possible and avoid sending sensitive content to external verification tools.

Risk: Automatically promoting lessons into always-loaded instruction files could preserve attacker-supplied guidance.

Mitigation: Require user approval before adding proven lessons to always-loaded guidance.

## Reference(s):

- [ClawVault Memory skill page](https://clawhub.ai/davidtkeane/skills/clawvault-memory)
- [ClawVault plugin homepage](https://github.com/davidtkeane/openclaw-plugin-clawvault)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline command and tool-call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the ClawVault plugin to provide the clawvault_* tools used by the workflow.]

## Skill Version(s):

1.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
