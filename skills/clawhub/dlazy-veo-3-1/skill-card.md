## Description:

Guides agents to generate cinematic videos from text prompts, images, or existing video with Google Veo 3.1 through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to direct an agent to generate or extend videos from prompts and selected media using the dLazy-hosted Veo 3.1 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy, and generated files are hosted there.

Mitigation: Use only media and prompts appropriate for sharing with the service; review its terms before uploading sensitive content.

Risk: Login can store an API key locally, and installing the CLI executes third-party software.

Mitigation: Protect or rotate the API key, and review the pinned CLI package before installation; use npx if a persistent global installation is unwanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1)
- [dLazy CLI source (listed in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and links to generated assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service can return hosted result URLs or an asynchronous task ID.]

## Skill Version(s):

1.3.30 (source: ClawHub release metadata; skill frontmatter states 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
