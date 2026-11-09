## Description:

投放前检查 AI 生成的商品图，给出风险等级、八项逐条判定、投放建议和可追加到生成提示词的修正句。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users preparing AI-generated product images for ecommerce can use the skill to review visual defects and platform concerns before listing. It returns a structured report with suggested prompt corrections when an image needs another generation pass.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is marked suspicious, and its security inspection was partial; uninspected behavior is not established as safe.

Mitigation: Review the ClawScan status and the skill's behavior before installing or using it with sensitive work.

Risk: The reported workflow may upload images and prompts to external services.

Mitigation: Check the reported uploads and external services against your privacy needs before submitting images or prompts.

Risk: The reported workflow may edit images and overwrite workflow files.

Mitigation: Review proposed edits and workflow changes, and keep recoverable copies before allowing overwrites.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [Model flags reference](references/model-flags.md)
- [Platform image specifications](references/platform-specs.md)
- [Example review report](https://github.com/dlazy-ai/ecommerce-skills/blob/main/docs/detect-task/example-report.md)
- [ClawHub listing](https://clawhub.ai/dlazyai/skills/detect-task)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Structured Chinese Markdown review with an English prompt-fix section]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Risk level, eight fixed checks, listing recommendation, and one to three prompt corrections when needed; supports up to ten images per call.]

## Skill Version(s):

1.0.31 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
