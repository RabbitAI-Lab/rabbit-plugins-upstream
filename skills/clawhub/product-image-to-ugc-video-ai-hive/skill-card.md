## Description:

将商品图转UGC带货视频需求转化为可审查的内容方案、UGC脚本、生成提示词、AI-HIVE图片/视频任务和交付验收清单。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants, cross-border sellers, and marketing operators use this skill to turn authorized product images and verified selling points into UGC-style commerce video plans, scripts, prompts, AI-HIVE generation commands, and acceptance checks for ecommerce and social platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE generation calls may upload media and submit billable image or video jobs.

Mitigation: Use authorized product media, review prompts, model configuration, price snapshots, and routing before submission, and run small samples before batch jobs.

Risk: The init flow can store an AI-HIVE API key locally in ~/.ai-hive/config.json.

Mitigation: Keep keys out of logs, screenshots, and committed files; prefer environment variables when appropriate and maintain restrictive local file permissions.

Risk: Marketing outputs can become misleading if product facts, claims, endorsements, or platform constraints are assumed.

Mitigation: Require verified selling points and authorized assets, mark unknown facts for review, and do not present generated content as real testimony or official brand endorsement.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/product-image-to-ugc-video-ai-hive)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with Chinese production briefs, bash commands, prompts, JSON task records, and file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AI-HIVE routing mode, model and pricing snapshot, taskId, task status, download locations, and acceptance checklist.]

## Skill Version(s):

1.0.0 (source: server release metadata, created 2026-08-25)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
