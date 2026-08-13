## Description:

A structured workflow skill dedicated to social-media carousel design using a confirmation-first, cover-first flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to plan and generate social-media carousel image sets through a single-confirmation, cover-first workflow using the dLazy CLI and hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media paths used for generation may be sent to dLazy's hosted service.

Mitigation: Use the skill only when that hosted-service workflow is acceptable, and avoid submitting sensitive prompts or media.

Risk: The login flow can store a dLazy API key in local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for per-session credentials when persistent local storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-social-carousel)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown workflow status, confirmation tables, prompt drafts, synchronous shell commands, and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; uses a staged workflow with user confirmation before each generation step.]

## Skill Version(s):

1.3.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
