## Description:

Helps agents turn one ecommerce product asset set into localized regional listing copy, size conversion tables, marketplace-specific image prompts, and compliance-label reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce operators, marketers, and developers use this skill to prepare cross-border product listings for different regions, including localized copy, sizing guidance, image generation commands, and pre-publish platform checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and product or reference images may be sent to the configured image provider.

Mitigation: Review the selected provider's data handling terms before using confidential catalog assets.

Risk: Generated foreign-language text, legal labels, and marketplace compliance cues may be incorrect or incomplete.

Mitigation: Manually verify translated text, sizing, legal compliance, and platform rules before publishing listings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/cross-border-localize)
- [Platform image specifications](references/platform-specs.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, tables, and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save generated ecommerce image files when the configured image provider is invoked.]

## Skill Version(s):

1.0.10 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
