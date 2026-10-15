## Description:

Helps sellers adapt product copy, sizing guidance, listing images, and compliance reminders for different markets and e-commerce platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and creative teams use this skill to prepare localized product copy, size charts, regional listing images, and reminders about labeling requirements before publishing across markets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured cloud generation providers may receive product prompts and uploaded images.

Mitigation: Use an approved provider, inspect the request with --dry-run, and avoid sending sensitive unpublished assets without approval.

Risk: Generated foreign-language text, sizing, and regional labeling suggestions may be inaccurate.

Mitigation: Have a native speaker check text, verify sizes against the brand chart, and confirm listing and labeling requirements before publication.

Risk: Generation may consume paid credits or produce imagery that does not match the intended brand or audience.

Mitigation: Inspect the --dry-run cost estimate and edit the brand configuration to reflect the actual brand constraints and intended model demographics.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/cross-border-localize)
- [Platform image specifications](references/platform-specs.md)
- [Generation provider guide](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Images, Guidance]

**Output Format:** [Localized product copy and size tables, generated listing images, and listing-check guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review translated image text and regional requirements before publication.]

## Skill Version(s):

1.0.18 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
