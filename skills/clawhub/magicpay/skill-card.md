## Description:

MagicPay guides agents through setup, balance checks, crypto transfers and reconciliation, and approved login, identity, checkout, donation, subscription, and payment workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xor777](https://clawhub.ai/user/xor777)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use MagicPay to complete protected payment, login, identity, checkout, donation, subscription, and crypto-transfer workflows while keeping sensitive values out of chat and requiring user approval for consequential actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MagicPay can support real payment, login, identity, and saved-data workflows.

Mitigation: Install it only when those workflows are intended, protect the MagicPay API key and browser/CDP endpoints, and review each approval link before acting.

Risk: Consequential actions may involve payment authorization or protected data submission.

Mitigation: Require scoped user approval for the exact live action and facts before continuing, and stop when required approval or live facts are missing.

Risk: Payment attempts can remain pending or uncertain before settlement.

Mitigation: Treat approval as permission only and report success only after MagicPay returns confirmed terminal settlement or the documented final result state.

Risk: Protected Memory values and payment details could be exposed if handled manually.

Mitigation: Use MagicPay Memory planning and returned commands to materialize values without printing, logging, or passing protected values through chat.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xor777/skills/magicpay)
- [OpenClaw Marketplace README](https://github.com/nuanu-ai/skills/blob/main/docs/magicpay/openclaw/marketplace/README.md)
- [MagicPay CLI npm Package](https://www.npmjs.com/package/@nuanu-ai/magicpay-cli)
- [Commands Reference](https://github.com/nuanu-ai/skills/blob/main/docs/magicpay/references/commands.md)
- [Guardrails Reference](https://github.com/nuanu-ai/skills/blob/main/docs/magicpay/references/guardrails.md)
- [Payment Operations Reference](https://github.com/nuanu-ai/skills/blob/main/docs/magicpay/references/payment-operations.md)
- [Setup Reference](https://github.com/nuanu-ai/skills/blob/main/docs/magicpay/references/setup.md)
- [Statuses Reference](https://github.com/nuanu-ai/skills/blob/main/docs/magicpay/references/statuses.md)
- [Workflow Reference](https://github.com/nuanu-ai/skills/blob/main/docs/magicpay/references/workflow.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the MagicPay CLI and MAGICPAY_API_KEY; approval and Memory request links should be handled as sensitive user-facing handoffs.]

## Skill Version(s):

0.1.45 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
