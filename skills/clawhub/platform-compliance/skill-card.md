## Description:

Checks marketplace listing images against platform requirements, reports rejection risks, and can fix measurable image issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and ecommerce teams check listing images against marketplace image rules before upload, review rejection risks, and optionally save corrected images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional generation tooling can send images and prompts to external providers.

Mitigation: Use the local compliance checker for routine checks; run cloud generation only after reviewing the selected provider and data sharing.

Risk: Image checks cannot identify all content issues, and marketplace rules can change.

Mitigation: Review text, watermarks, and product quality separately, and confirm current platform requirements before publishing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/platform-compliance)
- [Platform image specifications](artifact/references/platform-specs.md)
- [Optional generation provider guide](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Image files]

**Output Format:** [Human-readable or JSON compliance reports; optionally corrected image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports batch checks and platform-specific or custom rules.]

## Skill Version(s):

1.0.13 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
