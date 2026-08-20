## Description:

Daily Briefing generates daily or weekly operations task lists from sales, order, service-health, content, risk-alert, and account-cookie status, then formats them for administrator notification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Operations administrators use this skill to collect daily or weekly business, delivery, infrastructure, content, risk, and account-status tasks into a prioritized briefing for QQBot or stdout delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can surface sensitive sales, order, account-cookie, service-health, and risk-alert information.

Mitigation: Enable it only for administrators who are authorized to view those operational summaries.

Risk: The skill requests broad access and secrets that are not fully explained by its documentation.

Mitigation: Remove unexplained secrets such as SILICONFLOW_API_KEY and grant memory_search only when a concrete need is documented.

Risk: Briefing notifications and local briefing files may contain business-sensitive data.

Mitigation: Verify where QQBot notifications and local briefing files will be stored before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/daily-briefing)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Plain text or JSON briefing with prioritized task lists and notification status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write local briefing JSON files and send administrator notifications when configured.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
