## Description:

Helps an agent turn still images into short videos using Vidu Q2 through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide image-to-video generation with Vidu Q2, providing images and a prompt through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and provided media may be sent to dLazy's hosted service.

Mitigation: Review content before submission and avoid sending sensitive media or prompts without authorization.

Risk: Generation may use account credits.

Mitigation: Check the cost estimate with the dry-run option before generating.

Risk: The CLI may save an API key in local configuration.

Mitigation: Protect local configuration or provide the key per invocation instead.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-i2v)
- [dLazy CLI source and usage reference](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI may return JSON with generated media URLs or an asynchronous task ID; a save option downloads the result.]

## Skill Version(s):

1.3.22 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
