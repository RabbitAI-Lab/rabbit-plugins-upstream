## Description:

生成与编辑抖音短视频封面、抖音电商商品卡封面和巨量千川素材首图；支持文字生成、商品或人物参考图、批量封面方向和 AI Hive 自动任务下载。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, ecommerce operators, and marketing teams use this skill to turn a Douyin video topic, product selling point, or existing reference image into vertical cover-generation prompts and AI Hive image-generation commands. It emphasizes readable thumbnail composition, product fidelity, Chinese title review, and A/B cover directions for organic posts, product cards, ad testing, and account series covers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys may be exposed if pasted into shared commands, logs, or committed config files.

Mitigation: Prefer AI_HIVE_API_KEY or a private local config file, keep file permissions restricted, and avoid committing credentials.

Risk: Reference images and prompts are sent to AI Hive for generation.

Mitigation: Avoid confidential images, proprietary prompts, unreleased products, or private customer data unless approved for that service.

Risk: Generated covers can contain inaccurate Chinese text, altered product details, or unsupported marketing claims.

Mitigation: Manually review titles, product appearance, prices, claims, certifications, and platform marks before publishing.

Risk: Retrying a timed-out generation may duplicate billable work.

Mitigation: Keep the task ID and query task status before submitting another generation request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/douyin-viral-cover-image-generation)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key portal](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with bash command examples, configuration notes, and generated image files downloaded by the helper script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses AI_HIVE_API_KEY or a local AI Hive config file; generated assets should be reviewed before public use.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
