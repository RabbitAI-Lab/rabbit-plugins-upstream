## Description:

帮助用户检索医疗健康领域的招采公告，识别医院采购方与中标供应商，并分析医院的主要供应商。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thuanlynham-stack](https://clawhub.ai/user/thuanlynham-stack)

### License/Terms of Use:

MIT-0

## Use Case:

Healthcare procurement and business-development teams use the skill to find Chinese medical tenders, identify winning companies, and compare a hospital's main suppliers.

### Deployment Geography for Use:

Global (focused on Chinese procurement data)

## Known Risks and Mitigations:

Risk: The skill may create an external trial account and collect a hashed MAC-derived device identifier.

Mitigation: Provide ZLBX_API_KEY to avoid automatic registration, or obtain explicit consent before collecting device details and registering.

Risk: A newly issued API key is stored on the local device.

Mitigation: Review local credential storage and restrict access to ~/.zlbx/config.json.

Risk: Embedded instructions can influence authenticated API requests and transmit package and source headers.

Mitigation: Review the skill's request behavior and the data sent to the API before enabling authenticated use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thuanlynham-stack/skills/medical-health-bid-radar-yiliaozhaobiaocaigouwang)
- [Skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Search API reference](artifact/references/api-search.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account and registration guidance](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bid and supplier findings depend on available API data and account access.]

## Skill Version(s):

1.0.10 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
