## Description:

Generates visually distinct variants of existing e-commerce listing images while keeping the product unchanged, with prompt-based similarity control for multi-store publishing workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators and agents use this skill to transform one or more product listing images into new image variants for multi-platform or multi-store publishing while preserving the depicted product. It supports single-image and batch image-fission workflows and returns the generated image files with an original-to-result mapping.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts are sent to LinkFox services, and local images may be uploaded to publicly accessible HTTPS URLs.

Mitigation: Use only images that are approved for external processing and public upload; do not submit confidential, private, or embargoed product materials.

Risk: The workflow handles LinkFox account credentials, API keys, and billing or payment recovery flows.

Mitigation: Configure credentials through trusted first-party account flows, keep API keys out of shared logs or prompts, and require explicit user confirmation before purchases or payment actions.

Risk: The skill is intended for reducing image similarity in marketplace publishing workflows, which may conflict with marketplace rules.

Mitigation: Review target marketplace policies before use and do not use generated variants to bypass platform enforcement or disclosure requirements.

Risk: The similarity threshold is a prompt-level instruction rather than an independently verified measurement.

Mitigation: Manually review generated images and run any required similarity, policy, or content checks before publishing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-aigc-imagegen-image-fission)
- [图片裂变 - 业务流程详述](artifact/references/workflow.md)
- [图片裂变 - 数据字段汇总](artifact/references/data-fields.md)
- [AI 生图 API 参考](artifact/skills/linkfox-aigc-imagegen/references/api.md)
- [解决认证和积分问题](artifact/skills/linkfox-aigc-imagegen/references/onboarding.md)
- [文件上传底层说明](artifact/skills/linkfox-file-upload/references/api.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, API Calls, Guidance]

**Output Format:** [Markdown table with generated image file paths and failed-item notes; supporting scripts may emit JSON and saved file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are saved as local media files; local input images may be uploaded to public HTTPS URLs before processing.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
