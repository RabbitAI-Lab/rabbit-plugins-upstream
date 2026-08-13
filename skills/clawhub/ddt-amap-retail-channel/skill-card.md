## Description:

使用高德地图地址文本和店店通已发布门店快照，为零售品牌生成业态结构、城市覆盖、竞品差异与市场机会分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

External market, channel, and site-selection analysts use this skill to analyze published retail brands, pasted Amap address text, coordinates, or public store IDs. It helps summarize store scale, retail category mix, regional coverage, competitor differences, market opportunities, and data coverage from the DDT service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided brands, addresses, coordinates, or store IDs may be sent to the DDT API provider for retail analysis.

Mitigation: Use the skill only when sharing those retail query inputs with the DDT service is acceptable.

Risk: The DDT API key could be exposed if pasted into chats, logs, files, or version control.

Mitigation: Keep DDT_API_KEY in environment variables and avoid echoing or storing the real key in skill content or conversations.

Risk: Retail conclusions can be misleading when a brand, area, or surrounding profile is not covered by the current published snapshot.

Mitigation: Report coverage and data version from API responses, mark unavailable coverage as unavailable, and avoid filling missing values with assumptions.

## Reference(s):

- [DDT Claw Homepage](https://gotoshop-ai.com/ddtclaw/)
- [ClawHub Skill Page](https://clawhub.ai/horacetu/skills/ddt-amap-retail-channel)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown analysis with key metrics, coverage notes, and limited store details when explicitly requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DDT_API_KEY; uses published retail snapshots and avoids exposing API keys, internal identifiers, supplier fields, or unsupported API fields.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
