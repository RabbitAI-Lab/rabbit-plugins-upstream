## Description:

Helps agents prepare cross-border ecommerce listing variants with localized copy, size conversion guidance, regional image-generation prompts, platform image checks, and compliance-label reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketplace operators, ecommerce teams, and agent developers use this skill to turn one product asset set into region-specific listing guidance, localized image prompts, size tables, and platform image validation commands before publishing internationally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images and prompts may be uploaded to external generation providers.

Mitigation: Use only approved providers and avoid confidential product, customer, or unreleased brand assets unless the provider is cleared for that data.

Risk: The bundled tooling can fetch arbitrary image URLs and route requests to a custom ARK_BASE_URL.

Mitigation: Prefer local image files, restrict network egress in shared environments, and use only trusted HTTPS endpoints for provider overrides.

Risk: The package includes broader media-generation tasks, including an unrelated remove-watermark task, beyond cross-border localization.

Mitigation: Limit installed or executable tasks to the localization workflow and remove or block unrelated tasks when deploying in controlled environments.

Risk: Localized text, size conversions, and compliance-label suggestions can be inaccurate or incomplete.

Mitigation: Have native speakers, brand owners, and qualified compliance reviewers check final listing assets before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/cross-border-localize)
- [Platform image specifications](artifact/references/platform-specs.md)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands, generated image files, optional JSON command output, and listing-check reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call external image-generation providers and write generated media to local output paths.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
