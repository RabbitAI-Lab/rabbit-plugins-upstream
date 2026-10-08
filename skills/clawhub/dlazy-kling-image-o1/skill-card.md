## Description:

Guides agents to generate or edit images with Kling Image O1 through dLazy, using text prompts and optional reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request text-to-image generation or image edits using reference images, then retrieve hosted image results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and supplied local images may be sent to dLazy's hosted service, and generated images are hosted there.

Mitigation: Avoid sending sensitive content unless the user accepts the hosted-service data flow.

Risk: Login stores an API key in local CLI configuration.

Mitigation: Use a per-run environment variable when local key storage is unsuitable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-kling-image-o1)
- [dLazy CLI source (skill metadata; release provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Image links]

**Output Format:** [Markdown guidance and commands; JSON responses contain hosted image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Images may be downloaded to a local path; asynchronous requests return a task ID for polling.]

## Skill Version(s):

1.3.25 (source: ClawHub release; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
