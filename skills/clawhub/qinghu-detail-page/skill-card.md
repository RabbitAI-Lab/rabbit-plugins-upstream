## Description:

根据商品图自动生成详情页图片套图，整合卖点、场景、参数及营销内容，帮助快速制作高转化详情页。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External commerce sellers and content operators use this skill to generate ordered product detail-page image sets from a required product reference image, optional theme, and optional selling-point copy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party qhkit CLI that uploads product images to Qinghu and consumes account credits.

Mitigation: Use only when the user accepts Qinghu processing and credit consumption; estimate credits before generation and disclose actual credits after completion.

Risk: Setup and upgrade instructions give significant control to third-party npm tooling and remote messages.

Mitigation: Prefer a pinned local installation, review upgrade commands before running them, and avoid executing commands copied from untrusted CLI output.

Risk: Token setup can expose credentials if secrets are typed directly into command arguments.

Mitigation: Provide tokens through safer secret handling such as environment variables or the host secret mechanism instead of exposing them in shell history.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-detail-page)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown or text with inline shell commands and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ordered image URLs and actual credit usage returned by qhkit.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
