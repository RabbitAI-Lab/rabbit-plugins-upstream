## Description:

Rescale an image into LinkedIn article and Twitter/X banner versions with ImageMagick, preserving aspect ratio by fitting the image and adding black padding instead of cropping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, content creators, and documentation authors use this skill to convert a source image into social banner assets with fixed platform dimensions while keeping the original image unchanged.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated banner output paths could collide with existing files.

Mitigation: Confirm the source image, target dimensions, and exact output filenames before running ImageMagick, and stop for user approval if an output already exists.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j3ffyang/skills/resize-for-banner)
- [Publisher profile](https://clawhub.ai/user/j3ffyang)

## Skill Output:

**Output Type(s):** [shell commands, files, guidance]

**Output Format:** [Markdown guidance with ImageMagick shell commands and generated PNG file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces new banner PNG files beside the source image and leaves the original image unchanged.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
