## Description:

AI大模型专家｜电商品牌 GEO 内容优化 helps brand, e-commerce, content, short-drama, marketing, and AI search operations teams turn GEO and product AI search goals into actionable plans, structured evidence fields, generation tasks, and AI-HIVE image or video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External brand, e-commerce, content, and short-drama teams use this skill to plan GEO-oriented content structures, evidence-backed answer maps, project blueprints, and media generation workflows. Developers and operators can also use the included scripts to create JSON briefs, submit AI-HIVE image or video jobs, upload media, poll task status, and download generated assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and uploaded media are sent to AI-HIVE during image, video, chat, upload, and task workflows.

Mitigation: Use the skill only for content that may be processed by AI-HIVE, avoid submitting sensitive or unlicensed material, and confirm upload rights before running media commands.

Risk: The scripts can store an AI-HIVE API key in ~/.ai-hive/config.json for later local use.

Mitigation: Use a revocable API key, keep the config file local, rotate or revoke the key when access is no longer needed, and remove ~/.ai-hive/config.json to clear the saved credential.

Risk: Generated shell commands may start billable image or video tasks and may download generated files.

Mitigation: Review commands, model choices, pricing snapshots, output directories, and --no-download settings before execution.

Risk: GEO and AI search outputs may be mistaken for guaranteed indexing, ranking, or citation outcomes.

Mitigation: Treat generated plans as content operations guidance, keep source evidence and update times visible, and re-test visibility across target models periodically.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/ai-model-expert-drama-ecommerce-brand-geo)
- [AI-HIVE Homepage](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API Base](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local JSON blueprints and download generated media when users run the included scripts with AI-HIVE credentials.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
