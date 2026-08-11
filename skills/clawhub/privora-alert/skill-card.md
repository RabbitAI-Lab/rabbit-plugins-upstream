## Description:

Privora 实时告警 helps an agent configure one threshold rule for a subscribed asset field and send Feishu, WeChat, or generic webhook notifications when the field crosses the configured condition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guangfuwu](https://clawhub.ai/user/guangfuwu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to set up metric or price threshold alerts for already-visible data assets, verify webhook delivery, and arm the persisted alert rule. It is intended for one rule and one webhook-based notification workflow at a time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled scripts can list and execute arbitrary agent skills visible to the token, beyond the documented alert workflow.

Mitigation: Install and run the skill only with a narrowly scoped token for the realtime-alerting preset, and avoid granting unrelated scopes to the same token.

Risk: Webhook tests and alert tests send real outbound messages that cannot be withdrawn by the platform.

Mitigation: Warn recipients before testing, confirm the target channel, and use the generated webhook data source name rather than the human-readable label.

Risk: Creating or enabling an alert with a placeholder threshold can produce an unintended notification.

Mitigation: Create placeholder rules disabled, test them, patch in the real threshold, confirm the stored threshold, and only then toggle the rule on.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/guangfuwu/skills/privora-alert)
- [Publisher profile](https://clawhub.ai/user/guangfuwu)
- [Privora full quant skill package](https://clawhub.ai/guangfuwu/privora-cn-quant)
- [SKILL.md](artifact/SKILL.md)
- [CHANGELOG.md](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown with inline shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires LG_AGENT_BASE_URL and LG_AGENT_TOKEN; emitted commands call the Agent Skill Gateway and may create, test, patch, toggle, snooze, or inspect webhook-backed alert rules.]

## Skill Version(s):

1.0.1 (source: frontmatter and release evidence, released 2026-08-11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
