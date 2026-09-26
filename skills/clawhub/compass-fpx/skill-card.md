## Description:

Helps agents query Compass real-estate listings, property details, price history, and agent profiles from a shell using a paired browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and real-estate researchers use this skill to retrieve Compass listing and agent information, resolve addresses, and inspect price histories in shell-based workflows without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser-session-backed Compass requests may run afoul of site terms or exceed the user's authorization.

Mitigation: Confirm authorization and compliance with Compass terms before enabling the extension or automating requests.

Risk: Persistent browser pairing and WAF-aware access reuse the user's browsing session.

Mitigation: Use only a browser session you control and review the pairing and requested access before running the skill.

Risk: Search pages can expose only the first server-rendered results, so broad searches may appear complete when they are not.

Mitigation: Narrow searches by price or bedroom range and verify coverage before drawing market conclusions.

## Reference(s):

- [Compass request recipes](references/requests.md)
- [HTML data extraction helper](references/extract-global.mjs)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Guidance]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on Compass page availability and the user's paired browser session.]

## Skill Version(s):

1.1.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
