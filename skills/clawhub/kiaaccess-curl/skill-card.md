## Description:

Query and command a Kia vehicle directly with curl against the Kia Owners API for one-off vehicle status, location, EV charge, lock, unlock, and climate operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Kia owners use this skill for one-off shell access to Kia Owners API reads and commands when they need direct curl examples instead of a conversational MCP workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles reusable Kia account tokens and credential-derived session files.

Mitigation: Treat session files and temporary command outputs as sensitive, store reusable tokens with restrictive permissions, and avoid sharing terminal logs that may include account or vehicle data.

Risk: The skill can issue real vehicle commands such as lock, unlock, climate, and charging operations.

Mitigation: Run mutating commands only when explicitly intended, inspect generated curl commands before execution, and verify results with a fresh vehicle status read.

Risk: Vehicle location responses can reveal sensitive personal location information.

Mitigation: Request and display location data only when needed, minimize retention of location output, and avoid writing it to shared files or logs.

## Reference(s):

- [Ready-to-run requests](references/requests.md)
- [Kia Owners API endpoint](https://api.owners.kia.com/apigw/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with bash, curl, and jq command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes setup guidance for Kia account credentials, MFA bootstrap, reusable session storage, API reads, vehicle commands, and command verification by re-read.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
