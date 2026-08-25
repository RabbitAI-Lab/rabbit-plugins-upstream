## Description:

Use this skill when building dynamic HTML dashboards from API data or designing database schemas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design database schemas from user-provided data, create API-backed dashboard flows, and build real-time HTML charts that poll approved endpoints every 60 seconds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide work involving API endpoints, databases, credentials, and write operations.

Mitigation: Confirm the target API base URL, database, collection or table names, credentials source, and any write operation with the user before execution.

Risk: Dashboard code could send user data to an unapproved external endpoint if configuration is not reviewed.

Mitigation: Use only user- or organization-approved endpoints and environment or explicit configuration values; do not hardcode unknown third-party hosts.

Risk: The bundled linter is heuristic and advisory, so passing or failing it does not prove the dashboard is safe or correct.

Mitigation: Run the linter only on dashboard files the user chooses, then manually review endpoint usage, polling behavior, response handling, and placeholder substitution before deployment.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code, configuration details, and shell commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include advisory dashboard lint findings for user-selected HTML or JavaScript files.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
