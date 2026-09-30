## Description:

Checks listing images against machine-checkable marketplace requirements and can save corrected copies for supported image issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and their agents check product images for measurable listing requirements across supported marketplaces before upload. They can review rejection risks and optionally save corrected image copies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Marketplace requirements can change, and the checks cover only measurable image properties.

Mitigation: Confirm current platform requirements and have a person review text, watermarks, product accuracy, and other content before upload.

Risk: Automatic corrections may change image composition or quality.

Mitigation: Inspect corrected copies before publishing; keep the original images and approve changes before using --fix.

Risk: Optional generation helpers can send prompts or images to an external provider.

Mitigation: Use those helpers only with permission to share the inputs with the selected provider; the local checker does not require them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/platform-compliance)
- [Platform image specifications](artifact/references/platform-specs.md)
- [Optional provider usage and data flow](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Image files, Guidance]

**Output Format:** [Plain-text or JSON compliance report; optional corrected image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-check pass, warning, or fail results; corrected images are saved separately when requested.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
