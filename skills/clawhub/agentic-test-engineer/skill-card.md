## Description:

AI-powered autonomous test generation and self-healing test maintenance. Generates unit/integration/E2E tests, detects flaky tests, auto-fixes broken selectors, and maintains test coverage. Built for QA engineers and developers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gechengling](https://clawhub.ai/user/gechengling)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers and developers use this skill to generate unit, integration, API, and end-to-end tests, diagnose flaky failures, repair broken UI selectors, and prioritize coverage gaps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Effective use may expose project code, test logs, DOM snapshots, screenshots, and coverage files to the agent or connected tools.

Mitigation: Review data-sharing boundaries before use and avoid providing regulated or sensitive artifacts unless the execution environment is approved for them.

Risk: Generated tests or self-healed selectors can encode incorrect behavior or target the wrong UI element, especially in legal, financial, or production workflows.

Mitigation: Keep human review in the loop before merging generated tests or selector changes, and require stable selector contracts for high-impact workflows.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/gechengling/skills/agentic-test-engineer)

## Skill Output:

**Output Type(s):** [Analysis, Code, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with code blocks and structured recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include test cases, selector recommendations, root-cause reports, coverage triage, and configuration snippets for the user's own environment.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
