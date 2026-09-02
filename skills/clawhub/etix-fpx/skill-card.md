## Description:

Query etix.com event ticketing from a shell with the fpx CLI to search events, venues, and performers and retrieve event or venue details through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query public Etix discovery data from shell workflows when they need event, venue, performer, geolocation, or page-detail data without running the etix-mcp server. It is intended for anonymous discovery reads and excludes ticket purchases or authenticated account actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on the fpx CLI, the Transporter browser extension, and a persistent pairing scoped to etix.com.

Mitigation: Install only the required tooling, scope the fpx profile to etix.com, and approve pairing only for a browser tab intended for public Etix discovery.

Risk: Browser-mediated requests could be misused for purchases or authenticated account activity outside the documented discovery workflow.

Mitigation: Use the skill only for anonymous public event-discovery reads and avoid purchases, account actions, or logged-in Etix sessions.

Risk: Temporary files may contain event, venue, location, or query results.

Mitigation: Store temporary outputs in an expected workspace and remove them after use.

Risk: Etix HTML responses can contain a DataDome interstitial even when the fetch command exits successfully.

Mitigation: Check HTML responses for bot-wall markers such as captcha-delivery before parsing or trusting extracted data.

## Reference(s):

- [Etix consumer endpoints for fpx](artifact/references/etix-endpoints.md)
- [extract-datalayer.mjs](artifact/references/extract-datalayer.mjs)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/etix-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell, jq, and Node.js code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces command recipes and parsing guidance for public Etix event-discovery data; it does not perform ticket purchases.]

## Skill Version(s):

0.5.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
