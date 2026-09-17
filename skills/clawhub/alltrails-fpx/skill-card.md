## Description:

Query alltrails.com for trail search, trail details, reviews, photos, weather, saved lists, completed trails, and activity feed data from a shell using the fpx CLI through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical users use this skill to generate shell commands and request patterns for querying AllTrails data through a signed-in browser session when the AllTrails MCP server is unavailable or unnecessary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a signed-in AllTrails browser session and may access personal account data such as saved lists, completed trails, and activity feed entries.

Mitigation: Review before installing, use a dedicated browser profile when possible, and avoid sharing logs that contain account data or captured headers.

Risk: The setup relies on an unpinned global npm installation for @fetchproxy/cli.

Mitigation: Install without administrator privileges and review the package and version used in your environment before use.

Risk: The browser bridge can remain paired after setup and use the signed-in AllTrails session.

Mitigation: Unpair or remove the browser bridge when finished and keep browser site access scoped to alltrails.com.

## Reference(s):

- [AllTrails endpoint examples](artifact/references/endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON response-shape notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes read-only endpoint examples and troubleshooting notes for fpx, browser pairing, captured headers, and AllTrails response shapes.]

## Skill Version(s):

2.3.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
