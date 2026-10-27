## Description:

使用豆包 Seedream 5.0 Lite 极速生成图像，支持文生图与图生图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can request text-to-image or image-to-image generation with Doubao Seedream 5.0 Lite. The skill sends prompts and any selected reference images to dLazy's hosted generation service and returns generated image results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to dLazy's hosted service, and generation consumes service credits.

Mitigation: Use the skill only for explicit image-generation requests, share only content intended for the service, and use --dry-run to preview a request before submitting it.

Risk: An API key may be stored in the local dLazy CLI configuration.

Mitigation: Use DLAZY_API_KEY for per-command credentials if you prefer not to save the key locally, and rotate or revoke keys through the dLazy account controls when needed.

## Reference(s):

- [ClawHub Skill Release](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-lite)
- [dLazy](https://dlazy.com)
- [dLazy API Key Setup](https://dlazy.com/dashboard/organization/api-key)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Generated image assets with structured JSON result metadata, including image URLs and MIME types.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports text prompts and up to 10 reference images; image size and resolution are configurable.]

## Skill Version(s):

1.3.33 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
