## Description:

Generates 4MP high-resolution raster images through the dLazy hosted Recraft V4 Pro API for print-ready assets and large-format use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate high-resolution raster images via the dLazy CLI, optionally saving generated assets locally or running jobs asynchronously.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local media are sent to dLazy-controlled cloud services for generation.

Mitigation: Avoid submitting sensitive prompts or media unless the user accepts dLazy's service handling for that content.

Risk: Authentication may store a dLazy API key in the local CLI configuration.

Mitigation: Use normal local credential hygiene and rotate or revoke the API key from the dLazy dashboard when needed.

Risk: A global CLI install persists a third-party executable on the system.

Mitigation: Use the pinned npx invocation when a non-persistent install is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, JSON, image files, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image URLs are hosted by dLazy; outputs can also be saved to a local path when requested.]

## Skill Version(s):

1.3.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
