## Description:

Helps agents generate Kling V3 Omni videos from text prompts and optional reference images or video through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short videos from prompts and reference media, and to retrieve generated results through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials may be saved locally by the dLazy CLI.

Mitigation: Use a per-invocation API key when local storage is unsuitable; rotate or revoke keys if exposed.

Risk: Prompts and supplied media are sent to dLazy's cloud service.

Mitigation: Avoid supplying private prompts or media unless you are comfortable with the service handling them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include hosted media URLs or an asynchronous task identifier.]

## Skill Version(s):

1.3.22 (source: ClawHub release; bundled skill frontmatter states 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
