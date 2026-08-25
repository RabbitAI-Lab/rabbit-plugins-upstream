## Description:

Image generation skill that automatically selects an appropriate dLazy CLI image model based on the prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to generate, edit, upscale, vectorize, or segment images through the dLazy CLI and hosted dLazy API. The agent selects a suitable image model, checks its parameters, and runs the corresponding dlazy command.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and user-provided media paths may be sent to dLazy services for generation.

Mitigation: Use the skill only with data appropriate for dLazy processing and review the dLazy service terms before sending sensitive inputs.

Risk: Authentication can persist a dLazy API key in the local user configuration.

Mitigation: Use per-invocation DLAZY_API_KEY when persistence is not desired, and rotate or revoke keys from the dLazy dashboard when access should change.

Risk: A global installation persists the dLazy CLI on the system.

Mitigation: Use the pinned npx command for on-demand execution when a global install is not desired.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-image-generate)
- [dLazy CLI Source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Markdown guidance with inline bash commands; dlazy CLI responses are JSON envelopes with generated media URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and network access to api.dlazy.com and files.dlazy.com.]

## Skill Version(s):

1.3.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
