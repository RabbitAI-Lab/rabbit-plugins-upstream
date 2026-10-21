## Description:

Generates images from text prompts and optional reference images using the dLazy-hosted Qwen Image 2 Pro service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers generate images for mixed-language, text-heavy designs and photorealistic visuals from prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected input files are sent to the hosted dLazy service.

Mitigation: Avoid sending sensitive prompts or media unless the service's data handling meets your requirements.

Risk: The external CLI is installed from npm and login can save an API key locally.

Mitigation: Review the linked CLI package before installing; use a per-invocation API key environment variable if local key storage is unsuitable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen-image-2-pro)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Image URLs, Image files]

**Output Format:** [JSON with hosted image URLs; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID instead of an image URL.]

## Skill Version(s):

1.3.32 (source: ClawHub release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
