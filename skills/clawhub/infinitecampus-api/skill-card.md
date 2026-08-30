## Description:

Query a district-specific Infinite Campus Campus Parent portal with curl commands for login, session handling, and read access to grades, attendance, assignments, schedules, messages, documents, fees, and related student records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and authorized Infinite Campus portal users use this skill to issue direct curl and jq commands against their own district's Campus Parent portal when they need scriptable access without installing the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses real Infinite Campus credentials, session cookies, and XSRF tokens.

Mitigation: Use only authorized accounts, keep credentials in environment variables or a secret store, avoid shell history exposure, and delete cookie jars when finished.

Risk: Portal responses and downloaded files can contain sensitive student records such as grades, attendance, messages, fees, and reports.

Mitigation: Avoid shared machines and synced folders, minimize local copies, restrict file permissions, and remove downloaded records when they are no longer needed.

Risk: Some district modules or endpoints may be disabled, unconfirmed, or behave differently, and fetching a message body may mark it read in some configurations.

Mitigation: Check display options before treating 404 responses as failures, expect behavior and food service paths to vary, and treat message retrieval as potentially state-changing.

## Reference(s):

- [Infinite Campus endpoints for curl](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/infinitecampus-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and curl/jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return district portal responses that may include sensitive student records and downloaded documents.]

## Skill Version(s):

2.6.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
