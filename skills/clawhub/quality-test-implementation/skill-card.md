## Description:

Use when raising code quality or test coverage across a .NET, Java, or Python repository.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use this skill to stabilize .NET, Java, or Python repositories by reducing static-analysis findings, fixing security issues, improving architecture, and increasing test coverage before release or handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make broad local changes to a target repository, including code, tests, documentation, and changelog files.

Mitigation: Run it in a disposable clone or dedicated branch, then review generated files and commits before merging or publishing.

Risk: Dependency updates and tool installation commands may change build behavior or introduce supply-chain exposure.

Mitigation: Review dependency changes before committing and prefer pinned, project-local tool installs over global unpinned installs.

Risk: Automated quality, architecture, and CVE fixes can unintentionally alter application behavior.

Mitigation: Run the full project test suite, coverage checks, and security scanners after changes, and require human code review before pull request creation.

## Reference(s):

- [.NET Test Coverage](references/coverage-dotnet.md)
- [Java Test Coverage](references/coverage-java.md)
- [Python Test Coverage](references/coverage-python.md)
- [Coverage Dispatcher](references/run-coverage.sh)
- [Publisher Metadata URL](https://github.com/afonsoft/skills)
- [Keep a Changelog](https://keepachangelog.com/)
- [Semantic Versioning](https://semver.org/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May prepare repository file changes, local commits, coverage reports, README and CHANGELOG updates, and a detailed technical summary for manual pull request creation.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
