## Description:

Decide whether to fix, replace, or recycle a broken item using item type, age, symptoms, repair estimate, and scored factors for cost, lifespan, sentimental value, and environmental impact.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to make a structured repair-versus-replace decision for household, personal, or tool items by comparing costs, age, lifespan, condition, sentiment, and environmental factors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat repair, safety, financial, or environmental recommendations as professional advice.

Mitigation: Treat the output as structured decision support and consult qualified professionals for gas, electrical, vehicle, safety-critical, high-cost, or regulated repairs.

Risk: The recommendation depends on user-supplied repair estimates, replacement costs, age, condition, and lifespan assumptions.

Mitigation: Validate inputs against current repair quotes, comparable replacement prices, and the provided lifespan and decision-matrix references before acting.

## Reference(s):

- [Decision Matrix](references/decision-matrix.md)
- [Item Lifespans](references/item-lifespans.md)
- [Environmental Impact](references/environmental-impact.md)
- [Source Repository](https://github.com/voronindenis5/repair-or-replace)
- [ClawHub Skill Page](https://clawhub.ai/voronindenis5/skills/repair-or-replace)
- [Hermes Agent Documentation](https://hermes-agent.nousresearch.com/docs)

## Skill Output:

**Output Type(s):** [text, json, guidance]

**Output Format:** [Plain-text decision report or JSON object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local user-supplied item, cost, lifespan, condition, sentimental, and efficiency inputs; no networking, persistence, or hidden data access is indicated by the security evidence.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
