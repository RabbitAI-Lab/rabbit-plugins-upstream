## Description:

Converts PNG and JPG images into color vector images and returns a result URL for use with logos, icons, and flat illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and developers use this skill to vectorize raster logos, icons, and flat illustrations through the dLazy CLI and retrieve a hosted result URL or save the result locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images provided as local files are uploaded to dLazy's cloud service.

Mitigation: Only submit images or file paths you are comfortable uploading to dLazy.

Risk: The external dLazy CLI runs locally and saved login stores an API key in local configuration.

Mitigation: Review the CLI before installing; on shared machines, use DLAZY_API_KEY instead of saved login or remove ~/.dlazy/config.json when no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-vectorize)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [Result URL and optional locally saved vectorized image]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI responses include a hosted result URL; asynchronous requests may return a task ID instead.]

## Skill Version(s):

1.2.21 (source: ClawHub release; artifact frontmatter lists 1.2.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
