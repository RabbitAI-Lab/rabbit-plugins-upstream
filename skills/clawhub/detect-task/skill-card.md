## Description:

投前 AI 图真实性质检：审查待检图，输出风险等级、8 项逐条判定、投放建议，以及可追加到生成 prompt 的修正句。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, designers, and agent workflows use this skill before publishing AI-generated product imagery. It produces a concise quality-control report that identifies visual risks, recommends whether to publish, rerun, or manually retouch, and supplies prompt fixes for another generation pass.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User images and prompts may be sent to dLazy or to another configured provider.

Mitigation: Use only images and prompts that are appropriate for the selected provider, avoid sensitive or private images, and confirm provider selection before execution.

Risk: The artifact includes automatic rerun and file-output paths broader than simple image inspection.

Mitigation: Run dry-run checks first and use automatic rerun or fix scripts only when image generation, modification, and local output files are intended.

Risk: Model inspection can miss defects or flag acceptable images incorrectly.

Mitigation: Treat the report as pre-publication quality-control guidance and keep human review for final publication decisions.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/dlazyai/skills/detect-task)
- [Example Detection Report](https://github.com/dlazy-ai/ecommerce-skills/blob/main/docs/detect-task/example-report.md)
- [Model Flags](references/model-flags.md)
- [Provider CLI](references/provider-cli.md)
- [Platform Specs](references/platform-specs.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report text with optional shell commands and prompt-fix guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include a risk level, eight inspection items with evidence, a publication recommendation, and one to three English prompt-fix sentences when remediation is needed.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
