## Description:

使用高德地图地址文本和店店通已发布门店快照，帮助分析餐饮品牌开关店、区域扩张、竞对密度与候选点机会。

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

External business users, restaurant operators, and market analysts use this skill to turn pasted address text and published restaurant-location snapshots into network-change, competitor-density, regional-growth, and site-screening analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Restaurant brand names and pasted address queries are sent to the 店店通 API using the user's DDT_API_KEY.

Mitigation: Use only data appropriate for that provider, keep the API key in a local environment variable, and never display or share the key in agent responses.

Risk: Users may mistake results for official Amap data or live ground truth.

Mitigation: State that the skill is not an official Amap product and anchor conclusions to the provider's published snapshot coverage and data definitions.

Risk: Limited preview endpoints could be misused for bulk extraction or overbroad enumeration.

Mitigation: Respect size, page, truncation, and refinement limits; provide aggregate totals and ask for narrower filters rather than auto-paging or splitting regions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/horacetu/skills/ddt-amap-restaurant-network)
- [店店通 Claw homepage](https://gotoshop-ai.com/ddtclaw/)
- [店店通 API key setup](https://gotoshop-ai.com/ddtclaw/open)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with concise analysis, key metrics, coverage notes, limited detail rows when requested, and optional shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a user-supplied DDT_API_KEY and provider snapshot limits; preview-style detail responses should remain capped and refined instead of bulk exported.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
