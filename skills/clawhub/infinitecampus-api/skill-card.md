## Description:

Guides an agent to query a district-specific Infinite Campus Campus Parent portal with curl by logging in, capturing cookies and an XSRF token, and calling read-oriented endpoints for grades, attendance, assignments, schedules, messages, documents, and fees.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, parents, and authorized support staff use this skill to make authorized read-oriented curl requests against an Infinite Campus district portal. It is intended for scripts or environments where the Infinite Campus MCP server is not installed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses real Infinite Campus credentials, session cookies, and XSRF tokens.

Mitigation: Install and run it only for authorized district portal access, keep credentials and session artifacts out of repositories and logs, and delete temporary cookie or data files when finished.

Risk: Responses and downloaded documents may contain private student records.

Mitigation: Treat command output, PDFs, and intermediate files as sensitive records and limit storage or sharing to authorized workflows.

Risk: Some district modules or endpoints may be disabled or unconfirmed, and fetching a message body may mark it read on some configurations.

Mitigation: Check display options before treating 404 responses as failures and review message-reading side effects before using message endpoints in automation.

## Reference(s):

- [Infinite Campus endpoints for curl](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/infinitecampus-api)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes district-specific configuration variables, cookie and XSRF token handling, endpoint recipes, and notes about feature-gated portal modules.]

## Skill Version(s):

3.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
