## Description:

用已发布的零售品牌门店快照，帮助零售连锁团队分析门店网络、业态分类、区域覆盖、周边画像、品牌对比与坐标选址。

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

Retail market, expansion, and channel teams use this skill to analyze published retail-store snapshots for brand scale, regional coverage, store categories, surroundings, competitor comparisons, and location screening.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party API service and requires a DDT_API_KEY.

Mitigation: Confirm the service is trusted before installation and keep the API key out of skill files, chats, logs, and version control.

Risk: Retail-store results are based on published snapshots and limited previews, not a complete live market list.

Mitigation: Report coverage and data-version notes, avoid inferring openings or closures, and label unavailable coverage as not covered instead of treating it as zero.

## Reference(s):

- [店店通 retail network homepage](https://gotoshop-ai.com/ddtclaw/)
- [ClawHub skill page](https://clawhub.ai/horacetu/skills/ddtclaw-retail-network)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with concise findings and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should present conclusions, 3-6 key metrics, coverage and data-version notes, requested limited store details, and uncovered items while avoiding API keys, internal identifiers, and unsupported live-change claims.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
