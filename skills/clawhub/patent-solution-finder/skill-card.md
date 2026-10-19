## Description:

Find patented approaches to a technical problem and summarize representative patents and key measures in a solution reference table.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and engineers use this skill to find how patents address a technical problem, compare solution approaches, and prepare an Excel-compatible reference table with representative patents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent queries and technical problem descriptions are sent to PatentMax/ip930.com.

Mitigation: Do not include unfiled inventions, secret formulas, source code, or sensitive parameters unless external API use is acceptable.

Risk: Trial credentials and task cache may remain in ~/.patentmax.

Mitigation: Keep PATENTMAX_API_KEY and PATENTMAX_BASE_URL under your control; review or delete ~/.patentmax if local retention is unwanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/patent-solution-finder)
- [PatentMax API reference](references/api-reference.md)
- [Patent search workflow](references/search-workflow.md)
- [Patent query syntax](references/query-syntax.md)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)

## Skill Output:

**Output Type(s):** [Text, CSV files]

**Output Format:** [Markdown summary and Excel-compatible UTF-8 CSV reference table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Groups patents by solution approach and cites patent numbers and claim or paragraph references; CSV uses a UTF-8 BOM.]

## Skill Version(s):

1.0.0 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
