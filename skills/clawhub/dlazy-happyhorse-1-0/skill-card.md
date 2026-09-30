## Description:

Helps agents generate or edit videos from text, first frames, reference images, or existing videos through dLazy's Happy Horse 1.0 service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request video generation from text, a first frame, or reference images, and to edit an existing video through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-provided media are sent to dLazy's hosted service.

Mitigation: Confirm you trust dLazy and avoid submitting sensitive prompts or media without authorization.

Risk: The dLazy CLI stores an API key locally for authentication.

Mitigation: Protect the key and rotate or revoke it from the dLazy dashboard if needed.

Risk: Installing the third-party CLI runs external software.

Mitigation: Review the CLI before installation and use the pinned npx command if a persistent global install is unnecessary.

## Reference(s):

- [dLazy CLI source code](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with CLI commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return hosted result URLs or asynchronous task IDs.]

## Skill Version(s):

1.3.23 (source: ClawHub release metadata; bundled skill frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
