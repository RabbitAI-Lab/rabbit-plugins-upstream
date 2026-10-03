## Description:

Selects a dLazy audio model to generate speech, music, or sound effects from a user's prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to choose and run dLazy audio generation for speech, music, and sound effects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any media supplied to the CLI are sent to hosted services.

Mitigation: Review sensitive content before submitting prompts or files to dLazy.

Risk: Authentication can save an API key locally.

Mitigation: Protect the local key and rotate or revoke it if exposed.

Risk: The skill invokes a third-party CLI package.

Mitigation: Confirm you trust the pinned dLazy CLI and service before installing; use npx for one-off use if a global install is unwanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-audio-generate)
- [dLazy CLI homepage listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and generated audio links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns a JSON response with hosted output URLs.]

## Skill Version(s):

1.3.25 (source: ClawHub release; bundled skill frontmatter says 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
