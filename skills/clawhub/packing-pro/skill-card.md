## Description:

Generates smart, categorized packing lists based on destination weather, trip duration, activities, and transport type. Produces weighted checklists with a critical-items section and weather-adaptive recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to create trip-specific packing checklists that account for destination, duration, season or temperature, planned activities, and transport mode.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional --output argument can overwrite the file path provided by the user.

Mitigation: Choose the output path deliberately, or omit --output to print the packing list locally to stdout.

Risk: Packing recommendations and weight estimates are planning aids rather than precise measurements or travel compliance guarantees.

Mitigation: Review critical items, airline restrictions, medicine handling, and destination requirements before travel.

## Reference(s):

- [Item Database Reference](references/item-database.md)
- [Weather & Activity Logic Reference](references/weather-logic.md)
- [Server-resolved source repository](https://github.com/voronindenis5/packing-pro)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/packing-pro)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON packing-list examples and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated packing lists include critical items, categorized items, quantities, estimated item weights, notes, and an estimated total weight.]

## Skill Version(s):

0.1.1 (source: release metadata; artifact SKILL.md frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
