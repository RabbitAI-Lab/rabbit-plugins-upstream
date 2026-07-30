## Description: <br>
Modern PHP 8.4 and Laravel patterns: architecture, Eloquent, migrations, queues, testing; use when working with Laravel, Eloquent, Blade, artisan, or building/testing a framework-based PHP app. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill for Laravel application work, including architecture decisions, Eloquent modeling, migrations, queues, testing, and production hardening. It is aimed at framework-based PHP apps rather than PHP internals or standalone library design. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may guide an agent to propose Laravel framework commands, migrations, queues, scheduled jobs, tests, and configuration changes that affect application behavior. <br>
Mitigation: Review generated application changes before applying them, run the project's PHPStan and PHPUnit suites, and stage production-impacting changes before release. <br>
Risk: Framework guidance can be misapplied outside the skill's intended Laravel and framework-based PHP scope. <br>
Mitigation: Use the skill for Laravel, Eloquent, Blade, artisan, PHPUnit, PHPStan, and related framework work; route PHP internals, standalone libraries, and unrelated stacks to more specific guidance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-php-laravel) <br>
- [Laravel ecosystem patterns](references/laravel-ecosystem.md) <br>
- [Testing Laravel](references/testing.md) <br>
- [Feature testing patterns](references/feature-testing.md) <br>
- [Mocking and faking](references/mocking-and-faking.md) <br>
- [Factory patterns](references/factories.md) <br>
- [Production performance](references/production-performance.md) <br>
- [Laravel pitfalls deep reference](references/pitfalls-deep.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with PHP, Laravel, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Non-executable guidance for agent-generated application changes; review and test before applying to production projects.] <br>

## Skill Version(s): <br>
4.3.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
