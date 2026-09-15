## Description:

Modern PHP 8.4 and Laravel patterns: architecture, Eloquent, migrations, queues, testing. Use when working with Laravel, Eloquent, Blade, artisan, or building/testing a framework-based PHP app. Not for php-src internals, standalone PHP libraries, or general PHP language discussion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill for Laravel and framework-level PHP work, including architecture decisions, Eloquent persistence, migrations, queues, Blade, artisan workflows, PHPUnit, and PHPStan. It is scoped away from php-src internals, standalone PHP libraries, and general PHP language discussion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Suggested Laravel, PHP, artisan, composer, migration, cron, cache, or process-list commands may affect shared, production, or sensitive environments if run without review.

Mitigation: Review commands before execution, prefer scoped or non-production validation first, and apply extra care around migrations, queue workers, cache compilation, cron entries, and process inspection.

Risk: Some framework recommendations are version-sensitive across modern PHP and Laravel releases.

Mitigation: Confirm the installed PHP and Laravel versions before applying version-specific APIs, queue behavior, cache behavior, validation rules, or deployment guidance.

Risk: The skill gives implementation and review guidance that can influence security-sensitive application behavior such as authorization, serialization, logging, jobs, and data persistence.

Mitigation: Validate proposed changes through the real request, queue, migration, and test entrypoints, and keep security review focused on the affected Laravel boundary.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-php-laravel)
- [Laravel Ecosystem Patterns](references/laravel-ecosystem.md)
- [Testing Laravel (PHPUnit)](references/testing.md)
- [Feature Testing Patterns](references/feature-testing.md)
- [Mocking and Faking](references/mocking-and-faking.md)
- [Factory Patterns](references/factories.md)
- [Production Performance](references/production-performance.md)
- [Laravel Common Pitfalls](references/common-pitfalls.md)
- [Laravel Pitfalls - Deep Reference](references/pitfalls-deep.md)
- [Framework and Boundary Patterns](references/framework-patterns.md)
- [Persistence and Job Patterns](references/persistence-and-jobs.md)
- [Testing and Pitfall Checklist](references/testing-and-pitfalls.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with PHP/Laravel code snippets and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May recommend PHPStan, PHPUnit, artisan, composer, migration, queue, cache, cron, and process-list commands for review before execution.]

## Skill Version(s):

4.5.3 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
