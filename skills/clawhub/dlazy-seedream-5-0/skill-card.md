## Description:

Generates 2K, 3K, or 4K images from prompts and optional reference images for posters, key visuals, and large-format print.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, designers, and developers use this skill to generate high-resolution artwork from text prompts and reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a pinned third-party npm CLI and a hosted image-generation service.

Mitigation: Review the CLI source and service terms before installing or sending prompts.

Risk: The CLI can store a dLazy API key locally.

Mitigation: Use DLAZY_API_KEY for per-run access when preferred, and rotate or revoke the key through the dLazy dashboard if needed.

Risk: Local reference files passed to the CLI are uploaded to dLazy.

Mitigation: Pass only files approved for upload to the hosted service.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0)
- [dLazy CLI source (linked in release metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, JSON, Shell commands]

**Output Format:** [JSON response with image URLs; optional downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports 2K, 3K, and 4K resolutions, aspect-ratio selection, and up to 10 reference images.]

## Skill Version(s):

1.2.18 (source: ClawHub release; skill files specify 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
