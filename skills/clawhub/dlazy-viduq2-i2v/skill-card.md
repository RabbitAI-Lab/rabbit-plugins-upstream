## Description:

Helps an agent turn still images into short videos using Vidu Q2 through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide image-to-video generation from reference images or first and last frames, with options for duration, format, and audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are uploaded to dLazy, and generated outputs are hosted there.

Mitigation: Review media and account sensitivity before sending content to the service.

Risk: Logging in can save an API key locally, and installing the CLI uses a third-party package.

Mitigation: Consider per-invocation DLAZY_API_KEY or pinned npx usage to reduce local persistence; review the pinned package and source before installation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-i2v)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Text with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation may return a hosted result URL or an asynchronous task ID.]

## Skill Version(s):

1.3.30 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
