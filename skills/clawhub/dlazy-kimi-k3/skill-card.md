## Description:

Uses a Moonshot AI reasoning model to help with complex analysis, coding, and writing using text, images, or video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users use this skill for complex analysis, coding, and writing with optional image or video inputs through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected images or videos are sent to the dLazy service.

Mitigation: Confirm that the content can be shared with dLazy before sending prompts or files.

Risk: Logging in can store an API key on the local machine.

Mitigation: Use the DLAZY_API_KEY environment variable if persistent local key storage is undesirable.

Risk: Using the skill installs or invokes a third-party CLI package.

Mitigation: Confirm that you trust the dLazy package and service before use.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-kimi-k3)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Code, Guidance]

**Output Format:** [Text in a structured JSON response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task identifier instead of a completed answer.]

## Skill Version(s):

1.2.19 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
