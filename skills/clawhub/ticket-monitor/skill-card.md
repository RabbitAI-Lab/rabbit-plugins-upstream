## Description:

实时监控大麦网已开售演出的余票与售罄状态，在放票、回流票、售罄等变化时通过终端/日志、Webhook（Server酱/企业微信/钉钉/通用）或 Windows 桌面弹窗告警。当用户要监控大麦演出余票、抢票提醒、售罄/回流提醒时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[widoxm](https://clawhub.ai/user/widoxm)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to monitor Damai event ticket availability, sold-out status, restocks, returned tickets, and session or price-tier changes. It supports one-time snapshots, continuous polling, logs, webhook alerts, and Windows desktop notifications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can store and send a live Damai browser session cookie, which should be treated like a password.

Mitigation: Prefer running without a cookie when possible, avoid sharing configuration files or logs, and review any webhook destination before enabling it.

Risk: Aggressive polling or use of session cookies may conflict with platform rules or trigger anti-crawling controls.

Mitigation: Use conservative polling intervals, comply with the platform's rules, and review the skill before installing or running it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/widoxm/skills/ticket-monitor)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands, configuration examples, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill's runtime can also emit terminal/log text, JSON snapshots, webhook messages, and Windows toast notifications.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
