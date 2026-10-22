## Description:

Answers explicit questions about a local Beancount ledger with reproducible `bea` queries and reports, without editing records or providing investment or tax advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT No Attribution

## Use Case:

People who maintain a local Beancount ledger can use the skill to answer explicit questions about spending, trends, net worth, holdings, recurring charges, and anomalies using executed `bea` queries. It is not intended for ledger edits, investment or tax advice, or general Beancount documentation questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may read sensitive financial information from the selected ledger.

Mitigation: Select the intended ledger and review the requested scope before running queries.

Risk: The skill's read-only behavior is instructional and does not itself enforce filesystem access boundaries.

Mitigation: Use filesystem-level read-only access when enforcing that ledger contents cannot be changed.

Risk: Installation may download engine dependencies, and configured online price includes may access the network.

Mitigation: Review dependency installation and any network-enabled price configuration before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/puncsky/skills/beancount-ask)
- [Project documentation](https://github.com/bex-co/beancount-io/tree/main/skills)
- [bea CLI reference](references/bea-cli.md)
- [BQL recipes](references/bql-recipes.md)
- [Compatibility notes](references/compatibility.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Analysis]

**Output Format:** [Markdown answers with reproducible `bea` queries and reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only ledger analysis; reported figures are based on executed queries.]

## Skill Version(s):

1.0.4 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
