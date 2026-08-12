## Description:

Query the On the Cheap network from the shell with curl and jq for daily local event listings with times, prices, venues, and searchable articles about free and low-cost things to do.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they need shell-based access to public On the Cheap event and deal listings, especially when the onthecheap MCP server is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Event and deal results come from live public site HTML and WordPress responses that may be stale, malformed, truncated, or changed after retrieval.

Mitigation: Treat results as convenience data and verify important times, prices, venue details, and availability at the linked source before relying on them.

Risk: The skill depends on local command-line tools and live public web requests.

Mitigation: Confirm curl, jq, and any shown Python snippets are available locally, and review generated shell commands before execution.

## Reference(s):

- [Ready-to-run recipes](references/recipes.md)
- [Charlotte on the Cheap](https://www.charlotteonthecheap.com)
- [Mile High on the Cheap](https://www.milehighonthecheap.com)
- [Triangle on the Cheap](https://triangleonthecheap.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, guidance]

**Output Format:** [Markdown with inline bash, jq, and Python command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are convenience data from public site HTML and WordPress JSON responses; important times, prices, and venue details should be verified against the linked source.]

## Skill Version(s):

0.3.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
