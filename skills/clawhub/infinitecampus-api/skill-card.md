## Description:

Provides curl and jq recipes for logging into a district-specific Infinite Campus Campus Parent portal and querying grades, attendance, assignments, schedules, messages, documents, and fees.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and authorized parents or guardians use this skill to query Infinite Campus Campus Parent records with curl when they want direct scriptable access without running the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive student education records, login credentials, session cookies, XSRF tokens, and downloaded files.

Mitigation: Use the skill only for an authorized parent or guardian account, require HTTPS-only district URLs, avoid shared machines and shell logs, and protect or delete cookie jars and downloaded files after use.

Risk: Document download URLs may be absolute, which can expose portal cookies or XSRF headers if the destination is not verified.

Mitigation: For absolute document URLs, verify the destination is same-origin before sending portal cookies and XSRF headers, or omit those headers for non-portal destinations.

Risk: Some district modules or endpoints may be disabled or unconfirmed, and fetching a message body may mark it read on some district configurations.

Mitigation: Check displayOptions before treating a 404 as an error, expect district-specific endpoint differences, and avoid fetching message bodies unless the possible read-status side effect is acceptable.

## Reference(s):

- [Infinite Campus endpoint recipes](references/endpoints.md)
- [ClawHub release page](https://clawhub.ai/chrischall/skills/infinitecampus-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell command examples and JSON-oriented curl responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recipes are read-only in practice except for document downloads that write local files.]

## Skill Version(s):

2.8.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
