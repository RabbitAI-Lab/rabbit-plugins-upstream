## Description:

Query Homes.com from a shell with the fpx CLI to search listings, resolve addresses, fetch property details, photos, history, and saved account pages through the user's own browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and real-estate data analysts use this skill to run Homes.com search, property detail, address resolution, photo, history, nearby listing, market report, saved-home, and saved-search requests from an agent shell without a Homes MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests can ride a signed-in Homes.com browser session, and saved homes or saved searches can expose account-specific data.

Mitigation: Use a dedicated browser profile or sign out when only public listing data is needed, and run saved-home or saved-search recipes only when account access is intended.

Risk: The recipes write page captures and extracted data to predictable /tmp paths.

Mitigation: Use a private mktemp directory for captures and clean it up after the task.

Risk: The workflow depends on npm-installed fpx tooling and a browser extension bridge.

Mitigation: Pin and verify npm packages where possible, keep the extension paired only to the intended Homes.com profile, and check bridge health before collecting data.

## Reference(s):

- [homes.com request recipes](references/homes-requests.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with shell commands, JavaScript snippets, jq filters, endpoint paths, and troubleshooting notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The recipes produce HTML, extracted JSON-LD, JSON API responses, and derived tabular or structured fields when the agent runs the suggested commands.]

## Skill Version(s):

1.4.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
