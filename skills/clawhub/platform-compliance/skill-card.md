## Description:

Checks product listing images against measurable marketplace requirements and can create corrected images for supported issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketplace sellers and listing teams use this skill to check product images for platform-specific size, background, format, and composition requirements before upload, then optionally save corrected images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package includes optional cloud generation that may send prompts and product images to external providers.

Mitigation: Use the local image checker for local-only reviews; choose a provider deliberately and avoid sending confidential images without approval.

Risk: Pixel-based checks cannot detect watermarks, text, or damaged product depictions, and marketplace rules may change.

Mitigation: Review visual content separately and confirm current platform rules before relying on a pass result.

Risk: Automatic geometry fixes may crop product images or leave visual defects unchanged.

Mitigation: Inspect the proposed changes and review corrected images before uploading.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/platform-compliance)
- [Platform image specifications](artifact/references/platform-specs.md)
- [Provider CLI and data flow](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Image files]

**Output Format:** [Plain-text or JSON compliance reports; corrected image files when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports check outcomes and rejection risks; optional fixes are saved separately from input images.]

## Skill Version(s):

1.0.19 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
