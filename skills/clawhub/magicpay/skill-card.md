## Description:

Handle approved login, identity, checkout, donation, subscription, payment pages, and typed action approvals through the magicpay CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xor777](https://clawhub.ai/user/xor777)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use MagicPay to complete approved browser workflows that require saved login, identity, payment, wallet, or profile data while keeping raw stored values out of the agent prompt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive payment, identity, wallet, login, and saved-profile workflows.

Mitigation: Use MagicPay Memory and typed approval requests so protected values and final consequential actions stay behind explicit user approval gates.

Risk: MagicPay API keys, local configuration, and private CDP endpoints can expose account or browser authority if shared.

Mitigation: Keep API keys, config files, Memory refs, and CDP endpoints private; stop and rotate or revoke credentials if the workspace or browser session may be compromised.

Risk: A compromised browser, operating system, or shell can still affect sensitive workflows.

Mitigation: Use only trusted, user-approved browser sessions and do not treat MagicPay as protection for an untrusted runtime.

Risk: A payment or protected action may no longer match the facts the user approved.

Mitigation: Collect visible action facts such as amount, currency, recipient, recurring status, and task details before approval, and ask again if those facts change.

## Reference(s):

- [MagicPay OpenClaw Marketplace Documentation](https://github.com/nuanu-ai/skills/blob/main/docs/magicpay/openclaw/marketplace/README.md)
- [MagicPay CLI Package](https://www.npmjs.com/package/@nuanu-ai/magicpay-cli)
- [MagicPay Operating Guide](https://github.com/nuanu-ai/skills/blob/main/docs/magicpay/references/workflow.md)
- [MagicPay Command Guide](https://github.com/nuanu-ai/skills/blob/main/docs/magicpay/references/commands.md)
- [MagicPay Result States](https://github.com/nuanu-ai/skills/blob/main/docs/magicpay/references/statuses.md)
- [MagicPay Boundaries](https://github.com/nuanu-ai/skills/blob/main/docs/magicpay/references/guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON result interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses typed approval gates for consequential browser actions and value-free Memory planning before filling approved data.]

## Skill Version(s):

0.1.43 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
