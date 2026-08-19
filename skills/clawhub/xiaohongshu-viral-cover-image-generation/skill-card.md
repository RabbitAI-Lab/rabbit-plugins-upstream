## Description:

生成与编辑小红书笔记首图、种草封面、好物清单封面和品牌合作视觉，支持参考图、中文标题留白、批量创意方向和 AI Hive 自动下载。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and content agents use this skill to plan, generate, edit, and download Xiaohongshu/RED note cover images for product, review, tutorial, comparison, and series-account visuals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images and prompts are sent to AI Hive for generation.

Mitigation: Avoid uploading private or sensitive images unless intended, and review the provider's billing, content, and data-handling rules before use.

Risk: The skill stores or reads an AI Hive API key locally for later requests.

Mitigation: Use a dedicated API key where possible, keep the local configuration file access restricted, and rotate the key if it is exposed.

Risk: Generated cover visuals may imply claims, endorsements, pricing, or product results that were not supported by the source material.

Mitigation: Review titles, brand text, commercial disclosures, product claims, and comparison conditions before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/xiaohongshu-viral-cover-image-generation)
- [AI Hive API service endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown instructions with bash commands; generated image results are downloaded as image files unless no-download mode is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses AI Hive API credentials, can upload user-selected reference images, and downloads results to a local output directory by default.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
