## Description:

基于用户提供的抖音主页链接、分享文案或 sec_user_id，整理账号资料和近 30 天作品表现，并生成可执行的账号分析报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

抖音创作者及账号运营人员可使用主页链接、分享文本或 sec_user_id 查看账号资料和近期作品表现，定位内容问题并制定可执行的优化建议与 30 天测试计划。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted account links, identifiers, or share text are sent to SocialDataX, and API calls may consume paid credits.

Mitigation: Provide only the necessary public account reference, review the provider's terms, and confirm expected credit use before analysis.

Risk: Installing or running the third-party CLI carries ordinary software supply-chain risk, especially when using an unpinned latest version.

Mitigation: Protect the SOCIALDATAX_API_KEY and prefer a reviewed, pinned CLI version over @latest.

## Reference(s):

- [SocialDataX service and API key information](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/douyin-account-analysis-report)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Guidance]

**Output Format:** [Markdown account analysis report with account details, recent content performance, findings, recommendations, and a 30-day test plan]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses public account references and available metrics; missing fields should be identified rather than inferred or fabricated.]

## Skill Version(s):

0.1.3

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
