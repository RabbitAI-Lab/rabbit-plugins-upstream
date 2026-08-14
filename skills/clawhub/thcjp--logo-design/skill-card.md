## Description:

Logo设计工具专业版帮助企业和设计团队通过 Agent 工作流生成批量 Logo 方向、自动矢量化输出、管理品牌变体并进行设计质量审计。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users, designers, brand teams, and developers use this skill to guide AI agents through commercial logo design workflows, including batch ideation, vector conversion, brand variant production, asset export, and quality checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent to execute shell commands and write files in a project workspace.

Mitigation: Use it only in directories where file changes are acceptable and require confirmation before command execution.

Risk: The skill may involve external AI image generation or other service calls that require credentials.

Mitigation: Provide only narrowly scoped credentials and confirm provider retention terms before sending brand assets or confidential material.

Risk: Generated logo concepts and vectorized assets may be unsuitable, misleading, or expose intellectual-property concerns.

Mitigation: Review final assets manually, run brand and copyright checks, and keep human approval in the release workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/logo-design)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON, YAML, Python, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide an agent to write brand asset files, run local commands, call external AI image services, and generate SVG, PNG, ICO, audit reports, or workflow configuration.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact frontmatter states 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
