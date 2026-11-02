## Description:

Resize an image into a Twitter/X header banner (5:2, 1500x600) using ImageMagick. The image is rescaled to fit and the leftover space is padded black — never cropped, so no content is lost. Use when the user wants a Twitter/X banner for an article or infographic. Twitter/X is the only target: LinkedIn and blog headers accept the original image, so never generate a derivative for them. Never overwrites the original — writes a new file beside it.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to prepare an image as a Twitter/X header banner while preserving the full image and leaving the original file unchanged.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The example command may place the output in an unintended folder.

Mitigation: Before conversion, confirm the full output path beside the source, check that exact path for an existing file, and safely quote both file paths.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j3ffyang/skills/resize-for-banner)

## Skill Output:

**Output Type(s):** [Files]

**Output Format:** [PNG image]

**Output Parameters:** [1500×600 pixels (5:2 aspect ratio)]

**Other Properties Related to Output:** [Image is resized to fit and centered with black padding; it is not cropped, and the original remains unchanged.]

## Skill Version(s):

1.0.4 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
