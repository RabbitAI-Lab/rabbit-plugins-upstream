## Description:

pasm-npc helps agents use PASM-based game NPCs with persistent memory, emotion-modulated replies, persona-weighted actions, feedback shaping, growth-stage action unlocks, offline operation, and transparent light/core/bionic tier reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arronjack](https://clawhub.ai/user/arronjack)

### License/Terms of Use:

MIT-0

## Use Case:

Game developers and agent builders use this skill to add NPCs that remember player actions, respond with emotion-aware dialogue, and adjust behavior over time from explicit player feedback. It is suited for offline or local game-agent workflows that need persistent NPC state without an LLM dependency.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: NPC memories and state persist under ~/.pasm-agents/<agent_id>/, which may retain player or scenario data across sessions.

Mitigation: Avoid storing real personal or sensitive player data in NPC memories, and remove the relevant ~/.pasm-agents/<agent_id>/ directory when saved state should be cleared.

Risk: Using the skill normally involves installing and running the upstream pasm-agents package locally.

Mitigation: Install in a virtual environment and review the package source and dependencies according to the user's local software review process.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/arronjack/skills/pasm-npc)
- [pasm-agents homepage](https://github.com/arronJack/pasm-agents)
- [pasm-skills tutorial](https://github.com/arronJack/pasm-skills/blob/master/docs/TUTORIAL.md)
- [pasm-agents source install mirror](https://gitee.com/arronzheng/pasm-agents)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with Python and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance describes local state persistence under ~/.pasm-agents/<agent_id>/ and transparent runtime tier labels.]

## Skill Version(s):

0.4.9 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
