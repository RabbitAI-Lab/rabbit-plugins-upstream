## Description:

王者荣耀出装与节奏建议，基于本地装备、英雄、克制规则与野区数据，为玩家给出下一件装备、成装路线和资源节奏。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yzfly](https://clawhub.ai/user/yzfly)

### License/Terms of Use:

MIT

## Use Case:

王者荣耀 players and game-strategy agents use this skill during match-planning or live play to convert a hero, opposing threats, current equipment, and match timing into concise build and jungle-resource guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Jungle timings are manually maintained and may drift by season.

Mitigation: Treat timing guidance as a planning aid and verify it against the current in-game season state when precision matters.

Risk: The skill may activate on broad 王者荣耀 strategy questions where another game-specific skill could be more precise.

Mitigation: Use it for 王者荣耀 build, counter-item, equipment-route, and jungle-resource questions, and prefer a narrower skill when the user requests a different game or specialized domain.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yzfly/skills/wzry-build-advisor)
- [WZRY Atlas homepage](https://code.jiangshu.ai/wzry-atlas/)
- [Counter rules](references/counter-rules.md)
- [Equipment reference](references/equipment.md)
- [Heroes reference](references/heroes.md)
- [Jungle timing reference](references/jungle.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Concise Markdown with labeled Chinese recommendation sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces short next-item, follow-up build, final-build, and reminder sections; no executable output.]

## Skill Version(s):

1.1.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
