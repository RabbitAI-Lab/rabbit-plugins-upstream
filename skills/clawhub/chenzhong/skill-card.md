## Description: <br>
每日晨间简报助手。每天定时生成个性化简报，提醒你今天要做的事、正在推进的项目和需要关注的方向。不是新闻摘要，是你的个人AI副驾驶晨间仪表盘。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mofeiyun1](https://clawhub.ai/user/mofeiyun1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Individuals use this skill to generate a daily morning briefing from their configured local notes, journals, work logs, ideas, and project memory. It helps surface habits, project deadlines, stalled tasks, source files used for the briefing, and suggested next steps for the day. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads user-configured local diary, conversation, work-log, idea, and project files, which may contain sensitive personal or confidential information. <br>
Mitigation: Keep configured data-source paths narrow, exclude sensitive or third-party confidential material, and review the source list included in each briefing. <br>
Risk: Briefings can become too broad or repetitive if configured sources are stale, excessive, or no longer relevant. <br>
Mitigation: Adjust or remove data-source paths, provide feedback on useful and unhelpful reminders, disable the cron schedule, or reset the briefing data pool when needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/mofeiyun1/skills/chenzhong) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, shell commands, guidance] <br>
**Output Format:** [Markdown morning brief with JSON configuration examples and optional cron snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Briefings can include configured data-source listings, habit reminders, project reminders, stalled-task reminders, and suggestions.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and manifest.yaml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
