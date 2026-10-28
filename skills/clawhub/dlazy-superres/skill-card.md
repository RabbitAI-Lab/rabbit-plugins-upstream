## Description:

Image super-resolution tool: enhances image clarity and details, returning enhanced URL, suitable for low-res asset restoration and upscaling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to upscale low-resolution images and retrieve enhanced image results from dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images sent for upscaling are uploaded to dLazy's hosted service.

Mitigation: Only upload images you are comfortable sharing with dLazy.

Risk: Processing uses an API key and may incur service costs.

Mitigation: Prefer device login or DLAZY_API_KEY over sharing keys in chat, and check service costs before processing.

Risk: The skill depends on an external CLI package.

Mitigation: Review and trust the CLI package before installing or running it.

## Reference(s):

- [dLazy CLI project information](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)
- [ClawHub release](https://clawhub.ai/dlazyai/skills/dlazy-superres)

## Skill Output:

**Output Type(s):** [Images, URLs, JSON]

**Output Format:** [JSON result containing enhanced image URLs; optionally saves an image file to a local path.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous task identifier when run without waiting for completion.]

## Skill Version(s):

1.3.36 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
