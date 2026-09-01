## Description:

Intelligence gathering in Structs - scouting players, planets, guilds, and the galaxy before you act.

This skill is ready for commercial/non-commercial use.

## Publisher:

[abstrct](https://clawhub.ai/user/abstrct)

### License/Terms of Use:

MIT-0

## Use Case:

External Structs players and their agents use this skill to scout raid targets, profile opponents, survey guild and galaxy state, and refresh competitive intel before strategic decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can collect and retain competitive scouting notes about Structs players, planets, guilds, and markets.

Mitigation: Keep memory/intel/ private, periodically delete stale target profiles, and avoid storing more opponent detail than needed.

Risk: Stored scouting results can become stale because power and fleet state may change block-to-block.

Mitigation: Record block height with each finding and re-scout immediately before acting on raid or fleet decisions.

## Reference(s):

- [structs-intel on ClawHub](https://clawhub.ai/abstrct/skills/structs-intel)
- [Structs Combat](https://structs.ai/skills/structs-combat/SKILL)
- [Structs Conventions](https://structs.ai/skills/conventions)
- [Structs Scout Script](https://structs.ai/scripts/scout.sh)
- [Structs Memory README](https://structs.ai/memory/README)
- [Structs Guild Stack](https://structs.ai/skills/structs-guild-stack/SKILL)
- [Structs Database Schema](https://structs.ai/knowledge/infrastructure/database-schema)
- [Structs Streaming](https://structs.ai/skills/structs-streaming/SKILL)
- [structsd Install](https://structs.ai/skills/structsd-install/SKILL)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only scouting guidance and suggested memory records for retained intel.]

## Skill Version(s):

1.25.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
