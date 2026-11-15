## Description:

Generates text and code through Anthropic Claude Sonnet 5 via dLazy, with optional image and video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can generate text, code, and structured responses from prompts, with optional image or video inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanner coverage did not establish how the referenced CLI handles authentication credentials.

Mitigation: Review the pinned CLI and its authentication setup before entering an API key; use a key that can be rotated or revoked.

## Reference(s):

- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Code, JSON]

**Output Format:** [CLI JSON response envelope; generated content varies by prompt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous tasks can return a task status; results can be saved to a local path.]

## Skill Version(s):

1.2.43 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
