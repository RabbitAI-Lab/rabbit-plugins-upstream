## Description:

Test skills via TDD in fresh subagents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use this skill to design fresh-instance tests, compare baseline and with-skill behavior, and document whether a skill measurably improves agent responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Test logs may include secrets, private user data, or sensitive model outputs because the skill asks users to copy full responses for comparison.

Mitigation: Redact secrets and private data before storing or sharing test logs, and keep logs in an access-controlled location.

Risk: Testing in the same conversation where a skill was authored can produce biased results.

Mitigation: Use fresh conversations for baseline, with-skill, rationalization, and regression tests.

## Reference(s):

- [Testing Patterns](modules/testing-patterns.md)
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-abstract-subagent-testing)
- [OpenClaw Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/abstract)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown guidance with examples, templates, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only guidance; no hidden execution or privileged access is identified in the security evidence.]

## Skill Version(s):

1.9.18 (source: server release metadata; artifact frontmatter lists 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
