## Description:

Converts a static product main image into a 3-5 second listing-ready main image video with controlled camera motion and product-preserving prompt constraints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, ecommerce operators, and agent-assisted content teams use this skill to turn one product image into a short main-image listing video, preview the planned backend request, and save generated video output for marketplace review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and brand references may be sent to the selected video or image backend.

Mitigation: Use --dry-run first, set an explicit provider and model, and avoid private or internal image URLs unless that backend is approved for the data.

Risk: Generated files are written to paths chosen at invocation time.

Mitigation: Choose an explicit save path where media output is expected and permitted.

Risk: Video generation can amplify flaws in the source product image or alter product appearance during motion.

Mitigation: Inspect and repair the input image first, run a single short test clip, then review the result before batch use.

## Reference(s):

- [Provider CLI Reference](references/provider-cli.md)
- [Video Backend Configuration](references/video-backends.md)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Files]

**Output Format:** [Markdown guidance with inline bash commands; optional JSON command output and saved MP4 files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run previews, explicit provider/model selection, and user-selected save paths.]

## Skill Version(s):

1.0.8 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
