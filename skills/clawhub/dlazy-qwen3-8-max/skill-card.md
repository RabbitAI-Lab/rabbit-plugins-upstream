## Description:

Uses the dLazy-hosted Qwen model to generate text and code from prompts, with optional image inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can ask an agent to generate or analyze text and code using prompts and optional images through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files are sent to dLazy's hosted service.

Mitigation: Review prompts and image paths before submission; do not send sensitive content without authorization.

Risk: The CLI can save a dLazy API key locally.

Mitigation: Protect local credentials and rotate or revoke the key in the dLazy dashboard if needed.

Risk: A global CLI installation remains on the user's system.

Mitigation: Use the pinned npx invocation instead if a persistent installation is not wanted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen3-8-max)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Code, Guidance]

**Output Format:** [Text or code returned in a JSON result]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional asynchronous requests return a task ID for later retrieval.]

## Skill Version(s):

1.2.18 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
