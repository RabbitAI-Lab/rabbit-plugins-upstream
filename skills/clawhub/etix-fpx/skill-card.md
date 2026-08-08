## Description:

Query etix.com event ticketing data from a shell with the fpx CLI to search events, venues, and performers and retrieve event or venue details through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to issue one-shot shell requests for public Etix discovery data, including search suggestions, event details, venue details, and geolocation results, without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires installing a global CLI and pairing a browser extension that can fetch through the user's etix.com browser context.

Mitigation: Confirm this access model before installation, keep Transporter site access limited to etix.com, and use a dedicated browser profile where appropriate.

Risk: Browser-bridged requests can reflect the state of the user's active Etix browser context.

Mitigation: Use the skill only for anonymous public discovery reads and avoid purchases, account actions, or credentialed seller API workflows.

Risk: Etix pages may return a DataDome interstitial or other non-target HTML even when a fetch exits successfully.

Mitigation: Check fetched HTML for DataDome challenge markers before parsing or trusting extracted event and venue data.

## Reference(s):

- [Etix consumer endpoints for fpx](artifact/references/etix-endpoints.md)
- [DataLayer extraction helper](artifact/references/extract-datalayer.mjs)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/etix-fpx)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with inline shell, jq, and Node.js examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide an agent to fetch and parse public Etix discovery data; responses may be JSON, HTML-derived JSON-LD, microdata extracts, or shell diagnostics.]

## Skill Version(s):

0.4.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
