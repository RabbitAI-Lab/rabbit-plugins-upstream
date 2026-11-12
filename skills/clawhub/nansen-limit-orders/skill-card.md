## Description:

Guide users through native limit orders on Solana via `nansen trade limit-order create|list|cancel|update`, and the alert-based settlement-signal fallback for chains without native support. Use when a user wants a price-triggered buy or sell.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create, inspect, update, and cancel native Solana limit orders, or to configure best-effort settlement alerts on chains without native limit-order support.

### Deployment Geography for Use:

Global, subject to applicable geographic checks.

## Known Risks and Mitigations:

Risk: Creating or cancelling a native limit order can submit a transaction that affects wallet funds.

Mitigation: Use `--dry-run` to review the proposed action, and obtain the user's confirmation before submitting it.

Risk: Settlement alerts are best-effort transfer signals and may miss a venue's settlement pattern or match unrelated transfers if broadened.

Mitigation: Describe alerts as settlement signals rather than authoritative order tracking, and keep filters scoped to the intended wallet, chain, token, and side.

Risk: The skill documents API credentials and a cached trading-vault token.

Mitigation: Use the selected authenticated session or API key with its existing permissions, and stop on authentication failures rather than switching to anonymous payment.

## Reference(s):

- [Nansen CLI browser login platform scope](https://github.com/nansen-ai/nansen-cli/blob/main/docs/browser-login.md#preview-platform-scope)
- [nansen-cli package](https://www.npmjs.com/package/nansen-cli)
- [nansen-cli repository](https://github.com/nansen-ai/nansen-cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can create, update, or cancel live orders when executed.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
