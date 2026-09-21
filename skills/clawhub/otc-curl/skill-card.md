## Description:

Query the On the Cheap network from the shell with curl and jq for daily local event listings with times, prices, and venues, plus searchable articles on free and cheap things to do.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill as a fallback when the onthecheap MCP server is unavailable and they need shell-based access to public On the Cheap event and deal information. It helps retrieve articles, daily event listings, and calendar summaries while avoiding stale or truncated results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill guides agents to run shell and Python snippets that make public web requests.

Mitigation: Review generated commands before execution, especially when changing BASE to another site.

Risk: Using an ISO date path for event pages can silently return January 1, 1970 results.

Mitigation: Convert event dates to M-D-YYYY and confirm the page heading matches the requested date.

Risk: Expired category IDs and taxonomy IDs differ by site, so reused IDs can return stale or incorrect results.

Mitigation: Resolve category and location IDs on the selected site before querying or filtering results.

Risk: Month calendar pages show truncated listings in each day cell.

Mitigation: Use month pages for discovery only, then fetch day pages for complete event schedules.

## Reference(s):

- [Ready-to-run recipes](references/recipes.md)
- [Charlotte on the Cheap](https://www.charlotteonthecheap.com)
- [Mile High on the Cheap](https://www.milehighonthecheap.com)
- [Triangle on the Cheap](https://triangleonthecheap.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/otc-curl)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, markdown]

**Output Format:** [Markdown with inline bash, jq, and Python command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands make public web requests and may require local curl, jq, and Python for parsing or decoding.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
