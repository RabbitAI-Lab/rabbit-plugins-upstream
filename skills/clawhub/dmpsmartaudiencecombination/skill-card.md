## Description:

基于用户自然语言投放需求，按"需求解析→标签召回→画像补全→质量排序→用户选择→Overlap（仅MUST vs 可选）→递进组合→创建组合人群"的循序渐进流程，输出可直接用于明日DMP组合人群（audienceType=2）的标签组合规则与人群包创建参数。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mingri26](https://clawhub.ai/user/mingri26)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing operators and DMP users use this skill to translate natural-language audience targeting requirements into structured tag recommendations, overlap checks, combination rules, and audience package creation parameters for 明日DMP. The skill supports a staged confirmation workflow before final audience creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive DMP Access Key and Secret Key credentials.

Mitigation: Use it only in a controlled workspace, treat stored DMP credentials as sensitive, and avoid exposing credentials in conversation or logs.

Risk: The skill can rely on a local authentication helper and has authority to create DMP audience packages.

Mitigation: Install mingdata-dmp-auth from a trusted source first, avoid workspaces where untrusted files can influence local helpers, and require explicit user confirmation before audience-creation API calls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mingri26/skills/dmpsmartaudiencecombination)
- [技能总览](references/技能总览.md)
- [API reference](references/api_reference.md)
- [凭证获取指南](references/凭证获取指南.md)
- [技能安装与环境检查](references/技能安装与环境检查.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, API Calls, Configuration]

**Output Format:** [Chinese Markdown tables with structured JSON snippets and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces staged audience targeting recommendations, execution-parameter confirmations, overlap reports, and final DMP audience creation parameters.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
