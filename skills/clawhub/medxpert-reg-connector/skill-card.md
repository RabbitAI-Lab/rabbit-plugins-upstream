## Description:

医疗器械注册法规检索 MCP 连接器，覆盖 MDR/CE、FDA 510(k)、UDI、STED、分类界定、全球注册路径等场景；agent 通过 MCP 本地只读检索 NMPA/FDA/MDR/PMDA 等 27 枢纽法规知识库，无需联网外发、无需凭据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

External agents and regulatory-affairs users use this MCP connector to retrieve local medical-device regulatory reference material, official links, and classification or registration-pathway leads across NMPA, FDA, MDR, PMDA, and related markets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Regulatory and classification responses may be incomplete or stale if relied on as official conclusions.

Mitigation: Treat outputs as starting points and verify against current official NMPA, FDA, MDR, PMDA, or other target-market sources before business or compliance decisions.

Risk: A custom REG_HUB_REFS path could point the connector at unintended or unreviewed reference content.

Mitigation: Set REG_HUB_REFS only to an intended regulatory-reference directory and install from reviewed package contents.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhaoxinghua09-cell/skills/medxpert-reg-connector)
- [参考素材索引](references/README.md)
- [枢纽总览_全生命周期7阶段纲领](references/枢纽总览_全生命周期7阶段纲领.md)
- [注册工程师资料枢纽](references/注册工程师资料枢纽.md)
- [骨科手术器械_全球注册路径汇编](references/骨科手术器械_全球注册路径汇编.md)
- [UDI全球标识枢纽](references/UDI全球标识枢纽.md)
- [FDA UDI 实施实务](references/FDA_UDI实施实务.md)
- [EU MDR 上市后监管 PMS 实务](references/EU_MDR上市后监管PMS实务.md)
- [EUDAMED 欧盟医疗器械数据库实务](references/EU_EUDAMED数据库实务.md)
- [中国医疗器械委托生产（注册人制度）实务](references/CN_医疗器械委托生产MAH实务.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [JSON strings returned through MCP tools, including hub metadata, snippets, official links, and classification-pathway guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local read-only retrieval over bundled or user-selected regulatory reference Markdown files.]

## Skill Version(s):

1.0.0 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
