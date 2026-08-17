## Description:

跑店销售的目标门店筛选、拜访优先级与周边竞对判断；可将高德地图中复制出的地点名称和地址文本作为地点输入，并基于店店通已发布门店快照生成可核验结论。

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

External sales teams use this skill to screen automotive aftermarket store targets, prioritize visits, and assess nearby competitors from published 店店通 store snapshots. It is intended for brand, region, city, service-type, surroundings, and limited nearby-store analysis within the automotive aftermarket domain.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a DDT API key and sends user-provided brand, address, coordinate, or store lookup queries to the 店店通 API.

Mitigation: Configure the key only in a controlled local or runtime environment, do not paste real keys into chat or logs, and make users comfortable with the external API data flow before installation.

Risk: Store and market conclusions may be incomplete when coverage is limited, previews are truncated, or the queried brand or location is not covered.

Mitigation: Use the API response coverage fields as authoritative, label missing coverage as unavailable, narrow overbroad nearby searches, and stop rather than filling in metrics not returned by the API.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/horacetu/skills/ddt-amap-auto-sales)
- [店店通 Open API Homepage](https://gotoshop-ai.com/ddtclaw/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should summarize conclusions, key metrics, data coverage, requested limited store details, and uncovered items without exposing API keys or internal fields.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
