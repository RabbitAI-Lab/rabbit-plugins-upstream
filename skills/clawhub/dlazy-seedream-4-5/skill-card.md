## Description:

Helps agents generate images from text prompts or reference images using Doubao Seedream 4.5 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request text-to-image or image-to-image generation and retrieve the resulting image links or saved files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any media intentionally supplied to the cloud service may leave the user's environment; generated images are hosted by dLazy.

Mitigation: Share only prompts and media suitable for upload and use the skill deliberately for dLazy image generation.

Risk: Generation calls can spend credits.

Mitigation: Check the cost estimate with the dry-run option before making a paid request.

Risk: Authentication saves a revocable API key locally, and global installation persists a third-party CLI.

Mitigation: Protect or revoke the API key as needed; use the pinned npx invocation if a global installation is unwanted.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-seedream-4-5)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation may return hosted image URLs or save a result locally; asynchronous requests require polling.]

## Skill Version(s):

1.3.28 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
