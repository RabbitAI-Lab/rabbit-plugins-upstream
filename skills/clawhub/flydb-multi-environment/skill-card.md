## Description:

Organizes Flydb migration releases across multiple databases and environments, including configuration matrices, password injection, JSON/Plan approval gates, baseline handling for existing databases, and offline driver distribution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zzxcoding](https://clawhub.ai/user/zzxcoding)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release engineers use this skill to plan and document Flydb migration automation for multi-database, multi-environment deployments. It helps structure flydb.conf files, CI approval stages, baseline onboarding, secret injection, and offline driver handling while preserving human review for production writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help an agent draft CI steps for high-impact database migrations.

Mitigation: Use real approval gates, scoped migration accounts, protected secrets, and environment-specific dry-run review before production writes.

Risk: Production database credentials or migration plans could be exposed through command lines, logs, or public artifacts.

Mitigation: Inject secrets through environment variables or protected password files, separate stdout JSON from stderr logs, and store dry-run plans only in controlled artifact storage.

Risk: A dry-run plan or approval from one environment may be incorrectly reused for another environment.

Mitigation: Bind approvals to the target database, configuration, environment, Flydb version, scripts, drivers, and immutable plan artifacts; re-run and compare the plan before migration.

Risk: Long-running or interrupted migrations may leave the result uncertain.

Mitigation: Run migrations in the foreground with sufficient CI timeout, preserve exit codes, verify the database state after interruption, and avoid automatic replay when the outcome is unknown.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zzxcoding/skills/flydb-multi-environment)
- [Multi-environment reference](artifact/references/multi-environment.md)
- [Flydb project](https://github.com/zzxCoding/Flydb)
- [Flydb Gitee mirror](https://gitee.com/zzhenxuan/Flydb)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with configuration examples and inline shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CI stage outlines, file layouts, Flydb command sequences, approval-gate notes, and risk callouts.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
