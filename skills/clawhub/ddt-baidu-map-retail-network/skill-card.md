## Description:

零售品牌门店规模、业态结构、区域覆盖与候选点机会分析。 可将百度地图中复制出的地点名称和地址文本作为地点输入；基于店店通已发布门店快照生成可核验结论。本 Skill 非百度地图官方产品，和百度地图不存在合作、授权或数据来源关系。

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to analyze published retail-chain store networks, regional coverage, store categories, surroundings, and candidate-site context from Baidu Map address text, coordinates, or public store IDs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided retail brand names, addresses, coordinates, or public store IDs are sent to the DDT API.

Mitigation: Use the skill only with information appropriate for that API workflow, and avoid entering sensitive locations or confidential store identifiers.

Risk: The required DDT API key could be exposed if placed in prompts, files, logs, or shared transcripts.

Mitigation: Keep DDT_API_KEY in a controlled environment variable and do not include real keys in chat, skill files, logs, or version control.

Risk: Published snapshots, coverage gaps, or limited previews can make retail conclusions incomplete.

Mitigation: Report coverage and data-version limits, avoid filling missing metrics from assumptions, and treat nearby or site-screen results as constrained initial screening.

## Reference(s):

- [DDT ClawHub API homepage](https://gotoshop-ai.com/ddtclaw/)
- [ClawHub skill page](https://clawhub.ai/horacetu/skills/ddt-baidu-map-retail-network)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with concise conclusions, key metrics, coverage notes, and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses published retail data snapshots; only includes limited store details when the user provides coordinates or a public store ID.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
