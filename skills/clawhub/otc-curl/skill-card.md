## Description:

Query the On the Cheap network (charlotteonthecheap.com, milehighonthecheap.com and ~12 sister city sites) from the shell with curl and jq — daily local event listings with times/prices/venues, plus searchable articles on free and cheap things to do. Use when the user wants local event or deal data and the onthecheap MCP server is not available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use this skill to find local event listings and free or low-cost activities. It gives an agent shell commands for searching public city event pages and articles when the onthecheap MCP server is unavailable.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Event dates, prices, and availability can change after a page is read.

Mitigation: Confirm current dates, prices, and availability with the event source or venue before making plans.

Risk: An ISO-formatted event date can silently return results for January 1, 1970, and month grids may omit listings beyond the first four per day.

Mitigation: Use the documented M-D-YYYY date path, confirm the returned date heading, and fetch each day page when a complete schedule is needed.

## Reference(s):

- [Ready-to-run recipes](references/recipes.md)
- [Charlotte On the Cheap](https://www.charlotteonthecheap.com)
- [Mile High on the Cheap](https://www.milehighonthecheap.com)
- [Triangle on the Cheap](https://triangleonthecheap.com)
- [OnTheCheap MCP project linked by the skill](https://github.com/chrischall/onthecheap-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance and shell commands, with event listings and article results formatted as text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live event and article results depend on the selected city, date, and search terms.]

## Skill Version(s):

1.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
