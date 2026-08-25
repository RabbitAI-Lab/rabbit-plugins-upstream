## Description:

智能擦除商品图片中的人物、水印、文字及杂物，并自动补全背景，完成商品修图与素材优化。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users, ecommerce operators, and agent developers use this skill to guide an agent through removing watermarks, text, bystanders, or other unwanted elements from product images with LinkPix/qhkit image inpainting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or upgrade Node/npm tooling.

Mitigation: Prefer preinstalling and pinning qhkit in a controlled environment, and review install or upgrade commands before allowing agent execution.

Risk: The workflow uploads selected images to the qhkit/LinkPix service.

Mitigation: Confirm that submitted images are appropriate for third-party processing and avoid sending confidential or regulated content unless approved.

Risk: The workflow may ask the agent to handle a qhkit API token.

Mitigation: Provide credentials through platform secrets or QHKIT_TOKEN instead of pasting raw keys into chat, and rotate any exposed tokens.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-image-eraser)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide or execute qhkit CLI commands that return JSON with generated image URLs and credit usage.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
