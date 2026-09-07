## Description:

Modern PHP 8.4 and Laravel guidance for architecture, Eloquent, migrations, queues, testing, and framework-based PHP application work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill for Laravel and framework-level PHP implementation, review, testing, and production-readiness guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may suggest migrations, scheduled tasks, queue jobs, deploy commands, or storage changes that can affect live Laravel applications.

Mitigation: Review generated changes before applying them, especially database and storage changes, and validate them with Laravel tests and static analysis.

Risk: Generated shell or artisan commands may have environment-specific effects.

Mitigation: Treat commands as proposed steps and run them only in the intended environment after confirming configuration, data, and rollback expectations.

## Reference(s):

- [Laravel Ecosystem Patterns](references/laravel-ecosystem.md)
- [Testing Laravel (PHPUnit)](references/testing.md)
- [Feature Testing Patterns](references/feature-testing.md)
- [Mocking and Faking](references/mocking-and-faking.md)
- [Factory Patterns](references/factories.md)
- [Production Performance](references/production-performance.md)
- [Laravel Pitfalls - Deep Reference](references/pitfalls-deep.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with code snippets and shell commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces advisory Laravel/PHP implementation guidance; commands and code should be reviewed before use.]

## Skill Version(s):

4.5.1 (source: server release evidence and user changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
