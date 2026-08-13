## Description:

Decide whether to fix, replace, or recycle a broken item by scoring cost, lifespan, condition, sentimental value, and environmental impact.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill as a local decision aid for household repair choices, comparing repair estimates against replacement cost, remaining lifespan, item condition, sentiment, and sustainability factors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The recommendation may be mistaken for professional repair, safety, legal, or financial advice.

Mitigation: Treat the output as decision support only, and consult a qualified professional for gas, electrical, vehicle, or high-cost repairs.

Risk: Incomplete or unrealistic inputs can produce misleading cost and lifespan comparisons.

Mitigation: Use realistic repair estimates, comparable replacement prices, expected lifespan data, and condition scores before relying on the recommendation.

Risk: Safety-sensitive symptoms can change the decision beyond the scoring model.

Mitigation: For symptoms such as smoke, sparks, gas, overheating, fire, or electrical shock, stop using the item and consult a professional.

## Reference(s):

- [Source repository](https://github.com/voronindenis5/repair-or-replace)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/repair-or-replace)
- [Decision Matrix - Scoring Algorithm](references/decision-matrix.md)
- [Item Lifespans - Expected Useful Life Data](references/item-lifespans.md)
- [Environmental Impact - E-Waste and Sustainability](references/environmental-impact.md)
- [Hermes Agent documentation](https://hermes-agent.nousresearch.com/docs)
- [UN Global E-waste Monitor](https://ewastemonitor.info/)
- [iFixit Repair Guides](https://www.ifixit.com/Guide)
- [EPA Electronics Donation and Recycling](https://www.epa.gov/recycle/electronics-donation-and-recycling)
- [Repair Cafe International](https://repaircafe.org/)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Plain text decision report or JSON, with optional shell command examples in documentation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a recommendation, confidence level, factor scores, reasoning, and warnings; interactive mode can prompt for inputs.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
