## Description:

Answer reproducible questions from structured data files such as Excel, CSV, JSON, TSV, or Parquet by discovering useful inputs, reading data dictionaries, loading durable relations when helpful, inspecting schema, querying only what is needed, and returning traceable results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[raguets](https://clawhub.ai/user/raguets)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external users use this skill to answer questions from local tabular or structured project data while preserving source files, definitions, filters, query logic, and validation checks needed to reproduce the answer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may inspect local structured data and dictionaries, which can include sensitive project data.

Mitigation: Use it in projects where local data access is appropriate, and review which source files are used in the returned evidence.

Risk: Answers can be misleading if column semantics, status codes, units, dates, or data availability are assumed instead of verified.

Mitigation: Read available dictionaries or code tables first, state assumptions, and validate results with counts, null checks, uniqueness checks, or targeted samples.

Risk: Persistent DuckDB state can retain derived local data when persistence is used for reproducibility.

Mitigation: Persist only when repeated questions or expensive reloads justify it, and manage local database artifacts according to the project data policy.

## Reference(s):

- [Project Conventions](references/project-conventions.md)
- [ClawHub skill page](https://clawhub.ai/raguets/skills/ask-the-data)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [Markdown answer with evidence bullets and optional SQL or query summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source files or tables, business definitions, filters, assumptions, query logic, and validation checks when relevant.]

## Skill Version(s):

1.0.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
