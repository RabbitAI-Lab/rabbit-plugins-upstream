## Description:

投前 AI 图真实性质检：对待检图输出风险等级、8 项逐条判定和可直接追加到 prompt 的修正句，并支持自动重跑直到达标。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and creative teams use this skill to pre-screen AI-generated product images before advertising or listing. It produces a risk level, evidence for eight common image-quality risks, a go/no-go recommendation, and prompt-ready correction text for reruns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and images may be sent to the selected AI provider for visual review.

Mitigation: Use approved providers, prefer trusted local image files over untrusted URLs, and avoid submitting sensitive or rights-restricted images.

Risk: The visual review model may miss real defects or flag acceptable images incorrectly.

Mitigation: Treat the report as pre-screening guidance and keep a human final review before advertising, listing, or compliance decisions.

Risk: Custom provider endpoints or unverified CLI packages can create execution and data-handling risk.

Mitigation: Verify the dlazy executable or package source, avoid custom provider base URLs unless controlled, and use dry-run or doctor checks before production use.

Risk: Bundled shared tooling includes a remove-watermark task that can be misused when image rights are unclear.

Mitigation: Do not use watermark-removal behavior unless the user has clear rights to modify the image.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/detect-task)
- [Model flags for claude-sonnet-5](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [Platform image specs](references/platform-specs.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown report with tables and prompt correction snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes risk level, eight-item findings,投放建议, and up to three prompt correction sentences.]

## Skill Version(s):

1.0.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
