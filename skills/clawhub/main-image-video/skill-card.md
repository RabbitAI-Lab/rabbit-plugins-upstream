## Description:

静态主图转主图视频。一张商品图转换为 3-5 秒可上架的主图短视频，并 guides the agent through backend selection, prompt construction, dry-run checks, and generation commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, operators, and agent-assisted creative teams use this skill to turn an existing product hero image into a short main-image video for product listings. The skill helps the agent select a video backend, require an explicit model, draft motion prompts, dry-run requests, and save generated video files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images and prompts may be sent to the configured cloud video-generation provider.

Mitigation: Use only assets the user has rights to share, avoid sensitive inputs, and explicitly choose the provider and model before generation.

Risk: Video generation can incur cost or consume credits, especially during batch runs.

Mitigation: Run the documented dry-run path first, generate a single short clip for review, and batch only after confirmation.

Risk: Generated video can distort the product or fail marketplace video requirements.

Mitigation: Keep prompts constrained to preserve product shape, color, texture, and logo placement, then manually review the output against platform duration, ratio, file-size, and content rules.

Risk: Shared tooling references unrelated tasks, including watermark removal.

Mitigation: Ignore unrelated shared tasks unless the user has clear rights and the task is directly requested.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/main-image-video)
- [Video backend configuration](references/video-backends.md)
- [Provider CLI reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands, prompt templates, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May cause configured cloud providers to generate and save short video files from user-selected product images.]

## Skill Version(s):

1.0.9 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
