## Description:

Helps agents plan e-commerce main-image A/B tests by generating controlled image variants, recording hypotheses, checking listing compliance, and producing a recap template.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace operators, and e-commerce agents use this skill to plan controlled main-image experiments, generate image variants, run objective listing checks, and prepare a recap table for click-through and conversion data supplied by the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos, prompts, and brand references may be sent to the selected cloud generation provider.

Mitigation: Use dry-run mode or explicit provider selection before execution, avoid confidential assets and untrusted image URLs, and choose a provider whose data handling is acceptable.

Risk: API keys for selected providers could expose account access if mishandled.

Mitigation: Use scoped, revocable keys in provider-supported configuration or environment variables, and rotate or revoke keys when they are no longer needed.

Risk: Generated variants can undermine an A/B test if more than one variable changes or if platform compliance issues cause rejected listings.

Mitigation: Change one variable at a time, write the hypothesis before launch, run listing checks, and treat low-sample results as inconclusive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/listing-optimizer)
- [Platform image specifications](references/platform-specs.md)
- [Provider CLI reference](references/provider-cli.md)
- [platform-compliance skill](https://github.com/dlazyai/ecommerce-skills/blob/main/skills/platform-compliance/skill.md)
- [brand-kit skill](https://github.com/dlazyai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)
- [dLazy CLI](https://github.com/dlazyai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, image files]

**Output Format:** [Markdown guidance with bash commands, listing-check reports, optional JSON command output, and generated image files saved to disk.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated variants should change one experimental variable at a time; user-supplied marketplace metrics are needed for the recap.]

## Skill Version(s):

1.0.0 (source: evidence release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
