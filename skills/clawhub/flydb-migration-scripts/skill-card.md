## Description:

Helps developers create, modify, and organize Flydb migration SQL scripts, including V/R/U naming, version strategy, directory layout, placeholders, checksum discipline, and common Flydb migration-script errors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zzxcoding](https://clawhub.ai/user/zzxcoding)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database engineers use this skill when adding, reorganizing, or reviewing Flydb migration scripts in db/migration or configured locations. It helps follow project naming and versioning conventions, avoid rewriting already-applied migrations, and choose safe validation or dry-run checks before database changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated or edited SQL migration scripts may be incorrect for the target schema or database dialect.

Mitigation: Review generated SQL before applying it, then run Flydb validate and a dry-run migration before executing write operations.

Risk: Rewriting an already-applied versioned migration can cause checksum mismatches and repair-sensitive history changes.

Mitigation: Carry changes in a new versioned migration unless the user explicitly accepts the validation and repair impact.

Risk: Changing migration locations or reorganizing directories can make previously applied scripts appear missing.

Mitigation: Keep old and new locations available during transition and verify the migration set before applying changes.

## Reference(s):

- [Flydb migration naming and version rules](artifact/references/naming-and-versions.md)
- [Flydb script directory errors and discipline](artifact/references/errors-and-discipline.md)
- [Flydb project](https://github.com/zzxCoding/Flydb)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with SQL, configuration, and shell command examples when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Does not execute database write commands; advises validation and dry-run checks before applying migrations.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
