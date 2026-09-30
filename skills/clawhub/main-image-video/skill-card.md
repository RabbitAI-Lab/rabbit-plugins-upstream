## Description:

Turns a product image into a 3–5-second video for an e-commerce listing using a selected video provider.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and content teams use this skill to turn existing product photos into short listing videos with controlled camera motion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts may be uploaded to the selected cloud video provider.

Mitigation: Use non-sensitive assets and confirm the provider's data handling before generation.

Risk: Video generation and batch runs can incur charges.

Mitigation: Run --dry-run first, explicitly select the intended video model and provider, and confirm costs before batch generation.

Risk: Local generation depends on external executables.

Mitigation: Use trusted local binaries for dlazy, node, and ffmpeg.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/main-image-video)
- [Video backend configuration](references/video-backends.md)
- [Provider CLI reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and video prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can save generated MP4 clips locally; model and provider must be selected explicitly.]

## Skill Version(s):

1.0.11 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
