## Description:

A non-custodial USDC wallet on Base that an AI agent installs by itself, with spending limits enforced in the signing path rather than in a prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[graphiker-australia](https://clawhub.ai/user/graphiker-australia)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use this skill to give an AI agent a local non-custodial USDC wallet for receiving payments, sending bounded payouts, auto-paying HTTP 402/x402 charges, and reporting earned-versus-spent financial activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates and operates a real-money non-custodial USDC wallet with persistent local keys.

Mitigation: Install only after explicit operator approval, keep balances small, and require a human-held config lock before funding the wallet.

Risk: The artifact promotes one-line remote installer commands for software that grants financial authority.

Mitigation: Prefer a verified, pinned installer and inspect the installer source before execution.

Risk: Agent-controlled configuration changes could weaken spending limits or destination controls.

Mitigation: Use a destination allowlist and lock payment configuration so the agent cannot raise limits or empty the allowlist unilaterally.

Risk: The package includes referral monetization and a kina language feature beyond core wallet payments.

Mitigation: Review and disclose non-payment features and monetization behavior before enabling or funding the wallet.

## Reference(s):

- [stipend homepage](https://stipend.sh)
- [ClawHub skill page](https://clawhub.ai/graphiker-australia/skills/stipend)
- [Publisher profile](https://clawhub.ai/user/graphiker-australia)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline bash, Python, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI commands described by the skill return JSON; the skill also provides wallet setup, payment, safety, and troubleshooting guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 0.45.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
