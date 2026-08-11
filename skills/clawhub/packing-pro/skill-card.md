## Description:

Generates smart, categorized packing lists based on destination weather, trip duration, activities, and transport type.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

Travelers and agents use this skill to generate structured, weighted packing checklists with critical items, activity-specific gear, and weather-aware clothing recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The --output option writes directly to the user-specified path.

Mitigation: Use --output only with a path intended for creating or replacing the generated packing-list file.

Risk: Packing quantities and item weights are estimates for trip planning.

Mitigation: Review generated critical items, travel documents, medication needs, and baggage limits before relying on the checklist.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/packing-pro)
- [Publisher profile](https://clawhub.ai/user/voronindenis5)
- [Server-resolved GitHub repository](https://github.com/voronindenis5/packing-pro)
- [Item Database Reference](references/item-database.md)
- [Weather & Activity Logic Reference](references/weather-logic.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Structured JSON packing checklist, with optional shell commands and setup guidance in Markdown documentation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes critical items, categorized packing items, quantities, notes, and estimated total weight.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
