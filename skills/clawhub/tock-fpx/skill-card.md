## Description:

Query Tock restaurant discovery, availability, and signed-in user reservations from a shell with the fpx CLI instead of running the tock-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Tock metros, restaurant search results, venue availability, and a signed-in patron's reservations through shell commands. It is suited to read-only Tock data lookups where a paired browser bridge is acceptable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a persistent paired browser bridge to access a signed-in exploretock.com tab.

Mitigation: Install only when the user accepts pairing the third-party CLI and browser extension with that tab, and confirm the intended Tock tab is open before use.

Risk: Reservation and profile examples can expose personal Tock data such as names, emails, reservation IDs, and purchase details.

Mitigation: Avoid shared machines, delete saved responses after use, and query only the fields needed for the task.

Risk: Examples that write responses under fixed temporary paths can leave sensitive data on disk.

Mitigation: Use private working paths when saving responses and remove temporary files after inspection.

## Reference(s):

- [Tock requests for fpx](references/requests.md)
- [Redux slice extraction helper](references/extract-redux-slice.mjs)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tock-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands, jq filters, JSON request bodies, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Tock data retrieval through fpx; reservation/profile calls may expose personal data from a signed-in browser tab.]

## Skill Version(s):

0.5.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
