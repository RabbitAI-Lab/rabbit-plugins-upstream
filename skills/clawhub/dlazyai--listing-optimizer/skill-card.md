## Description:

Creates controlled product-image A/B variants with a single-variable hypothesis for each group and a template for reviewing results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and listing teams use it to plan product-image comparisons, changing one visual variable at a time and recording a hypothesis before testing. It also provides a fill-in review template; sellers supply their own marketplace metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports a mismatch between the stated A/B purpose and some behavior, and notes that analysis was incomplete.

Mitigation: Review the proposed prompts, commands, and outputs before running them, and confirm they match the intended experiment.

Risk: Prompts and supplied product images may be sent to an external image-generation service.

Mitigation: Choose a provider whose data handling suits the material and avoid sending images you cannot share with that provider.

Risk: Built-in image checks cover a limited subset of marketplace rules, which can change.

Mitigation: Check current official marketplace requirements before publishing; do not treat automated image checks as complete approval.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/dlazyai/skills/listing-optimizer)
- [Platform compliance skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/platform-compliance/skill.md)
- [Brand kit skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)

## Skill Output:

**Output Type(s):** [Images, Markdown, Shell commands, Guidance]

**Output Format:** [Image files and Markdown experiment plans with hypotheses and a review table; shell commands for generation and image checks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Marketplace metrics are entered by the user; the skill does not assess statistical significance.]

## Skill Version(s):

1.0.29 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
