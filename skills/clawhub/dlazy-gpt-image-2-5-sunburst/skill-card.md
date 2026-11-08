## Description:

Generates and edits images with GPT Image 2.5 Sunburst, with reference image support and controls for aspect ratio and output quality.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams can generate new images or edit supplied images when fine detail, composition, or in-image text matters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local images are sent to dLazy's hosted service, and generated images are hosted there.

Mitigation: Send only prompts and media you intend to upload; avoid including sensitive content.

Risk: The CLI saves an API key locally, and image generation consumes paid credits.

Mitigation: Protect the local key and rotate or revoke it if exposed; check credit use before running generation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-sunburst)
- [CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Image files, JSON]

**Output Format:** [Generated image assets with JSON result metadata and URLs]

**Output Parameters:** [Prompt, optional reference images (up to five), aspect ratio, and quality]

**Other Properties Related to Output:** [Supports aspect ratios up to 21:9 and quality up to max; generation uses paid credits.]

## Skill Version(s):

1.2.27 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
