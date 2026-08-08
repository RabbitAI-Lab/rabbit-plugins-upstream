## Description:

When a fault is localized and the proximate cause is known but the systemic root is not, chain evidence-linked whys with a counterfactual stop and a countermeasure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tjboudreaux](https://clawhub.ai/user/tjboudreaux)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and incident responders use this skill after a fault has been localized to build an evidence-linked causal chain, identify systemic roots, and define recurrence-preventing countermeasures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Root-cause conclusions can be misleading when the provided incident evidence is incomplete or speculative.

Mitigation: Require each why step to cite concrete evidence, rule out alternatives, and stop when evidence is missing.

Risk: Incident materials may contain sensitive logs, code, configuration, or witness information.

Mitigation: Provide only evidence relevant to the incident and redact unnecessary sensitive details before analysis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tjboudreaux/skills/thinking-five-whys-plus)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured Markdown-style root-cause analysis with evidence, causal set checks, roots, countermeasures, and verification steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No tool calls or direct system actions; output quality depends on user-provided incident evidence.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
