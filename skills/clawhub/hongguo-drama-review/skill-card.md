## Description:

根据用户提供的红果短剧名称、链接或 series_id，整理剧评样本、口碑主题、剧情争议和角色反馈，并比较多部剧的观众评价。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use this skill to review audience feedback for one to three Hongguo short dramas, organize comment evidence by theme, examine plot or character disputes, and compare audience responses across titles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks the skill suspicious because its commands use an automatically installed, changeable latest CLI version, which could expose credentials or other resources available to the runtime if the package is compromised.

Mitigation: Wait to install until the CLI version is fixed and reviewed. If using it sooner, consider which credentials and resources are available in that execution environment, and keep API keys out of chat, logs, and command text.

## Reference(s):

- [SocialDataX API key and service information](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/hongguo-drama-review)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Guidance]

**Output Format:** [Markdown report with sample scope, comment evidence, audience themes, disputes, and review suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Usually covers up to three dramas, with up to two pages and 20 main comments per drama by default; reports sample limits and does not infer platform-wide ratings or viewing outcomes.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
