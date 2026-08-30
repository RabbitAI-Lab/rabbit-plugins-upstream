## Description:

Session retrospective and skill audit for reviewing lessons learned, session effectiveness, and what went well or wrong.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to run structured retrospectives, identify actionable improvements, audit invoked skills, and decide which lessons should be preserved for future sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Approved retrospectives can persist session lessons or explicit remember: items into project memory, which could preserve sensitive data or temporary preferences.

Mitigation: Avoid approving secrets, private customer details, personal data, or short-lived preferences for persistence.

Risk: Skill audit diffs could introduce incorrect or misleading guidance into future skill behavior.

Mitigation: Review proposed skill diffs and scan the skill before applying or releasing changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-reflect)
- [SPEC.md](artifact/SPEC.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, code, shell commands, configuration]

**Output Format:** [Markdown guidance with proposed diffs, numbered improvement lists, and optional commands or configuration paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose persistent memory updates only after user approval.]

## Skill Version(s):

4.5.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
