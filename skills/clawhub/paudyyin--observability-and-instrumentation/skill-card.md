## Description:

Adds observability and instrumentation guidance for applications across metrics, logs, traces, dashboards, and alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paudyyin](https://clawhub.ai/user/paudyyin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to plan and review telemetry for production applications, including structured logs, low-cardinality metrics, distributed traces, dashboards, symptom-based alerts, and verification checklists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Instrumentation changes may accidentally capture secrets or sensitive personal data in logs or telemetry.

Mitigation: Review generated logging and telemetry fields before implementation; use allowlisted fields and redact secrets, tokens, passwords, and full personal data.

Risk: Metric labels with unbounded values can create high-cardinality telemetry and overload observability backends.

Mitigation: Keep labels to small fixed sets such as route templates, status classes, and provider names; put request IDs and user-specific details in logs or traces instead.

Risk: The skill text is mostly Chinese and contains visible encoding damage, which may make some guidance ambiguous.

Mitigation: Have a reader fluent in the text review ambiguous passages before relying on them for production instrumentation decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/observability-and-instrumentation)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code examples, checklists, and implementation recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only guidance; proposed telemetry changes should be reviewed before implementation.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
