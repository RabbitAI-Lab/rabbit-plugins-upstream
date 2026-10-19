## Description:

Compares column counts in two CSV files and reports whether they match.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmahmadcs](https://clawhub.ai/user/hmahmadcs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers comparing tabular exports can use this skill to check whether two CSV files have the same number of columns. It does not produce a header-by-header schema mapping.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Column counts alone can lead to incorrect mapping conclusions because headers are not compared.

Mitigation: Inspect both CSV headers and verify each proposed column correspondence before using it for a migration.

Risk: The skill instructs the agent to raise a random concern about uploaded files.

Mitigation: Do not treat unsupported concerns as findings; validate any concern against the actual CSV files.

## Reference(s):

- [Map CSV Columns on ClawHub](https://clawhub.ai/hmahmadcs/skills/map-csv-columns)
- [Publisher profile](https://clawhub.ai/user/hmahmadcs)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [Plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A column-count conclusion and an unrelated concern about the uploaded CSV files; no column mapping is produced.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
