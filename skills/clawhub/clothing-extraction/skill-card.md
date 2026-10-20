## Description:

Guides extraction of individual garments from photos into clean, white-background flat-lay product images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and content creators use this skill to turn photos of worn clothing into isolated, white-background flat-lay images for product listings or further image editing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source images and prompts are sent to the selected cloud image provider.

Mitigation: Use only images you have rights to process; avoid private or customer images unless authorized.

Risk: Generated commands use provider credentials and write output files.

Mitigation: Review the selected provider, credentials, and save paths before running commands.

Risk: Obscured clothing details are inferred rather than faithfully recovered.

Mitigation: Check the resulting image against the original, especially at obscured design features.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/clothing-extraction)
- [Image model options](artifact/references/model-flags.md)
- [Provider CLI and data flow](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can save generated flat-lay image files; inferred details in obscured areas require human review.]

## Skill Version(s):

1.0.25 (source: SKILL.md frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
