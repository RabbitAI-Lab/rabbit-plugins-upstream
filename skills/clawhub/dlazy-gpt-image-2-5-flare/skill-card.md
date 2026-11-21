## Description:

GPT Image 2.5 Flare, the speed tier of OpenAI's GPT Image 2.5 series, for text-to-image and image editing. Fast and cost-effective for high-volume everyday generation; supports reference images, aspect ratios up to 21:9 and quality up to max.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and content creators use this skill to generate images from text prompts or edit images with GPT Image 2.5 Flare through dLazy's hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports a benign verdict with medium confidence and partial scan coverage; one scanner noted an unexplained login step, and the results do not establish credential theft.

Mitigation: Before installing or entering credentials, review the CLI authentication flow and dLazy service details.

Risk: Prompts and local reference files are sent to dLazy's hosted API and media storage for generation.

Mitigation: Avoid sending sensitive prompts or files unless you are comfortable with dLazy handling them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-flare)
- [CLI repository listed by the skill](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Images, JSON, Shell commands]

**Output Format:** [Generated image files or URLs with a JSON CLI response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports optional reference images (up to 5), aspect ratio and quality settings, asynchronous task IDs, and saving results to a local path.]

## Skill Version(s):

1.2.32 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
