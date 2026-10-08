## Description:

Helps sellers adapt product listings for different markets with localized copy, size conversions, regional image variants, and labeling reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and listing teams use this skill to prepare region-specific product copy, size guides, and listing images for marketplaces. It offers platform checks and labeling reminders, not legal or translation certification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied images may be sent to the selected AI provider.

Mitigation: Choose the provider explicitly and submit only images and product information approved for external processing.

Risk: Untrusted image URLs could point to internal or sensitive resources.

Mitigation: Use trusted local images or approved public URLs; avoid untrusted internal URLs.

Risk: Generated images and automatic fixes write to output paths, while localized text, sizes, and listing requirements can be inaccurate.

Mitigation: Review target paths and retain originals; have a native speaker check important copy, verify measurements, and confirm current marketplace and labeling rules before listing.

Risk: Shared tooling exposes unrelated tasks, including watermark removal.

Mitigation: Invoke only the intended localization tasks and use other tasks only with a lawful, deliberate purpose.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/cross-border-localize)
- [Platform image specifications](artifact/references/platform-specs.md)
- [Provider CLI and data flow](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands, Image files]

**Output Format:** [Localized copy and size tables in text or Markdown; generated marketplace images and image-check results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image variants and checks depend on the chosen market, platform, provider, and supplied reference images.]

## Skill Version(s):

1.0.15 (source: skill frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
