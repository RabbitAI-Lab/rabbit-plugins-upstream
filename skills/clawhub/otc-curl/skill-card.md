## Description:

Helps agents find local events and affordable activities on On the Cheap city sites using public web pages and WordPress APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People looking for free or inexpensive local activities can use an agent with this skill to find event listings and related articles when the onthecheap MCP server is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Results rely on live third-party websites and may be outdated or incomplete.

Mitigation: Check the requested date against the page heading, fetch full day listings rather than relying on truncated month views, and verify important details on the source page.

Risk: Article searches can return expired offers.

Mitigation: Look up and exclude each site's expired category before showing deals.

## Reference(s):

- [On the Cheap query recipes](references/recipes.md)
- [otc-curl on ClawHub](https://clawhub.ai/chrischall/skills/otc-curl)
- [Charlotte on the Cheap](https://www.charlotteonthecheap.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with event and article details, links, and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on live public website content.]

## Skill Version(s):

1.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
