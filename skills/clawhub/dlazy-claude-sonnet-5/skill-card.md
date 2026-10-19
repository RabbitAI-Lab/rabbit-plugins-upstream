## Description:

Enables agents to generate text and code with Claude Sonnet 5 using prompts and optional image or video inputs through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents use this skill to request generated prose, reasoning, or code from a hosted model, optionally supplying images or videos for context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied images or videos are sent to dLazy's hosted service.

Mitigation: Avoid submitting confidential content unless its transfer to dLazy is approved.

Risk: Authentication can store a dLazy API key on the local device.

Mitigation: Protect the local account and rotate or revoke the key if it may be exposed.

Risk: The skill relies on a third-party CLI for hosted generation.

Mitigation: Review the CLI before installation; use its on-demand option if a global install is unwanted.

## Reference(s):

- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [Generated response returned in a JSON result envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task identifier before the generated response is ready.]

## Skill Version(s):

1.2.33 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
