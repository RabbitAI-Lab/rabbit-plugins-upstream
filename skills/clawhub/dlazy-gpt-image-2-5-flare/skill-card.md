## Description:

Generates and edits images from prompts and optional reference images through the dLazy-hosted GPT Image 2.5 Flare service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate or edit images from text prompts and reference images, including everyday high-volume image work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied image files may be sent to dLazy, and generated images are hosted by dLazy.

Mitigation: Only provide content you are comfortable sharing with the service; review its terms before uploading sensitive material.

Risk: Login may persist an API key locally, and installing the CLI requires trusting the dLazy package.

Mitigation: Review the pinned CLI before installation and use per-invocation DLAZY_API_KEY or npx if less local persistence is preferred.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-flare)
- [dLazy CLI source (linked by skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON results]

**Output Format:** [JSON with hosted image URLs; optional downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports reference images, aspect-ratio and quality settings, and asynchronous jobs.]

## Skill Version(s):

1.2.14 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
