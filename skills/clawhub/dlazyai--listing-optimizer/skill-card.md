## Description:

Helps ecommerce teams plan controlled main-image A/B tests, generate comparison image sets, check listing constraints, and prepare a retrospective template.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and developers use this skill to run single-variable listing-image experiments, generate candidate image sets, check platform image constraints, and capture user-supplied performance results for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and reference images may be sent to dLazy or a selected third-party generation provider.

Mitigation: Use explicit provider settings when vendor choice matters, avoid sensitive or unlicensed images, and review provider terms before generation.

Risk: Generated listing images can be inaccurate, overpromise product qualities, or miss platform rules that pixel checks cannot detect.

Mitigation: Run the listing checks, then manually review product accuracy, text, watermarks, claims, and platform-specific requirements before publishing.

Risk: A/B conclusions can be misleading when more than one variable changes or the sample size is too small.

Mitigation: Change one variable at a time, write the hypothesis before launch, and require adequate exposure before drawing conclusions.

Risk: Bundled shared task metadata includes a remove-watermark task outside the core listing-optimizer workflow.

Mitigation: Ignore watermark-removal behavior unless the user has rights to the source material.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/listing-optimizer)
- [Platform image specifications](references/platform-specs.md)
- [Provider CLI reference](references/provider-cli.md)
- [Platform compliance companion skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/platform-compliance/skill.md)
- [Brand kit companion skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands, listing-check results, and retrospective tables; generation commands can save image files and optional JSON status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided product prompts, optional reference images, provider credentials, and post-launch performance metrics.]

## Skill Version(s):

1.0.1 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
