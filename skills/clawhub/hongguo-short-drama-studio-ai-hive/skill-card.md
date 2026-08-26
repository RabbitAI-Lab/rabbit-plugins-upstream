## Description:

帮助竖屏短剧、电商和营销团队把原创或已授权剧本转化为剧本结构、人物场景板、逐镜提示词、AI-HIVE 生成任务和成片验收清单。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, production teams, marketers, and developers use this skill to plan Chinese vertical short-drama campaigns, prepare scripts and shot prompts, run AI-HIVE image or video generation commands, and check finished clips for continuity, authorization, and factual claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE generation can incur paid API charges, especially for batch jobs.

Mitigation: Review prompts, routing mode, model configuration, and price snapshots before submitting generation tasks; run a small sample before batch execution.

Risk: Local media paths provided to the scripts may be read, uploaded, and used as generation references.

Mitigation: Pass only media the user has rights to use, review absolute paths before execution, and keep original files available for audit.

Risk: Running init stores an AI-HIVE API key locally.

Mitigation: Prefer environment variables for temporary use, keep local config permissions restricted, and rotate the key if it appears in logs, screenshots, or shared files.

Risk: Generated short-drama or marketing content could include unsupported claims, unauthorized imitation, or platform-compliance assumptions.

Mitigation: Require source facts and authorized materials, avoid copying protected expression, and do not promise traffic, review approval, sales lift, or investment returns.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/hongguo-short-drama-studio-ai-hive)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with prompts, scripts, shell commands, JSON task records, checklists, and local file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit paid AI-HIVE API generation tasks after user confirmation; can upload local media and download generated outputs to configured directories.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
