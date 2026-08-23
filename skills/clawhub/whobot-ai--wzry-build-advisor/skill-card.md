## Description:

王者荣耀出装与节奏建议：基于本地装备、英雄、克制规则与野区数据，为玩家给出下一件装备、后续成装路线和资源节奏提醒。

This skill is ready for commercial/non-commercial use.

## Publisher:

[whobot-ai](https://clawhub.ai/user/whobot-ai)

### License/Terms of Use:

MIT

## Use Case:

External users and players use this skill during or around 王者荣耀 matches to make faster equipment and jungle-resource decisions from partial match context. It is intended to return compact gameplay guidance rather than long-form coaching.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Gameplay recommendations may become stale when 王者荣耀 equipment, hero, or jungle timing data changes between seasons.

Mitigation: Treat recommendations as bundled-data guidance and compare important decisions against current game data before relying on them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/whobot-ai/skills/wzry-build-advisor)
- [王者荣耀 Atlas](https://code.jiangshu.ai/wzry-atlas/)
- [Counter Rules](references/counter-rules.md)
- [Equipment Reference](references/equipment.md)
- [Hero Reference](references/heroes.md)
- [Jungle Reference](references/jungle.md)

## Skill Output:

**Output Type(s):** [guidance, markdown]

**Output Format:** [Short Markdown with structured Chinese labels for next item, follow-up items, final build, and reminders]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses bundled reference text; recommendations should be reviewed against the current game season.]

## Skill Version(s):

1.0.0 (source: server release metadata; source skill frontmatter and changelog mention 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
