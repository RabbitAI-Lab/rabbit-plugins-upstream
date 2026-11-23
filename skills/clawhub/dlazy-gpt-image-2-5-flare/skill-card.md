## Description:

GPT Image 2.5 Flare, the speed tier of OpenAI's GPT Image 2.5 series, for text-to-image and image editing. Fast and cost-effective for high-volume everyday generation; supports reference images, aspect ratios up to 21:9 and quality up to max.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams can use the skill to generate images from text prompts or edit reference images with GPT Image 2.5 Flare through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is partial and does not establish how the authentication operation connects to image features.

Mitigation: Review the dLazy CLI authentication flow before use, and keep API credentials private and revocable.

Risk: Local reference images supplied to the skill are uploaded to dLazy's hosted media service.

Mitigation: Only submit images that are appropriate to process through that service.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-flare)
- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, API Calls]

**Output Format:** [JSON result containing image URLs and metadata; optionally saved image files]

**Output Parameters:** [Text prompt, up to five reference images, aspect ratio, and image quality]

**Other Properties Related to Output:** [Image results are hosted by dLazy; asynchronous runs can return a task ID and status.]

## Skill Version(s):

1.2.33 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
