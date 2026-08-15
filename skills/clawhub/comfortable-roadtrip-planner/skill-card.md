## Description:

Plans comfort-first multi-day self-drive trips around fixed hotels and traveler stamina, then produces scannable itinerary guidance or a one-file interactive HTML route app with map links, priority-ranked stops, weather, meals, tickets, and calendar import.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crazyricemaker](https://clawhub.ai/user/crazyricemaker)

### License/Terms of Use:

MIT

## Use Case:

External users and travel-planning agents use this skill to turn fixed-anchor road trips into comfort-first driving plans that protect daylight, meal, restroom, and stamina constraints. It is especially useful for family, elderly, pregnant, or low-stamina travelers who need prioritized stops, skippable alternatives, map links, live-fact checks, and reusable HTML or Markdown route artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated route artifacts can expose precise itinerary details to third-party map providers, including Baidu links over plain HTTP.

Mitigation: Review generated HTML before sharing; generalize private lodging, home addresses, medical constraints, and sensitive dates; change or remove Baidu HTTP links before relying on the artifact.

Risk: Generated plans may include private lodging details, medical constraints, or other sensitive travel information if supplied by the user.

Mitigation: Keep public artifacts free of private addresses, booking confirmations, personal medical details, emails, phone numbers, and payment information unless the user explicitly requests local/private output.

Risk: Travel facts such as weather, road closures, venue hours, ticket availability, parking, restaurant hours, and traffic can change after the artifact is produced.

Mitigation: Refresh volatile facts for the trip dates using official sources and record checked dates in source provenance before reuse.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/crazyricemaker/skills/comfortable-roadtrip-planner)
- [Project homepage](https://github.com/CrazyRiceMaker/comfortable-roadtrip-planner)
- [Comfort Routing Reference](references/comfort-routing.md)
- [Artifact Patterns Reference](references/artifact-patterns.md)
- [Interactive HTML Route App Reference](references/interactive-html-artifact.md)
- [Trip Data Contract](references/trip-data-contract.md)
- [Trip Data Schema](schemas/trip-data.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance and single-file HTML route artifacts, with optional calendar data and validation commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include interactive map links, source provenance, image credits or placeholders, ticket and venue links, route cut rules, and browser-generated .ics downloads.]

## Skill Version(s):

1.1.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
