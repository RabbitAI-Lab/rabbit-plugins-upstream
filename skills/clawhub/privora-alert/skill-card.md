## Description:

Privora 实时监控 helps an agent configure threshold rules for subscribed asset fields, including gold, funds, Hong Kong stocks, U.S. stocks, and A-shares, and send Feishu, WeChat, or generic webhook notifications when a configured condition is crossed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guangfuwu](https://clawhub.ai/user/guangfuwu)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to set up and validate persistent Privora threshold alerts for market or fund data they have subscribed to. It guides the agent through channel setup, rule creation, webhook testing, threshold patching, activation, and post-setup verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A broad Privora token could allow the bundled API wrapper to perform actions beyond this package's narrow alerting workflow if used outside the documented flow.

Mitigation: Use a dedicated Privora token limited to the realtime-alerting preset and avoid granting extra scopes for this skill.

Risk: The skill creates persistent alert rules and sends real webhook messages during validation, so mistakes can notify live channels or leave rules enabled.

Mitigation: Follow the documented create-disabled, test, patch, toggle, and verification sequence, and confirm the final rule state with metric.alert.get and metric.alert.logs.

Risk: Changing LG_AGENT_BASE_URL or relying on the local allowlist as an authorization boundary can weaken operator control over where authenticated requests are sent and what calls are attempted.

Mitigation: Keep LG_AGENT_BASE_URL pointed at the trusted Privora endpoint and rely on server-side token scope enforcement, not the editable local allowlist, for authorization.

## Reference(s):

- [Privora Alert Skill on ClawHub](https://clawhub.ai/guangfuwu/skills/privora-alert)
- [Privora Marketplace](https://privora.cn/marketplace?utm_source=clawhub&utm_medium=agent_skill&utm_campaign=privora-alert)
- [Privora Token Settings](https://privora.cn/profile/tokens?utm_source=clawhub&utm_medium=agent_skill&utm_campaign=privora-alert)
- [Privora CN Quant Companion Skill](https://clawhub.ai/guangfuwu/privora-cn-quant)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown instructions with shell command examples and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operational guidance for Privora alert setup; commands require LG_AGENT_TOKEN and optionally LG_AGENT_BASE_URL.]

## Skill Version(s):

1.0.4 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
