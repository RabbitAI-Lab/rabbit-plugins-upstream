## Description:

Creates, edits, and organizes Flydb V/R/U migration SQL scripts, covering naming, version families, directory layouts, path filters, placeholders, and checksum-safe change discipline.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zzxcoding](https://clawhub.ai/user/zzxcoding)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to manage Flydb migration SQL files, choose correct V/R/U script names and versions, reorganize migration locations, and troubleshoot script-related FLYDB-2xxx errors. It supports script authoring and review while leaving database execution, repair, and recovery operations to separate Flydb CLI workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated migration SQL can introduce incorrect schema or data changes if applied without review.

Mitigation: Review generated SQL before applying it and run Flydb validate plus dry-run migrate checks where available.

Risk: Changing an already-applied versioned migration can cause checksum validation failures or require explicit repair decisions.

Mitigation: Carry historical changes in a new versioned script and require user confirmation before any repair workflow.

Risk: Directory reorganization, path filters, and placeholder settings can change which scripts Flydb sees or how script text is interpreted.

Mitigation: Verify effective locations, filtering, version selection, and placeholder behavior before execution.

## Reference(s):

- [Flydb migration script naming and version rules](references/naming-and-versions.md)
- [Flydb script directory errors and change discipline](references/errors-and-discipline.md)
- [Flydb GitHub project](https://github.com/zzxCoding/Flydb)
- [Flydb Gitee mirror](https://gitee.com/zzhenxuan/Flydb)
- [ClawHub skill page](https://clawhub.ai/zzxcoding/skills/flydb-migration-scripts)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with SQL snippets, configuration examples, and shell command suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose SQL file changes and read-only validation commands; database write operations are out of scope.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
