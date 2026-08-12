## Description:

Stage 7 of FDE Delivery Loop turns POC run evidence into an adoption plan, value measurement, and next-investment decision covering target users, behavior change, value metrics, baselines, data sources, risks, and scale conditions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xukun0821](https://clawhub.ai/user/xukun0821)

### License/Terms of Use:

MIT-0

## Use Case:

Delivery teams use this skill after a POC run to determine whether real users adopted the solution, whether measurable value exists, and whether to scale, correct, pause, or stop further investment. It helps structure adoption evidence, value metrics, full costs, risk boundaries, enablement needs, and productization candidates into an adoption and value review package.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may process sensitive operational signals, adoption data, cost data, support issues, or customer business metrics.

Mitigation: Use only authorized customer or internal data, limit access to relevant participants, and avoid adding unnecessary personal or confidential information to prompts or outputs.

Risk: Adoption and value outputs can influence investment, scale, procurement, or personnel-impact decisions.

Mitigation: Keep human review and accountable business ownership for those decisions; treat the skill output as evidence organization, not final approval.

Risk: ROI, attribution, or scale recommendations can be misleading when baselines, denominators, costs, or confounding factors are incomplete.

Mitigation: Mark evidence status explicitly, separate technical quality from adoption and business value, include full incremental costs, and state attribution limits before recommending scale.

## Reference(s):

- [Adoption and Value Input Guide](references/adoption-input-guide.md)
- [Use Diagnostic and Expansion Rules](references/adoption-rules.md)
- [Value Measurement Rules](references/value-measurement.md)
- [Adopt and Value Review Package Template](references/adoption-value-plan.md)
- [Adoption and Value Quality Score](references/adoption-quality-rubric.md)
- [Adoption and Value Field Manual](references/adoption-field-handbook.md)
- [User Empowerment, Support and Knowledge Transfer](references/enablement-and-handover.md)
- [Full Example of Adoption and Value](references/adoption-worked-example.md)
- [Public Method Sources](references/public-sources.md)
- [Microsoft Cloud Adoption Framework: Strategy](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/strategy/)
- [AWS: Designing Generative AI for Success POC](https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/dev-architecting.html)
- [AWS: Continuous Delivery of Generative AI Value](https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/prod-value.html)
- [OpenAI: A Business Leader's Guide to Working with Agents](https://cdn.openai.com/business-guides-and-resources/a-business-leaders-guide-to-working-with-agents.pdf)
- [Atlassian Goals, Signals, Measures](https://www.atlassian.com/team-playbook/plays/goals-signals-measures)
- [ClawHub Skill Page](https://clawhub.ai/xukun0821/skills/fde-adoption-and-value)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown adoption and value review package with tables and decision guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces analysis documents only; it does not execute scripts or make investment, scale, procurement, financial audit, or personnel-impact decisions.]

## Skill Version(s):

1.0.0 (source: server release metadata and TRUST-CARD.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
