## Description:

Image matting tool: separates foreground from background and returns transparent background URL, suitable for product image processing, character cutout, and composition. 图像抠图工具：将前景与背景分离并返回透明背景的 URL，适用于产品图片处理、人物抠图和合成。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People processing product photos, character images, or other compositions can use this skill to separate foreground subjects from image backgrounds and obtain a transparent-background result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images and request parameters are sent to dLazy for processing, and local image files are uploaded to its media storage.

Mitigation: Submit only images and information approved for processing by the external service.

Risk: The dLazy API key is saved in the local CLI configuration when using the login flow.

Mitigation: Protect access to the local account and configuration, and rotate or revoke the key from the dLazy dashboard if exposed.

Risk: Image processing may incur charges, and the external CLI was not fully audited in this review.

Mitigation: Review the CLI before installation and use its dry-run cost estimate before submitting paid requests.

## Reference(s):

- [CLI project page listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-imageseg)

## Skill Output:

**Output Type(s):** [JSON, Image URLs]

**Output Format:** [JSON containing a URL for the transparent-background image]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The result may include an asynchronous task identifier when requested; the image is hosted by dLazy.]

## Skill Version(s):

1.3.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
