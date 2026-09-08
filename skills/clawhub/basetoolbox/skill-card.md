## Description:

Base toolbox helps agents check Base Uniswap v3 swap preflights, allowances, transaction explanations, transfer checks, token USD prices, EIP-1559 gas, and ENS resolution through an optional paid HTTP API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cartonpliant](https://clawhub.ai/user/cartonpliant)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to inspect Base swap, allowance, transfer, gas, token price, and ENS questions before approving payments, allowances, signatures, or submissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid POST endpoints may disclose wallet, transaction, token, recipient, calldata, or ENS details to the remote service and PayAI.

Mitigation: Show the exact endpoint, price, recipient, network, asset, facilitator, and JSON fields before payment, and avoid adding extra identifiers.

Risk: Remote calldata or approve/revoke suggestions could be unsafe if treated as authorization.

Mitigation: Require fresh user approval for each paid call, run local approval verification before on-chain allowance changes, reject unlimited approvals, and do not sign or submit transactions based only on remote calldata.

## Reference(s):

- [Base toolbox API](https://basetoolbox.cartonpliant.workers.dev)
- [Base toolbox ClawHub listing](https://clawhub.ai/cartonpliant/skills/basetoolbox)
- [PayAI facilitator](https://facilitator.payai.network)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill proposes HTTP API calls and local verification commands; paid calls, token allowances, and transaction signing each require separate fresh approval.]

## Skill Version(s):

1.3.6 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
