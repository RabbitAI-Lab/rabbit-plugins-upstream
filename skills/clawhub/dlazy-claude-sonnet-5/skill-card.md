## Description:

Uses the dLazy CLI to send prompts and optional image or video inputs to dLazy's hosted Claude Sonnet 5 service and return generated results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate text, code, and other model responses, including responses based on image or video inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied image or video files are sent to dLazy's hosted API; local media files may be uploaded to its media storage.

Mitigation: Avoid sending sensitive prompts or files unless the service is approved for that data.

Risk: The partial scan did not inspect the external CLI package's internal behavior and noted login, API-key, and package-invocation instructions.

Mitigation: Review the package source and confirm its purpose before installing or invoking it; authenticate only when expected.

## Reference(s):

- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Code, JSON, Guidance]

**Output Format:** [CLI response envelope containing prompt-dependent generated content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID; generated content depends on the prompt.]

## Skill Version(s):

1.2.46 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
