## Description:

Helps e-commerce teams localize one product asset set into region-specific listing copy, size-conversion tables, marketplace image variants, and compliance-label reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, localization teams, and developers use this skill to prepare marketplace-ready assets for cross-border listings, including localized copy, image-generation prompts, regional size guidance, and platform checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts, reference images, and provider credentials may be sent to the selected generation provider, and the Ark provider can use an environment-configured endpoint.

Mitigation: Use only trusted providers, avoid confidential assets, and leave ARK_BASE_URL unset or pin it to a reviewed HTTPS Ark endpoint.

Risk: An unreviewed or unpinned dLazy CLI installation can change the behavior of generation commands.

Mitigation: Prefer a reviewed and pinned dLazy CLI installation before running production workflows.

Risk: Generated non-English text, size conversions, and compliance-label suggestions can be incorrect or incomplete.

Mitigation: Have native speakers and appropriate compliance reviewers check localized text and required labels before publishing listings.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/cross-border-localize)
- [Platform Image Specs](references/platform-specs.md)
- [Provider CLI Reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON status output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save generated images to local paths; dry-run mode can report provider, model, prompt size, and estimated credits.]

## Skill Version(s):

1.0.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
