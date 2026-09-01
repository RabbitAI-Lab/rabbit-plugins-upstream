## Description:

Localizes ecommerce product assets into region-specific listing copy, size conversion guidance, marketplace image variants, and compliance-label prompts for cross-border sales.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce operators, marketplace teams, and developers use this skill to adapt product listings for multiple regions by rewriting listing copy, preparing image-generation prompts, checking platform image requirements, and documenting size and compliance notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and referenced images may be sent to the configured generation provider.

Mitigation: Use dry-run and explicit provider selection when possible, and avoid confidential or customer-sensitive media.

Risk: Localized text, non-English image text, size conversions, and compliance-label prompts may be inaccurate.

Mitigation: Review translated text with a qualified native speaker and confirm compliance labels through appropriate professional channels before publishing listings.

Risk: Marketplace image rules can change and automated checks cover only a subset of listing requirements.

Mitigation: Check the latest marketplace requirements and manually inspect text, watermark, border, layout, and policy-sensitive content before upload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/cross-border-localize)
- [Platform image specifications](references/platform-specs.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, JSON, Guidance]

**Output Format:** [Markdown guidance with bash commands, generated image files, and optional JSON status or listing-check reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run and provider selection; image generation may send prompts and referenced images to the configured provider.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
