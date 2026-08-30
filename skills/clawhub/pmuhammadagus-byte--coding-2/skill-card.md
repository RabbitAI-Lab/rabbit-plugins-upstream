## Description:

Use this skill to build dynamic HTML dashboards from API data or design database schemas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to design database schemas, configure API-backed dashboard data flows, and generate dynamic HTML dashboards with independently updating charts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dashboard generation may involve API and database actions against the wrong target.

Mitigation: Confirm the API base URL, session or group ID, database target, collection names, and any write operations before use.

Risk: Credentials or user data could be exposed if embedded directly in generated dashboard code or sent to unapproved endpoints.

Mitigation: Keep credentials in environment variables or explicit configuration, redact secrets from logs, minimize PII, and do not approve unknown third-party endpoints.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with HTML, JavaScript, JSON, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dashboard API targets, session or group identifiers, database targets, collection names, and write operations should be supplied or approved by the user at runtime.]

## Skill Version(s):

1.1.0 (source: release metadata, _meta.json, and openclaw metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
