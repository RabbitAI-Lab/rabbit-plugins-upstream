## Description:

Alibaba's flagship Qwen reasoning model supports text and image input for complex reasoning, code engineering, and long-context analysis through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to call Qwen 3.8 Max through the dLazy hosted API for text generation, image-aware prompting, reasoning, coding, and long-context analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, parameters, and user-selected media files to the third-party dLazy cloud service for inference.

Mitigation: Do not pass private files or sensitive prompts unless upload to dLazy is intended; review the service and source links before use.

Risk: Authentication can persist a dLazy API key in the local CLI configuration.

Mitigation: Use DLAZY_API_KEY for temporary credentials when persistence is not desired, and rotate or revoke keys from the dLazy dashboard as needed.

Risk: A globally installed third-party CLI remains on the system after installation.

Mitigation: Use the pinned npx invocation for on-demand execution when a persistent global binary is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen3-8-max)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and network access to dLazy API and file endpoints.]

## Skill Version(s):

1.2.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
