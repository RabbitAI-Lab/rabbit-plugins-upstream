## Description:

Helps agents perform whole-repository quality interventions in .NET, Java, and Python projects by reducing static-analysis warnings, addressing CVEs, improving architecture, and raising test coverage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill when a repository needs a broad quality push before release or handoff. It guides an agent through build stabilization, static-analysis remediation, vulnerability cleanup, architecture improvements, coverage generation, documentation updates, and commit preparation without opening a pull request automatically.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make broad source, dependency, documentation, and commit-preparation changes across an entire repository.

Mitigation: Run it on a clean branch or disposable clone, review the diff carefully, and keep pull request creation under user control.

Risk: Quality and coverage commands may install or execute project tooling and dependency checks.

Mitigation: Review proposed tool and dependency installs before execution, especially for repositories or package sources you do not fully trust.

Risk: Automated fixes for warnings, CVEs, and architecture issues can change behavior if applied too broadly.

Mitigation: Require the existing test suite, new coverage report, and generated technical summary to be reviewed before merging.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/quality-test-implementation)
- [Source collection](https://github.com/afonsoft/skills)
- [.NET Test Coverage](references/coverage-dotnet.md)
- [Java Test Coverage](references/coverage-java.md)
- [Python Test Coverage](references/coverage-python.md)
- [Coverage Dispatcher](references/run-coverage.sh)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline commands, code/configuration edits, coverage reports, README and changelog updates, commit preparation, and a technical summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Does not automatically open a pull request.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
