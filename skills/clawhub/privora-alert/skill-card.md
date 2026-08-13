## Description:

Privora realtime monitoring helps agents configure threshold alerts for subscribed gold, fund, Hong Kong, U.S., and A-share assets, with Feishu, WeChat, or generic webhook notifications when numeric fields cross configured rules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guangfuwu](https://clawhub.ai/user/guangfuwu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide an agent through creating, testing, and enabling Privora metric-alert rules for subscribed market data assets. It is suited for one-rule-at-a-time threshold monitoring where the operator wants webhook delivery proof and persistent rule verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included gateway scripts use a Privora bearer token and can enumerate visible skills or send arbitrary skill execution requests within the token's granted scopes.

Mitigation: Use a dedicated Privora token limited to the realtime-alerting preset, and avoid adding broader scopes for unrelated workflows.

Risk: Webhook tests and alert tests send real external messages to Feishu, WeChat, or generic webhook destinations.

Mitigation: Warn recipients before testing, verify the destination channel manually, and treat successful API responses as incomplete until the operator confirms receipt.

Risk: A placeholder threshold can cause an unwanted alert if the rule is enabled before the real threshold is patched in.

Mitigation: Create placeholder-threshold rules with enabled:false, run the proof test, patch the real threshold, confirm rule state, then toggle once to enable.

Risk: Threshold-crossing alerts are numeric monitoring signals and can be mistaken for investment recommendations.

Mitigation: Present alerts as review prompts only, and require human judgment before any trading or financial action.

## Reference(s):

- [Privora Alert Skill Listing](https://clawhub.ai/guangfuwu/skills/privora-alert)
- [Privora Marketplace](https://privora.cn/marketplace?utm_source=clawhub&utm_medium=agent_skill&utm_campaign=privora-alert)
- [Privora Token Settings](https://privora.cn/profile/tokens?utm_source=clawhub&utm_medium=agent_skill&utm_campaign=privora-alert)
- [Privora CN Quant Skill](https://clawhub.ai/guangfuwu/privora-cn-quant)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operator-facing workflow guidance for Privora alert setup; command execution requires LG_AGENT_TOKEN and may use LG_AGENT_BASE_URL.]

## Skill Version(s):

1.0.3 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
