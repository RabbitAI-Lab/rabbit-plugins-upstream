## Description:

Uses dLazy's hosted Qwen 3.8 Max model for text generation, reasoning, code assistance, and prompts with image inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to generate text, assist with reasoning and code tasks, and work with text or image inputs through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied image paths are sent to dLazy's cloud service.

Mitigation: Avoid submitting sensitive prompts or images unless approved for external processing.

Risk: Logging in saves an API key in the local user profile.

Mitigation: Protect local credentials and rotate or revoke the key from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen3-8-max)
- [dLazy CLI repository (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Code, Guidance]

**Output Format:** [JSON response containing generated content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional asynchronous requests return a task ID.]

## Skill Version(s):

1.2.22 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
