## Description:

帮助市场与渠道规划人员使用高德地图地址文本和店店通已发布门店快照，分析汽车后市场连锁品牌的规模、区域覆盖、服务类型和竞争格局。

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

External market, channel, and sales-planning users use this skill to analyze automotive aftermarket chain brands across national coverage, regional concentration, service categories, location profiles, and local competition. The skill is intended for published DDT snapshot data and stops when brand coverage, coordinates, or API responses do not support a business conclusion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a local DDT API key and network requests that may include queried brands, addresses, or coordinates.

Mitigation: Use it only in an approved environment, keep DDT_API_KEY out of chats, logs, files, and version control, and avoid sending sensitive locations unless that use is authorized.

Risk: Published snapshot coverage, truncated previews, or failed API responses can make unsupported market conclusions misleading.

Mitigation: Check ok, coverage fields, data-version information, and preview.truncated before answering; label unavailable coverage as not covered and stop when the response does not support the conclusion.

Risk: Users may mistake the Amap-address workflow for an official Amap integration or source relationship.

Mitigation: State that the skill is not an official Amap product and that store conclusions come from published DDT data snapshots.

## Reference(s):

- [DDT Claw Homepage](https://gotoshop-ai.com/ddtclaw/)
- [ClawHub Skill Page](https://clawhub.ai/horacetu/skills/ddt-amap-auto-channel)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown analysis with concise metrics, coverage notes, and optional inline bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs avoid API keys, storage IDs, supplier details, unsupported fields, and English enum leakage.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
