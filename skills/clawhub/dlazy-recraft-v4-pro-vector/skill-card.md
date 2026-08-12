## Description:

High-fidelity text-to-vector model with 4MP-tier quality for production-grade SVG assets and detailed illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted Recraft V4 Pro Vector model from an agent workflow and generate vector-style visual assets from prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts are sent to the dLazy hosted API for generation.

Mitigation: Do not submit sensitive, confidential, or restricted prompts unless dLazy is approved for that data.

Risk: The skill requires a dLazy API key that may be saved in local CLI configuration.

Mitigation: Use per-command DLAZY_API_KEY when persistent local storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro-vector)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [API Calls, Files, Shell commands]

**Output Format:** [JSON response containing generated output metadata and hosted file URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; supports asynchronous task polling through generateId.]

## Skill Version(s):

1.3.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
