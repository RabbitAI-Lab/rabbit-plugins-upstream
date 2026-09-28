## Description:

Helps agents assess PR and MR review feedback against code and evidence before accepting, challenging, or implementing suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to triage review comments, verify claims, explain disagreements, and implement verified changes within authorized scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unverified reviewer suggestions could result in incorrect code changes.

Mitigation: Verify each claim against the current code and test each authorized fix before reporting it resolved.

Risk: Review replies or thread resolution could be published without approval.

Mitigation: Draft replies first and obtain authorization before posting or resolving threads.

## Reference(s):

- [Skill release](https://clawhub.ai/iliaal/skills/compound-eng-receiving-code-review)
- [Feedback triage](references/feedback-triage.md)
- [Evidence and disagreement](references/evidence-and-disagreement.md)
- [Fix and handoff](references/fix-and-handoff.md)
- [Headless mode](references/headless-mode.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Code, Markdown]

**Output Format:** [Markdown findings and replies, with code changes when authorized]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return structured triage in headless mode; posting replies and resolving threads require authorization.]

## Skill Version(s):

5.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
