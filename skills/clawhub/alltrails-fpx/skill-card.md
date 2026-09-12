## Description:

Query alltrails.com for trail search, trail details, reviews, photos, weather, saved lists, completed trails, and activity feed data from a shell using the fpx CLI through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to query AllTrails data from shell scripts or machines where the AllTrails MCP server is not installed. It is suited for read-only trail lookup, endpoint exploration, and signed-in personal list or activity retrieval through the user's own browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow pairs fpx/Transporter with an AllTrails browser session.

Mitigation: Install and use it only when browser-session access is acceptable, and restrict the extension's site access to alltrails.com.

Risk: A global @fetchproxy/cli install increases dependency and update risk.

Mitigation: Prefer a pinned or local @fetchproxy/cli install.

Risk: Captured session output and endpoint responses can include saved lists, completed trails, or activity feed data.

Mitigation: Treat this output as personal information and avoid storing captured session output in predictable temp files.

## Reference(s):

- [AllTrails endpoints for fpx](references/endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON response-shape notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only workflow; command examples use fpx and jq and may return AllTrails JSON from the user's browser session.]

## Skill Version(s):

2.3.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
