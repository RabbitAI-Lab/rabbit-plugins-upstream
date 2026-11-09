## Description:

A local bus that lets CAD and quantity-takeoff skills share project state and reuse cad-contract/v1 without parsing drawings again.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT

## Use Case:

Developers using CAD reading and quantity-takeoff skills use the local bus to share project state and a single drawing-analysis contract across skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates the skill suspicious with medium confidence, citing a risk that cached drawing data may be reused for a different drawing with the same filename.

Mitigation: Consider avoiding installation until filename-based cache matching is addressed, or manually verify reused drawing data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lisong2003-lgtm/skills/lis-skill-bus)
- [Publisher profile](https://clawhub.ai/user/lisong2003-lgtm)

## Skill Output:

**Output Type(s):** [JSON, Configuration instructions, Shell commands, Guidance]

**Output Format:** [JSON state and contract data, with shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State and contracts are stored locally.]

## Skill Version(s):

0.1.11 (source: SKILL.md frontmatter; server release 0.1.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
