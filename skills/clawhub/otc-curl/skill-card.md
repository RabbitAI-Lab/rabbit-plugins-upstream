## Description:

Helps agents query public On the Cheap city sites for local events and affordable activities using curl, jq, and lightweight parsing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can find local event schedules and inexpensive activities when the On the Cheap MCP server is unavailable.

### Deployment Geography for Use:

Global (covers participating US city sites)

## Known Risks and Mitigations:

Risk: Commands make network requests to public city websites.

Mitigation: Review the selected city and base URL before running commands.

Risk: Expired posts can make retired deals appear current.

Mitigation: Resolve and exclude the expired category separately for each site.

Risk: Incorrect event date paths can silently return unrelated listings.

Mitigation: Use M-D-YYYY paths and check that the page heading matches the requested date.

Risk: Monthly calendar cells omit listings beyond the first four.

Mitigation: Check overflow counts and fetch individual day pages for complete schedules.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/otc-curl)
- [Ready-to-run recipes](references/recipes.md)
- [Charlotte on the Cheap](https://www.charlotteonthecheap.com)
- [Mile High on the Cheap](https://www.milehighonthecheap.com)
- [Triangle on the Cheap](https://triangleonthecheap.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown with bash snippets and event or article summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected city site and requested date.]

## Skill Version(s):

1.1.8 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
