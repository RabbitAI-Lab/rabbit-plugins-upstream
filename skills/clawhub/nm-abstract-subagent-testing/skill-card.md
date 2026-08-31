## Description:

Test skills via TDD in fresh subagents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use this skill to evaluate agent skills in fresh conversations, compare baseline and with-skill behavior, and check for priming bias or rationalization failure modes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Testing prompts and copied responses may include secrets, proprietary data, or private production details in test logs.

Mitigation: Use sanitized prompts and redact sensitive values before recording baseline, with-skill, or rationalization test results.

Risk: Broad testing-related triggers may activate the skill for requests that only need ordinary troubleshooting or validation.

Mitigation: Confirm that the user is evaluating a skill or agent behavior before applying the full TDD testing methodology.

## Reference(s):

- [Testing Patterns](modules/testing-patterns.md)
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-subagent-testing)
- [Publisher profile](https://clawhub.ai/user/athola)
- [Project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/abstract)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown guidance with templates and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only output for planning, recording, and comparing skill tests.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
