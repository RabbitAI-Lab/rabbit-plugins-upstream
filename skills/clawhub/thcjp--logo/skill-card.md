## Description:

用AI图像工具自动生成专业Logo，支持提示语结构、结果校验及多格式导出，适合品牌设计与视觉创作。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, developers, independent creators, and brand teams use this skill to draft logo prompts, check generated logo quality, and prepare exports for brand and visual design workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad local read, write, and execution authority for a logo-design workflow.

Mitigation: Run it only in a constrained agent environment and prefer a narrowed version that removes execution permission unless command use is explicitly needed.

Risk: The artifact includes unrelated automation and security-review claims that do not directly support logo design.

Mitigation: Rely on the logo prompt, validation, and export guidance only, and review unrelated operational claims before use.

Risk: API-key setup guidance appears in the artifact.

Mitigation: Provide credentials through the host agent's secret-management mechanism and avoid committing API keys or generated configuration containing secrets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/logo)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration, Shell commands]

**Output Format:** [Markdown with prompt templates, parameter guidance, validation notes, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include logo prompt structures, quality checks, export guidance, and setup notes for API-key-based image generation workflows.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
