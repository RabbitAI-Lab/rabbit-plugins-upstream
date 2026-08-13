## Description:

零售品牌门店规模、业态结构、区域覆盖与候选点机会分析，可使用腾讯地图中复制出的地点名称和地址文本作为地点输入，并基于店店通已发布门店快照生成可核验结论。

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

External retail analysts, expansion teams, and agent users use this skill to evaluate published retail brand store networks, regional coverage, store categories, competitive context, and candidate site surroundings from DDT snapshots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user-provided coordinates, addresses, or retail queries to the disclosed DDT API when nearby or site-screening features are used.

Mitigation: Use the API key only in a controlled environment, avoid pasting secrets into chat, and confirm users are comfortable sending location inputs to the DDT service.

Risk: Store-network conclusions may be incomplete or misleading if API coverage is missing, truncated, or unavailable.

Mitigation: Check API coverage, data version, ok status, and preview.truncated fields before forming conclusions, and label unavailable coverage as not covered.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/horacetu/skills/ddt-tencent-map-retail-network)
- [DDT Claw homepage](https://gotoshop-ai.com/ddtclaw/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with concise conclusions, key metrics, coverage notes, and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should avoid API keys, internal identifiers, supplier fields, unsupported metrics, and undisclosed data sources.]

## Skill Version(s):

1.0.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
