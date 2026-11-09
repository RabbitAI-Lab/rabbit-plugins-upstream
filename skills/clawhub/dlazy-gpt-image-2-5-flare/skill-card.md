## Description:

Use GPT Image 2.5 Flare, the speed tier of OpenAI's GPT Image 2.5 series, for fast, cost-effective text-to-image generation and image editing, including reference images, aspect ratios up to 21:9, and quality up to max.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams use this skill to generate or edit images from text prompts and reference images, then retrieve the resulting image assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports a mismatch between the image-generation purpose and the documented `dlazy login` command; its confidence is medium and its evidence is incomplete.

Mitigation: Before installing or logging in, review the CLI's credential handling and confirm the login workflow is expected.

Risk: The skill documentation says prompts and supplied local image paths are sent to dLazy's hosted API and media storage.

Mitigation: Avoid sending sensitive prompts or images unless you are comfortable sharing them with the service.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-flare)
- [dLazy](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Image files, JSON]

**Output Format:** [Generated image assets returned as hosted URLs in a JSON response; image files can also be saved locally.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports text prompts, up to five reference images, aspect ratios through 21:9, and quality settings from low to max.]

## Skill Version(s):

1.2.28 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
