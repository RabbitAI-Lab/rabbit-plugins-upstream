## Description:

Modern PHP 8.4 and Laravel patterns: architecture, Eloquent, migrations, queues, testing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill for framework-level PHP and Laravel work, including architecture, Eloquent, migrations, queues, and testing. It is intended for Laravel application development rather than PHP internals or general PHP discussion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queue-worker examples may act on shared or production jobs when run against a live queue.

Mitigation: Run queue-worker commands only against an isolated test queue.

Risk: Session-deletion schedules may remove data according to their configured criteria and retention period.

Mitigation: Review the schedule's effects and retention policy before enabling it.

Risk: Document uploads may be stored in an unintended location or under unsuitable access and retention settings.

Mitigation: Confirm the upload destination and its access and retention settings before using upload flows.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/iliaal/skills/compound-eng-php-laravel)
- [Framework and boundary patterns](references/framework-patterns.md)
- [Persistence and jobs](references/persistence-and-jobs.md)
- [Testing and pitfalls](references/testing-and-pitfalls.md)
- [Laravel ecosystem patterns](references/laravel-ecosystem.md)
- [PHPUnit testing](references/testing.md)
- [Feature testing patterns](references/feature-testing.md)
- [Mocking and faking](references/mocking-and-faking.md)
- [Factory patterns](references/factories.md)
- [Production performance](references/production-performance.md)
- [Common pitfalls](references/common-pitfalls.md)
- [Deep Laravel pitfalls](references/pitfalls-deep.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Task-specific guidance routed to the relevant reference material]

## Skill Version(s):

5.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
