## Description:

Provides modern PHP 8.4 and Laravel patterns for architecture, Eloquent, migrations, queues, and testing, for framework-based PHP work with Laravel, Eloquent, Blade, or artisan.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill for framework-level PHP work with Laravel, including application architecture, Eloquent and migrations, queues, Blade, and testing. It is not intended for PHP internals, standalone PHP libraries, or general PHP language questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The queue verification workflow can process a real queued job if it is pointed at a shared or production queue.

Mitigation: Use a dedicated test connection and queue containing only the intended test job, with disposable data and sandboxed services. Require explicit approval before processing shared or production queues.

Risk: Adopting the examples without checking the environment may affect session retention or send data to the configured S3 destination.

Mitigation: Check session retention and the configured S3 destination before adopting those examples; review the application configuration and dependencies, which were not supplied with this release.

## Reference(s):

- [Framework patterns](artifact/references/framework-patterns.md)
- [Persistence and jobs](artifact/references/persistence-and-jobs.md)
- [Testing and pitfalls](artifact/references/testing-and-pitfalls.md)
- [Common pitfalls](artifact/references/common-pitfalls.md)
- [Laravel ecosystem](artifact/references/laravel-ecosystem.md)
- [Testing](artifact/references/testing.md)
- [Feature testing](artifact/references/feature-testing.md)
- [Mocking and faking](artifact/references/mocking-and-faking.md)
- [Factories](artifact/references/factories.md)
- [Production performance](artifact/references/production-performance.md)
- [Deep pitfalls](artifact/references/pitfalls-deep.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with PHP examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

5.1.4 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
