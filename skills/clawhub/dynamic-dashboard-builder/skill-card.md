## Description:

Builds dynamic HTML dashboards from existing database tables with periodic refresh, requiring approval for endpoints, polling rate, and schema before setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to turn approved database tables or API-backed data sources into dynamic HTML dashboards with configurable polling, schema review, and data-exposure checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dashboards may expose private database, API, PII, or secret-bearing data if configured carelessly.

Mitigation: Use only trusted and explicitly approved endpoints and tables, confirm polling and schema changes before setup, and minimize or redact sensitive data before rendering.

Risk: Unapproved schema changes or hardcoded endpoints could make the generated dashboard unreliable or unsafe to operate.

Mitigation: Keep endpoints configurable through environment variables or user-approved configuration, and require explicit approval before CREATE or ALTER operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/dynamic-dashboard-builder)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-approved endpoint, polling interval, schema, and PII handling before implementation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
