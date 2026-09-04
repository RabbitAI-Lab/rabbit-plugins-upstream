## Description:

Turn consequential choices, uncertain claims, recurring failures, serious learning, and evidence-bearing reviews into provisional judgments, discriminating tests, and user-owned action.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sirsws](https://clawhub.ai/user/sirsws)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to structure consequential uncertain prompts into provisional judgments, failure conditions, low-cost tests, and user-owned next actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Implicit activation can change how an agent answers consequential uncertain prompts.

Mitigation: Install only when this decision-support behavior is desired, and review outputs before acting on high-impact recommendations.

Risk: Decision-support guidance may be incorrect, over-applied, or treated as replacing the user's judgment.

Mitigation: Keep the user as the decision owner, require evidence and failure conditions, and use the proposed tests as reviewable advice rather than automatic action.

Risk: README installation examples use npx to invoke an external installer under user control.

Mitigation: Run installer commands only in trusted environments after reviewing the package source and requested changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sirsws/skills/judgment-loop)
- [Decision Mode](references/decision.md)
- [Research Mode](references/research.md)
- [Learning Mode](references/learning.md)
- [Review Mode](references/review.md)
- [Evaluation Protocol](evals/trigger-cases.md)
- [Examples](examples/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responds in the user's language and scales depth to consequence.]

## Skill Version(s):

1.1.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
