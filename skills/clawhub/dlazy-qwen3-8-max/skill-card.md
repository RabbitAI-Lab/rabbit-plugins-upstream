## Description:

Use the dLazy CLI to submit text and image prompts for Qwen 3.8 Max and return generated results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can send prompts, optionally with images, to dLazy's hosted Qwen 3.8 Max service and receive generated results through the CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any supplied local image files are sent to dLazy hosted services, and the CLI uses an API key whose handling is outside this skill's verified evidence.

Mitigation: Send only content approved for external processing, review dLazy's service terms and CLI credential handling before use, and rotate or revoke the API key if needed.

Risk: The security scan was partial and did not confirm the claimed model functionality or resolve several references.

Mitigation: Review the release and CLI behavior before relying on generated results, especially for consequential tasks.

## Reference(s):

- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [CLI response in JSON with generated results; optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task status responses and optional asset saving.]

## Skill Version(s):

1.2.39 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
