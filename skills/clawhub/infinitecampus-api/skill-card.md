## Description:

Guides authorized Campus Parent users through district-specific sign-in and read-only queries for grades, attendance, assignments, schedules, messages, documents, and fees using curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized parents, guardians, and developers use this skill to retrieve student portal information from their own district without installing the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portal credentials and session tokens can expose a student's account if disclosed.

Mitigation: Use only an account you are authorized to access on a trusted private machine; keep credentials and cookie jars out of logs and shared or synced folders, and delete temporary cookies after use.

Risk: Downloaded documents and query results can contain sensitive student records.

Mitigation: Limit access to authorized users, avoid logging record contents, and remove saved documents when finished.

## Reference(s):

- [Infinite Campus endpoint recipes](references/endpoints.md)
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/infinitecampus-api)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Text]

**Output Format:** [Markdown with curl and jq command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses depend on the district's enabled portal modules; some example endpoints are unconfirmed.]

## Skill Version(s):

3.1.9 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
