## Description:

Safely migrates OpenClaw memory from LanceDB Pro, official LanceDB list captures, QMD, or Markdown into memory-core. Use when an owner asks to migrate, audit, deduplicate, benchmark, cut over, or roll back an OpenClaw memory backend.

This skill is ready for commercial/non-commercial use.

## Publisher:

[airbing11](https://clawhub.ai/user/airbing11)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw operators use the skill to migrate memory from supported backends into memory-core, audit and stage the resulting records, and plan a reviewed cutover or rollback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan is incomplete and flagged possible state-changing commands during a documented dry run, so it does not establish safety.

Mitigation: Consider avoiding installation until the dry-run behavior is clarified and the partially inspected code is reviewed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/airbing11/skills/memory-core-migrator)
- [Compatibility guide](references/compatibility.md)
- [Operations guide](references/operations.md)
- [FAQ](docs/faq.md)
- [Operator recipes](docs/recipes.md)
- [Benchmark methodology](docs/benchmark-methodology.md)
- [Compatibility matrix](docs/compatibility-matrix-2026-11-11.md)

## Skill Output:

**Output Type(s):** [Files, JSON, Markdown, Shell commands, Guidance]

**Output Format:** [JSON reports and records, staged Markdown files, and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local migration outputs are reviewable; cutover and rollback steps require operator review.]

## Skill Version(s):

0.1.0-rc.3 (source: package.json, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
