## Description:

Counterfactual Decision evaluates factual and counterfactual outcomes for explicit weighted linear threshold decision models, reporting decision flips and marginal variable contributions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and decision analysts use this skill to run local what-if checks against a transparent weighted scoring model and understand whether a proposed intervention changes the final decision. It is useful for traceable decision reversal analysis and variable attribution when the model, state, and intervention are provided as JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can keep local usage history and preferences in learned_patterns.json.

Mitigation: Use the calculator directly for sensitive decision inputs and run the learning module only when retaining local history is intentional.

Risk: The artifact includes self-improvement behavior that is broader than the counterfactual-analysis purpose.

Mitigation: Review any learned-pattern updates before deployment and keep generated learning records out of sensitive or shared releases unless they are explicitly intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/counterfactual-decision)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON counterfactual results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with no declared external dependencies; outputs factual and counterfactual scores, flip status, margin, and per-variable contributions.]

## Skill Version(s):

1.0.0 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
