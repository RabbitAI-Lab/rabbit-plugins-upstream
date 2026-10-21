## Description:

Record a described options trade or lifecycle event as validated transactions in a local Beancount ledger through bea, after review and confirmation. Use for single-leg or multi-leg opens, closes, rolls, assignment, exercise and expiration, including pasted broker confirmations. Skip options education, pricing/greeks, tax planning, analytics, broker statement imports, other manual entries (beancount-add), share, fund, and crypto trades and realized-gains reports (beancount-trade), ledger `option` settings such as operating_currency, and ledgers hosted on Beancount.io.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and developers maintaining Beancount ledgers use this skill to turn a described options trade or lifecycle event into proposed ledger transactions, then review, confirm, and validate those entries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local-ledger scope conflicts with instructions that allow hosted-ledger access.

Mitigation: Use hosted-ledger access only with separate, explicit authorization.

Risk: A fallback may allow financial entries to be written without validation.

Mitigation: Require a working ledger validator and backup, and approve the exact entries and destination before writing.

## Reference(s):

- [Skill project page (metadata homepage)](https://github.com/bex-co/beancount-io/tree/main/skills)

## Skill Output:

**Output Type(s):** [Beancount transactions, Shell commands, Guidance]

**Output Format:** [Beancount transaction entries and account-open directives with review and validation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Proposed ledger writes require review, explicit confirmation, and validation]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
