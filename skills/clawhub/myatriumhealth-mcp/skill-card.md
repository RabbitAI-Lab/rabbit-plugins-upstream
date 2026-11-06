## Description:

Read MyAtriumHealth (Atrium Health's Epic MyChart patient portal) — test results, medications, allergies, immunizations, health issues, visits, goals — from a shell with the fpx CLI (@fetchproxy/cli), by relaying requests through your signed-in Chrome tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals use the skill to read their own MyAtriumHealth records from a shell through an active signed-in Chrome session. It supports selecting fields from test results, medications, allergies, immunizations, health issues, visits, goals, and messages for scripts or one-off queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup requests MyChart session-cookie access and cookie-header capture despite the skill's statement that session cookies are never extracted or stored; the external CLI and extension were not included for inspection.

Mitigation: Have the publisher reconcile the cookie-safety promise with setup, remove unnecessary session-cookie and header-capture permissions, and document the narrowest supported scope and revocation steps.

Risk: Health records are returned through command output and may be exposed in logs or shared results.

Mitigation: Handle logs and shared results carefully, and project only the fields needed for the task.

## Reference(s):

- [MyAtriumHealth endpoint recipes](references/endpoints.md)
- [MyAtriumHealth MCP on ClawHub](https://clawhub.ai/chrischall/skills/myatriumhealth-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [MyAtriumHealth portal](https://my.atriumhealth.org/)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Shell commands with JSON API responses and jq projections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may contain personal health information; project only needed fields and handle command output carefully.]

## Skill Version(s):

1.4.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
