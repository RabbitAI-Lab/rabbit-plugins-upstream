## Description:

Production-ready Go testing guidance for writing, reviewing, auditing, and debugging table-driven tests, testify suites and mocks, parallel tests, fuzzing, coverage, integration tests, and flaky or slow test behavior.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create and evaluate Go test suites that emphasize observable behavior, idiomatic structure, useful assertions, isolation, race and leak detection, and maintainable CI-ready coverage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated or modified tests may assert incorrect behavior or mask defects.

Mitigation: Review proposed test changes and run the relevant Go test suite before committing.

Risk: The skill may edit repository files and run Go, gotests, golangci-lint, and git commands in the workspace.

Mitigation: Use it only in projects where those file edits and commands are acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/samber/skills/golang-testing)
- [Project homepage](https://github.com/samber/cc-skills-golang)
- [HTTP Handler Testing](references/http-testing.md)
- [Integration Testing](references/integration-testing.md)
- [Mocking and Test Fixtures](references/mocking.md)
- [Test Helpers](references/helpers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Go code snippets, shell commands, configuration examples, review findings, and proposed test changes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May recommend or make repository file edits and test command runs; review generated tests before committing.]

## Skill Version(s):

1.3.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
