## Description:

Calculates required breathing flow for battery pack enclosures under temperature and altitude changes and recommends explosion-proof valve specifications using pressure-flow data and a cell gas-rate safety constraint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[julio916](https://clawhub.ai/user/julio916)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and battery pack engineers use this skill to estimate enclosure breathing flow for pressure balancing and compare valve candidates against thermal, altitude, and cell gas-generation constraints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Engineering output may be mistaken for a certified valve-safety determination.

Mitigation: Verify valve data, safety factors, and physical assumptions against applicable battery-pack design standards before using recommendations in real battery pack design.

Risk: The bundled pressure-flow curve and typical operating assumptions may not match the specific valve model or pack environment.

Mitigation: Replace or confirm the valve data and environmental assumptions with manufacturer data and project-specific requirements before relying on the recommendation.

## Reference(s):

- [Formula Reference](artifact/references/formulas.md)
- [Valve Data Reference](artifact/references/valve_data.md)
- [Server-Resolved GitHub Provenance](https://github.com/Julio916/explosion-proof-valve-selection)
- [ClawHub Skill Page](https://clawhub.ai/julio916/skills/explosion-proof-valve-selection)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with JSON calculation results and optional bash or Python snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes required flow, recommended valve pressure point, valve flow, safety factor, and mitigation options when no candidate satisfies the constraints.]

## Skill Version(s):

0.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
