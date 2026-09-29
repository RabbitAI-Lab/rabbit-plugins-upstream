## Description:

Helps agents generate images from text prompts using Qwen Image 2 Pro through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request images from text prompts, optionally using reference images, and retrieve generated image links or saved files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied local media are sent to a third-party hosted service, and generated images are hosted remotely.

Mitigation: Avoid sensitive prompts and files unless approved for upload; review the hosted service's terms and data handling.

Risk: The third-party CLI may store an API key locally after login.

Mitigation: Review the pinned CLI package before installing and use DLAZY_API_KEY per invocation if local key storage is unwanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen-image-2-pro)
- [dLazy CLI repository (listed in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, JSON, Image links]

**Output Format:** [CLI JSON response with generated image URLs; agent-facing text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are hosted remotely; the CLI can optionally save them to a local path.]

## Skill Version(s):

1.3.22 (source: ClawHub release; supplied skill frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
