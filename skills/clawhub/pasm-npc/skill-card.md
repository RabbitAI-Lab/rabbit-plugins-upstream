## Description:

pasm-npc provides guidance and examples for building game NPC agents on PASM with persistent memory, emotion-modulated replies, feedback-shaped behavior, growth-stage actions, offline operation, and transparent engine tier labels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arronjack](https://clawhub.ai/user/arronjack)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and game engineers use this skill to integrate NPCs that remember player interactions, vary responses with emotion, and adapt behavior based on explicit player feedback without relying on an external LLM.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on pasm-agents and related third-party Python packages.

Mitigation: Review upstream packages and dependency versions before installing in sensitive environments.

Risk: NPC state and remembered interactions are persisted locally under ~/.pasm-agents/<agent_id>/.

Mitigation: Treat saved NPC state as application data and apply appropriate local data retention and access controls.

Risk: The main documentation is written in Chinese, which may limit review by some teams.

Mitigation: Have a qualified reviewer translate or validate operational instructions before production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/arronjack/skills/pasm-npc)
- [pasm-agents repository](https://github.com/arronJack/pasm-agents)
- [pasm-skills tutorial](https://github.com/arronJack/pasm-skills/blob/master/docs/TUTORIAL.md)
- [pasm-agents Gitee source install path](https://gitee.com/arronzheng/pasm-agents)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with Python and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes local state path guidance and engine tier distinctions.]

## Skill Version(s):

0.4.11 (source: evidence release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
