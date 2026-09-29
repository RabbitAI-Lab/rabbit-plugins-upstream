## Description:

Helps create Chinese-language ecommerce product images with concise selling points and promotional badges from a supplied product photo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers and designers use this skill to prepare a product hero image with readable Chinese feature text and a verified promotional message.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos, selling points and prompts may be sent to a cloud image provider.

Mitigation: Choose the provider explicitly, inspect the request with --dry-run, and obtain approval before submitting confidential assets.

Risk: Generated copy or visuals may misstate product features or promotions or render Chinese text incorrectly.

Mitigation: Verify feature claims and promotion terms against source information, and inspect the finished image and text before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/item-selling-point)
- [Provider CLI reference](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands]

**Output Format:** [Markdown with image prompts and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Running the commands can save generated product images locally; review the image and text before publication.]

## Skill Version(s):

1.0.14 (source: SKILL.md frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
