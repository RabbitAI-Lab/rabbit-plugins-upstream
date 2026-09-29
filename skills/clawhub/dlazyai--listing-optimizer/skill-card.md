## Description:

Helps ecommerce teams generate controlled A/B variants of product main images, record hypotheses, check image compliance, and prepare a results-review template.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers and marketing teams use this skill to compare product listing images while changing one variable at a time, then record hypotheses and review performance after they supply campaign data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos and prompts may be sent to an external image-generation provider.

Mitigation: Check the selected provider with dry-run or doctor options and obtain organizational approval before sending confidential or regulated images.

Risk: Generated assets are saved to local paths and images may not meet marketplace requirements.

Mitigation: Review output paths before saving and check images against the target platform's requirements before publishing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/listing-optimizer)
- [Platform image specifications](references/platform-specs.md)
- [Image-generation provider guide](references/provider-cli.md)
- [Platform compliance guidance](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/platform-compliance/skill.md)

## Skill Output:

**Output Type(s):** [Image files, Markdown, Guidance]

**Output Format:** [Generated product images and a Markdown A/B experiment review template]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each group includes a predeclared hypothesis; users must supply exposure, click, and conversion data for review.]

## Skill Version(s):

1.0.10 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
