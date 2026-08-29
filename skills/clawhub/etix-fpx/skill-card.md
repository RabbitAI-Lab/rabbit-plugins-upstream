## Description:

Query etix.com from a shell with the fpx CLI to search events, venues, and performers and retrieve event or venue details through a browser-backed fetch call.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query public Etix event-discovery data from shell scripts or agent workflows, resolve event and venue IDs, and extract event or venue details without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Event search terms or city and ZIP geolocation queries are sent to Etix through the user's browser-backed fpx bridge.

Mitigation: Use the skill for anonymous discovery reads only, avoid sensitive search or location inputs, and confirm the user is comfortable sharing these queries with Etix.

Risk: Ticket purchasing and seller-account API access can introduce financial or credential risk.

Mitigation: Keep usage limited to public event discovery; do not automate ticket purchases or use venue or box-office credentials.

Risk: A successful HTML fetch can still return a DataDome interstitial instead of event or venue content.

Mitigation: Check HTML responses for DataDome interstitial markers before parsing and retry only after the browser tab has cleared the challenge.

## Reference(s):

- [Etix consumer endpoints for fpx](references/etix-endpoints.md)
- [extract-datalayer.mjs](references/extract-datalayer.mjs)
- [Etix website](https://www.etix.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/etix-fpx)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell, jq, and Node.js snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include fpx command lines, jq filters, endpoint paths, and extraction snippets; ticket purchasing and seller-account API credentials are out of scope.]

## Skill Version(s):

0.4.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
