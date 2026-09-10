## Description:

Query homes.com from a shell with the fpx CLI to search listings, resolve addresses, fetch property detail, photos, history, and access signed-in saved homes or searches through the user's own browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve homes.com listing and property data from shell workflows when they need fpx-backed browser-session access instead of a homes.com MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a signed-in homes.com browser tab, including access to saved homes and saved searches.

Mitigation: Install it only when that browser-session access is acceptable, and ask the agent to fetch saved homes or saved searches only when explicitly needed.

Risk: Saved homes and saved searches may contain private account data.

Mitigation: Treat those outputs as private and prefer private temporary directories or direct pipelines instead of fixed shared /tmp files.

## Reference(s):

- [homes.com request recipes](references/homes-requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/homes-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration, Guidance, Markdown]

**Output Format:** [Markdown with inline shell, Node.js, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces request and extraction recipes for homes.com pages and fpx profile setup.]

## Skill Version(s):

1.4.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
