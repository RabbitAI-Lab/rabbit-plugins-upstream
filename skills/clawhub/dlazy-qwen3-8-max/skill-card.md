## Description:

Uses dLazy's hosted Qwen 3.8 Max model to generate text from prompts and optional images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can request text for reasoning, coding, and analysis from a hosted model, with optional image input.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly provided media are sent to dLazy's hosted service.

Mitigation: Review service terms and avoid submitting sensitive prompts or files without authorization.

Risk: Authentication can store an API key locally.

Mitigation: Protect the local key and rotate or revoke it if exposed.

Risk: The English usage instructions describe a different model command and output.

Mitigation: Confirm the Qwen command and response format before following those examples.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-qwen3-8-max)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI project](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON response containing generated text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID instead of immediate output.]

## Skill Version(s):

1.2.26 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
