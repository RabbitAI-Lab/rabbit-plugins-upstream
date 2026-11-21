## Description:

Generates short product videos from static product images, with controllable camera movement and material motion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers and teams use this skill to turn an existing product image into a short listing video, typically 3–5 seconds long, with a chosen camera move or subtle material motion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts and input images to an external generation provider; the security review also notes unclear tool scope and a possible mismatch between the stated purpose and broader capabilities.

Mitigation: Choose a provider whose data handling fits the images, review the scripts and requested scope, and use --dry-run to inspect a request before generation.

Risk: The benign security assessment has medium confidence: only half of the listed components were fully scanned, and some code could not be fully interpreted.

Mitigation: Review the skill before use and begin with one short clip before running a batch.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/main-image-video)
- [Video backend setup](references/video-backends.md)
- [Provider and CLI reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Video files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Short product video files (typically MP4), with shell commands and prompt guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically 3–5 seconds; available duration and output details depend on the selected video model.]

## Skill Version(s):

1.0.30 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
