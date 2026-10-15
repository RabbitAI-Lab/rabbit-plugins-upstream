## Description:

Helps agents generate Kling V3 Omni videos from prompts and optional image or video references using the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short videos from text prompts and optional image or video references, with generated assets returned through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media may be sent to the dLazy cloud service, and generated assets are hosted there.

Mitigation: Confirm before uploading local files; avoid sharing sensitive prompts or media without authorization.

Risk: Generation requests may consume paid API credits.

Mitigation: Confirm before spending credits and use a cost estimate when available.

Risk: The CLI may store a dLazy API key locally.

Mitigation: Protect the local key and rotate or revoke it if exposed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON results]

**Output Format:** [Markdown guidance with shell commands and links to generated assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a task ID for asynchronous generation; generated assets are hosted by dLazy.]

## Skill Version(s):

1.3.28 (source: ClawHub release metadata; skill frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
