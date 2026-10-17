## Description:

帮助分析工程建设招投标信息，提取项目金额、企业资质背景和关键字段，并汇总相关业绩。

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

建筑行业从业者及分析人员可查询工程招投标项目，比较项目金额与中标企业背景，并汇总项目业绩。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts zhiliaobiaoxun services and may create an account using a hashed device identifier.

Mitigation: Review the account flow and obtain informed consent before collecting device attributes or registering; use a manually supplied API key where possible.

Risk: An automatically obtained service API key is stored locally and could be exposed if the file is accessible to others.

Mitigation: Prefer a trusted secret mechanism for ZLBX_API_KEY and protect access to ~/.zlbx/config.json.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/pkuycl/skills/construction-tender-analyzer-jianshetong)
- [API search reference](references/api-search.md)
- [Company registry reference](references/api-registry.md)
- [Account registration reference](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Analysis, Markdown, Guidance]

**Output Format:** [Markdown text with project details and performance summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on access to the service and its available records.]

## Skill Version(s):

1.0.10 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
