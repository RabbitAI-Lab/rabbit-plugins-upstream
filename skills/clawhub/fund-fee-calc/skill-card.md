## Description:

fund-fee-calc helps agents run an offline fund fee and net return calculator that estimates management, custody, and sales fee costs, net returns, and guaranteed-return claim screening.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Financial product reviewers, developers, and agents use this skill to estimate fund fee drag and net return from provided rates and holding period. It also flags promotional text that claims guaranteed principal, risk-free returns, or guaranteed returns as a preliminary compliance screen.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented one-command global install path uses mutable, unpinned remote execution.

Mitigation: Use a reviewed manual or pinned installation method before deployment.

Risk: Calculator outputs can be misleading if unusual numeric inputs or regulated investment scenarios are treated as final advice.

Mitigation: Treat outputs as preliminary screening only and require professional review for investment, legal, or regulated compliance decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/fund-fee-calc)
- [Publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [Project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON from a command-line calculator, with guidance for agent use.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic local output; returns rc=0 for pass, rc=1 for flagged promotional claims, and rc=2 for usage errors.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
