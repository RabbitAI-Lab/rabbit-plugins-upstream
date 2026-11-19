## Description:

Removes watermarks, text, logos, badges, and decorative frames from images by reconstructing the covered areas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to remove unwanted text and graphics from images or prepare clean images for downstream image workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks this release suspicious because reported capabilities extend beyond watermark removal, it may send images or prompts to external providers without clear disclosure, and parts of the scan were incomplete.

Mitigation: Review the provider and its data-sharing terms before use, avoid sensitive images or prompts unless approved, and review the skill with a complete security scan.

## Reference(s):

- [Provider CLI guide](references/provider-cli.md)
- [Image model parameters](references/model-flags.md)
- [Fission Pattern workflow](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/fission-pattern/skill.md)
- [Clothing Grass Planting workflow](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/clothing-grass-planting/skill.md)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Guidance]

**Output Format:** [Reconstructed image files (JPEG by default) and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reconstructed areas are model-inferred and may alter occluded details or nearby image content; inspect results before use.]

## Skill Version(s):

1.0.34 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
