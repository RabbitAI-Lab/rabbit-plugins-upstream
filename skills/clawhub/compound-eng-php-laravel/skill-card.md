## Description:

Modern PHP 8.4 and Laravel guidance for architecture, Eloquent, migrations, queues, testing, Blade, artisan, PHPStan, and framework-based PHP application work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to implement, refactor, test, and review Laravel and PHP 8.4 applications with idiomatic architecture, data access, migrations, queues, APIs, testing, and production practices. It is not intended for php-src internals, standalone PHP libraries, or general PHP language discussion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated Laravel guidance may include database migrations, delete operations, scheduled jobs, or production cache and deploy commands that can change an application when a user directs an agent to apply them.

Mitigation: Review generated code and commands before use, run static analysis and tests, and apply database or deployment changes through the project's normal controlled release process.

Risk: Examples involving queues, files, external services, and caches can introduce side effects if copied directly into a live application.

Mitigation: Use Laravel fakes, staging environments, idempotent jobs, retries, and explicit production review before enabling live side effects.

## Reference(s):

- [Laravel Ecosystem Patterns](references/laravel-ecosystem.md)
- [Testing Laravel](references/testing.md)
- [Feature Testing Patterns](references/feature-testing.md)
- [Mocking and Faking](references/mocking-and-faking.md)
- [Factory Patterns](references/factories.md)
- [Production Performance](references/production-performance.md)
- [Laravel Pitfalls - Deep Reference](references/pitfalls-deep.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with PHP and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Laravel/PHP code snippets, artisan or Composer commands, testing guidance, and production configuration recommendations.]

## Skill Version(s):

4.4.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
