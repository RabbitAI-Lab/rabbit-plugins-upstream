## Description:

Query the On the Cheap network (charlotteonthecheap.com, milehighonthecheap.com and sister city sites) from the shell with curl and jq for daily local event listings, prices, venues, and searchable articles on free and cheap things to do.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill when they need current local event or deal data from public On the Cheap city sites and the onthecheap MCP server is unavailable. It provides curl and jq recipes for article search, event extraction, category filtering, and date-safe calendar lookups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may request data from an unintended On the Cheap city site if BASE is set incorrectly.

Mitigation: Keep BASE pointed at the intended public city site before running generated curl commands.

Risk: Event queries can return misleading results when dates are formatted incorrectly or month calendar pages are treated as complete listings.

Mitigation: Use the documented M-D-YYYY event path format, confirm the rendered heading matches the requested date, and fetch day pages for complete schedules.

Risk: Article searches may include expired deals if the per-site expired category is not resolved and excluded.

Mitigation: Resolve the expired category ID for the selected site and include it in categories_exclude for article queries.

Risk: Search terms or dates may be interpreted incorrectly by public WordPress endpoints.

Mitigation: URL-encode user search terms and use full timestamps for before and after filters when narrowing posts by date.

## Reference(s):

- [Ready-to-run recipes](references/recipes.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/otc-curl)
- [Related onthecheap MCP project](https://github.com/chrischall/onthecheap-mcp)
- [Charlotte on the Cheap](https://www.charlotteonthecheap.com)
- [Mile High on the Cheap](https://www.milehighonthecheap.com)
- [Triangle on the Cheap](https://triangleonthecheap.com)

## Skill Output:

**Output Type(s):** [Shell commands, Markdown, Guidance]

**Output Format:** [Markdown with inline bash, jq, and Python command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only web request recipes; users must provide the target city site and search/date inputs.]

## Skill Version(s):

0.4.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
