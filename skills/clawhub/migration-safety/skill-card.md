## Description:

Reviews schema migrations for production safety under live traffic, focusing on destructive changes, lock-taking DDL, deploy and rollback ordering, batched backfills, and explicit rollback paths without executing migrations or database commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review database schema migrations before release, especially when live production traffic, old and new application versions, large tables, and rollback safety matter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Static migration review can be misleading when database engine, engine version, table size, traffic level, or deployment order is missing.

Mitigation: State assumptions explicitly, ask for missing context when needed, and downgrade findings that depend on unknown production conditions.

Risk: Fix suggestions for schema changes can affect production data if applied without review.

Mitigation: Keep default behavior read-only, require explicit separate approval before drafting changes, and never execute migrations, DDL, or SQL.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dennisrongo/skills/migration-safety)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown review report with ranked findings, assumptions, file-line references, failure scenarios, and safer alternatives.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only review output; the skill does not execute migrations, DDL, or SQL.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
