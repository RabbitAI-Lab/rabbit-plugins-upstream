## Description:

Selects a dLazy audio model to generate speech, music, or sound effects from a user's request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to select and run a dLazy model for text-to-speech, dialogue, music, or sound effects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media supplied to the CLI may be uploaded to dLazy's hosted service.

Mitigation: Use the service only when sharing the supplied prompts and media with dLazy is acceptable.

Risk: Authentication can save an API key on the local device.

Mitigation: Use a per-invocation environment variable when local key storage is inappropriate.

## Reference(s):

- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned through hosted output URLs.]

## Skill Version(s):

1.3.28 (source: ClawHub release evidence; bundled skill frontmatter says 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
