## Description:

Modern PHP 8.4 and Laravel guidance for framework-level development, including architecture, Eloquent, migrations, queues, testing, Blade, artisan, PHPUnit, and PHPStan.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill for Laravel and framework-level PHP application work, including controllers, Eloquent data access, migrations, queues, testing, and production configuration guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Guidance applied to migrations, backfills, or storage cleanup can affect production data.

Mitigation: Review generated changes before execution, require backups or rollback plans for data-changing work, and test migrations or cleanup actions in a non-production environment first.

Risk: Guidance applied to queues, scheduled tasks, deploy caches, or runtime configuration can affect application availability and behavior.

Mitigation: Review operational changes with the deployment owner, validate queue and scheduler behavior in staging, and confirm deploy/cache commands match the target Laravel environment.

## Reference(s):

- [Factory Patterns](references/factories.md)
- [Feature Testing Patterns](references/feature-testing.md)
- [Laravel Ecosystem Patterns](references/laravel-ecosystem.md)
- [Mocking and Faking](references/mocking-and-faking.md)
- [Laravel Pitfalls: Deep Reference](references/pitfalls-deep.md)
- [Production Performance: OPcache, JIT, Preloading, Laravel caches](references/production-performance.md)
- [Testing Laravel (PHPUnit)](references/testing.md)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration, markdown]

**Output Format:** [Markdown prose with PHP code examples, shell commands, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent output should be reviewed before applying changes to application code, migrations, queues, storage cleanup, or deployment settings.]

## Skill Version(s):

4.4.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
