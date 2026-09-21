## Description:

Privora realtime alerting helps an agent configure threshold rules for subscribed asset fields, including gold, funds, Hong Kong stocks, U.S. stocks, and A-shares, and send Feishu, WeChat, or generic webhook notifications when a value crosses the configured threshold.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guangfuwu](https://clawhub.ai/user/guangfuwu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create, test, enable, inspect, snooze, and update Privora metric-alert rules for subscribed market-data assets. It is intended for one-rule-at-a-time webhook alert setup, not asset ingestion, trading, escalation management, or background polling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Privora bearer token to create and manage alert rules.

Mitigation: Use the narrowest realtime-alerting token scopes available, keep the token private, and rotate it if exposure is suspected.

Risk: Webhook test actions send real messages to configured Feishu, WeChat, or generic webhook destinations.

Mitigation: Verify the webhook destination before testing and confirm with the operator that test messages were received in the intended channel.

Risk: Enabled alert rules persist on Privora after setup.

Mitigation: Confirm rule state and threshold before enabling, then snooze or toggle off rules that should stop generating notifications.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/guangfuwu/skills/privora-alert)
- [Publisher profile](https://clawhub.ai/user/guangfuwu)
- [Privora marketplace](https://privora.cn/marketplace?utm_source=clawhub&utm_medium=agent_skill&utm_campaign=privora-alert)
- [Privora token settings](https://privora.cn/profile/tokens?utm_source=clawhub&utm_medium=agent_skill&utm_campaign=privora-alert)
- [Privora CN Quant companion skill](https://clawhub.ai/guangfuwu/privora-cn-quant)
- [Privora API host](https://privora.cn)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with bash command examples and expected JSON response snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operator-facing steps for Privora alert workflows and may invoke webhook test messages through the documented shell wrapper.]

## Skill Version(s):

1.0.7 (source: SKILL.md frontmatter and ClawHub release evidence, released 2026-09-18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
