## Description:

Query alltrails.com trail search, trail detail, reviews, photos, weather, saved lists, completed trails, and activity feed data from a shell with the fpx CLI through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve AllTrails data from shell workflows when they need one-shot read access without running the AllTrails MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill works through a signed-in browser session and captured headers, so command output or logs may contain account-linked information.

Mitigation: Use the skill only for authorized read-only access and avoid sharing logs, shell history, captured headers, or account-linked output.

Risk: AllTrails requests can fail or return non-JSON interstitial responses when the browser session or challenge state is not ready.

Mitigation: Follow the documented fpx pairing, header capture, health check, and exit-code guidance before relying on returned data.

## Reference(s):

- [AllTrails endpoints for fpx](artifact/references/endpoints.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell command examples and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only AllTrails GET and read POST workflows through a signed-in browser session.]

## Skill Version(s):

2.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
