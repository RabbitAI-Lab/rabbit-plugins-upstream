## Description:

Render plain or styled text into SVG, PNG, JPG, or JPEG image files and return local file metadata, with optional data URI output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickong](https://clawhub.ai/user/erickong)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to convert text specs into local image files for upload, sharing, or embedding. It supports dimensions, output format, full-text and partial text colors, font size, wrapping, alignment, multilingual text, and transparent or solid backgrounds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can write generated image files to arbitrary paths when an explicit output path is supplied.

Mitigation: Run it in an environment that restricts filesystem writes and prefer tmp or workspace-only output paths.

Risk: Untrusted text specs can produce SVG output or large data URI payloads that may be unsafe or resource intensive downstream.

Mitigation: Avoid processing untrusted specs as SVG, disable data URIs for large renders, and review generated SVG before reuse.

Risk: Large image dimensions or input text can increase memory and processing cost because the skill does not enforce its own size limits.

Mitigation: Set external limits for image dimensions and input size before invoking the renderer.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/erickong/skills/text-to-image)

## Skill Output:

**Output Type(s):** [files, text, shell commands, configuration]

**Output Format:** [JSON metadata with a local image file path and optional data URI; generated files are SVG, PNG, JPG, or JPEG.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default output is written under the skill tmp folder; explicit output paths and data URI inclusion are supported.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
