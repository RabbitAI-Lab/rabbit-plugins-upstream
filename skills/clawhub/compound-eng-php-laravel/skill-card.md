## Description:

Modern PHP 8.4 and Laravel patterns for architecture, Eloquent, migrations, queues, testing, Blade, artisan, and framework-based PHP application work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill for Laravel and framework-level PHP implementation guidance, including application architecture, Eloquent modeling, migrations, queues, testing, performance, and production readiness. It is not intended for PHP internals, standalone PHP libraries, or general language discussion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated Laravel migrations, database operations, queue jobs, scheduled tasks, storage operations, or deploy cache commands can change application state.

Mitigation: Review generated changes before applying them, run them first in a controlled environment, and verify database, storage, queue, and cache effects before production use.

Risk: Framework guidance may need adjustment for the installed Laravel, PHP, PHPUnit, PHPStan, database, queue, and infrastructure versions.

Mitigation: Confirm version-specific APIs and configuration options against the target project before merging generated code or commands.

## Reference(s):

- [Laravel Ecosystem Patterns](artifact/references/laravel-ecosystem.md)
- [Testing Laravel (PHPUnit)](artifact/references/testing.md)
- [Feature Testing Patterns](artifact/references/feature-testing.md)
- [Mocking and Faking](artifact/references/mocking-and-faking.md)
- [Factory Patterns](artifact/references/factories.md)
- [Production Performance - OPcache, JIT, Preloading, Laravel caches](artifact/references/production-performance.md)
- [Laravel Pitfalls - Deep Reference](artifact/references/pitfalls-deep.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with PHP, Laravel, PHPUnit, configuration, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Focuses on framework-level PHP and Laravel work; excludes php-src internals, standalone PHP libraries, and general PHP language discussion.]

## Skill Version(s):

4.4.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
