## Description:

为小红书电商与品牌合作生成和编辑商品卡图片、笔记轮播、真实使用图、卖点证明及聚光广告素材。Use this skill for 小红书电商图片、小红书商品图、笔记轮播、种草套图、品牌合作、蒲公英、聚光广告、好物分享、商品详情和UGC素材；支持参考图保真及 AI Hive 生成。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and brand marketers use this skill to generate and edit Xiaohongshu product cards, note carousel images, unboxing visuals, usage scenes, proof-oriented detail images, and Spotlight ad hypotheses with AI Hive. It helps preserve provided product, packaging, creator, and brand references while avoiding fabricated reviews, results, discounts, or claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI Hive API keys are read from command-line input, environment variables, or a local configuration file.

Mitigation: Use a scoped AI Hive key, prefer environment variables or the generated 0600 config file, and rotate the key if it is exposed.

Risk: Prompts and selected reference files are uploaded to the AI Hive service for generation.

Mitigation: Do not provide private, regulated, or unreleased product images unless upload to AI Hive is approved for that material.

Risk: Generated ecommerce images can imply product effects, user experiences, discounts, or endorsements that were not supplied.

Mitigation: Review outputs against real product evidence and platform rules, and add only approved disclosures, prices, claims, and calls to action in the formal publishing workflow.

Risk: Generated result files are downloaded from remote task URLs and saved locally.

Mitigation: Save outputs to a controlled directory and review files before reuse or publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/xiaohongshu-ecommerce-image-generation-editing)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown instructions with bash command examples, JSON task status, and downloaded local image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts prompt text, optional reference images, batch size, model parameters, output directory, and no-download mode.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
