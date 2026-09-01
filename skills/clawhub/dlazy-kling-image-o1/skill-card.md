## Description:

Generate exquisite images with Kling o1 model, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate or edit images through the dLazy Kling Image O1 CLI workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, generation parameters, and referenced local media can be sent to dLazy's hosted service.

Mitigation: Avoid sending sensitive prompts or media unless the user is comfortable with dLazy handling that data.

Risk: The dLazy CLI can save an API key in the local user configuration.

Mitigation: Use per-invocation credentials or rotate and revoke organization API keys when tighter control is required.

Risk: Installing the global CLI persists a binary on the system.

Mitigation: Use the pinned npx invocation when a non-persistent execution path is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-image-o1)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The generated image result is returned by the dLazy CLI as JSON containing hosted image output URLs; asynchronous mode can return a generation task identifier.]

## Skill Version(s):

1.3.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
