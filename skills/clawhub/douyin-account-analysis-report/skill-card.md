## Description:

帮助代理基于用户提供的抖音主页链接、分享文案或 sec_user_id 获取公开账号资料和近期作品样本，并输出账号诊断、内容表现复盘和 30 天测试计划。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External operators, creators, and analysts use this skill to diagnose a Douyin account from a user-provided profile link, share text, or sec_user_id. It fetches public profile and recent-post data through SocialDataX and turns visible metrics into an evidence-based account analysis report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user-provided Douyin account identifiers to SocialDataX and requires access to a SocialDataX API key.

Mitigation: Use only when that data sharing is acceptable, configure the API key through the documented SOCIALDATAX_API_KEY environment variable, and avoid pasting unrelated secrets into prompts or command arguments.

Risk: The analysis is based on sampled public profile and recent-post data, not complete platform coverage or proof of Douyin recommendation behavior.

Mitigation: Present conclusions as evidence-based directional findings, call out missing fields, and avoid claims about true play volume, account weight, recommendation status, or guaranteed growth.

## Reference(s):

- [SocialDataX API key and product page](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/douyin-account-analysis-report)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown account diagnosis report with optional shell command examples and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses public Douyin profile and recent post data returned for the provided account; missing fields should be called out rather than invented.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
