## Description:

Answer questions about a local Beancount ledger using shown, reproducible bea queries and reports for spending, trends, net worth, holdings, subscriptions and anomalies. Strictly read-only; figures come from executed queries. Skip ledgers hosted on Beancount.io, recording transactions (beancount-add), reconciliation, migration, ledger edits, option pricing or greeks, investment or tax advice, and general Beancount, BQL, or `bea` documentation questions (including what `bea ask` does).

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and developers can query a local Beancount ledger for spending, trends, net worth, holdings, subscriptions, and anomalies. The skill returns figures from executed, reproducible queries and does not modify the ledger or provide investment or tax advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ledger files contain sensitive financial records.

Mitigation: Limit access to the intended ledger and its files.

Risk: Shared workflow examples should not be treated as authorization to change the ledger.

Mitigation: Keep this skill read-only and use separate skills for edits or imports.

Risk: The skill's hosted-ledger wording is inconsistent.

Mitigation: Use connected-server reporting only when that route is intended; otherwise keep reporting on the local ledger.

## Reference(s):

- [bea CLI reference](references/bea-cli.md)
- [BQL query recipes](references/bql-recipes.md)
- [Compatibility guidance](references/compatibility.md)
- [ClawHub skill page](https://clawhub.ai/puncsky/skills/beancount-ask)
- [Project homepage](https://github.com/bex-co/beancount-io/tree/main/skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Markdown with reported figures and reproducible BQL queries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; figures come from executed queries; does not modify ledger files.]

## Skill Version(s):

1.0.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
