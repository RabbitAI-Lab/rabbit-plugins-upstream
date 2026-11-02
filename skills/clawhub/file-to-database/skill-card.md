## Description:

Turns CSV, Excel, JSON, JSONL, and TSV files into validated database schemas and deliverables, then supports safe natural-language database operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thomaszhou22](https://clawhub.ai/user/thomaszhou22)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to profile flat files, design and validate relational databases, and generate schemas, ERDs, seed scripts, and migrations. They can also use natural-language requests to query or safely modify the resulting database.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Required tests may lack isolation safeguards, and database changes may trigger full database exports.

Mitigation: Use a disposable database copy until rollback rehearsals and constraint tests provide reliable isolation and cleanup; make full exports opt-in and review their contents and delivery channel because exports can retain personal data.

## Reference(s):

- [ClawHub Skill Release](https://clawhub.ai/thomaszhou22/skills/file-to-database)
- [Source Repository](https://github.com/Thomaszhou22/file-to-database-skill)
- [Database Design Methodology](references/methodology.md)
- [Runtime Operations](references/operations.md)
- [Engineering Hardening](references/engineering.md)

## Skill Output:

**Output Type(s):** [Code, Markdown, Shell commands, Guidance]

**Output Format:** [SQL DDL, Mermaid ERD, Python or SQL seed scripts, reversible migrations, validation results, and natural-language reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deliverables may be generated as files and depend on the selected database engine and available data.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
