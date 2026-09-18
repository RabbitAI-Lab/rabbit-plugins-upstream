## Description:

Provides Datadog search and read access for metrics, monitors, timeseries points, and API key validation through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Datadog action schemas and retrieve monitoring data such as metric metadata, active metric names, monitor details, monitor search results, and timeseries points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Datadog queries and results are routed through OOMOL.

Mitigation: Use a dedicated read-only Datadog key with minimum scopes and review OOMOL credential and data-handling controls before installation.

Risk: The artifact documents remote installer commands for the oo CLI.

Mitigation: Run installer commands only when the CLI is missing and only after verifying the installer source and integrity.

Risk: Broad Datadog requests through the connector may expose sensitive monitoring data.

Mitigation: Inspect the live action schema before each request and keep queries limited to the data needed for the task.

## Reference(s):

- [ClawHub Datadog Skill Listing](https://clawhub.ai/oomol/skills/oo-datadog)
- [Datadog Homepage](https://www.datadoghq.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Datadog connector responses containing data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
