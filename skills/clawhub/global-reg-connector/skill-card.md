## Description:

Global Regulatory MCP Connector wraps 27 medical device regulatory hub documents into a local read-only MCP server that lets agents retrieve regulatory snippets, official links, and verification notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Regulatory engineers, medical device developers, and agent users use this skill to search bundled medical device regulatory references across China, the United States, the European Union, Japan, Latin America, and Southeast Asia. It supports quick lookup of registration pathways, UDI, PMS, quality-system, supplier, labeling, and product-classification reference material.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Regulatory references can become outdated or may contain items marked for verification.

Mitigation: Verify important classification, registration, deadline, and compliance decisions against the current official regulator source before acting.

Risk: A custom REG_HUB_REFS directory may expose user-selected Markdown contents to the MCP client.

Mitigation: Set REG_HUB_REFS only to curated Markdown directories whose contents are appropriate for the connected agent or client.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/global-reg-connector)
- [Reference material index](references/README.md)
- [Lifecycle regulatory hub overview](references/枢纽总览_全生命周期7阶段纲领.md)
- [Registration engineer materials hub](references/注册工程师资料枢纽.md)
- [Global orthopedic surgical device registration pathways](references/骨科手术器械_全球注册路径汇编.md)
- [UDI global identification hub](references/UDI全球标识枢纽.md)
- [Technical file and STED writing hub](references/技术文件STED撰写枢纽.md)
- [Risk management hub](references/风险管理枢纽.md)
- [EU MDR post-market surveillance practice](references/EU_MDR上市后监管PMS实务.md)
- [FDA UDI implementation practice](references/FDA_UDI实施实务.md)
- [China medical device MAH contract manufacturing practice](references/CN_医疗器械委托生产MAH实务.md)
- [EU EUDAMED database practice](references/EU_EUDAMED数据库实务.md)
- [NMPA medical device regulations](https://www.nmpa.gov.cn/xxgk/fgwj/)
- [FDA device advice and regulatory assistance](https://www.fda.gov/medical-devices/device-advice-comprehensive-regulatory-assistance)
- [EU MDR 2017/745](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32017R0745)
- [EUDAMED information](https://health.ec.europa.eu/medical-devices-eudamed_en)
- [PMDA medical device review services](https://www.pmda.go.jp/review-services/drug-reviews/about-reviews/devices/0026.html)

## Skill Output:

**Output Type(s):** [text, json, markdown, guidance]

**Output Format:** [JSON strings containing hub lists, search results, full Markdown reference content, snippets, official links, and verification hints.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are generated from bundled local Markdown references or a user-selected REG_HUB_REFS directory; important regulatory conclusions should be checked against current official sources.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
