## Description:

tock-fpx helps an agent query Tock restaurant discovery, venue availability, and signed-in reservation data through the fpx CLI and a user's browser session instead of running the tock-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation agents use this skill to fetch Tock metros, restaurant search results, venue calendars, and reservation history from shell workflows when the MCP server is not installed. It is read-only and directs booking or cancellation actions back to Tock.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a persistent browser bridge while the user may be signed in to Tock.

Mitigation: Use a pinned and trusted @fetchproxy/cli version, limit browser extension site access to exploretock.com, and remove the fpx pairing when finished.

Risk: Reservation examples can expose personal reservation details such as names and email addresses.

Mitigation: Avoid running reservation examples on shared machines, stream or filter output when possible, and do not retain raw personal data longer than needed.

Risk: The release security verdict requires review before installation.

Mitigation: Review the skill before installing and verify that its read-only behavior and browser-bridge requirements are acceptable for the deployment environment.

## Reference(s):

- [Skill source](SKILL.md)
- [Tock requests for fpx](references/requests.md)
- [Redux slice extractor](references/extract-redux-slice.mjs)
- [Tock](https://www.exploretock.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, jq filters, JSON request bodies, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only retrieval guidance and command examples for browser-bridged Tock requests.]

## Skill Version(s):

0.5.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
