## Description:

Smart Travel Planner helps agents create travel itineraries, destination guides, budget estimates, route optimizations, food recommendations, visa guidance, and packing lists for multiple travel scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to prepare structured travel plans, compare travel options, estimate trip budgets, and adapt itineraries for family, couple, solo, business, and long-distance travel scenarios.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can keep a local history of usage, notes, errors, and preferences.

Mitigation: Make memory collection explicit and opt-in, scope retained data to the skill, and provide a clear deletion path before broad use.

Risk: The skill describes behavior that can evolve its own SKILL.md instructions over time.

Mitigation: Require human review and security scanning before any instruction changes are accepted or deployed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/smart-travel-planner)

## Skill Output:

**Output Type(s):** [markdown, text, guidance, shell commands, configuration]

**Output Format:** [Structured Markdown travel plans with itinerary timelines, budget tables, practical tips, fallback options, and optional learner command snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use current web information for travel data and may maintain local usage, error, note, and preference history through learned_patterns.json.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
