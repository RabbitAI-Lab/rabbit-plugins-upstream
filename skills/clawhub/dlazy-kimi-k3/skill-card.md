## Description:

Helps agents use Kimi K3 for text generation, complex analysis, coding, and writing with optional image and video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can generate text, analyze complex questions, and draft code or writing with optional image and video context through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly selected media files may be sent to dLazy's cloud service.

Mitigation: Review prompts and files for sensitive content before submitting them.

Risk: Logging in stores a dLazy API key in the local CLI configuration.

Mitigation: Protect local credentials and rotate or revoke the key if it is exposed.

Risk: Running the third-party CLI requires trusting its npm package and associated service.

Mitigation: Review the package and linked source before installing when that trust boundary matters.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-kimi-k3)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code]

**Output Format:** [JSON-wrapped generated text, which may contain Markdown or code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task identifier instead of immediate generated text.]

## Skill Version(s):

1.2.17 (source: server-resolved ClawHub release; bundled CLI install specifies 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
