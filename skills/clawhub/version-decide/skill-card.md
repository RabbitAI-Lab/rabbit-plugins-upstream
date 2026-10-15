## Description:

Recommends one next SemVer version for an upcoming release based on the scope of code changes, with reasons tied to the relevant standards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elisabeth15501](https://clawhub.ai/user/elisabeth15501)

### License/Terms of Use:

MIT

## Use Case:

Developers deciding the version number for an upcoming release use this skill to assess change compatibility, calculate a SemVer bump, and explain the recommendation. It asks for clarification when the current version or breaking-change status is uncertain.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An incorrect compatibility assessment could lead to an unsuitable version recommendation.

Mitigation: Confirm the current released version, public API boundary, and any breaking changes before acting on the recommendation.

Risk: Maintainer documentation mentions publishing and repository release actions that are outside normal version advice.

Mitigation: Treat those steps as documentation; perform release-management actions only when explicitly requested.

## Reference(s):

- [Version Decider on ClawHub](https://clawhub.ai/elisabeth15501/skills/version-decide)
- [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html)
- [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/)
- [Python versioning (PEP 440)](https://peps.python.org/pep-0440/)
- [Cargo version requirements](https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html)
- [Go module version numbering](https://go.dev/doc/modules/version-numbers)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Markdown with a single version recommendation, rationale, questions, and a suggested command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [English or Chinese responses; includes relevant standard clauses and does not change project files.]

## Skill Version(s):

1.0.0 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
