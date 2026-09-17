## Description:

Query Tock restaurant discovery, availability, and signed-in reservation data from a shell with the fpx CLI instead of running the tock-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to retrieve Tock metros, restaurant search results, venue availability, and reservation history from shell workflows without running the tock-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a browser bridge connected to a signed-in Tock tab.

Mitigation: Install and pair it only in trusted environments, review the requested commands before running them, and limit browser site access to exploretock.com.

Risk: The examples install @fetchproxy/cli globally without pinning a reviewed version.

Mitigation: Use a pinned, reviewed @fetchproxy/cli version and repeat review before upgrading.

Risk: Reservation and profile commands can expose private names, emails, dates, venues, and party details.

Mitigation: Treat command output as private and avoid writing responses to shared or predictable temporary paths.

## Reference(s):

- [Tock requests for fpx](references/requests.md)
- [extract-redux-slice.mjs](references/extract-redux-slice.mjs)
- [Tock skill page](https://clawhub.ai/chrischall/skills/tock-fpx)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request bodies, jq filters, and a helper JavaScript parser]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Tock access; reservation/profile examples can produce private account and reservation data.]

## Skill Version(s):

0.5.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
