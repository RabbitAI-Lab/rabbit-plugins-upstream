## Description:

上架前平台合规校验与自动修复。待上架图 → Amazon / TikTok Shop / Temu / Shopee / 淘宝 各平台的通过或驳回风险报告，可一键修成合规图。当用户说「会不会被驳回」「合规检查」「白底不达标」「主图规格」「传上去被拒」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, ecommerce operators, and marketplace teams use this skill to check product listing images against platform-specific machine-checkable requirements, identify rejection risks, and optionally create fixed copies for compliant upload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled cloud generation workflows can send prompts and images to a selected provider and use local API credentials or CLI authentication.

Mitigation: Use the local compliance checker path for routine checks, and invoke generation workflows only after confirming the provider, credential source, data sharing expectations, and billing impact.

Risk: Fix and generation modes can write new files locally, including corrected listing images or downloaded provider outputs.

Mitigation: Run with explicit input paths and output directories, review generated files before upload, and avoid using broad output locations for untrusted batches.

## Reference(s):

- [Platform Image Specifications](references/platform-specs.md)
- [Provider CLI Reference](references/provider-cli.md)
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/platform-compliance)
- [ClawHub Publisher Profile](https://clawhub.ai/user/dlazyai)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands, optional JSON checker results, and optional corrected image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Checker output can use nonzero exit codes for rejection risk; fix mode writes separate corrected copies rather than overwriting originals.]

## Skill Version(s):

1.0.10 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
