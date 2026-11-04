## Description:

This skill should be used when the user asks about Workvivo — their company's employee intranet / social feed (Zoom Workvivo) — through the workvivo-mcp server's workvivo_* tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees use this skill to find and read company news, posts, events, people, spaces, pages, and linked documents in their organization's Workvivo. It provides read-only access and does not publish or interact with content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workvivo may contain internal company content.

Mitigation: Use a trusted Workvivo server and bridge, and make requests only when authorized by the company.

Risk: Search queries are recorded in the user's Workvivo history.

Mitigation: Consider the visibility of a query before searching, and avoid including information that should not appear in that history.

Risk: The referenced API guide and server code are absent, so access restrictions and redaction behavior were not verified.

Mitigation: Use only a trusted server and bridge; do not rely on unverified access restrictions or redaction behavior when deciding what content to access.

## Reference(s):

- [Workvivo MCP on ClawHub](https://clawhub.ai/chrischall/skills/workvivo-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text and Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Workvivo content; space digests and linked documents may be returned as Markdown.]

## Skill Version(s):

0.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
