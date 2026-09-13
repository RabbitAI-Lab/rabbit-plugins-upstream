## Description:

Use when raising code quality or test coverage across a .NET, Java, or Python repository.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to make broad repository quality interventions across .NET, Java, or Python projects, including static-analysis cleanup, test coverage improvements, dependency remediation, documentation updates, and delivery summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is designed to make broad quality, test, dependency, README, CHANGELOG, and commit changes across a repository.

Mitigation: Use a disposable branch, review the complete diff carefully, and run the project's normal build, test, and security checks before merging.

Risk: Optional package or tool installation may occur while preparing coverage and static-analysis tooling.

Mitigation: Run installs in a virtual environment or otherwise pinned and sandboxed tool environment.

## Reference(s):

- [.NET Test Coverage](artifact/references/coverage-dotnet.md)
- [Java Test Coverage](artifact/references/coverage-java.md)
- [Python Test Coverage](artifact/references/coverage-python.md)
- [Coverage Dispatcher Script](artifact/references/run-coverage.sh)
- [ClawHub Skill Page](https://clawhub.ai/afonsoft/skills/quality-test-implementation)
- [Source Repository Metadata URL](https://github.com/afonsoft/skills)
- [Keep a Changelog](https://keepachangelog.com/)
- [Semantic Versioning](https://semver.org/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline code, shell commands, configuration snippets, repository edits, and a detailed technical summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce broad repository changes, coverage artifacts, README and CHANGELOG updates, and a conventional commit for user review.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata); artifact metadata.version is 1.1.1

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
