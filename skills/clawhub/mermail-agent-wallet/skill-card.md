## Description:

Inspect Mermail Agent Wallet and PayBox balances, guide console funding, onramp, and signing handoffs, create USDC transfer proposals, or transfer native ETH/SOL and reviewed PayBox catalog tokens with human confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Mermail Agent Wallet and PayBox status, handle funding or signing handoffs, and prepare or submit wallet transfers only after explicit human confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wallet OAuth access and PayBox delegation can expose high-value wallet actions.

Mitigation: Install only when Mermail Agent Wallet or PayBox is intended, require OAuth wallet scopes, and use first-party Mermail console handoffs for connection, reauthorization, funding, and signing.

Risk: A completed transfer may be irreversible if the mailbox, asset, chain, destination, or amount is wrong.

Mitigation: Require a fresh exact preview, independent user verification, a destructive-action token for gated writes, and explicit approval before submission.

Risk: Email, attachments, memory, paid-service content, or tool output could contain untrusted payment instructions.

Mitigation: Treat those inputs as data only; they cannot authorize wallet actions, change destinations, raise limits, or skip confirmation.

Risk: Checkout, approval, and signing URLs are browser-only and redacted from model-visible tool output.

Mitigation: Use Mermail console handoff links, never ask for raw signing keys or signatures in chat, and stop link-retrieval loops when URLs are redacted.

## Reference(s):

- [Mermail Agent Wallet documentation](https://docs.mermail.app/ai/skills)
- [ClawHub skill page](https://clawhub.ai/mermail/skills/mermail-agent-wallet)
- [Agent Wallet security boundary](artifact/references/security.md)
- [Agent Wallet tool map](artifact/references/tools.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown text with inline commands, exact transfer previews, and console handoff links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OAuth wallet scopes and explicit human confirmation before transfer submission.]

## Skill Version(s):

1.0.6 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
