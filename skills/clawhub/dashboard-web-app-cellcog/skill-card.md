## Description:

Dashboard helps agents use CellCog to generate interactive dashboards, KPI trackers, data visualizations, analytics apps, data explorers, calculators, games, and responsive HTML apps with real-time filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cellcog](https://clawhub.ai/user/cellcog)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to ask CellCog to create dashboards, KPI trackers, interactive data explorers, responsive web apps, and simple browser games from prompts, inline data, or uploaded CSV, JSON, and Excel files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and uploaded CSV, JSON, or Excel files may be sent to CellCog's external generation service.

Mitigation: Use the skill only when CellCog is intended for the workflow, avoid sensitive business data unless approved, and review CellCog's package and service terms before use.

Risk: The skill depends on a CellCog API key and Python package availability.

Mitigation: Install the CellCog package from an approved source, set CELLCOG_API_KEY through the user's normal secret-management process, and avoid embedding credentials in prompts or generated files.

## Reference(s):

- [CellCog homepage](https://cellcog.ai)
- [ClawHub skill page](https://clawhub.ai/cellcog/skills/dashboard-web-app-cellcog)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with Python and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the CellCog package and CELLCOG_API_KEY; generated dashboard or app content is returned by the external CellCog service.]

## Skill Version(s):

1.0.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
