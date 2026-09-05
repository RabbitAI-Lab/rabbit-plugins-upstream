## Description:

Part of the Overpowered skill suite, this skill helps design or review where human approval, judgment, or accountability must remain in an automated workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[raguets](https://clawhub.ai/user/raguets)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, automation designers, and process owners use this skill to decide which workflow steps need human approval, judgment, or accountability and which manual steps can be automated when controls are sufficient.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat gate-design guidance as authorization for legal, financial, safety, or policy decisions.

Mitigation: Apply the organization's current authority, legal, financial, and safety policies before changing or removing human approval steps.

Risk: Automation may remove a human review step that still carries accountability, material ambiguity, or unacceptable risk.

Mitigation: Retain gates with explicit triggers, owners, evidence, allowed outcomes, timeout paths, and downstream effects when policy or risk requires human involvement.

## Reference(s):

- [Overpowered suite](https://github.com/raguets/overpowered)
- [ClawHub skill page](https://clawhub.ai/raguets/skills/human-gates)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Text]

**Output Format:** [Markdown or plain text gate-design table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Expected structure: Gate | Trigger | Why human | Required evidence | Owner | Outcomes]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
