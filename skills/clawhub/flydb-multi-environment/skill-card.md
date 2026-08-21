## Description:

Organizes Flydb CLI database migration automation across multiple database families and test, staging, and production environments, covering configuration matrices, external password injection, CI gate sequences, baseline adoption, driver distribution, and offline execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zzxcoding](https://clawhub.ai/user/zzxcoding)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, database engineers, and platform engineers use this skill to design Flydb migration layouts and CI release steps for multiple database families and environments. It helps keep credentials externalized, production migrations gated by review, legacy databases baselined before automation, and offline execution paths planned.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Production migration guidance can lead to database changes if applied without review.

Mitigation: Use the documented dry-run step, compare the planned migration list with the target database state, and require an explicit approval gate before running production migrate.

Risk: Database credentials can leak through committed config files, command-line flags, shell history, process lists, or CI logs.

Mitigation: Keep passwords outside version control and command arguments; use CI secrets, environment substitution, or restricted password files with dedicated migration accounts.

Risk: Legacy production databases can be incorrectly baselined if historical migrations are not reconciled first.

Mitigation: Manually reconcile applied versions, rehearse the baseline process in a test environment, and avoid automatic repair in the pipeline.

Risk: Network-restricted production runners may fail when resolving database drivers, or may mishandle vendor driver redistribution obligations.

Mitigation: Pre-provision drivers through runner images or an internal repository, enable offline mode where required, and respect vendor driver licensing.

## Reference(s):

- [Multi-environment automation reference](references/multi-environment.md)
- [Flydb project](https://github.com/zzxCoding/Flydb)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with configuration examples and bash command sequences]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
