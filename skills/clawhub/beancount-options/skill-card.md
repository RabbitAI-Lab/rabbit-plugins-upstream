## Description:

Record a described options trade or lifecycle event as validated transactions in a local Beancount ledger through bea, after review and confirmation. Use for single-leg or multi-leg opens, closes, rolls, assignment, exercise and expiration, including pasted broker confirmations. Skip options education, pricing/greeks, tax planning, analytics, broker statement imports, other manual entries (beancount-add), share, fund, and crypto trades and realized-gains reports (beancount-trade), ledger `option` settings such as operating_currency, and ledgers hosted on Beancount.io.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT-0

## Use Case:

External investors and bookkeepers use this skill to turn described options trades and lifecycle events into proposed Beancount ledger transactions, then review and approve the exact entries before they are added to a local ledger.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release has conflicting guidance about stock-purchase entries and estimated trade prices.

Mitigation: Review scope conflicts, use actual broker fill prices, route separate stock purchases through the stock-trade workflow, keep a ledger backup, and approve the exact destination and every entry.

Risk: A successful ledger check could be mistaken for verification that supplied trade details are accurate.

Mitigation: Verify trade details against broker records; treat the ledger check as a bookkeeping-consistency check only.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/puncsky/skills/beancount-options)
- [Project homepage (release metadata)](https://github.com/bex-co/beancount-io/tree/main/skills)
- [Shared bea command recipes](references/bea-cli.md)
- [Single-leg options](references/single-leg.md)
- [Assignment](references/assignment.md)
- [Exercise](references/exercise.md)
- [Rolling](references/rolling.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Beancount transaction blocks and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transaction proposals target a local ledger and require user approval before writing; a ledger check confirms bookkeeping consistency, not trade-detail accuracy.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
