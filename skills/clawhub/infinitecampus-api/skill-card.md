## Description:

Query an Infinite Campus Campus Parent portal district directly with curl by logging in with real credentials, capturing session cookies and an XSRF token, and retrieving grades, attendance, assignments, schedules, messages, documents, and fees.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically capable guardians use this skill to script authorized, district-specific Infinite Campus Campus Parent portal reads without running the Infinite Campus MCP server. It helps retrieve student records through curl and jq recipes for local inspection or automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authentication cookies, XSRF tokens, environment files, and raw portal outputs can expose sensitive student records.

Mitigation: Use only accounts you are authorized to access, avoid shared machines, protect .env files and cookie jars, and do not share raw outputs.

Risk: Document download commands can send cookies and XSRF tokens to an untrusted absolute URL.

Mitigation: Before sending authentication headers or cookies, allow only HTTPS document URLs on the same district portal host.

Risk: Fetching a message body may mark the message as read on some district configurations.

Mitigation: Treat message-body retrieval as potentially state-changing and confirm before fetching message content.

## Reference(s):

- [Infinite Campus endpoints for curl](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/infinitecampus-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and jq command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-oriented command recipes; command output may include sensitive student records and downloaded documents.]

## Skill Version(s):

2.8.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
