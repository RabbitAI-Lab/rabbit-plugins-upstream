## Description:

Provides framework-agnostic guidance for designing and reviewing agent interfaces, including tool calls, approvals, status, progress, accessibility, disclosure, and auditability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arunk3](https://clawhub.ai/user/arunk3)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and product teams use this skill to design or review interfaces where AI agents communicate, call tools, request approvals, show progress, or change user data. It provides practical guidance and a checklist for clear, accessible, and accountable agent screens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Model-generated text in an agent interface could be mistaken for trusted markup or executable content.

Mitigation: Render model output as text, keep it distinct from app-provided evidence, and do not execute code or links supplied by the model.

## Reference(s):

- [Candor Agent UI on ClawHub](https://clawhub.ai/arunk3/skills/candor-agent-ui)
- [Approvals, blast radius and undo](artifact/references/approvals.md)
- [AI disclosure and accessibility](artifact/references/disclosure-and-accessibility.md)
- [The nine honesty rules](artifact/references/honesty-rules.md)
- [Progress and recovery](artifact/references/progress.md)
- [Review checklist](artifact/references/review-checklist.md)
- [Status vocabulary and tool-call states](artifact/references/status-and-states.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Review checklists]

**Output Format:** [Markdown guidance and checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Framework- and design-system-agnostic; includes examples and review criteria.]

## Skill Version(s):

3.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
