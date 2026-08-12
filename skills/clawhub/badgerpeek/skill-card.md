## Description:

Inspect Honeybadger projects, faults (error groups), fault details, and notices (error occurrences) through the bundled GET-only BadgerPeek CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivankuznetsov](https://clawhub.ai/user/ivankuznetsov)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use BadgerPeek to inspect recent Honeybadger projects, fault groups, fault details, and notices without Honeybadger MCP or Docker.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Honeybadger project names, error details, context, and stack traces may contain sensitive information.

Mitigation: Use a least-privilege Honeybadger token and avoid pasting unnecessary returned fields into chats or logs.

Risk: Authentication tokens could be exposed if handled outside the intended workflow.

Mitigation: Provide tokens through HONEYBADGER_PERSONAL_AUTH_TOKEN or HONEYBADGER_AUTH_TOKEN, never print token values, and rely on the CLI's recursive credential redaction.

Risk: Using broader Honeybadger integrations could expand access beyond read-only inspection.

Mitigation: Use the bundled GET-only BadgerPeek CLI and avoid Honeybadger MCP, Docker, or unrestricted API clients for this workflow.

## Reference(s):

- [BadgerPeek ClawHub release](https://clawhub.ai/ivankuznetsov/skills/badgerpeek)

## Skill Output:

**Output Type(s):** [guidance, shell commands, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON responses from the bundled CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports compact single-line JSON output; Honeybadger responses are redacted for credential-like fields.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
