## Description:

Plans an optimized multi-stop errand itinerary by estimating travel time, applying stop hours and dwell time, and returning ETAs, wait time, totals, and closing-time violations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to choose an order for everyday errands, pickups, and drop-offs when stops have travel time, dwell time, and opening-hours constraints. It is intended for small local planning tasks rather than live turn-by-turn navigation or fleet logistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Errand inputs may contain personal location and schedule details.

Mitigation: Keep route files and CLI arguments local, avoid adding unnecessary sensitive details, and remove temporary inputs when they are no longer needed.

Risk: The itinerary is planning guidance, not live navigation or traffic guidance.

Mitigation: Treat ETAs as estimates, keep schedule buffer, and verify real-time traffic, store hours, road closures, and access constraints before acting.

Risk: Large errand sets or tight time windows can produce infeasible routes or local-optimum results.

Mitigation: Use the skill for small errand runs, review violation flags, and use a dedicated routing solver for larger or operational logistics workloads.

## Reference(s):

- [Errand Routing - Model & Math Reference](references/routing-model.md)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/errand-router)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text itinerary or JSON route object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include stop order, leg distance, drive time, arrival and departure times, wait time, totals, and time-window violation flags.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
