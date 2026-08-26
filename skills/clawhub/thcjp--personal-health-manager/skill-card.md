## Description:

健康管理器 helps users track personal health data, manage medications, analyze symptoms, and receive general wellness guidance in Chinese.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill for personal health tracking, medication organization, symptom triage support, and wellness guidance. It should be treated as informational support, not a substitute for clinician review or emergency care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask an agent to handle sensitive health and medication details without clear privacy, retention, deletion, or clinician-review boundaries.

Mitigation: Review privacy handling before installation, avoid entering unnecessary identifiers, and require clinician review for medical decisions.

Risk: The skill declares broad read, write, and execute capabilities beyond the health use case.

Mitigation: Restrict tool permissions where possible and review proposed file or command actions before execution.

Risk: The security summary flags mixed unrelated automation and command-execution claims in a health assistant.

Mitigation: Test the skill in a controlled workspace and verify that behavior is limited to the intended health-management workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/personal-health-manager)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Conversational guidance with optional JSON, text, or Markdown responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May involve sensitive health and medication details; outputs should remain informational and be reviewed for medical appropriateness.]

## Skill Version(s):

1.0.1 (source: server release evidence; artifact frontmatter lists 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
