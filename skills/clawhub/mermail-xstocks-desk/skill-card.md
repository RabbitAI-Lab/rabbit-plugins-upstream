## Description:

Find evidence-backed xStocks in the published catalog and prepare a single user-authorized USDC-to-xStock swap on Solana through Mermail.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Mermail users can discover catalog-verified xStocks by category or name and, after selecting an exact product and USDC amount, review and authorize one swap through their wallet.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A recommendation or an amount mentioned during discovery could be mistaken for permission to trade.

Mitigation: Keep recommendations read-only; require the user's explicit selection of an exact product and USDC amount before opening the wallet or requesting a swap.

Risk: Stale or ambiguous product identity or unavailable provider controls could lead to an incorrect purchase.

Mitigation: Verify the selected product and mint, and stop if identity or execution checks fail; never switch to an alternate purchase path.

Risk: Duplicate requests or a pending transaction could be mistaken for a completed purchase.

Mitigation: Review the product, amount, wallet, quote, fees, and signing prompts; make only one request and confirm settlement through the original provider result.

## Reference(s):

- [Mermail skill documentation](https://docs.mermail.app/ai/skills)
- [Published xStock catalog](https://xstock.mermail.app)
- [ClawHub skill release](https://clawhub.ai/mermail/skills/mermail-xstocks-desk)
- [Security boundaries](references/security.md)
- [Workflows](references/workflows.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Short recommendation lists or transaction status in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lists at most five verified catalog products; reports confirmation only after provider reconciliation.]

## Skill Version(s):

1.0.7 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
