## Description:

Turns a product image into a short, motion-controlled product listing video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Online sellers and creative teams use the skill to turn an existing product image into a 3–5 second video for a product listing, with suggested camera and material motion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images and prompts are sent to the configured generation provider.

Mitigation: Choose the provider explicitly and send confidential assets only when its data handling is acceptable.

Risk: Generation can incur charges or retrieve untrusted image URLs.

Mitigation: Use --dry-run before paid runs and avoid untrusted or internal image URLs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/main-image-video)
- [Video backend configuration](references/video-backends.md)
- [Provider CLI reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Video files, Shell commands, Guidance]

**Output Format:** [MP4 video and text instructions with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically 3–5 seconds; duration and platform requirements depend on the selected model and marketplace.]

## Skill Version(s):

1.0.19 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
