## Description:

Query etix.com event discovery data from a shell with the fpx CLI, including event, venue, performer, and detail lookups through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve public Etix event discovery data from shell workflows when they need one-shot CLI calls instead of a running MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fpx workflow uses a browser extension and persistent profile to route requests through an Etix browser tab.

Mitigation: Keep the fpx profile scoped to etix.com, avoid granting cookie, storage, or download capabilities unless intentionally needed, and revoke the Transporter trust/profile when finished.

Risk: HTML responses can be DataDome interstitial pages instead of the expected Etix content.

Mitigation: Check for captcha-delivery or the documented interstitial text before parsing HTML, and refresh an Etix tab until the DataDome check clears.

Risk: The full-text Etix search endpoint returns an opaque payload that is not usable as JSON.

Mitigation: Use search/suggest to resolve event, venue, and performer identifiers before requesting detail pages.

Risk: Ticket purchasing is a financial action outside the scope of this skill.

Mitigation: Limit use to anonymous, read-only event discovery and do not use the skill to complete purchases or account actions.

## Reference(s):

- [etix-fpx ClawHub listing](https://clawhub.ai/chrischall/skills/etix-fpx)
- [Etix consumer endpoints for fpx](references/etix-endpoints.md)
- [extract-datalayer.mjs](references/extract-datalayer.mjs)
- [Etix endpoint host](https://www.etix.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JavaScript snippets, and JSON extraction examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Etix discovery guidance; no ticket purchasing or account actions are in scope.]

## Skill Version(s):

0.4.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
