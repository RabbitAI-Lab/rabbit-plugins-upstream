## Description:

Access Artsonia student-art portfolios, comments, and fans via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and other authorized Artsonia account users use the skill to view linked students’ artwork and activity, download portfolios, manage fans and notifications, and post comments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles Artsonia credentials and can access private student artwork.

Mitigation: Use it only with a server you trust with the Artsonia password and student content; protect configuration and session-cache files, and set include_private=false when private artwork should be excluded.

Risk: The skill can post comments or invite fans, affecting Artsonia accounts and student portfolios.

Mitigation: Keep MCP_CONFIRM_MODE=ask-user so proposed writes require user review and approval.

Risk: An unreviewed package release could change behavior or access to account data.

Mitigation: Pin a reviewed package version.

## Reference(s):

- [Artsonia MCP on ClawHub](https://clawhub.ai/chrischall/skills/artsonia-mcp)
- [artsonia-mcp on npm](https://www.npmjs.com/package/artsonia-mcp)

## Skill Output:

**Output Type(s):** [Text, Files, Guidance]

**Output Format:** [Artsonia portfolio and account information as text; downloaded artwork images and optional JSON index or metadata files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the linked Artsonia account and requested actions; artwork downloads can include private student work unless excluded.]

## Skill Version(s):

1.3.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
