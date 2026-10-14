## Description:

Turns a product image into a short, motion-focused video for an ecommerce listing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers and creative teams use this skill to turn a product photo into a short listing video with controlled camera and material motion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts are sent to the configured generation provider.

Mitigation: Obtain approval for external processing and avoid internal-only URLs or sensitive customer imagery.

Risk: Generation may use paid provider credits and require API credentials.

Mitigation: Review a dry run, choose the intended video model and provider explicitly, and limit exposure of API keys.

Risk: Generated motion can distort products or miss marketplace video requirements.

Mitigation: Inspect a single test clip before batching and check the final video against the target marketplace's specifications.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/main-image-video)
- [Video backend configuration](references/video-backends.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy CLI documentation](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline bash commands and video prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs can save a short MP4 clip; duration and model support depend on the configured provider.]

## Skill Version(s):

1.0.17 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
