## Description:

Routes complex work requests to the right WorkFn skill or skill sequence, preserving evidence, required inputs, handoff fields, stop conditions, and next actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zaynpeng](https://clawhub.ai/user/zaynpeng)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, operators, and developers use this skill to decide whether a single skill is enough, when a staged skill chain is needed, what evidence and parameters should pass between steps, and when to stop for missing or conflicting information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A downstream skill recommended by this router may perform public research, customer follow-up, account monitoring, or business-data analysis with its own risks.

Mitigation: Review the downstream skill and its security posture before use, especially when the routed task touches external communication or business data.

Risk: Incomplete or conflicting task inputs can lead to an unsuitable skill chain or premature continuation.

Mitigation: Use the documented parameter status check and stop conditions; pause when the user problem, target outcome, subject identity, jurisdiction, time range, or required evidence is unclear.

Risk: Internal business strategy could be mixed into customer-facing replies if handoffs are not separated.

Mitigation: Keep internal strategy labels separate from external expression fields, and pass only confirmed facts, communication goals, boundaries, and allowed relationship-preserving openings to reply-generation skills.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-route)
- [README](artifact/README.md)
- [Changelog](artifact/changelog.md)
- [Examples](artifact/examples.md)
- [Tests](artifact/tests.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown tables and concise routing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes parameter status, problem type, single-skill or multi-skill recommendation, ordered skill chain, handoff notes, stop conditions, and final output skill.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact documentation lists internal rule version 0.1.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
