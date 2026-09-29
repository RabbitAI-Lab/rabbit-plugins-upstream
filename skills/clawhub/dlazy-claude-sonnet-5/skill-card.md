## Description:

Connects agents to dLazy's hosted Claude Sonnet 5 text generation for writing, reasoning, and code tasks, with optional image and video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use this skill to request generated text, explanations, and code through dLazy's hosted model service, optionally providing images or videos as context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts sent to dLazy's hosted service may contain sensitive information.

Mitigation: Remove confidential information before submitting prompts and use the service only when its data handling is acceptable.

Risk: Providing local media paths may upload private files to dLazy.

Mitigation: Review each image or video before providing its path; do not submit private files unless upload is intended.

Risk: The CLI may store an API key locally, and installation runs a third-party package.

Mitigation: Protect the local key, review the pinned package before installing, and use the on-demand install option if a persistent binary is undesirable.

## Reference(s):

- [dLazy CLI source listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [Generated text or code returned in JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID instead of an immediate result.]

## Skill Version(s):

1.2.24 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
