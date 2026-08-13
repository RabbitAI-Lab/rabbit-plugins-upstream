## Description:

FDE Engagement Charter turns a validated customer problem-discovery package into a POC engagement charter covering outcomes, proof criteria, scope, commitments, timeline, and governance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xukun0821](https://clawhub.ai/user/xukun0821)

### License/Terms of Use:

MIT-0

## Use Case:

Customer-facing delivery teams and field engineers use this skill to convert a validated discovery package into a bounded POC charter with success criteria, governance, scope controls, customer commitments, and decision gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated charters may describe customer data, access, commitments, and POC decisions without creating binding agreement by themselves.

Mitigation: Review generated charters with accountable business, technical, and risk owners before treating them as binding.

Risk: A structurally complete charter can still be misleading if baselines, customer commitments, or hard security and compliance gates are missing.

Mitigation: Keep missing inputs as owned preconditions, freeze success criteria before PRD handoff, and pause or stop the POC when critical data, users, access, or risk approvals are unavailable.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/xukun0821/skills/fde-engagement-charter)
- [Publisher profile](https://clawhub.ai/user/xukun0821)
- [Charter input guide](references/charter-input-guide.md)
- [Charter rules](references/charter-rules.md)
- [Engagement charter template](references/engagement-charter-template.md)
- [Charter quality rubric](references/charter-quality-rubric.md)
- [Atlassian Project Poster](https://www.atlassian.com/team-playbook/plays/project-poster)
- [Atlassian Goals, Signals, Measures](https://www.atlassian.com/team-playbook/plays/goals-signals-measures)
- [AWS Designing Generative AI for Success POC](https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/dev-architecting.html)
- [GOV.UK Discovery Phase Guidance](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands]

**Output Format:** [Markdown charter document with optional validator command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces or verifies POC charter documents; the included validator checks structure but does not confirm customer commitment.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
