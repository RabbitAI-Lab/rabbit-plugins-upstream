## Description:

Game NPC agents built on the PASM cognitive engine with persistent memory, emotion-modulated replies, persona-weighted action selection, feedback-driven behavior shaping, growth-stage actions, offline operation, and transparent engine tier reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arronjack](https://clawhub.ai/user/arronjack)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and game teams use this skill to add NPCs that remember player interactions, express mood, choose persona-shaped actions, and adapt behavior from explicit player feedback without relying on an external LLM.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dependency installation can introduce ordinary package supply-chain and environment risks.

Mitigation: Install in a virtual environment under a normal user account and prefer a pinned, reviewed package version.

Risk: The skill persists NPC interaction state locally, which can retain sensitive player or user data.

Mitigation: Avoid entering sensitive real user data unless local storage under ~/.pasm-agents/ is acceptable for the deployment.

Risk: Source-install fallback paths may execute unreviewed local project code.

Mitigation: Use the package install path when possible, and review source-install code before running it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/arronjack/skills/pasm-npc)
- [Publisher profile](https://clawhub.ai/user/arronjack)
- [pasm-agents project homepage](https://github.com/arronJack/pasm-agents)
- [pasm-skills tutorial](https://github.com/arronJack/pasm-skills/blob/master/docs/TUTORIAL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python examples, shell commands, configuration details, and reference tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers local state persistence under ~/.pasm-agents/<agent_id>/ and reports light/core/bionic engine tiers.]

## Skill Version(s):

0.4.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
