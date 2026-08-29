## Description:

Query a district-specific Infinite Campus Campus Parent portal with curl by logging in, capturing cookies and an XSRF token, and calling read endpoints for grades, attendance, assignments, schedules, messages, documents, and fees.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical users can use this skill to make authorized, read-oriented curl requests against their district's Infinite Campus Campus Parent portal without running an MCP server. It is intended for retrieving portal data such as students, grades, attendance, assignments, schedules, messages, documents, fees, teachers, assessments, and feature flags.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles live school-portal credentials and session cookies.

Mitigation: Use only accounts you are authorized to access, keep credentials and cookie jars in protected locations, and delete session files when finished.

Risk: Portal responses and downloaded documents may contain student records.

Mitigation: Avoid saving student records into shared or cloud-synced folders and restrict files to protected local storage.

Risk: Document URLs may be relative or absolute and could be mishandled during download.

Mitigation: Validate document URLs against the district portal before downloading.

## Reference(s):

- [Infinite Campus endpoints for curl](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/infinitecampus-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and jq command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces guidance for authorized portal access and read-oriented API calls; users supply district URL, app name, username, and password through environment variables.]

## Skill Version(s):

2.5.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
