## Description:

Helps agents generate and edit images with Nano Banana 2 using text prompts and optional reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request new images or edit existing images through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media may be sent to dLazy's cloud service.

Mitigation: Avoid sharing sensitive prompts or files without authorization.

Risk: Login saves an API key locally, and running the skill requires an external CLI package.

Mitigation: Use DLAZY_API_KEY instead of stored credentials where appropriate, and review the pinned CLI package before installation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-banana2)
- [dLazy CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell examples and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service returns image URLs or asynchronous task IDs; images can be saved locally.]

## Skill Version(s):

1.3.25 (source: ClawHub release; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
