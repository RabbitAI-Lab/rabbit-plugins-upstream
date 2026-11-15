## Description:

Extracts a garment from a photo and produces a clean, white-background e-commerce flat-lay image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce teams use this skill to turn photos of people wearing garments into clean product flat-lay images for listings or downstream image workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source photos may be sent to external image services, and the security scan notes that some code was only partially analyzed.

Mitigation: Before use, decide whether each photo is appropriate for external processing, and review the skill before installation.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [Image model parameters](references/model-flags.md)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/clothing-extraction)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Guidance]

**Output Format:** [JPEG or PNG flat-lay images, with Markdown guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The image presents the selected garment flat, centred, and on a white background; obscured design details may be inferred and should be reviewed.]

## Skill Version(s):

1.0.33 (source: frontmatter, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
