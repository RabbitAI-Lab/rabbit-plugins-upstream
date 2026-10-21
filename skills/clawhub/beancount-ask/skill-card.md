## Description:

Answer questions about a Beancount ledger using reproducible, read-only bea queries and reports for spending, trends, net worth, holdings, subscriptions, and anomalies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT-0

## Use Case:

External users maintaining Beancount ledgers use this skill to answer personal-finance questions with reproducible queries and reports, while seeing the data limits and query behind each figure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The guidance conflicts on whether connected Beancount.io ledgers are in scope despite the local-only, read-only framing.

Mitigation: Resolve the scope conflict before use; default to the user's selected local ledger and read-only commands, and use a hosted-ledger workflow only when explicitly chosen.

## Reference(s):

- [bea CLI recipes](references/bea-cli.md)
- [BQL recipes](references/bql-recipes.md)
- [CSV import guidance](references/bea-import.md)
- [Deduplication guidance](references/dedup.md)
- [Compatibility guidance](references/compatibility.md)
- [Realized gains reference](references/realized-gains.md)
- [Related skill suite homepage](https://github.com/bex-co/beancount-io/tree/main/skills)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands]

**Output Format:** [Markdown with query results and inline shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only answers; figures come from executed queries, with relevant data limitations stated.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
