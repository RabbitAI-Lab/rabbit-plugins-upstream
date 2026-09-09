## Description:

Happy Horse 1.0 is a dLazy video-generation skill that routes text-to-video, first-frame-to-video, reference-to-video, and video-editing requests to the matching hosted model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, developers, and agents use this skill to generate or edit videos through the dLazy hosted Happy Horse 1.0 model using prompts and optional image or video inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, media files, and API-key-backed requests are handled through dLazy's hosted service.

Mitigation: Install and use the skill only when sharing that data with dLazy is acceptable; avoid sensitive inputs and manage the API key separately.

Risk: A persistent global CLI install can leave a long-lived binary and local dLazy configuration on the machine.

Mitigation: Use npx or another isolated environment when avoiding a persistent global binary, and rotate or revoke dLazy API keys if access should change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-happyhorse-1-0)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [CLI JSON responses with generated media URLs, plus optional downloaded media files when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; supports async task IDs with follow-up status polling.]

## Skill Version(s):

1.3.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
