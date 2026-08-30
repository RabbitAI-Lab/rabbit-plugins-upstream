## Description:

GEO 多平台内容生成器｜AI-HIVE helps content teams turn verified facts, platform requirements, and usage constraints into Chinese GEO articles, FAQ, Zhihu-style answers, social posts, image prompts, and AI-HIVE generation commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External content, ecommerce, advertising, and marketing teams use this skill to create platform-adapted Chinese GEO content for Baidu, WeChat, Zhihu, Xiaohongshu, and websites from a shared fact base, with optional AI-HIVE image or video generation after human confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE initialization can store an API key in a local plaintext config file protected by file permissions.

Mitigation: Prefer environment variables for temporary use, keep the config file restricted to the local user, and do not place API keys in prompts, logs, screenshots, or committed files.

Risk: Image and video generation tasks, especially batch jobs, may incur cost.

Mitigation: Review prompts, model choice, routing mode, batch size, and price snapshot before submission, and run a small sample before larger batches.

Risk: Uploaded reference media may contain sensitive or unlicensed material.

Mitigation: Confirm rights and privacy suitability before upload; if rights are unclear, use only abstract structure guidance and new creative assets.

Risk: Marketing content can overstate performance, product claims, platform approval, search ranking, or return on investment.

Mitigation: Tie important claims to verifiable sources, mark uncertainty and dates, and require human review before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/geo-content-writer-ai-hive)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown with structured sections, inline shell commands, JSON records, and optional generated media file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, routing choices, price snapshots, local output paths, and generated blueprint JSON when the helper scripts are run.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
