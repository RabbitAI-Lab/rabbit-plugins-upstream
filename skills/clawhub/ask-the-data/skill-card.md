## Description:

Part of the Overpowered skill suite, this skill helps agents answer reproducible questions from structured data files such as Excel, CSV, JSON, TSV, or Parquet by discovering useful inputs, reading data dictionaries, loading durable relations when helpful, inspecting schema, querying only what is needed, and returning traceable results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[raguets](https://clawhub.ai/user/raguets)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and other users use this skill to ask questions over local structured datasets and receive answers backed by source files, business definitions, query logic, and validation checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can inspect local structured data files that may contain sensitive or inappropriate project data.

Mitigation: Install and use it only in projects where those files are appropriate for the agent to read.

Risk: A persisted local DuckDB database may retain copied or transformed data beyond a single question.

Mitigation: Persist a database only when repeated analysis or reproducibility requires it, and manage generated database files according to the project's data-handling rules.

Risk: Answers may be misleading if column names, codes, dates, units, currencies, or business definitions are guessed.

Mitigation: Read available dictionaries or codebooks first and report assumptions, filters, query logic, and validation checks with the answer.

## Reference(s):

- [Overpowered suite](https://github.com/raguets/overpowered)
- [ClawHub skill page](https://clawhub.ai/raguets/skills/ask-the-data)
- [Project conventions](references/project-conventions.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [Markdown with direct answers, evidence lists, query summaries, and optional SQL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers should include source, definition, filter, assumption, query, and validation provenance when material.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
