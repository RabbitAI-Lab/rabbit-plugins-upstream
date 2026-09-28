## Description:

Scan a resolved Polymarket market for wallets exhibiting suspicious trading patterns: fresh funding, single-market focus, extreme ROI, late entry at high prices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and developers use this skill to examine winners in resolved Polymarket markets and identify wallet trading patterns worth further review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated research calls, especially wallet-scanning loops, may consume credits or spend funds under existing wallet authorization.

Mitigation: Review the Nansen CLI package, wallet payment policy, spending limits and likely call volume before running the scan.

Risk: Heuristic flags may wrongly suggest suspicious conduct.

Mitigation: Treat wallet scores as leads for human review, not proof of wrongdoing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/nansen-devops/skills/nansen-polymarket-insider-scan)
- [Publisher profile](https://clawhub.ai/user/nansen-devops)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Wallet scores and flagged trading patterns for further review.]

## Skill Version(s):

0.1.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
