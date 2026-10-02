## Description:

Generates images from text prompts with Qwen Image 2 Pro, including designs with detailed visuals and mixed Chinese and English text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images from text prompts, with optional reference images, through the dLazy-hosted Qwen Image 2 Pro service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied reference images are sent to dLazy's cloud service.

Mitigation: Use only prompts and files you are comfortable sharing with dLazy.

Risk: Authentication can save an API key in the local CLI configuration.

Mitigation: Use a per-run DLAZY_API_KEY if you prefer not to save the key locally.

Risk: The skill relies on a third-party npm CLI.

Mitigation: Review the dLazy CLI source and package before installing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen-image-2-pro)
- [dLazy CLI source (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON result with image URLs; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID to poll for the image.]

## Skill Version(s):

1.3.24 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
