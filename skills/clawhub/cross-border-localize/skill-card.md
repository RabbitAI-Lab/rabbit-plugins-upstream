## Description:

Localizes one set of cross-border e-commerce product assets into region-ready copy, size tables, marketplace image variants, and compliance-label prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, marketplace operators, and cross-border e-commerce teams use this skill to adapt listing copy, image prompts, sizing information, and platform checks for target regions before publishing product listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images and prompts may be uploaded to the selected cloud generation provider.

Mitigation: Use only approved providers for the workflow, avoid unreleased or confidential product assets unless approved, and run with --dry-run to inspect planned requests before upload or spending credits.

Risk: Generated non-English text can contain wording, character, or typography errors.

Mitigation: Prefer generating text-free base images and adding localized copy in post-production, or have native speakers review all text before publishing.

Risk: Compliance-label suggestions are not legal advice.

Mitigation: Treat labels such as composition, origin, and certification marks as prompts for review and confirm final requirements with qualified regional channels before listing.

Risk: Marketplace image rules can change and the checker covers only machine-checkable image properties.

Mitigation: Confirm current marketplace documentation, override built-in rules when needed, and manually review text, watermarks, borders, and collage-like layouts.

## Reference(s):

- [Platform image specifications](artifact/references/platform-specs.md)
- [Provider CLI and data flow reference](artifact/references/provider-cli.md)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/cross-border-localize)
- [dLazy CLI source](https://github.com/dlazyai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands, optional JSON status output, and generated image files when a provider is called.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include localized listing copy, size conversion tables, image-generation commands, platform check results, and saved marketplace image assets.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
