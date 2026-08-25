## Description:

dnd-dm is an AI Dungeon Master skill for D&D 5e that supports modular play, combat adjudication, character creation, saves, SRD lookup, and D&D Lens subskills for lore retrieval, module generation, and anonymized real-experience mapping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ackiles](https://clawhub.ai/user/ackiles)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run D&D 5e sessions with an AI Dungeon Master, structured rules support, local save management, and helper workflows for lore, module creation, and anonymized story mapping.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact includes unrelated personal-assistant instructions alongside the D&D skill.

Mitigation: Install the skill only in a dedicated D&D workspace and remove or ignore the bundled AGENTS.md heartbeat and personal-assistant instructions before enabling it.

Risk: The skill persists local game and derived story data, including echo-map outputs from user-provided real-life stories.

Mitigation: Back up existing saves and module files, and avoid using echo-map with sensitive real-life stories unless local derived storage is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ackiles/skills/dnd-dm-skill)
- [SKILL.md](artifact/SKILL.md)
- [CHANGELOG.md](artifact/CHANGELOG.md)
- [DM_RULES.md](artifact/references/DM_RULES.md)
- [DM_TEMPLATES.md](artifact/references/DM_TEMPLATES.md)
- [DND Lens world-lore workflow](artifact/world-lore/references/world-lore-workflow.md)
- [DND Lens module-forge workflow](artifact/module-forge/references/module-forge-workflow.md)
- [DND Lens echo-map workflow](artifact/echo-map/references/echo-map-workflow.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with JSON files, shell commands, and generated D&D campaign text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local D&D workspace files such as saves, module indexes, scene caches, party state, and anonymized module drafts.]

## Skill Version(s):

1.2.0 (source: server release metadata and CHANGELOG, released 2026-08-19; SKILL.md frontmatter reports 1.1.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
