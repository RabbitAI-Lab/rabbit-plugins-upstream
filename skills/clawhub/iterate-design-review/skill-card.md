## Description:

Refine architecture designs or execution plans through a context-grounded independent review loop.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xukp20](https://clawhub.ai/user/xukp20)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to refine architecture designs or execution plans before approval or implementation. It helps converge on scope, layering, data ownership, interfaces, completeness, and simplicity through independent review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may cause an agent to read project context and update a design draft during design refinement.

Mitigation: Use it only on repositories where that review and draft-update activity is appropriate, and review proposed design changes before implementation.

Risk: Independent review findings may introduce incorrect or misleading guidance if accepted without checking the supporting evidence.

Mitigation: Apply the skill's materiality and plausibility gates, require evidence for findings, and keep the primary agent responsible for final decisions.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/xukp20/codex-design-review-loop/tree/main/skills/iterate-design-review)
- [ClawHub skill page](https://clawhub.ai/xukp20/skills/iterate-design-review)
- [Publisher profile](https://clawhub.ai/user/xukp20)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text design review guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include prioritized findings, evidence, impact, correction proposals, residual uncertainty, and updates to a canonical design or plan.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
