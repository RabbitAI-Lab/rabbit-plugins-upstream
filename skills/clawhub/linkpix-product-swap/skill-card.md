## Description:

一键替换图片中的商品主体，自动保留场景、构图及光影效果，大幅提升商品素材复用效率。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce operators use this skill to replace a product subject in one or more scene images while preserving the scene, composition, and lighting. It guides an agent through qhkit setup, option lookup, estimation, confirmation, generation, and delivery for LinkPix product replacement workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may prompt users to provide an API key in chat and persist the token for CLI use.

Mitigation: Prefer QHKIT_TOKEN or a secure local secret store, avoid pasting raw keys into chat, and rotate any key that was exposed.

Risk: The workflow can install qhkit and Node dependencies on the user's machine.

Mitigation: Review installation commands before execution, prefer the official npm registry, and preserve the documented checksum verification step for Node downloads.

Risk: The workflow uploads product and scene images to the provider and may consume service credits.

Mitigation: Confirm the exact files, model, output count, and estimate before generation, and use only images the user is allowed to upload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-product-swap)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [iQinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Markdown]

**Output Format:** [Markdown with inline bash commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce external image-generation task URLs after user confirmation and qhkit execution]

## Skill Version(s):

0.1.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
