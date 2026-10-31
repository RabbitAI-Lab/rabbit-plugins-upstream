## Description:

每日自动领取积分、签到打卡的执行器。当用户要配置、新增、运行、调试每日签到、自动领积分、打卡领奖励或每日任务领取类任务，或检查今天是否已领取、积分是否到账、Cookie 是否过期时使用。支持多站点、模板变量和灵活的成功或已领判定规则，可挂定时任务每天自动执行。

This skill is ready for commercial/non-commercial use.

## Publisher:

[junci003](https://clawhub.ai/user/junci003)

### License/Terms of Use:

MIT-0

## Use Case:

面向需要维护每日签到或积分领取任务的用户，帮助他们配置站点请求、运行领取并查看结果；开发者也可用它排查 Cookie 过期、接口变化和结果判定问题。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local site configuration contains login credentials, and request previews may not fully hide secrets.

Mitigation: Keep the configuration private and remove all credentials before sharing configuration, requests, or previews.

Risk: Disabling certificate verification can expose login credentials to interception.

Mitigation: Keep certificate verification enabled and resolve certificate errors instead of bypassing them. Review each endpoint before enabling daily execution.

## Reference(s):

- [配置指南：抓包、站点配置与判定规则](references/config-guide.md)
- [排错手册](references/troubleshooting.md)
- [ClawHub release](https://clawhub.ai/junci003/skills/daily-points-claim)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Text or JSON run summaries, shell command examples, and JSON configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-site status and messages, optional points, and a dry-run request preview.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
