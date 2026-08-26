## Description:

Moonshot AI thinking model with text, image, and video understanding, suited to complex analysis, coding, and writing that needs long reasoning chains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and external users use this skill to call Kimi K3 through the dLazy CLI for long-form reasoning, analysis, coding, writing, and image or video understanding tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly attached local media files are sent to dLazy hosted services for inference.

Mitigation: Use the skill only with data that is acceptable to send to dLazy, and avoid attaching sensitive local media unless the user's policy permits it.

Risk: Authentication can store a dLazy API key in local CLI configuration.

Mitigation: Use per-invocation DLAZY_API_KEY where persistence is not desired, protect the local config file, and rotate or revoke the key if the machine is shared or compromised.

Risk: A global CLI install persists a local binary on the system.

Mitigation: Use the pinned npx invocation when a temporary, non-global execution path is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kimi-k3)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON response values from the CLI, with generated content and optional async task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can accept prompts plus image or video inputs; --no-wait returns an async generateId, and --save can download returned assets.]

## Skill Version(s):

1.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
