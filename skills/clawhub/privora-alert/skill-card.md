## Description:

Privora 实时监控 helps an agent configure threshold rules for subscribed asset fields, verify webhook delivery, and keep alerts online for gold, funds, Hong Kong stocks, U.S. stocks, and A-shares.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guangfuwu](https://clawhub.ai/user/guangfuwu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to create, test, update, snooze, and inspect Privora metric-alert rules for already-subscribed financial data assets. It is intended for workflow guidance and API execution around webhook-based monitoring, not for investment advice or asset onboarding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The realtime-alerting token can read subscribed asset data, create webhook channels, send test webhook messages, and create or change persistent alert rules.

Mitigation: Use a token scoped to the realtime-alerting preset, avoid broader Privora scopes, and rotate the token if it may have been exposed.

Risk: On shared Windows/MSYS2 machines, alert request bodies may briefly exist as temporary files.

Mitigation: Run the workflow in an isolated environment for sensitive alert data and avoid shared temporary directories when possible.

Risk: Webhook tests and alert tests send real messages to the configured external channel.

Mitigation: Warn channel participants before testing and require user confirmation that the expected message arrived before enabling a rule.

Risk: Using a placeholder threshold incorrectly or retrying a toggle without checking state can create false alerts or leave a rule disabled.

Mitigation: Create the rule disabled, test with the placeholder threshold, patch to the real threshold, inspect the rule state, and only then toggle it online.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/guangfuwu/skills/privora-alert)
- [Publisher profile](https://clawhub.ai/user/guangfuwu)
- [Privora marketplace](https://privora.cn/marketplace?utm_source=clawhub&utm_medium=agent_skill&utm_campaign=privora-alert)
- [Privora token settings](https://privora.cn/profile/tokens?utm_source=clawhub&utm_medium=agent_skill&utm_campaign=privora-alert)
- [Privora CN Quant companion skill](https://clawhub.ai/guangfuwu/privora-cn-quant)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operator-facing workflow steps for calling Privora alerting skill IDs through scripts/lg_agent_exec.sh.]

## Skill Version(s):

1.0.6 (source: frontmatter and ClawHub release metadata, released 2026-09-15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
