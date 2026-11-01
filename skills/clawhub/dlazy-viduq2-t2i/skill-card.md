## Description:

Generate high-quality images with Vidu Q2 from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People using an AI agent can create or edit images by supplying a text prompt and, optionally, reference images. They can choose an aspect ratio and resolution and receive generated image assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images are sent to dLazy's hosted service, and image generation can spend credits.

Mitigation: Submit only prompts and images you are comfortable sending to dLazy; use --dry-run to preview cost before generation.

Risk: The dLazy API key is stored in the local CLI configuration when using the login flow.

Mitigation: Protect the saved API key and rotate or revoke it from the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-t2i)
- [CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Image assets returned as URLs in a JSON response; optional local image files when saved.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports text prompts, up to 10 reference images, multiple aspect ratios and resolutions, and asynchronous task IDs.]

## Skill Version(s):

1.3.36 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
