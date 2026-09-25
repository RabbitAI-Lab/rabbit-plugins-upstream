## Description:

Fast response and generation of short videos with Google Veo 3.1 Fast.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate or extend short videos through the dLazy CLI using Google Veo 3.1 Fast. It supports text prompts, image frame inputs, video extension inputs, asynchronous polling, and saving returned media assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, generation parameters, and selected local media paths or files may be sent to dLazy hosted services.

Mitigation: Use the skill only with content suitable for dLazy cloud processing, and review the requested inputs before invoking the CLI.

Risk: Authentication stores or uses a dLazy API key on the local system.

Mitigation: Prefer the documented login or environment-variable flow, restrict local config file access, and rotate or revoke the key from the dLazy dashboard if exposed.

Risk: Global installation persists a pinned third-party CLI binary on the machine.

Mitigation: Review the pinned package/source before installation or use the documented npx invocation to avoid a persistent global install.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1-fast)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The dLazy CLI can return generated media URLs, async task identifiers, status data, and downloaded result files when --save is used.]

## Skill Version(s):

1.3.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
