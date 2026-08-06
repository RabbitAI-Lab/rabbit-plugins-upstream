## Description:

Decide whether to fix, replace, or recycle a broken item by scoring item type, age, symptoms, repair estimate, lifespan, sentimental value, and environmental impact.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to structure repair-versus-replace decisions for broken household items, electronics, tools, and appliances. It compares repair and replacement costs, remaining lifespan, condition, sentiment, and environmental impact to produce a recommendation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Outputs could be mistaken for professional repair, electrical, gas, financial, or safety advice.

Mitigation: Treat recommendations as advisory decision support and get qualified review before acting on costly or safety-sensitive repairs.

Risk: A recommendation can be misleading if repair estimates, replacement costs, item condition, or expected lifespan are inaccurate.

Mitigation: Verify inputs, include diagnosis, parts, labor, shipping, and hidden costs, and compare lifespan assumptions against the bundled reference data.

Risk: Disposal recommendations may miss privacy or environmental handling requirements for electronics and appliances.

Mitigation: Use certified recycling or manufacturer takeback programs, remove batteries when appropriate, and wipe data from electronics before disposal.

## Reference(s):

- [Decision Matrix - Scoring Algorithm](references/decision-matrix.md)
- [Environmental Impact - E-Waste and Sustainability](references/environmental-impact.md)
- [Item Lifespans - Expected Useful Life Data](references/item-lifespans.md)
- [Server-resolved GitHub provenance](https://github.com/voronindenis5/repair-or-replace)
- [ClawHub release page](https://clawhub.ai/voronindenis5/skills/repair-or-replace)
- [Hermes Agent skills documentation](https://hermes-agent.nousresearch.com/docs)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, JSON, Shell commands]

**Output Format:** [Markdown decision report or JSON from the included command-line script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes recommendation, confidence, weighted factor scores, reasoning, and warnings; no network calls or external dependencies are required.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; source frontmatter version is 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
