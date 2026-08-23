## Description:

用 Seedance 2.5 和 AI Hive 将真实商品图、产品主档和可选动作参考转换为可剪辑的产品宣传片镜头包。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce teams, and developers use this skill to prepare product-video shot commands, preview prompts, submit approved product media to AI Hive, and retrieve generated Seedance 2.5 video shots for product launches, marketplace listings, social commerce, and brand films.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Non-preview generation uploads product images and any motion-reference video to AI Hive or its HTTPS upload destination.

Mitigation: Use preview mode first, and only submit media that is approved for upload to that service.

Risk: Generation uses an AI Hive API key and may create billable tasks.

Mitigation: Keep the API key private, use environment or local config storage carefully, and review prompt previews before submitting generation jobs.

Risk: Generated video can alter product details or imply unsupported claims if prompts are not constrained and outputs are not reviewed.

Mitigation: Use product fact sources, continuity locks, and final frame-by-frame review before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedance-2-5-product-video)
- [AI Hive OpenAPI endpoint](https://ai-hive.iclip.cn/api/openapi/v1)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with bash command examples, JSON preview output, configuration snippets, and downloaded MP4 video files when generation is executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preview mode prints the selected model, prompt, product sources, motion reference, and params without uploading media or billing; non-preview mode may upload user-provided images or video and download completed MP4 outputs.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
