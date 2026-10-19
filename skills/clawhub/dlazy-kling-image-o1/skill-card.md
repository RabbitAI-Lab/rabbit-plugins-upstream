## Description:

Generate images from text prompts or reference images using Kling Image O1 through dLazy's cloud service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request text-to-image generation or image-to-image editing through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images supplied to the CLI are sent to dLazy's cloud service.

Mitigation: Use the service only when you are comfortable sharing those inputs; avoid submitting sensitive images or prompts.

Risk: The CLI may store a dLazy API key in local user configuration.

Mitigation: Protect the local key and rotate or revoke it when you stop using the service.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-kling-image-o1)
- [dLazy CLI source link (skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return image URLs or an asynchronous task ID and can save generated images locally.]

## Skill Version(s):

1.3.30 (source: ClawHub release metadata; bundled skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
