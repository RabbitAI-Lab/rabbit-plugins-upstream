## Description:

Helps users record stock, fund, and crypto events in Beancount by proposing entries and lot treatment before any confirmed write.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT-0

## Use Case:

Individual investors and Beancount users can record described investment events, review proposed lots and cost basis, and inspect realized gains. Ledger changes are proposed first and written only after approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected hosted-ledger operation may not match a local-only expectation.

Mitigation: If local-only operation is required, disable the hosted fallback; otherwise separately approve the hosted service and ledger. Back up the ledger and review every proposed financial entry.

## Reference(s):

- [Project homepage](https://github.com/bex-co/beancount-io/tree/main/skills)
- [bea-cli.md](references/bea-cli.md)
- [bea-import.md](references/bea-import.md)
- [bql-recipes.md](references/bql-recipes.md)
- [compatibility.md](references/compatibility.md)
- [dedup.md](references/dedup.md)
- [realized-gains.md](references/realized-gains.md)

## Skill Output:

**Output Type(s):** [Text, Code, Guidance]

**Output Format:** [Markdown with proposed Beancount entries and summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write proposals only after explicit approval; realized-gains reports are read-only.]

## Skill Version(s):

1.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
