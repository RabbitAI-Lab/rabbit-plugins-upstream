## Description:

Durable memory and self-improving workflow guidance for agents using the ClawVault plugin to recall, verify, save, consolidate, and learn from conversation-derived memories in a local SQLite database.

This skill is ready for commercial/non-commercial use.

## Publisher:

[davidtkeane](https://clawhub.ai/user/davidtkeane)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to give an OpenClaw agent durable local memory, including searched recall, verified saves, consolidation of related memories, and lessons from failures or corrections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist selected conversation facts and lessons across sessions in local memory.

Mitigation: Disclose memory use, avoid storing secrets or sensitive personal details, and honor user requests to stop remembering or not save specific content.

Risk: Stored memories may become inaccurate if unchecked claims are saved as facts.

Mitigation: Follow the skill's verify-before-save posture: use ground-truth checks and save unverified claims only as unverified items or questions to confirm.

Risk: The skill requires a separate ClawVault plugin, so users must trust and install that plugin for the skill to function.

Mitigation: Install only the named ClawVault plugin, review the plugin before trusting it, and confirm the expected clawvault_* tools are available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/davidtkeane/skills/clawvault-memory)
- [ClawVault plugin homepage](https://github.com/davidtkeane/openclaw-plugin-clawvault)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline command and tool-call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to create, search, consolidate, or inspect local memory entries through the required ClawVault plugin.]

## Skill Version(s):

1.1.8 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
