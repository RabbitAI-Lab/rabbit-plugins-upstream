## Description:

Privora configures threshold-based monitoring for subscribed assets, including gold, funds, Hong Kong stocks, U.S. stocks, and A-shares, and sends Feishu, WeChat, or generic webhook notifications when a configured rule crosses its threshold.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guangfuwu](https://clawhub.ai/user/guangfuwu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to create, test, enable, pause, and inspect Privora metric-alert rules for assets they have already subscribed to. The workflow helps an agent verify data availability, configure a webhook channel, test alert delivery, and leave the real threshold rule enabled for platform-side evaluation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an authenticated Privora token that can read subscribed asset data, create and modify alert rules, create webhook channels, and send webhook test messages.

Mitigation: Use a token limited to the documented realtime-alerting preset, avoid broader Privora scopes, and review proposed commands before execution.

Risk: Webhook channel tests and alert tests can send real messages to Feishu, WeChat, or generic webhook destinations.

Mitigation: Confirm the destination channel before testing and warn recipients that setup and validation messages may be sent.

Risk: Request bodies may be temporarily written to disk, and the evidence calls out Windows/MSYS2 temporary-file exposure for sensitive webhook URLs or business alert details.

Mitigation: Run the wrapper in a trusted environment, avoid shared Windows/MSYS2 hosts for sensitive alert configuration, and keep webhook URLs and alert messages minimally sensitive.

Risk: The packaged allowed-skills file is a client-side packaging control, not an authorization boundary.

Mitigation: Rely on server-side token scope enforcement and keep Privora tokens scoped to the alerting workflow instead of adding unrelated capabilities.

Risk: Threshold alerts are numeric signals and may be mistaken for investment advice.

Mitigation: Treat alert results as operator-reviewed monitoring signals, not buy, sell, or trading recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/guangfuwu/skills/privora-alert)
- [Publisher profile](https://clawhub.ai/user/guangfuwu)
- [Privora marketplace](https://privora.cn/marketplace?utm_source=clawhub&utm_medium=agent_skill&utm_campaign=privora-alert)
- [Privora token settings](https://privora.cn/profile/tokens?utm_source=clawhub&utm_medium=agent_skill&utm_campaign=privora-alert)
- [Privora CN Quant full skill](https://clawhub.ai/guangfuwu/privora-cn-quant)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline bash commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operational steps for Privora alert setup and verification; API calls use LG_AGENT_BASE_URL and LG_AGENT_TOKEN.]

## Skill Version(s):

1.0.6 (source: frontmatter and server release, released 2026-09-15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
