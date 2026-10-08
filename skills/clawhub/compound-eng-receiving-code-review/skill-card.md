## Description:

Helps developers assess code review feedback against the codebase before responding or making authorized changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to verify and triage PR or merge-request review comments, respond with evidence, and implement verified fixes only within authorized scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Review suggestions could lead to incorrect or out-of-scope code changes.

Mitigation: Verify feedback against code and tests; review proposed edits and restrict changes to authorized scope.

Risk: Posting PR replies or resolving threads can affect external discussions.

Mitigation: Require explicit approval before posting replies or resolving threads.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/iliaal/skills/compound-eng-receiving-code-review)
- [Feedback triage](references/feedback-triage.md)
- [Evidence and disagreement](references/evidence-and-disagreement.md)
- [Fix and handoff](references/fix-and-handoff.md)
- [Headless mode](references/headless-mode.md)
- [Review modes](references/review-modes.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code]

**Output Format:** [Markdown findings and responses; code changes when authorized]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Evidence-backed dispositions and explicit uncertainty where verification is incomplete.]

## Skill Version(s):

5.0.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
