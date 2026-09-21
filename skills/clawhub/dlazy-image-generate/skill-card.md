## Description:

Image generation skill that helps an agent select and run an appropriate dLazy CLI image model from a user prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for image generation, editing, upscaling, vectorization, and related visual asset workflows through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files may be sent to the dLazy cloud service.

Mitigation: Avoid passing private or sensitive media unless the user intends to upload it to dLazy, and review the service terms before use.

Risk: The dLazy API key may be stored in a local CLI configuration file.

Mitigation: Use operating-system account protections, rotate or revoke keys from the dLazy dashboard when needed, or pass DLAZY_API_KEY per invocation.

Risk: A global CLI installation persists a third-party executable on the system.

Mitigation: Use the pinned npx invocation when a non-persistent CLI execution path is preferred.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-image-generate)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands; dLazy CLI calls return JSON envelopes with generated media URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and network access to dLazy API and media endpoints.]

## Skill Version(s):

1.3.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
