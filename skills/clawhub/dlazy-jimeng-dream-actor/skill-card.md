## Description:

Helps turn a static character image into an action video using Jimeng Dream Actor through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate an action video from a character image and a text prompt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media may be sent to dLazy's cloud service.

Mitigation: Only submit media you are authorized to share; review sensitive content before using the service.

Risk: The external CLI requires an API key and login can save it locally.

Mitigation: Review the CLI package before installation; use a per-invocation API key when local key storage is undesirable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-dream-actor)
- [dLazy CLI documentation and source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown guidance and shell commands; the CLI returns JSON with generated media links or an asynchronous task ID]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media can be saved locally with the CLI.]

## Skill Version(s):

1.3.32 (source: ClawHub release evidence; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
