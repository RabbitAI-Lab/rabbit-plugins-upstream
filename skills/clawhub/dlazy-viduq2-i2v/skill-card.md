## Description:

Convert static images into dynamic videos using the Vidu Q2 image-to-video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative operators use this skill to turn reference images or first/last frames into short Vidu Q2 videos through the dLazy hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to dLazy's hosted service for generation.

Mitigation: Use only media and prompts approved for that external service before invoking the skill.

Risk: Authentication can store a dLazy API key in a local CLI configuration file.

Mitigation: Use the environment-variable option for per-invocation credentials when persistent local storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The examples use an image flag that conflicts with the listed `--images` option.

Mitigation: Run `dlazy viduq2-i2v -h` before execution and use the flag shown by the installed CLI version.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-i2v)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON responses containing generated media URLs or asynchronous task IDs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and may upload selected local media files to dLazy-hosted endpoints for generation.]

## Skill Version(s):

1.3.20 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
