## Description:

Helps agents turn static images into short videos with Vidu Q2 through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide image-to-video generation from reference images or first and last frames, with optional audio and output settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the skill's external dLazy CLI adds a third-party dependency.

Mitigation: Review the pinned CLI package and its listed source before installing.

Risk: Signing in stores an API key in the local CLI configuration.

Mitigation: Use a per-invocation environment variable instead when persistent key storage is unsuitable.

Risk: Media files supplied for generation are uploaded to dLazy's cloud service.

Mitigation: Submit only media that is appropriate to share with that service.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns JSON containing a generated asset URL or an asynchronous task ID.]

## Skill Version(s):

1.3.26 (source: server-resolved ClawHub release; supplied skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
