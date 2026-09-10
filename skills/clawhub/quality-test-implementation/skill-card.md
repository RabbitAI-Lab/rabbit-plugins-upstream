## Description:

Improves code quality, reduces technical debt, raises test coverage, fixes static-analysis warnings, remediates security CVEs, and applies SOLID, DDD, and Clean Architecture practices in .NET, Java, and Python repositories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill for whole-repository quality interventions in .NET, Java, and Python projects. It guides build stabilization, static-analysis remediation, test coverage improvement, CVE cleanup, architecture-focused refactoring, documentation updates, changelog updates, and a final technical summary without automatically opening a pull request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is designed for broad repository changes, including code quality, tests, dependencies, documentation, changelog updates, and commits.

Mitigation: Use it only when a whole-repository quality intervention is intended, review proposed diffs before merging, and keep pull request creation under user control.

Risk: Coverage and test commands can execute build or test code from the target repository.

Mitigation: Run the workflow in a sandbox or container without host credentials for repositories that are not fully trusted.

Risk: Tooling and dependency remediation can vary across .NET, Java, and Python project setups.

Mitigation: Prefer pinned tool versions and project-local or disposable tool environments where practical.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/quality-test-implementation)
- [Source repository link from metadata](https://github.com/afonsoft/skills)
- [.NET coverage guide](references/coverage-dotnet.md)
- [Java coverage guide](references/coverage-java.md)
- [Python coverage guide](references/coverage-python.md)
- [Coverage command dispatcher](references/run-coverage.sh)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline command examples, code/configuration changes, documentation updates, and a technical summary.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow may prepare commits and reports, but it does not automatically open a pull request.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
