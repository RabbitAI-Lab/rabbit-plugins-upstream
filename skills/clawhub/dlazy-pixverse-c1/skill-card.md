## Description:

Helps agents generate PixVerse C1 videos from text prompts, images, first and last frames, or reference images through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request video generation from text or image inputs and retrieve the resulting media link.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The third-party CLI and hosted service receive prompts and may upload media files supplied for generation.

Mitigation: Review the CLI before installation and share only prompts and media appropriate for the hosted service.

Risk: Signing in can persist an API key in local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation authentication if persistent storage is undesirable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-pixverse-c1)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON result details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide a generated media URL or an asynchronous task ID; saved files are optional.]

## Skill Version(s):

1.2.32 (source: ClawHub release; artifact frontmatter lists 1.2.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
