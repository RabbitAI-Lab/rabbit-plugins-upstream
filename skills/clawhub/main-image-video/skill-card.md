## Description:

静态主图转主图视频。一张商品图生成 3-5 秒可上架的主图短视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and developers use this skill to turn an existing product hero image into a short image-to-video clip with controlled camera motion, brand styling, and platform-oriented constraints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A brand configuration can reference readable local assets that may be uploaded to the selected cloud provider.

Mitigation: Inspect brand YAML files and referenced paths before use, avoid untrusted brand files, and run with --dry-run first to review extra images.

Risk: Prompts and uploaded images are sent to the configured generation backend.

Mitigation: Use only approved provider configuration and avoid sending confidential product images or prompts unless that provider is acceptable for the data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/main-image-video)
- [Provider CLI reference](references/provider-cli.md)
- [Video backend configuration](references/video-backends.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with inline shell commands and generated video file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May emit dry-run details, JSON command output, MP4 video files, storyboard sidecar files, or subtitles depending on selected mode and backend.]

## Skill Version(s):

1.0.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
