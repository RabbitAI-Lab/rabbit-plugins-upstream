## Description:

MagicPay handles first-time setup, exact balance checks, crypto transfers and reconciliation, plus approved login, identity, checkout, donation, subscription, and payment workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xor777](https://clawhub.ai/user/xor777)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use MagicPay to manage protected payment, checkout, identity, login, donation, subscription, and saved Memory workflows while requiring explicit approval for consequential actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can coordinate high-impact payment, checkout, identity, login, and protected Memory workflows.

Mitigation: Use it only when that authority is intended; verify exact amount, currency, recipient, recurring status, country, and balance before approval, and treat only confirmed terminal settlement as success.

Risk: The security evidence flags hidden continuation comments and command automation as requiring careful review.

Mitigation: Review the continuation comments before deployment and require the runtime to validate returned commands against the current MagicPay session and the approved action.

Risk: MAGICPAY_API_KEY, local configuration, CDP endpoints, OTPs, and saved Memory values are sensitive.

Mitigation: Keep those values out of chat, logs, reports, and shared command arguments; rotate or revoke credentials if the environment is shared or compromised.

## Reference(s):

- [MagicPay Marketplace Documentation](https://github.com/nuanu-ai/skills/blob/main/docs/magicpay/openclaw/marketplace/README.md)
- [MagicPay CLI Package](https://www.npmjs.com/package/@nuanu-ai/magicpay-cli)
- [MagicPay Command Guide](references/commands.md)
- [MagicPay Boundaries](references/guardrails.md)
- [Native Payment Operations](references/payment-operations.md)
- [MagicPay Setup](references/setup.md)
- [MagicPay Result States](references/statuses.md)
- [MagicPay Operating Guide](references/workflow.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with MagicPay CLI commands and JSON-aware command handling]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the MagicPay CLI and MAGICPAY_API_KEY; consequential actions depend on exact returned commands, user approval, and terminal settlement.]

## Skill Version(s):

0.1.49 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
