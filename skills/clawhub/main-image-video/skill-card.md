## Description:

Converts one static product image into a 3-5 second listing-ready main image video with controlled camera motion and material movement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, marketers, and developers use this skill to turn a product hero image into a short marketplace listing video. It supports short test runs before paid generation and can reuse brand settings for consistent batch production.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts may be sent to the selected cloud video or image provider.

Mitigation: Use only providers approved for the product data, prefer local image paths or trusted HTTPS URLs, and avoid sensitive or embargoed assets.

Risk: Video generation can incur provider costs, especially during batch runs.

Mitigation: Use dry-run mode and one short test clip before starting paid batch generation.

Risk: Video models may amplify source-image defects or alter product details during motion.

Mitigation: Inspect the source image first, use subtle camera-motion prompts, review each generated clip, and manually check marketplace video requirements.

Risk: The scripts write generated video, subtitle, and assembly files to local output paths.

Mitigation: Use explicit output directories and review generated files before publishing or reusing them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/main-image-video)
- [Provider CLI Reference](references/provider-cli.md)
- [Video Backend Configuration](references/video-backends.md)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands; scripts can emit JSON status and local MP4/SRT/video assembly files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses explicit video model configuration, supports dry-run checks, and writes generated outputs to caller-specified local paths.]

## Skill Version(s):

1.0.2 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
