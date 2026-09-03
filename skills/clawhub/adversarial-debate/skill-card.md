## Description:

Adversarial Debate guides an agent through a cross-vendor adversarial review of a plan, proposal, or design, using evidence-anchored objections, tagged rulings, consensus categories, and mandatory fresh-judge checks when outcomes look too clean.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical reviewers use this skill when they explicitly want a model from another vendor to challenge a plan, proposal, design, or prior review output before committing to action. It helps separate verified consensus, unresolved questions, and still-disputed objections while requiring user confirmation before any durable record is written.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The prepared debate brief may be sent to an external model provider through the configured CLI or handoff backend.

Mitigation: Redact secrets, credentials, customer data, regulated data, and proprietary material before running the debate, and confirm the selected backend first.

Risk: Cross-vendor debate output can appear authoritative even when items are unresolved, disputed, or not verified.

Mitigation: Keep unresolved and still-disputed items separate from verified consensus, and require explicit user confirmation before recording any outcome as a decision, plan, or ticket.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xiaoba-dev/skills/adversarial-debate)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, analysis]

**Output Format:** [Markdown with structured debate sections and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces candidate review findings and handoff recommendations; verified consensus still requires explicit user confirmation before durable records are written.]

## Skill Version(s):

2.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
