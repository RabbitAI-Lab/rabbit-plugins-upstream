## Description:

Selects a dLazy image model for a prompt and helps generate images through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to choose an image-generation model and generate visual assets from prompts or reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied reference media may be sent to the third-party dLazy cloud service.

Mitigation: Avoid sharing sensitive prompts or media unless approved for third-party processing.

Risk: Authentication can save an API key in local CLI configuration.

Mitigation: Protect the local configuration and rotate or revoke the key if exposed.

## Reference(s):

- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-image-generate)

## Skill Output:

**Output Type(s):** [Image links, Shell commands, Guidance]

**Output Format:** [Markdown with image links and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media may be returned as hosted URLs.]

## Skill Version(s):

1.3.26 (source: ClawHub release metadata; bundled frontmatter: 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
