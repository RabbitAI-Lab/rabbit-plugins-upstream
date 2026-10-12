## Description:

Guides an agent to turn still images into short videos using Vidu Q2 through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide an agent in generating short videos from reference images or first and last frames, with optional audio and output settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The third-party CLI processes supplied prompts and uploads selected local media to dLazy's cloud service.

Mitigation: Review the CLI package before installation and send only media and prompts approved for this service.

Risk: The CLI can save an API key in a local configuration file.

Mitigation: Use revocable keys or supply DLAZY_API_KEY per invocation if persistent storage is not desired.

## Reference(s):

- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-i2v)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell examples and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides retrieval of hosted generation results or asynchronous task IDs.]

## Skill Version(s):

1.3.28 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
