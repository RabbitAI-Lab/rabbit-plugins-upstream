## Description:

Localizes ecommerce product materials for cross-border markets with region-aware copy, size references, imagery, platform specifications, and compliance-label guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and ecommerce listing teams use this skill to adapt product copy, size references, imagery, and platform checks for selected regional marketplaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images and prompts may be sent to an external image provider.

Mitigation: Choose the provider explicitly, use --dry-run before sending images or spending credits, and provide only material you can share with that provider.

Risk: The image checker has an exit-code defect, so its exit status may not reflect the report accurately.

Mitigation: Read the checker report for errors instead of relying on its exit code.

Risk: Generated translations or regional compliance guidance may be incorrect or incomplete.

Mitigation: Manually verify translations and compliance details before listing; consult a professional channel for formal compliance advice.

## Reference(s):

- [Platform Image Specifications](references/platform-specs.md)
- [Image Provider CLI Reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Images, Shell commands, Guidance]

**Output Format:** [Localized listing copy, sizing tables, image assets, and platform-check reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation uses the selected provider; translations and compliance guidance need human review.]

## Skill Version(s):

1.0.26 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
