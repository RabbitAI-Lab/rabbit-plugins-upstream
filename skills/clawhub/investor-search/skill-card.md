## Description:

Builds sourced investor lists for a market, separating investors from advisers, deduplicating firms, and producing CSV outputs whose claims carry citations and checked status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chainleo](https://clawhub.ai/user/chainleo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, fundraisers, and business-development teams use this skill to research verifiable family offices, investment groups, private equity firms, VCs, and angels in a market. It is suited to deal sourcing, fundraising prospect lists, CRM enrichment, and filling gaps in existing investor data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local investor-search CSV files may contain public business research, named individuals, LinkedIn URLs, and rejection notes in the agent working directory.

Mitigation: Use the skill in a workspace appropriate for that data, especially when the working directory is shared, and keep investors-rejected.csv as local working data rather than publishing it.

Risk: The skill cannot support a completeness claim when files cannot be written, read back, or located.

Mitigation: Report those runs as partial, print CSV and ledger output in chat when needed, and do not claim exhaustion without the required local record.

Risk: The stopping-rule gates are argued from field tests but have not all been measured in a completed exhaustion run.

Mitigation: Name the searched surfaces, preserve pending and rounds files, drain resolvable pending names before claiming exhaustion, and label budget-limited work as partial.

Risk: Investor research output may be mistaken for investment advice or a ranked recommendation list.

Mitigation: Use the output as sourced research only; the skill does not rank, score, recommend, infer email addresses, or make claims beyond each row's checked date.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chainleo/skills/investor-search)
- [README](artifact/README.md)
- [Field Tests](artifact/FIELD-TESTS.md)
- [Environment](artifact/reference/environment.md)
- [Lists](artifact/reference/lists.md)
- [Why Each Rule Exists](artifact/reference/why.md)

## Skill Output:

**Output Type(s):** [Files, Markdown, Guidance]

**Output Format:** [CSV files, ledger text, and Markdown summary; fenced CSV and ledger text when files cannot be written]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes scoped local files under investor-search/<market>/ and reads them back on later runs; rejection files are local working data.]

## Skill Version(s):

1.1.0 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
