## Description:

Jary66原创，企业战略专利布局分析（模板驱动版）。通过了解企业产品及经营动态与企业全球专利，做对比映射分析。从知产管理视角了解企业的专利布局情况、优势、不足、风险、下一步行动计划等。输出为独立HTML文件（所有CSS和图表内联，零外部依赖）。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, IP teams, and patent strategy analysts use this skill to turn uploaded enterprise patent lists and business context into a structured patent strategy report. The report compares product and operating signals with global patent assets to surface layout strengths, gaps, risks, and action plans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to install Python packages and authorize the PatSnap/Zhihuiya MCP integration.

Mitigation: Approve installation and MCP access only in a trusted runtime and account approved for the intended patent analysis workflow.

Risk: Patent lists and business context can contain confidential strategy or intellectual property data.

Mitigation: Avoid highly confidential files unless the configured platform, runtime, and MCP account are approved for that data.

## Reference(s):

- [Skill Definition](artifact/SKILL.md)
- [HTML Skeleton Template](artifact/references/html_skeleton.md)
- [Section Specifications](artifact/references/section_specs.md)
- [Data Preparation Specification](artifact/references/data_prep.md)
- [PatSnap Zhihuiya Open Platform](https://open.zhihuiya.com/)

## Skill Output:

**Output Type(s):** [analysis, code, shell commands, configuration, guidance, files]

**Output Format:** [Standalone HTML report with inline CSS and base64 chart images, plus Markdown and Python guidance during execution]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires approved Python package installation and PatSnap/Zhihuiya MCP authorization for full data retrieval; final report is designed to have zero external runtime dependencies.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
