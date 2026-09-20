## Description:

Clusters and attributes related wallets using Nansen research profiler signals including funding chains, shared signers, CEX deposit patterns, counterparties, and historical balances.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and investigators use this skill to guide read-only wallet attribution workflows with Nansen CLI commands, including cluster expansion, pair comparison, L2 counterparty checks, and confidence scoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend Nansen API credits when agents run profiler and trace commands.

Mitigation: Use the documented pagination, batch limits, and trace width guidance; ask before expanding to newly discovered addresses.

Risk: Wallet attribution can involve privacy or compliance-sensitive analysis.

Mitigation: Keep analysis scoped to the user's stated investigation, rely on the confidence rules, and avoid treating weak signals such as ENS-only matches as attribution.

Risk: Attribution results may be incomplete or misleading when counterparty data is sparse or cross-chain activity is missed.

Mitigation: Use the documented L2 coverage workflow, historical balance checks, and confidence labels before presenting conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nansen-devops/skills/nansen-wallet-clustering)
- [Wallet Attribution Reference](artifact/REFERENCE.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands and attribution table fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires NANSEN_API_KEY and the nansen CLI; outputs are user-directed research guidance, not autonomous attribution decisions.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
