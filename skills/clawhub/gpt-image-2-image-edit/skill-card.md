## Description:

使用 GPT Image 2 对现有图片进行精确、可复核的编辑，包括删除或替换物体、局部修复、改颜色材质、人物与服装调整、扩图改版和广告版本适配，并通过 AI Hive 上传原图和下载结果。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, marketers, and content teams use this skill to perform controlled image edits with GPT Image 2, including object removal or replacement, localized repair, recoloring, material changes, outpainting, product edits, portrait edits, and batch variants. The skill emphasizes change-ticket scoping and visual diff review before accepting generated results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected source images are uploaded to AI Hive for processing.

Mitigation: Use the skill only with images that are appropriate to send to AI Hive, and avoid private or regulated images unless that provider is acceptable for the use case.

Risk: Generated edits may alter people, product facts, logos, packaging text, or advertising claims in ways that are not acceptable for publication.

Mitigation: Review results against the change ticket, inspect sensitive details such as faces, hands, logos, package text, pricing, and legal copy, and require human approval before final use.

Risk: API usage can affect the user's AI Hive account and billing.

Mitigation: Use a dedicated AI Hive API key where possible and review provider account and billing implications before running generation jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/gpt-image-2-image-edit)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash command examples and downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires at least one input image for generation; supports multiple reference images, batch count, routing mode, model parameters, task lookup, and custom output directory.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
