## Description:

Query an Infinite Campus (Campus Parent portal) district directly with curl instead of running the infinitecampus-mcp server, including login, session cookie and XSRF token capture, and reads for grades, attendance, assignments, schedules, messages, documents, and fees.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, technical parents, and authorized operators use this skill to make direct, scriptable curl requests against an Infinite Campus district portal when they need Campus Parent data without installing or running the related MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles Infinite Campus credentials, session cookies, XSRF tokens, downloaded PDFs, and raw JSON responses that may contain sensitive student records.

Mitigation: Use it only with authorized accounts, avoid shared terminals and logs, store secrets securely, and delete session and data files when finished.

Risk: Some portal reads may expose district-specific behavior or module availability, and fetching a message body may mark it read on some district configurations.

Mitigation: Check feature flags and endpoint responses before treating 404s as errors, and review message-body fetches before running them in automated workflows.

## Reference(s):

- [Infinite Campus endpoints for curl](references/endpoints.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline shell commands and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces user-directed curl patterns for read-oriented portal access; downloaded documents and raw JSON responses may contain sensitive student records.]

## Skill Version(s):

2.5.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
