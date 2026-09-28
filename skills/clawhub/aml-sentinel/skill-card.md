## Description:

Checks transaction records for simple anti-money-laundering warning patterns, including structuring, rapid movement, missing counterparty KYC, and unreported large transactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and compliance teams use this local helper to screen transaction records for basic AML warning patterns and prioritize human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Simple heuristic flags can miss suspicious activity or incorrectly flag legitimate transactions.

Mitigation: Use results only for triage; verify against current official AML requirements and have qualified personnel review consequential decisions.

Risk: Transaction records may contain sensitive financial or identifying information.

Mitigation: Keep transaction files local and restrict access to them.

## Reference(s):

- [Publisher's LGD hub](https://zhaoxinghua09-cell.github.io/lgd-hub/)
- [AML Sentinel on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/aml-sentinel)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text or JSON transaction risk results; agent guidance in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports matched patterns, heuristic risk score and level; exit status indicates whether high risk was found.]

## Skill Version(s):

1.0.2 (source: published ClawHub release; bundled files show different versions)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
