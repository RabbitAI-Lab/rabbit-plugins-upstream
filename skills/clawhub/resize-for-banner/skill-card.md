## Description:

Rescale a source image into LinkedIn and Twitter/X banner sizes with ImageMagick, preserving aspect ratio with padding and leaving the original file untouched.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, content creators, and agents use this skill to convert screenshots or other images into social banner formats for LinkedIn articles and Twitter/X headers without cropping source content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs local ImageMagick commands on user-selected images and creates new banner files next to the source.

Mitigation: Confirm the source path, target sizes, and exact output filenames before conversion; verify generated dimensions after execution and leave the original file unchanged.

Risk: Existing output filenames could conflict with files already present beside the source image.

Mitigation: Check proposed output paths before writing and stop for user confirmation or alternate filenames when an output already exists.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/j3ffyang/skills/resize-for-banner)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Markdown with inline shell commands and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates new banner image files beside the source image; does not modify the original file.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
