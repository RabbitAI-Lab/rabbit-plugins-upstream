## Description:

Helps developers assess PR and MR review feedback, verify suggested changes, and respond to or implement justified fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to triage incoming code review comments, substantiate disagreements, and make verified fixes within their authorized scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unverified review suggestions could lead to incorrect code changes.

Mitigation: Check each suggestion against the code and tests before making a scoped fix; verify each change individually.

Risk: Code edits or public PR replies could exceed the user's authorization.

Mitigation: Keep normal approval boundaries for edits, pushes, and public comments; draft replies for approval before posting.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/iliaal/skills/compound-eng-receiving-code-review)
- [Feedback triage](references/feedback-triage.md)
- [Evidence and disagreement](references/evidence-and-disagreement.md)
- [Fix and handoff](references/fix-and-handoff.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code]

**Output Format:** [Markdown review dispositions and optional code changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes supporting evidence and verification results; replies are drafted unless posting is authorized.]

## Skill Version(s):

5.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
