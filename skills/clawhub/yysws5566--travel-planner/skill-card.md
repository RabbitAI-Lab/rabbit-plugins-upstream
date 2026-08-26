## Description:

性价比优先的智能旅行规划 Agent，覆盖需求澄清、目的地研究、多源比价、POI 精选、行程优化与 HTML 行程书输出。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yysws5566](https://clawhub.ai/user/yysws5566)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and travel-planning agents use this skill to clarify trip requirements, compare transportation, lodging, food, and attraction options, optimize daily routes, and produce a practical HTML itinerary with budget and risk information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated itinerary HTML can contact third-party CDNs, map tile providers, Xiaohongshu, and booking platforms when opened or clicked.

Mitigation: Review generated links before sharing or opening in restricted environments, and allow network access only to domains needed for the itinerary.

Risk: Shared itinerary files may expose trip dates, locations, budgets, lodging choices, or other personal travel details.

Mitigation: Avoid including highly sensitive details in shared itinerary files and remove private information before sending the file to others.

Risk: Booking and payment links may lead users away from the itinerary to third-party sites.

Mitigation: Verify booking domains and payment pages independently before entering credentials or payment information.

Risk: Generated output may overwrite an existing file if the destination path is reused.

Mitigation: Confirm the output path and filename before saving generated itinerary files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yysws5566/skills/travel-planner)
- [Skill definition](artifact/SKILL.md)
- [Usage guide](artifact/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance plus generated HTML itinerary files and JavaScript DATA configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated itineraries may include third-party map tiles, CDN scripts, booking links, Xiaohongshu search links, budgets, routes, POI coordinates, and risk notes.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
