## Description:

This skill guides agents to turn a single ecommerce product image into a short 3-5 second main-image video using an explicitly selected video generation backend.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, ecommerce operators, and listing teams use this skill to create short product-slot videos from existing product images. It helps agents choose a video backend, craft constrained image-to-video prompts, run a dry run or short test clip, and save usable video outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts may be sent to the selected cloud video provider.

Mitigation: Confirm the intended provider and credentials before use, and avoid sending product images that should not leave the local environment.

Risk: Video generation can incur cost.

Mitigation: Run dry-run mode or a short 3-second test clip before longer or batch generation.

Risk: Generated video can amplify defects in the source image or distort products and faces.

Mitigation: Inspect and repair the source image first, use subtle motion prompts, and review the generated clip before publishing.

Risk: Marketplace video requirements may vary by platform.

Mitigation: Manually check duration, aspect ratio, file size, and content rules against the target platform before release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/main-image-video)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [Video backend configuration](artifact/references/video-backends.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline bash commands and JSON examples; generated artifacts are MP4 files, optional SRT subtitles, and JSON status output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses explicit provider credentials and model selection; supports dry-run checks before cloud video generation.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
