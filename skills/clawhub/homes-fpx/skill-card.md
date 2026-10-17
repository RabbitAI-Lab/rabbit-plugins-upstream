## Description:

Guides agents in querying homes.com listings, property details, and saved homes using fpx through the user's browser session without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search US homes.com listings, resolve addresses, inspect property information, and optionally retrieve their own saved homes and searches without running an MCP server.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Pairing a browser bridge gives the agent access to the user's homes.com session.

Mitigation: Install and pair the bridge only if comfortable granting the agent access to that browser tab.

Risk: Saved-home and saved-search requests can expose account-specific property data in temporary outputs.

Mitigation: Request saved data only intentionally, and avoid logging or sharing the temporary HTML and JSON outputs.

## Reference(s):

- [homes.com request recipes](references/homes-requests.md)
- [homes-fpx release](https://clawhub.ai/chrischall/skills/homes-fpx)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Guidance]

**Output Format:** [Markdown with shell and JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can retrieve HTML and JSON, including account-specific saved properties when requested.]

## Skill Version(s):

2.1.11 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
