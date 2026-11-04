## Description:

Text-to-image generation with Jimeng, quickly converting text to high-quality images. 使用即梦 (Jimeng) 进行文生图创作，快速将文字转化为高质量图像。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can generate images from text prompts with Jimeng, optionally supplying reference images and choosing an output size.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any supplied local reference images are sent to dLazy's hosted service for generation.

Mitigation: Send only prompts and images that are appropriate to share with the service.

Risk: Image generation may consume organization credits.

Mitigation: Review the CLI cost estimate with --dry-run before submitting a generation request.

Risk: The dLazy API key is stored in local CLI configuration or supplied through an environment variable.

Mitigation: Protect the local configuration and environment, avoid sharing the key, and rotate or revoke it if exposed.

Risk: The downloaded CLI and hosted service were not fully verified in the supplied security assessment.

Mitigation: Review the package and service terms before installation or use, and install only if you trust dLazy with your prompts and selected images.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [dLazy API key setup](https://dlazy.com/dashboard/organization/api-key)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [CLI repository listed in skill metadata (provenance unavailable)](https://github.com/dlazy-ai/cli)
- [ClawHub release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-t2i)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Generated image assets with a JSON result envelope containing output URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts, optional reference images, and image size control generation; asynchronous requests may return a task identifier before images are ready.]

## Skill Version(s):

1.3.37 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
