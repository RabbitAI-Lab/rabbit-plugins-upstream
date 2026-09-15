## Description:

上架前平台合规校验与自动修复。待上架图 → Amazon / TikTok Shop / Temu / Shopee / 淘宝 各平台的通过或驳回风险报告，可一键修成合规图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace operators, and developers use this skill to check whether listing images meet marketplace image requirements before upload and to apply local geometric or color fixes when supported.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional generation scripts can send prompts, images, and configured credentials to external AI providers.

Mitigation: Use the local checker for compliance inspection unless external generation is intended, and avoid configuring provider API keys for local-only workflows.

Risk: Automated fixes only address geometric and color compliance and do not detect or remove watermarks, text, compositing issues, or product defects.

Mitigation: Review fixed images before marketplace upload and use visual inspection or a separate content-quality process for issues outside pixel-level checks.

Risk: Image parsing depends on Pillow and processes user-supplied files.

Mitigation: Install Pillow in an isolated, pinned environment and process trusted files where possible.

## Reference(s):

- [Platform Image Specifications](references/platform-specs.md)
- [Provider CLI Reference](references/provider-cli.md)
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/platform-compliance)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and optional JSON checker output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce fixed image files when the local checker is run with --fix.]

## Skill Version(s):

1.0.8 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
