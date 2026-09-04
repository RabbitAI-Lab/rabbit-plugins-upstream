## Description:

Guides agents in querying a district-specific Infinite Campus Campus Parent portal with curl by logging in, capturing session cookies and an XSRF token, and making read-oriented requests for grades, attendance, assignments, schedules, messages, documents, and fees.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and authorized Infinite Campus users use this skill to generate curl and jq commands for accessing their own district portal data without running the MCP server. It is intended for scripted, user-directed reads of Campus Parent records where credentials, session cookies, XSRF tokens, and downloaded student records are handled securely.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portal credentials, session cookies, XSRF tokens, and downloaded student records are sensitive.

Mitigation: Use a secure secret store, restrict permissions on cookie jars and downloads, avoid shared machines and synced folders, and delete session artifacts and records when finished.

Risk: The skill should only be used with an Infinite Campus account the user is authorized to access.

Mitigation: Confirm authorization before installing or running the generated commands, and scope use to the user's own district portal and account permissions.

Risk: Some district modules or endpoints may be disabled or vary by district, and two documented paths are unconfirmed against enabled live modules.

Mitigation: Check displayOptions and treat expected 404 responses as disabled modules before assuming an endpoint or command failed unexpectedly.

Risk: Fetching a message body may mark the message as read on some district configurations.

Mitigation: Avoid fetching message bodies unless that possible side effect is acceptable for the authorized account.

## Reference(s):

- [Infinite Campus endpoints for curl](references/endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with curl and jq shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only command recipes depend on district-specific Infinite Campus hosts, enabled portal modules, and valid user credentials.]

## Skill Version(s):

2.7.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
