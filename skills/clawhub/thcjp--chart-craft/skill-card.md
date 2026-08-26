## Description:

图表工坊专业版 guides an agent through local chart and report generation workflows, including chart type selection, theming, batch CSV inputs, and PNG, SVG, PDF, or JSON export planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and teams use this skill to plan and run local chart/report generation tasks from CSV, JSON, or structured data. It is intended for data analysis, report generation, statistical insight, and data visualization workflows rather than realtime stream processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent to run Python commands and create chart or report files.

Mitigation: Review commands before execution, install only expected dependencies, and use explicit output paths outside shared or sensitive directories.

Risk: The documentation contains broad and inconsistent statements about networked or API-backed behavior.

Mitigation: Clarify whether any networked or API-backed feature is actually present before relying on it; treat the artifact as local chart-generation guidance unless stronger evidence is available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/chart-craft)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands, JSON/CSV examples, and chart/report file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local chart or report files when the agent follows Python-based generation commands.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
