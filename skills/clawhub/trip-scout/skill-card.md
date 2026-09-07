## Description:

Trip Scout helps an agent search flights and hotels, screen hotel risk, monitor flight prices, plan road-trip itineraries, query car-rental locations, and generate travel map or guide outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[treesan](https://clawhub.ai/user/treesan)

### License/Terms of Use:

MIT

## Use Case:

External travelers and agents use this skill to compare flight and hotel options, evaluate hotel review risk, plan family or road-trip itineraries, monitor airfare, and produce practical trip outputs such as recommendations, maps, guide content, and supporting commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles personal platform cookies for services such as Xiaohongshu and Ctrip.

Mitigation: Use the skill only in an isolated environment, avoid entering personal cookies unless acceptable, and delete or restrict cookie files after use.

Risk: Some platform access relies on reverse-engineered or anti-detection API behavior.

Mitigation: Review before installation and prefer official platform APIs where they can satisfy the workflow.

Risk: Generated itinerary HTML may include external hotel or review text.

Mitigation: Inspect generated HTML before sharing or opening it in a sensitive environment.

Risk: Executable code paths and dependencies require review before trust-sensitive use.

Mitigation: Install in an isolated environment, pin dependencies where possible, and run security review before deployment.

## Reference(s):

- [Trip Scout ClawHub Page](https://clawhub.ai/treesan/skills/trip-scout)
- [Flight Search Workflow](references/flight-search.md)
- [Hotel Search and Screening Workflow](references/hotel-search.md)
- [Review Analysis Engine](references/review-analysis.md)
- [Road Trip Planning Methodology](references/road-trip-planning.md)
- [Trip Planning Methodology](references/trip-planning.md)
- [Car Rental Store Lookup](references/car-rental-stores.md)
- [Hotel Trust System](references/hotel-trust-system.md)
- [Xiaohongshu Hotel Research Workflow](references/xhs-hotel-research.md)
- [Xiaohongshu Route Search Workflow](references/xhs-route-search.md)
- [Memory Format and Learning Rules](references/memory-format.md)
- [AMap LBS Skill](https://clawhub.ai/lbs-amap/skills/amap-lbs-skill)
- [AMap MCP Server Documentation](https://developer.amap.com/api/mcp-server/summary)
- [Spider_XHS](https://github.com/cv-cat/Spider_XHS)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with command examples, JSON data from helper scripts, and generated HTML itinerary files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write runtime memory, flight-price history, cookie files, and generated itinerary HTML under local user directories or output folders.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
