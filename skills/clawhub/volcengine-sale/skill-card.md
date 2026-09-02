## Description:

Use when the user asks to purchase, subscribe, provision, open, or place an order for a Volcengine commercial product, including Chinese purchase or provisioning intents paired with a Volcengine product name.

This skill is ready for commercial/non-commercial use.

## Publisher:

[volc-sdk-team](https://clawhub.ai/user/volc-sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route Volcengine product purchase or provisioning requests, install required dependent skills with authorization, and guide CommonBuy order flows for supported products such as TOS.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help place real Volcengine orders through the ve CLI.

Mitigation: Review the displayed command and require explicit user confirmation before executing any purchase.

Risk: The skill may request installation of dependent skills or external source repositories.

Mitigation: Install dependencies only after user authorization and only from trusted marketplace or source locations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/volc-sdk-team/skills/volcengine-sale)
- [Product routing rules](references/product-rule.md)
- [CommonBuy order flow](references/commonbuy.md)
- [CommonBuy error handling](references/commonbuy-errors.md)
- [TOS CommonBuy parameters](references/tos.md)
- [Volcengine Ark CLI](https://github.com/volcengine/ark-cli)
- [Volcengine TLS CLI](https://github.com/volcengine-tls/ve-tls-cli)
- [Volcengine TOS console](https://console.volcengine.com/tos)
- [Volcengine TOS resource packages](https://console.volcengine.com/tos/resource)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Volcengine CLI commands that require user review and confirmation before execution.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
