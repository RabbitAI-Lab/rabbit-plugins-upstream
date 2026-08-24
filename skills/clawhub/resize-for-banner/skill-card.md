## Description:

Rescale an image into social banner versions using ImageMagick while preserving aspect ratio, padding unused space, and leaving the original image untouched.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to prepare profile, article, channel, and custom banner images without cropping source content or modifying the original file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image conversion writes new files and could target an unexpected path or filename.

Mitigation: Confirm the source image, target dimensions, and exact output paths with the user before running ImageMagick.

Risk: An existing output file could be overwritten if the chosen banner filename already exists.

Mitigation: Stop when an output file already exists and ask whether to overwrite it or choose a different suffix.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j3ffyang/skills/resize-for-banner)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Markdown guidance with inline ImageMagick shell commands and generated PNG image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are new banner PNG files named beside the source image; the original image is preserved.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
