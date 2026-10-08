## Description:

Checks product listing images against measurable marketplace requirements and can create revised images to address supported issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and developers check product images before listing them on Amazon, TikTok Shop, Temu, Shopee, Shopify, or Taobao, and optionally generate revised images for measurable specification failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An automated pass does not check text, watermarks, or product quality.

Mitigation: Review image content separately before publishing.

Risk: Automatic revisions may change image framing, and marketplace requirements can change.

Mitigation: Review revised images before publishing and compare requirements with current marketplace guidance.

Risk: Optional provider-backed generation can transmit prompts and images to external services and requires credentials.

Mitigation: Use the local listing checks by default; use provider-backed generation only when intended and after reviewing data sharing and credentials.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/platform-compliance)
- [Platform image specifications](artifact/references/platform-specs.md)
- [Optional provider tooling and data flow](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Images]

**Output Format:** [Human-readable check report or JSON; optional revised image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports batch checks and exit status for listing risks; revisions are saved separately from originals.]

## Skill Version(s):

1.0.17 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
