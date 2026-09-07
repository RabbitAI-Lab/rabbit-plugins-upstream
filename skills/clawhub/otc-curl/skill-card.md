## Description:

Query the On the Cheap network (charlotteonthecheap.com, milehighonthecheap.com and ~12 sister city sites) from the shell with curl and jq for daily local event listings with times, prices, and venues, plus searchable articles on free and cheap things to do.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill when they need shell-based guidance for retrieving local event and deal information from public On the Cheap city websites, especially when the onthecheap MCP server is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent makes live curl requests to public On the Cheap city websites and formats responses with local jq or Python commands.

Mitigation: Use the skill only where public website requests and local formatting commands are acceptable, and review generated commands before execution.

Risk: Live event and deal listings can be stale, expired, truncated, or parsed with the wrong site-specific identifiers or date format.

Mitigation: Check result freshness, resolve expired categories and term identifiers per site, verify event date headings, and fetch day pages for complete event listings.

## Reference(s):

- [Ready-to-run recipes](references/recipes.md)
- [Charlotte On the Cheap](https://www.charlotteonthecheap.com)
- [Mile High on the Cheap](https://www.milehighonthecheap.com)
- [Triangle on the Cheap](https://triangleonthecheap.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, jq, and Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance focuses on public website requests, local formatting commands, and checks for freshness and parsing pitfalls.]

## Skill Version(s):

0.4.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
